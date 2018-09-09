f=open('RemovedBlanksMerge.txt','r')
lines=f.readlines()
Word1=None
wordC=None
prevWord=""
for line in lines:
#    line=",".join(line.split(',1,'))
#    line=",".join(line.split(',2,'))
#    print(line)
    if int(line.split(',')[1])==1:
        wordC="[{0}".format(line.rpartition("[")[2])
        Word1=line.split(',')[0].rstrip()
    if int(line.split(',')[1])==2:
        if (line.split(',')[0].rstrip()!=prevWord):
            index=line.split(',')[2]
            New_Word=line.split(',')[0].rstrip()
            if (New_Word!=prevWord):
                wordC=wordC.replace(',','')
                print("{0},{1},{2}".format(int(index),Word1.rstrip(),wordC))
            prevWord=line.split(',')[0].rstrip()
#        print(wordC)

#    while int(line.split(',')[1])==2:
#        print("{0},{1},{2}".format(int(line.rpartition(",")[2]),line.split(",")[0], wordC))
