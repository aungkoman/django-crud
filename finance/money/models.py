from django.db import models


class TransactionCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    income = models.BooleanField(default=False)
    transaction_category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
    created_date = models.DateTimeField("date published")
