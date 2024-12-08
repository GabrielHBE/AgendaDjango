from django.shortcuts import render


from contact.forms import ContactForm

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