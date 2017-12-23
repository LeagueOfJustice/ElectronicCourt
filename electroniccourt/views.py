from django.shortcuts import render, get_object_or_404, redirect

from electroniccourt.forms import UserForm, DocumentForm, TemplateForm
from .models import *


# Create your views here.

def main_page(request):
    mails = Mail.objects.all().filter(sender__role__name="Господарський суд")
    return render(request, 'electroniccourt/main_page.html', {'mails': mails})


def mail_detail(request, id_mail):
    mail = get_object_or_404(Mail, id_mail=id_mail)
    feedbacks = Feedback.objects.filter(mail__id_mail=id_mail)
    return render(request, 'electroniccourt/mail_detail.html', {'mail': mail, 'feedbacks': feedbacks})


def users_list_page(request):
    users = User.objects.all()
    return render(request, 'electroniccourt/users_list_page.html', {'users': users})


def admin_page(request):
    user = User.objects.all()
    template = Document_template.objects.all()
    return render(request, 'electroniccourt/admin_page.html', {'template': template, 'add_user': user})


def new_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        return redirect('users_list_page')
    else:
        form = UserForm()
    return render(request, 'electroniccourt/new_user.html', {'form': form})


def creating_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document_form = form.save(commit=False)
            document_form.date_created = timezone.now()
            document_form.save()
            return redirect('main_page')
    else:
        form = DocumentForm()
    return render(request, 'electroniccourt/creating_document.html', {'form': form})


def document_templates(request):
    document_templates = Document_template.objects.all()
    return render(request, 'electroniccourt/document_templates.html', {'document_templates': document_templates})


def new_template(request):
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            new_templates = form.save(commit=False)
            new_templates.save()
            return redirect('document_templates')
    else:
        form = TemplateForm()
    return render(request, 'electroniccourt/new_template.html', {'form': form})
