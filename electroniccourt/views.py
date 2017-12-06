from django.shortcuts import render, get_object_or_404
from .models import * 

# Create your views here.

def main_page(request):
	mails = Mail.objects.all().order_by('date_send')
	return render(request, 'electroniccourt/main_page.html', {'mails':mails})

def mail_detail(request, id_mail):
	mail = get_object_or_404(Mail, id_mail=id_mail)
	return render(request, 'electroniccourt/mail_detail.html', {'mail': mail})
	
def users_list_page(request):
	users = User.objects.all()
	return render(request, 'electroniccourt/users_list_page.html', {'users':users})

