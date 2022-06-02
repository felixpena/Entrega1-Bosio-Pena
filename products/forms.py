from django import forms
from products.models import Products, Categoria, Cliente
# Este formulario esta declarado a mano para hacer todos los campos a mano.
# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField()

# Buena forma de credar form "LUCA" formulario que hereda de ModelForm, 
# Este form esta basado en un modelo. video playground intermedio parte 3 minuno 1:00:00.
# Este metodo es ideal para pedir los campos de un modelo. de models.
class Product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'    #trae todo

class Categoria_form(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        #  atributo de exclusión de la clase Meta interna de ModelForm en 
        # una lista de campos que se excluirán del formulario. Por ejemplo:
        #exclude = ['title'] 