from django.contrib import admin

# Register your models here.
from .models import TypeDocument, TypePayment


admin.site.register(TypeDocument)
admin.site.register(TypePayment)