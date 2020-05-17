from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse

from newsapi import NewsApiClient
import pprint
import requests
import pyrebase


#get service account as json from firebase
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

authe = firebase.auth()
database=firebase.database()

# Create your views here.
def index(request):
    # add myapp in installed apps list in mysite 'settings'

    # Init
    # url = 'https://newsapi.org/v2/everything?'
    # parameters = {
    # 'q': 'big data', # query phrase
    # 'pageSize': 20,  # maximum is 100
    # 'apiKey': '992d09763cc4473d8612788b6ddc1326'
    # }


    # response = requests.get(url, params=parameters)

    # # Convert the response to JSON format and pretty print it
    # response_json = response.json()
    # pprint.pprint(response_json)


    json_obj = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=992d09763cc4473d8612788b6ddc1326').json()
    # print(json_obj)


    articles = json_obj['articles']

    print(type(articles))
    for i, article in enumerate(articles):

        source= article['source']['name']
        title= article['title']
        description = article['description']
        url = article['url']
        urlToImage= article['urlToImage'] 
        data = {"source":source,"title":title,"description":description,"url":url,"urlToImage":urlToImage}
        database.child('news').child(i).set(data)
    # from win32com.client import Dispatch 
    # speak = Dispatch("SAPI.Spvoice") 
    # speak.Speak(d)  
    #name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request, 'myapp/index.html')