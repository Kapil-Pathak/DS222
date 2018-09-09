import csv
def OutPutCurrentK():
    if currentK is not None:
        print("{0},1,{1}".format(currentK, wordCount))
currentK=None
wordCount=[]
filename="NewDictionary.csv"
with open(filename, 'r') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    for row in csv_read:
        if row[0]==currentK:
            wordCount.append((row[1],int(row[2])))
        else:
            OutPutCurrentK()
            currentK=row[0]
            wordCount=[]
            wordCount.append((row[1],int(row[2])))
    OutPutCurrentK()
