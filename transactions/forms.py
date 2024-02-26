from django import forms 
from .models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount']

class DepositeForm(TransactionForm):
    def clean_amount(self):
        min_deposit = 100
        amount = self.cleaned_data.get('amount')
        if amount< min_deposit:
            raise forms.ValidationError(
                f"You need to deposit at least {min_deposit}" 
            )
        return amount 