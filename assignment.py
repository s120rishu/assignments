#question1:-
#Access Tokens :- Access tokens are the thing that applications use to make API requests on behalf of a user.
# It represents the authorization of a specific application to access specific parts of a user's data.
#Access tokens must be kept confidential in transit and in storage.
'''
consumer_key="kJ265aBQRlOtLDlJopV8gq6cv"
consumer_secret="qOqLdg4x76Q7rIBG65ymhXSZCJ9BW55PeBYwlrEgvMVJnrbXaY"
access_token="2637240448-rQtSdBwXl0fqaR5EqBDhZJDT3kFVnuO2uMx8dgm"
access_secret="USV2SVNRz1zNQlrbimqw1y0DIKpTF8BgMjHniMRTt5u5D"

#question2:-

#IP Address of wynk	151.101.34.25
#IP Address of flipkarat 163.53.78.128
#IP Address of Snapchat 216.58.217.115

#question3:-
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth = tweepy.OAuthHandler(consumer_key ,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#modi"))
print(api.get_user("@SumitSinghDhima"))
#question4:-
#library:- It is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)
# API:- It is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)


#Library:It is written in same language which is collection of all the function required
#API: It can be written in any language

#Library: It contains re-usable chunks of code
#API:The re-usable codes of library is linked to our program through API

#Library:-Every library has API that defines how it will interact with external code.

#API:-It is sum of all public/exported stuff.
#question5:-
'''
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp(api_key='e946d3fe76334b5a934be2b70615a194')
model = app.models.get('general-v1.3')
image = ClImage(url='https://tse3.mm.bing.net/th?id=OIP.a3rNho7KbBXBv0_xciCHjQHaE5&pid=15.1&P=0&w=262&h=174')
model.predict([image])
