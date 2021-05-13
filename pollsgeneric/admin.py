from django.contrib import admin

# Register your models here.
from .models import QuestionGeneric,ChoiceGeneric
admin.site.register(QuestionGeneric)
admin.site.register(ChoiceGeneric)