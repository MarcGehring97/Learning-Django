from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='')
    email = forms.EmailField()
    description = forms.CharField(required=True, widget=forms.Textarea)
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email

"""
class RawProductForm(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=True, widget=forms.Textarea)
    price = forms.DecimalField(initial=199.99)
"""