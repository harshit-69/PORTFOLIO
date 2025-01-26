from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("nlp/",views.nlp,name="nlp"),
     path("flask",views.flask,name="nlp"),
    path("about",views.about,name="about"),
    path('bi',views.bi,name="bi"),
    path('ml',views.ml,name="bi"),
    path("certificate",views.certificate,name="certificate"),
    path("contact",views.contact,name="contact")
]