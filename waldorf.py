import random

words = ["luna", "shadow", "alexis", "andrew", "phantom", "forces", "lawn" ]

#words = ["luna", "shadow", "alexis" ]

# m is col width
# n is row count
n = 8
m = 10

list = []

# initalized list
for i in range(n):
    l = [ "-" for j in range(m)]
    list.append(l)

# populate the list

for w in words:

    #for i in range(n):
     #   print(list[i])

    length = len(w)


    loop = True
    count = 0

    while loop:

        x = random.randint(0, m - 1)
        y = random.randint(0, n - 1)
        count += 1
        #print("Word: ", w, ", Length: ", length, ", X: ", x, ", Y: ", y)

        clean = True
        # 0 is left, 1 is up, 2 is right, 3 is down
        # 4 is nw, 5 is ne, 6 is se, 7 is sw
        dir = random.randint(0,7)
        #print ("dir: ", dir)
        if dir == 0:
            endx = x - length
            if endx < 0:
                continue
            else:
                for k in range(length):
                    nextl = list[y][x-k]
                    #print ("Next: ", nextl)
                    if nextl != '-' and nextl != w[k]:
                        #print ("Conflict")
                        clean = False
                if clean:
                    for k in range(length):
                        list[y][x-k] = w[k]
                    loop = False
        elif dir == 1:
            endy = y - length
            if endy < 0:
                continue
            else:
                for k in range(length):
                    nextl = list[y-k][x]
                    #print ("Next: ", nextl)

                    if nextl != '-' and nextl != w[k]:
                        #print("Conflict")
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
                    #print ("Next: ", nextl)

                    if nextl != '-' and nextl != w[k]:
                        #print("Conflict")
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
                   #print("Next: ", nextl)

                   if nextl != '-' and nextl != w[k]:
                        #print("Conflict")
                        clean = False
               if clean:
                    for k in range(length):
                        list[y + k][x] = w[k]
                    loop = False

        # nw
        elif dir == 4:
            endx = x - length
            endy = y - length
            if endx < 0 or endy < 0:
                continue
            else:
                for k in range(length):
                    nextl = list[y - k][x - k]
                    if nextl != '-' and nextl != w[k]:
                        clean = False
                if clean:
                    for k in range(length):
                        list[y - k][x - k] = w[k]
                    loop = False

        # ne
        elif dir == 5:
            endx = x + length
            endy = y - length
            if endx > n - 1 or endy < 0:
                continue
            else:
                for k in range(length):
                    nextl = list[y - k][x + k]
                    if nextl != '-' and nextl != w[k]:
                        clean = False
                if clean:
                    for k in range(length):
                        list[y - k][x + k] = w[k]
                    loop = False

        # se
        elif dir == 6:
            endx = x + length
            endy = y + length
            if endx > m - 1 or endy > n - 1:
                continue
            else:
                for k in range(length):
                    nextl = list[y + k][x + k]
                    if nextl != '-' and nextl != w[k]:
                        clean = False
                if clean:
                    for k in range(length):
                        list[y + k][x + k] = w[k]
                    loop = False

        # sw
        elif dir == 7:
            endx = x - length
            endy = y + length
            if endx < 0 or endy >  n - 1:
                continue
            else:
                for k in range(length):
                    nextl = list[y + k][x - k]
                    if nextl != '-' and nextl != w[k]:
                        clean = False
                if clean:
                    for k in range(length):
                        list[y + k][x - k] = w[k]
                    loop = False

# print the contents
#for i in range(n):
#    print (list[i])
    print ("Word: ", w, ", Attempts: ", count)


for i in range(n):
    a = "".join(list[i])
    print (a)

#for i in words:
#    print (i)



