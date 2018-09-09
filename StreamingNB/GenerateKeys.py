import re
import time
from nltk.corpus import stopwords
import nltk
stop_words = stopwords.words('english')
start=time.time()
def text_processing(line):
    s=re.sub(r'<.+?>', '', line)
    s =re.sub("\d+", "", s)
    s=s.replace('@en .', '')
    s= re.sub(r'[\(\)\"\:\.\$\&\'\#\%\[\]\+\!\?\-\\]','',s)
    s=s.replace('\n','')
    s=s.replace(';','')
    s=re.sub(r"\b[a-zA-Z]\b", "", s)
    #s=re.sub(r"[^a-zA-Z]","",s)

    return s
f=open('verysmall_train1.txt','r')
lines=f.readlines()
lines=lines[3:]
Vocab=set()
for line in lines:
    line=text_processing(line)
    line=line.lower()
    for title in line.split('\t')[0].split(','):
        print("Y1={0},{1}".format(title.rstrip(),1))
        print("Y=ANYTITLE,{0}".format(1))

    for word in line.split('\t')[1].split():
        word=re.sub(r"[^a-zA-Z]","",word)
        if word not in stop_words:
            Vocab.add(word)
            for title in line.split('\t')[0].split(','):

                print("Y={0} AND W={1},{2}".format(title.rstrip(),word.rstrip(),1))
                print("Y={0} AND W=ANYWORD,{1}".format(title.rstrip(),1))
end=time.time()
#print(end-start)
