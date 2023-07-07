from ast import mod
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
        return f'{self.pk}/ {self.title}/ {self.total:,}'
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    piePerPackage = models.IntegerField()
    weight = models.FloatField()
    pacLong = models.FloatField()
    pacWidth = models.FloatField()
    pacHeight = models.FloatField()

    def __str__(self):
        return f'{self.name}'
    

class Volume(models.Model):
    volume = models.FloatField(null=True, blank=True)
    weight = models.FloatField()

    def __str__(self):
        return self.pk
    

class Employee(models.Model):
    employee = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    supervisor = models.BooleanField(default=False)

    def save(self, *arg, **kwargs):
        if self.supervisor:
            self.available = False
        super(Employee, self).save(*arg, **kwargs)

    def __str__(self):
        return f'{self.employee}'

class Schedule(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.date