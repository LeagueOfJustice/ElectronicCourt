from django import forms

from .models import User, Document


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'name', 'password',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('plaintiff', 'defendant', 'subject', 'statement', 'date', 'case_id', 'template', 'author')
