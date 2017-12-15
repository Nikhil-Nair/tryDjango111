from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
    title = "Sign Up!"
    form = SignUpForm(request.POST or None)

    context = {
        "title" : title,
        "form" : form

    }

    if form.is_valid():
        instance = form.save(commit = False)
        if not instance.full_name:
            instance.full_name = "Justin"
        instance.save()
        context = {
            "title" : "Thank You!",

        }


    return render(request, "home.html", context)

def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")


        subject = "Site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,'yourotheremail@email.com']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email
        )
        send_mail(subject,
         contact_message,
         from_email,
         [to_email],
         fail_silently=False
        )


    context = {
        "form" : form,
        "title" : title
    }
    return render(request, "forms.html", context)
