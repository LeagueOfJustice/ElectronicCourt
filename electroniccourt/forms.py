from django import forms

from .models import User, Document, Document_template


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'name', 'password')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('template','author', 'case_id', 'plaintiff', 'defendant', 'subject', 'statement', 'date', 'state', )


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Document_template
        fields = ('name', 'template')

