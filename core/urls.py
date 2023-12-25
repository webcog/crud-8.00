from django.urls import path
from core.views import home,about, faq

urlpatterns = [
   path("", home, name="home"),
   path("about/", about, name="about"),
   path("faq/", faq, name="faq"),
]