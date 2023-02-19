from django import forms
from .models import Income
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'description', 'date']
