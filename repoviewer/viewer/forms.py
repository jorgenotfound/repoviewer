from django import forms

class HomeQueryForm(forms.Form):

    query = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite el login de una organizacion'}
    ))
