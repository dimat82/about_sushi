from django import forms
from order.models import *


class SushiOrderForm(forms.ModelForm):
    class Meta:
        model=OrderSushi
        fields=['name','phone','food']


class SetsOrderForm(forms.ModelForm):
    class Meta:
        model = OrderSets
        fields = ['name', 'phone', 'food']

class SoupOrderForm(forms.ModelForm):
    class Meta:
        model=OrderSoup
        fields=['name','phone','food']

class RollOrderForm(forms.ModelForm):
    class Meta:
        model=OrderRolls
        fields=['name','phone','food']
