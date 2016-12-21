import random

#ords = ["luna", "shadow", "alexis", "andrew", "phatom", "forces", "lawn" ]

words = ["luna", "shadow", "alexis" ]


n = 8
m = 10

list = []

# initalized list
for i in range(n):
    l = [ "-" for j in range(m)]
    list.append(l)

# populate the list

for w in words:

    for i in range(n):
        print(list[i])

    length = len(w)

    x = random.randint(0, m-1)
    y = random.randint(0, n-1)

    print("Word: ", w, ", Length: ", length, ", X: ", x, ", Y: ", y)

    loop = True
    while loop:
        clean = True
        # 0 is left, 1 is up, 2 is right, 3 is down
        dir = random.randint(0,3)
        if dir == 0:
            endx = x - length
            if endx <= 0:
                continue
            else:
                for k in range(length):
                    nextl = list[y][x-k]
                    print ("Next: ", nextl)
                    if nextl != '-':
                        print ("Conflict")
                        clean = False
                if clean:
                    for k in range(length):
                        list[y][x-k] = w[k]
                    loop = False
        elif dir == 1:
            endy = y - length
            if endy <= 0:
                continue
            else:
                for k in range(length):
                    nextl = list[y-k][x]
                    print ("Next: ", nextl)

                    if nextl != '-':
                        print("Conflict")
                        clean = False
                if clean:
                    for k in range(length):
                        list[y-k][x] = w[k]
                    loop = False

        elif dir == 2:
            endx = x + length
            if endx > m-1:
                continue
            else:
                for k in range(length):
                    nextl = list[y][x+k]
                    print ("Next: ", nextl)

                    if nextl != '-':
                        print("Conflict")
                        clean = False
                if clean:
                    for k in range(length):
                        list[y][x + k] = w[k]
                    loop = False
        elif dir == 3:
            endy = y + length
            if endy > n-1:
                continue
            else:
               for k in range(length):
                   nextl = list[y+k][x]
                   print("Next: ", nextl)

                   if nextl != '-':
                        print("Conflict")
                        clean = False
               if clean:
                    for k in range(length):
                        list[y + k][x] = w[k]

                    loop = False



                        #@elif dir == 1:



# print the contents
for i in range(n):
    print (list[i])



#for i in words:
#    print (i)



