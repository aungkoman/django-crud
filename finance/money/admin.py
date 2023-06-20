from django.contrib import admin

from .models import TransactionCategory, Transaction


admin.site.register(TransactionCategory)
admin.site.register(Transaction)