from django import forms
from django.forms import ModelForm

from .models import Answer


class AnswerForm(ModelForm):
    value = forms.CharField(label='Your Answer')

    class Meta:
        model = Answer
        fields = ('value', )
