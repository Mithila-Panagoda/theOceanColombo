import pyrebase

from theOceanColombo.views import firebase

firebaseConfig={'apiKey': "AIzaSyBew42hA7iZHy7zs47WMqIg-GSBnxP-ttM",
    'authDomain': "theoceancolombo-c128a.firebaseapp.com",
    'databaseURL': "https://theoceancolombo-c128a.firebaseio.com",
    'projectId': "theoceancolombo-c128a",
    'storageBucket': "theoceancolombo-c128a.appspot.com",
    'messagingSenderId': "925636680144",
    'appId': "1:925636680144:web:da1ab5d4f3b0d3231b01d5",
    'measurementId': "G-YH7TV23J8J"}

pyrebase.initialize_app(firebaseConfig)
#db=firebase.database()
authe = firebase.auth()

email="mithilapanagoda@gmail.com"
pwd ="123456789"

authe.create_user_with_email_and_password(email,pwd)
