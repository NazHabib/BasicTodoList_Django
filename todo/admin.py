from django.contrib import admin
from django import forms
from .models import Todo
# Register your models here.

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        