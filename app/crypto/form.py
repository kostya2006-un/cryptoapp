from django import forms
from crypto.models import Currency

class PorfolioItemsForm(forms.Form):
    currency = forms.ModelChoiceField(queryset=Currency.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=6)