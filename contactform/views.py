from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.

def contact(request):

    if request.method == 'POST':
        name=request.POST.get('nom-prenom')
        email=request.POST.get('email')
        objet=request.POST.get('objet')
        message=request.POST.get('message')
        
        data={
            'name': name,
            'email': email,
            'objet': objet,
            'message': message
        }
        message='''
        Nom et Prenom: {}
        Nouveau Message: {}
        Mon Email est : {}
        '''.format(data['name'], data['message'], data['email'])
        send_mail(data['objet'], message, '', ['agencedosso4@gmail.com'])
        
        return HttpResponse("votre message a été envoyé avec succès. Merci.")

    return render(request, 'contactform/contactform.html')