from django import forms
from django.core.exceptions import ValidationError
from .models import Expense, Income


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'item', 'amount', 'category']
        labels = {
            'date': 'Date',
            'item': 'Item',
            'amount': 'Amount',
            'category': 'Category'
        }

    # def clean_amount(self):
    #     amount = self.cleaned_data.get('mount')

    #     if amount <= 0.0:
    #         msg = (
    #             'Cannot add amount less than 0'
    #         )
    #         raise ValidationError(_(msg))

    #     return amount


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'amount', 'source']
        labels = {
            'date': 'Date',
            'amount': 'Amount',
            'source': 'Source'
        }
