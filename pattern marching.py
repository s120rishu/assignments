import re
from typing import Any, Pattern

emails = '''
zuck26@facebook.com
page33@google.com"
jeff42@amazon.com'''
output=[]
output=re.findall("[\w]{1,20}",emails)
for i in output:
    print(i)


##Q2

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
output1=re.findall("[b|B][\w]{0,10}",text)
print(output1)

##q3
sentence = "A, very very; irregular_sentence"
match=re.compile("[,|;|_]")
sentence=match.sub(" ",sentence)
print(sentence)

##optional question
tweet ='''
Good advice! RT @TheNextWeb: What I would do differently if 
I was learning to code today 
http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
message=re.compile("[@|:|#|!]")
tweet=message.sub(" ",tweet)
l=re.findall("[http]")
print(tweet)