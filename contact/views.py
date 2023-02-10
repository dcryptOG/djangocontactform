
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import ContactForm

# Create your views here.
def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            email = form.cleaned_data['email']

# CONFIG IN SETTINGS.PY TO USE GMAIL AS SENDER
            send_mail(
                'CONTACT FORM: ' + name, #subject
                'Thank you! Your message has been receieved' + 
                name + '\n' + content, #message
                'settings.EMAIL_HOST_USER', #sender if avialable
                [email],
                fail_silently=False
            )
            return redirect('index')
    else:
        form = ContactForm()


    return render(request, 'contact/index.html', {
        'form': form
    })
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')