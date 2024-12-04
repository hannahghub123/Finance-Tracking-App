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


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'amount', 'source']
        labels = {
            'date': 'Date',
            'amount': 'Amount',
            'source': 'Source'
        }
