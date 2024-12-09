from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.urls import reverse

def create(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        context = {
            'title':'Create contact',
            'form': form 
        }

        if form.is_valid():
            form.save() #salvar os dados na base de dados

            return redirect('contact:create')
        
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