import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income
from common.literal_constants import constant_vars
from django.db.models import Sum
from datetime import datetime


def dashboard(request):
    total_income = sum(income.amount for income in Income.objects.all())
    total_expense = sum(expense.amount for expense in Expense.objects.all())

    return render(
        request, 'tracker/dashboard.html',
        {
            'total_income': total_income,
            'total_expense': total_expense
        }
    )


def add_expense(request):
    status = 0
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            status = 1

    serialized_data = json.dumps({
        'status': status, "data": form.errors, 'message': "success",
    })
    response = HttpResponse(
        serialized_data, content_type=constant_vars['jsonContentType']
    )
    return response


def add_income(request):
    status = 0
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save()
            income.save()
            status = 1

    serialized_data = json.dumps({
        'status': status, "data": form.errors, 'message': "success",
    })
    response = HttpResponse(
        serialized_data, content_type=constant_vars['jsonContentType']
    )
    return response


def list_expenses(request):
    expenses = Expense.objects.all()
    total_expense = sum(expense.amount for expense in Expense.objects.all())

    expense_form = ExpenseForm()
    return render(
        request, 'tracker/list_expenses.html',
        {
            'expenses': expenses,
            'expense_form': expense_form,
            'total_expense': total_expense
        }
    )


def list_income(request):
    income = Income.objects.all()
    total_income = sum(income.amount for income in Income.objects.all())

    income_form = IncomeForm()
    return render(
        request, 'tracker/list_income.html',
        {
            'income': income,
            'income_form': income_form,
            'total_income': total_income
        }
    )


def get_financial_data(request):
    # Retrieve data for the current year or any specific period
    year = datetime.now().year
    income_data = Income.objects.filter(
        date__year=year
    ).values('date__month').annotate(
        total_income=Sum('amount')
    ).order_by('date__month')
    expense_data = Expense.objects.filter(
        date__year=year
    ).values('date__month').annotate(
        total_expense=Sum('amount')
    ).order_by('date__month')

    # Format data for the chart
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]
    total_income = [0] * 12
    total_expense = [0] * 12

    for item in income_data:
        month_index = item['date__month'] - 1
        total_income[month_index] = item['total_income']

    for item in expense_data:
        month_index = item['date__month'] - 1
        total_expense[month_index] = item['total_expense']

    # Calculate balance for each month
    balance = [
        income - expense for income, expense in zip(
            total_income, total_expense
        )
    ]

    # Prepare JSON data
    data = {
        "labels": months,
        "datasets": [
            {
                "label": "Total Income",
                "data": total_income,
                "backgroundColor": "rgba(54, 162, 235, 0.5)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 1
            },
            {
                "label": "Total Expense",
                "data": total_expense,
                "backgroundColor": "rgba(255, 99, 132, 0.5)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            },
            {
                "label": "Balance",
                "data": balance,
                "backgroundColor": "rgba(75, 192, 192, 0.5)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }
        ]
    }

    return JsonResponse(data)
