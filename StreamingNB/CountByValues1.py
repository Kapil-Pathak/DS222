def OutPutCurrentKey():
    if currentKey is not None:
        print("{0},{1}".format(currentKey, sumForCurrentKey))

currentKey=None
sumForCurrentKey=0
while (1):
    try:
        if input().split(',')[0]==currentKey:
            sumForCurrentKey=sumForCurrentKey+int(input().split(',')[-1])
        else:
            OutPutCurrentKey()
            currentKey=input().split(',')[0]
            sumForCurrentKey=int(input().split(',')[-1])
    except EOFError:
        break
OutPutCurrentKey()
