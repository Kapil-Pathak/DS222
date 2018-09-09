import re
from nltk.corpus import stopwords
import nltk
stop_words = stopwords.words('english')
def text_processing(line):
    s=re.sub(r'<.+?>', '', line)
    s =re.sub("\d+", "", s)
    s=s.replace('@en .', '')
    s= re.sub(r'[\(\)\"\:\.\$\&\'\#\%\[\]\+\!\\]','',s)
    s=s.replace('\n','')
    return s

while (1):
    try:
        print(input())
    except EOFError:
        break
f=open('verysmall_test.txt','r')
lines=f.readlines()
lines=lines[3:]
id=0
for line in lines:
    line=text_processing(line)
    line=line.lower()
#    line.split('\t')[1]=text_processing(line.split('\t')[1])
    line1="".join(line.split('\t')[1].split(','))
#    print(line)
    id+=1
    for word in line1.split():
        if word not in stop_words:
            word = ("".join(e for e in word if e.isalpha()))
            if word!=None:
                print("{0},2,{1}".format(word.rstrip(),id))
