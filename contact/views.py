from django.shortcuts import render, redirect
from contact.form import Contact_form
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# Create your views here.


def contact(request):
    
    if request.method == 'POST':
        
        
        info_contact = Contact_form(request.POST)
        
        
        if info_contact.is_valid():
            
            
            data_cleaning = info_contact.cleaned_data
            
            recipient = 'conniipighn@gmail.com'
            
            contact = data_cleaning['message'] + '\n\n' + data_cleaning['email']
            
            
            try:
                send_mail(data_cleaning['subject'], contact, data_cleaning.get('email', 'yanmarcoblanvo@gmail.com'), [recipient], True)
            
            
                return redirect('/contact/?valid')
            
            
            except:
                
                return redirect('/contact/?error')
    
    
    else:
        
        return render(request, 'contact/Contact.html', {'form':Contact_form})