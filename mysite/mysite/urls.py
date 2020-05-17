"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import pyrebase


#this config has been used for flask project also
firebaseConfig = {
    "apiKey": "AIzaSyBch3rJHdrjwxzJzl-644FLtjLteaEKVqU",
    "authDomain": "django-project-90f04.firebaseapp.com",
    "databaseURL": "https://django-project-90f04.firebaseio.com",
    "projectId": "django-project-90f04",
    "storageBucket": "django-project-90f04.appspot.com",
    "messagingSenderId": "578131955207",
    "appId": "1:578131955207:web:c0695cf66586c8303fe4a2",
    "measurementId": "G-25D5PVMCW1",
    "serviceAccount": "/root/Downloads/django-project-90f04-firebase-adminsdk-q72wc-375d8b509c.json"
} 


# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(firebaseConfig)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
