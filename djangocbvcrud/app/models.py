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
        return self.category.get_category_display()
    

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory)
    title = models.CharField(max_length=255)
    amount = models.DecimalField()
    total = models.DecimalField()