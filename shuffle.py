from random import randint

import cProfile

SIZE = 100

a = []
b = [False] * SIZE


for i in range(SIZE):
    x = randint(0,SIZE-1)
    a.append(x)
    #b[x] = True

#print (a)
#print (b)

def fill_from_left():
    for j in range(SIZE):
        if b[j] == False:
            a[i] = j
            b[j] = True
            print ("exiting fill_from_left with j = " + str(j))
            return


def random_fill():
    numtry = 0
    while True:
        x = randint(0, SIZE - 1)
        #print("  trying random_fill with x = " + str(x))
        numtry += 1
        if b[x] == False:
            a[i] = x
            b[x] = True
            print("exiting random_fill with x = " + str(x) + ", # of tries: " + str(numtry))

            return


def fix():

    for i in range(SIZE):
        if b[a[i]] == True:
            random_fill()
        else:
            b[a[i]] = True


def fix2():

    for i in range(SIZE):
        if b[a[i]] == True:
            fill_from_left()
        else:
            b[a[i]] = True


cProfile.run("fix()")
#cProfile.run("fix2()")
