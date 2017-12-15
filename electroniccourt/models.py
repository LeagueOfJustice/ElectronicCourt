from django.db import models
from django.utils import timezone

# Create your models here.

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, default=1)
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
    template = models.ForeignKey(Document_template)
    author = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)
    case_id = models.CharField(max_length=20)
    plaintiff = models.CharField(max_length=50)
    defendant = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    statement = models.TextField()
    state = models.CharField(max_length=50, default="new")

    def __str__(self):
    	result = (str(self.template.name) + ' ' + str(self.subject) + ' ' + str(self.case_id))
    	return result
        #return self.subject

    def set_rejected(self):
        self.state = "rejected"
        self.save()

    def set_corrected(self):
        self.state = "corrected"
        self.save()

    def set_accepted(self):
        self.state = "accepted"
        self.save()

class Mail(models.Model):
    id_mail = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name='sender')
    reciever = models.ForeignKey(User, related_name='reciever')
    document = models.ForeignKey(Document, related_name='document')
    sending_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.document.subject

    def get_document(self):
        return self.document

    def send(self):
        self.sending_date = timezone.now
        self.save()

class Feedback(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    mail = models.ForeignKey(Mail, related_name="mail")
    author = models.ForeignKey(User, related_name="author")
    publish_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text

    def publish(self):
    	self.publish_date = timezone.now
    	self.save()

class Permission(models.Model):
    id_permission = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")

    def __str__(self):
    	return self.name

class User_Permission(models.Model):
	id_user = models.ManyToManyField(User, related_name="user")
	id_permission = models.ManyToManyField(Permission, related_name="permission")

	def __str__(self):
		name_str = ""
		permission_str = ""
		for name in self.id_user.all():
			name_str += name.name + " "
		for permission in self.id_permission.all():
			permission_str += permission.name + " "
		result = name_str + permission_str
		#return ('%s %s' % (self.id_user.name, self.id_permission))
		return result
