from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=20)

    class Meta:
        model = Producto
        fields = ['nombre','precio']
        