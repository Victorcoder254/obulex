from django.shortcuts import render, redirect
from .models import *
from app_home.models import *

def contact_view(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        
        # Create a new ContactRequest instance and save it
        ContactRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        return redirect('contact-success')

    # Fetch footer and about info
    footer_info = FooterContactInfo.objects.first()

    context = {
        'footer_info': footer_info,
    }
    return render(request, 'files/contact.html', context)

def contact_success_view(request):
    # Fetch footer and about info
    footer_info = FooterContactInfo.objects.first()

    context = {
        'footer_info': footer_info,
    }
    return render(request, 'files/success.html', context)


