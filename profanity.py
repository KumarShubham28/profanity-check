while True:
    words = []
    racial_slurs =["amateur", "anal", "angry", "arse"]
    filename = input('Enter the file name ')
    try:
        fhand = open(filename)
    except:
        print('filename does not exist')
        continue
    for file in fhand:
        words.append(file.strip().split())
    for i in words:
        total = 0
        a=[]
        for j in range(len(i)):
            for k in racial_slurs: 
                if(i[j] == k):
                    total +=1
        if(len(i) > 0):
            a.append(total)
            print('degree of profanity = ', total/len(i))
            