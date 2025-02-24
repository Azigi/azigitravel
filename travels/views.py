from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_body = f"""
            You have received a new message:

            Name: {name}
            Phone: {phone}
            Email: {email}
            Subject: {subject}

            Message:
            {message}
            """

            try:
                send_mail(
                    subject=f"Contact Form Submission: {subject}",
                    message=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['azigitravel@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                logger.error(f"Email sending failed: {e}")
                messages.error(request, f"Failed to send your message: {e}")

            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def service_work_abroad(request):
    return render(request, 'service-details.html')

def service_study_abroad(request):
    return render(request, 'service-study-abroad.html')

def service_visa_assistance(request):
    return render(request, 'service-visa-assistance.html')

def service_flight_reservation(request):
    return render(request, 'service-flight-reservation.html')

def hotel_reservation(request):
    return render(request, 'hotel_reservation.html')

def passport_birth_certificate_support(request):
    return render(request, 'passport_birth_certificate_support.html')

