

l1 = [1,2,3,4]
l2 = [1,5,6,2]


for e in l1[:]:
    print(e)
    if e in l2:
        l1.remove(e)
        
        

        