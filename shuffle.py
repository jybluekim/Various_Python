from random import randint

SIZE = 10

a = []
b = [False] * SIZE


for i in range(SIZE):
    x = randint(0,SIZE-1)
    a.append(x)
    #b[x] = True

print (a)
print (b)



for i in range(SIZE):
    if b[a[i]] == True:
#        for j in range(SIZE):
        while True:
            x = randint(0, SIZE-1)
            if b[x] == False:
                a[i] = x
                b[x] = True
                break
    else:
        b[a[i]] = True



print (a)
print (b)
