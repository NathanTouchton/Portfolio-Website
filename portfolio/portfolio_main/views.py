from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class HomepageView(TemplateView):
    """This is the view for displaying the homepage."""
    template_name = "portfolio_main/homepage.html"

def email_view(request):
    """This sends an email when submitting the form on the contact page."""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = "Contact form submission"

        send_mail(
            subject=subject,
            message=f"Name: {name}, email: {email}, message\n\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["ntouchton@protonmail.com"],
            fail_silently=False,
        )
    return HttpResponseRedirect(reverse("portfolio:home"))
