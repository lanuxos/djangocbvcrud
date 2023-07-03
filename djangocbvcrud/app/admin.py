from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)