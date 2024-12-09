from django.shortcuts import render, redirect,get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse 
from contact.models import Contact

def create(request):

    form_action = reverse('contact:create')

    if request.method == 'POST':

        form = ContactForm(request.POST)

        context = {
            'title':'Create contact',
            'form': form,
            'form_action': form_action

        }

        if form.is_valid():
            contact = form.save() #salvar os dados na base de dados

            return redirect('contact:update',contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context
            )
    
    context = {
                'title':'Create contact',
                'form': ContactForm(),
                'form_action': form_action,
            }
    
    return render(
            request,
            'contact/create.html',
            context
            )


def update(request,contact_id):

    contact = get_object_or_404(Contact,pk=contact_id,show=True)
    form_action = reverse('contact:update',args=(contact_id,))

    if request.method == 'POST':

        form = ContactForm(request.POST,instance=contact)

        context = {
            'title':'Create contact',
            'form': form,
            'form_action': form_action

        }

        if form.is_valid():
            contact = form.save() #salvar os dados na base de dados

            return redirect('contact:update',contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context
            )
    
    context = {
                'title':'Create contact',
                'form': ContactForm(instance=contact),
                'form_action': form_action,
            }
    
    return render(
            request,
            'contact/create.html',
            context
            )