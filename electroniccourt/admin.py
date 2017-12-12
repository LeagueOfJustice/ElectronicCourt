from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Document_template)
admin.site.register(Document)
admin.site.register(Mail)
admin.site.register(Feedback)
admin.site.register(Permission)
admin.site.register(User_Permission)
admin.site.register(Role)