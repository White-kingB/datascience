fname = input('Enter File:  ')
if len(fname)<1 : fname = 'code3-clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        #print('**', w , di.get(w,-99))

#if the key is not there the count is zero
        #oldcount = di.get(w,0)
        #print(w,'old',oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount
        #print(w,'NEW',newcount)

        #idiom = retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,'NEW',di[w])

        #if w in di :
            #di[w] = di[w] + 1
            #print('**Existing**')
        #else:
            #di[w] = 1

            #print ('**NEW**')
        #print (w , di[w])

#print(di)

#NOW TO FIND THE MOST COMMON WORD
largest = -1
theword = None
for k,v in di.items() :
    #print (k,v)
    if v > largest :
        largest = v
        theword = k #capture/remember the key that was largest
print (theword, largest)
