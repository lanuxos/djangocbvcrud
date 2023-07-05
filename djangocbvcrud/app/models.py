from unicodedata import category
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()

    def __str__(self):
        return self.title


class ExpenseCategory(models.Model):
    categories = (
        ('i', 'income'),
        ('o', 'outcome'),
    )
    category = models.CharField(max_length=10, choices=categories)

    def __str__(self):
        return self.get_category_display()
    

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *arg, **kwargs):
        if self.total:
            pass # when total field is not empty, ignore below code
        else:
            lastRecord = Expense.objects.last()
            if lastRecord:
                income = ExpenseCategory.objects.get(category='i')
                if self.category == income:
                    self.total = lastRecord.total + self.amount
                else:
                    self.total = lastRecord.total - self.amount
            else:
                self.total = self.amount
        super(Expense, self).save(*arg, **kwargs)

    def __str__(self):
        return f'{self.pk}/{self.title}/{self.total}'