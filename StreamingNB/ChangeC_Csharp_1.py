while(1):
    try:
        print("{0},{1},{2}".format(input().split(',')[0].rpartition("=")[2].rstrip(),input().split(',')[0].rstrip(),input().split(',')[1].rstrip()))
    except EOFError:
        break
