from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
from pusher_push_notifications import PushNotifications
from newsapi import NewsApiClient
import pprint
import requests
import pyrebase


#authentication part has been done with flask project with nandanpandeysmvdu@gmail.com
#this django project is being done with artificial intelligence work@gmail.com
# note : image size of nearly 150kb can be uploaded on storage of firebase successfully


#get service account as json from firebase so that u can enter data in database
firebaseConfig = {
    "apiKey": "AIzaSyBch3rJHdrjwxzJzl-644FLtjLteaEKVqU",
    "authDomain": "django-project-90f04.firebaseapp.com",
    "databaseURL": "https://django-project-90f04.firebaseio.com",
    "projectId": "django-project-90f04",
    "storageBucket": "gs://django-project-90f04.appspot.com",
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




def uploader(request):
    return render(request,'myapp/upload.html')    



def push_notify(name,progress,work):

    pn_client = PushNotifications(instance_id='d01b2036-e93f-4125-9842-599b86adf848',secret_key='A3A80F519C3087269057B0660CD7DF4ED50E6F63EA413983BEA26B31297AE7D3')
    response = pn_client.publish(interests=['hello'],publish_body={'apns': {'aps': {'alert': 'Report Created'}},'fcm': {'notification': {'title': str(name), 'body': 'Progress: '+str(progress) +" work: " +str(work) }}})
    print(response['publishId'])



def post_create(request):
    work = request.POST.get('work')
    progress =request.POST.get('progress')

    url = request.POST.get('url')
    data = {"work":work,'progress':progress,'url':url}
    push_notify(url,progress,work)
    database.child('users').child('reports').set(data)
    name = database.child('users').child('reports').child('url').get().val()
    return render(request,'myapp/welcome.html',{'i':name})

