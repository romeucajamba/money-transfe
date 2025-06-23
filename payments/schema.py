from ninja import ModelSchema
from .models import Transations

class TransactionSchema(ModelSchema):
    class Meta:
        model = Transations
        exclude = ['id', 'date']