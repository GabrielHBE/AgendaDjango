from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error('first_name',ValidationError('Error message',code='invalid1'))
        self.add_error('first_name',ValidationError('Error message',code='invalid2'))
    

        return super().clean()


def create(request):

    if request.method == 'POST':

        #Pegar o valor da barra 

        context = {
            'title':'Create contact',
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
            )
    
    context = {
                'title':'Create contact',
                'form': ContactForm()
            }
    
    return render(
            request,
            'contact/create.html',
            context
            )