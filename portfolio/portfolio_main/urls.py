from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.HomepageView.as_view(), name="home"),
    path("contact/", views.email_view, name="contact"),
]
