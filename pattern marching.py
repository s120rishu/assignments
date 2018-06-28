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

##optional question THIS question is not don yet

print("optional question")
print("desired_output=")
tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstat"
reg=re.compile("[!]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[R][T]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[@]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[T][h][e][N][e][x][t][W][e][b][:] ")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile(" [h][t][t][p][:][/][/][t][.][c][o][/][l][b][w][e][j][p][x][O][d]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[c][c][:][@][g][a][r][y][b][e][r][n][h][a][r][d][t][#][r][s][t][a][t]")
for i in sentence:
    tweet=reg.sub("",tweet)
print(tweet)
