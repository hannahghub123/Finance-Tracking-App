from django.contrib import admin
from .models import Category, Source, Expense, Income

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Expense)
admin.site.register(Income)
