from django import forms
from calls.models import personal


class personal_form(forms.ModelForm):
    class Meta:
        model = personal
        fields = '__all__'  # ['username', 'email', 'phone']
