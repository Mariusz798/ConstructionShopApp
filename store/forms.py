from django import forms

from store.models import Opinions, Orders


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['product', 'if_delivery', 'payment_method']
        widgets = {
            'product': forms.CheckboxSelectMultiple()
        }
        labels = {
            'product_name': 'Nazwa produktu',
            'if_delivery': 'Dostawa',
            'payment_method': 'Sposób płatności'
        }


class CreateOpinionForm(forms.ModelForm):
    class Meta:
        model = Opinions
        fields = ['product', 'text']
        widgets = {
            'text': forms.Textarea
        }
        labels = {
            'product': 'Nazwa produktu',
            'text': 'Treść opnii'
        }