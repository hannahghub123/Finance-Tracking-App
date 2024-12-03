from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
    path('list-expenses/', views.list_expenses, name='list_expenses'),
    path('list-income/', views.list_income, name='list_income'),
    path(
        'api/financial-data/',
        views.get_financial_data,
        name='get_financial_data'
    ),

]
