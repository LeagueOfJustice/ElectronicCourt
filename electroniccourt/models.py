from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Document_template(models.Model):
    id_document_template = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    template = models.FileField(upload_to='document_templates/')

    def __str__(self):
        return self.name

class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    id_document_template = models.OneToOneField(Document_template)
    id_creator = models.OneToOneField(User)
    date_created = models.DateTimeField(default=timezone.now)
    case_id = models.CharField(max_length=20)
    plaintiff = models.CharField(max_length=50)
    defendant = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    statement = models.TextField()

    def __str__(self):
        return self.subject

class Mail(models.Model):
    id_mail = models.AutoField(primary_key=True)
    id_sender = models.OneToOneField(User, related_name='sender')
    id_reciever = models.OneToOneField(User, related_name='reciever')
    id_document = models.OneToOneField(Document, related_name='document')
    date_send = models.DateTimeField(default=timezone.now)
    feedback = models.TextField(default='')

    def __str__(self):
        return self.id_document.subject

    def get_document(self):
        return self.id_document
