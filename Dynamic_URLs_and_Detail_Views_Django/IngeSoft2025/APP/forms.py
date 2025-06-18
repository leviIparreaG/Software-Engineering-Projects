from django import forms

class NewForm(forms.Form):
    name = forms.CharField(label = "Nombre", max_length=50, required = False, help_text = "Ingresa tu nombre")
    lastName = forms.CharField(label = "Apellido", max_length=50, required = False, help_text = "Ingresa tu apellido")
    num_cuenta = forms.CharField(label = "Numero de Cuenta", max_length=50, required = False, help_text = "Ingresa tu numero de cuenta")

