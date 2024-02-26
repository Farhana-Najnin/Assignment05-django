from django.db import models
from user.models import UserBankAccount
# Create your models here.
TRANSACTIONTYPE = (
    (1, 'Deposit'),
)
class Transactions(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'transaction', on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    balance_after_transaction = models.DecimalField( max_digits = 10,decimal_places = 2)
    timestamp = models.DateTimeField(auto_now_add = True)
    transactionType = models.IntegerField(choices=TRANSACTIONTYPE, null=True)
    class Meta:
        ordering = ['timestamp']