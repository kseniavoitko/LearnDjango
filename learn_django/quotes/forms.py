from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Authors, Qoutes


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter fullname"}
        ),
    )
    born_date = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    born_location = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Authors
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter quote"}
        ),
    )
    author = forms.IntegerField(widget=forms.Select())

    class Meta:
        model = Qoutes
        fields = ["quote"]
        exclude = ["author"]
