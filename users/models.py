from django.db import models
from django.contrib.auth.models  import AbstractUser
from decimal import Decimal

# Create your models here.

class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super(User, self).save(*args, **kwargs)
    
    def pay(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError("Valor deve ser do tipo decimal")
        
        self.amount -= value

    def receive(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError("Valor dev ser do tipo Decimal")
        
        self.amount += value