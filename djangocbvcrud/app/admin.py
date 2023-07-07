from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(Product)
admin.site.register(Volume)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'employee','available', 'supervisor')
    list_editable = ('employee', 'available', 'supervisor')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Schedule)