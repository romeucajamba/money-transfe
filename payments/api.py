from ninja import Router
from payments.schema import TransactionSchema
from django.shortcuts import get_object_or_404
from users.models import User
from rolepermissions.checkers import has_permission
from django.db import transaction as django_transaction
import requests
from django.conf import settings
from .models import Transations
from django_q.tasks import async_task
from .task import send_notification

payments_router = Router()

@payments_router.post("/", response={200: TransactionSchema, 400: dict, 403: dict})
def transation(request, transaction: TransactionSchema):
    print(transaction.dict())
    payer = get_object_or_404(User, id=transaction.payer)
    payee = get_object_or_404(User, id=transaction.payee)
    
    if payer.amount < transaction.amount:
        return 400, {"error": "Insufficient funds"}
    
    if not has_permission(payer, 'can_make_transaction'):
        return 403, {"error": "You do not have permission to make transactions"}
    
    if not has_permission(payee, 'can_receive_transaction'):
        return 403, {"error": "Payee does not have permission to receive transactions"}
    
    with django_transaction.atomic():
        payer.pay(transaction.amount)
        payee.receive(transaction.amount)

        transaction = Transations(
            amount=transaction.amount,
            payer_id=transaction.payer,
            payee_id=trasaction.payee,
        )
        payer.save()
        payee.save()

        response = requests.get(settings.AUTHORIZE_TRANSFER_ENDPOINT).json()

        if response.get("status") != "authorized":
            raise ValueError("Transfer not authorized by external service")
    
    async_task(send_notification, payer.username, payee.username, transaction.amount) 

    return 200, transaction