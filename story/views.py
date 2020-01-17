from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from shop.models import Item

def howItWorks(request):
    
    return render(request, 'story/howitworks.html')
    

def blogPage(request):
    
    return render(request, 'story/blog.html')
    
def blogPost1(request):
    
    return render(request, 'story/blogpost1.html')
    
def blogPost2(request):
    
    return render(request, 'story/blogpost2.html')

def blogPost3(request):
    
    return render(request, 'story/blogpost3.html')
    
def faqPage(request):
    
    return render(request, 'story/faq.html')
    
def contactPage(request):
    items = Item.objects.filter().order_by('price')
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            try:
                name = request.POST["name"]
                contact_number = request.POST["contact_number"]
                email = request.POST["email"]
                message = request.POST["message"]
                interest = request.POST.getlist("session-name")
                subject = "An Enquiry has been received! "
                text_content = """
Enquiry POC Name: {}
                        
Enquiry POC Contact: {}
                        
Enquiry POC Email: {}

Enquiry POC Message: {} 

Interested in the following classes:

{}
                        
Regards,
Admin @OlecraFit
                """.format(name, contact_number, email, message, interest)
                sender = "no-reply@mail.sgmuaythai.org"
                administrator = settings.COMPANY_EMAIL
                msg = EmailMultiAlternatives(subject, text_content, sender, [administrator])
                msg.send()
                messages.success(request, "Your enquiry has been successfully sent, we'll be in touch soon!")
                return HttpResponseRedirect(reverse('home'))
            except ValidationError as e:
                return HttpResponse(e)
        else:
            return render(request, "payment/payment/oops.html")
        
    else:
        contact_form = ContactForm()
        return render(request, 'story/contactform.html',{
            "contact_form" : contact_form,
            "items":items
        })
