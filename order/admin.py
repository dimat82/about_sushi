from django.contrib import admin
from order.models import *

# Register your models here.
@admin.register(OrderRolls,OrderSoup,OrderSets,OrderSushi)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','phone','food','date']
