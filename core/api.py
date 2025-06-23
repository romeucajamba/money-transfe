from ninja import NinjaAPI
from users.api import users_router
from payments.api import payments_router

api = NinjaAPI()
api.add_router("/v1/users/", users_router)
api.add_router("/v1/payments/", payments_router)