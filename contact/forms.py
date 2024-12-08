from . import models
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    class Meta: 
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self):
        #cleaned_data = self.cleaned_data

        self.add_error('first_name',ValidationError('Error message',code='invalid1'))
        self.add_error('first_name',ValidationError('Error message',code='invalid2'))
    

        return super().clean()
