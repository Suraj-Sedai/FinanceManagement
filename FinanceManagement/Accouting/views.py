from django.shortcuts import render, redirect
from .forms import IncomeForm
from .forms import ExpenseForm
from .models import Income, Expense
from django.db.models import Sum

def balance(request):
    # Calculate the total income from the Income model using the aggregate() method
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate the total expenses from the Expense model using the aggregate() method
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate the balance by subtracting the total expenses from the total income
    balance = total_income - total_expenses

    # Render the balance.html template with the balance as a context variable
    return render(request, 'balance.html', {'balance': balance})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'income/income_list.html', {'incomes': incomes})

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'income/add_income.html', {'form': form})

