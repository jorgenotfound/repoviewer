from django import forms


class HomeQueryForm(forms.Form):

    query = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite el login de una organizacion'}
    ))


class RepositoryQueryForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre del repo'}
    ))

    FIELD_CHOICES = (
        ('', 'Ordenar por'),
        ('created_at', 'Fecha de creacion'),
        ('last_updated', 'Fecha del ultimo commit')
    )
    sorting_field = forms.ChoiceField(
        required=False,
        choices=FIELD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    ORDER_CHOICES = (
        ('', 'Ascendente'),
        ('-', 'Descendente')
    )
    sorting_order = forms.ChoiceField(
        required=False,
        choices=ORDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
