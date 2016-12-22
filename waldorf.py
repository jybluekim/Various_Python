import random

#words = ["luna", "shadow", "alexis", "andrew", "phantom", "forces", "lawn", "dog", "cat" ]

NUM_WORDS = 10
# m is col width
# n is row count
n = 8
m = 10

list = []



words = []
dict = { }
with open("make_you_feel_my_love.txt", 'r') as file:
    for l in file:
        tl = l.split()
        for t in tl:
            if len(t) >= 4 and t.isalpha() and len(t) <= n and len(t) <= m:
               dict[t.lower()] = 1

print ("# words: ", len(dict.keys()))
print (dict.keys())

words = random.sample(dict.keys(), NUM_WORDS)
print (words)
#words = ["luna", "shadow", "alexis" ]

def outof_bounds(val, ref, pol):
    if pol == 0: # val >= ref
        if val >= ref:
            return True
        else:
            return False
    else: # val < ref
        if val < ref:
            return True
        else:
            return False


def is_path_clear(word, x, y, xdir, ydir):
    for k in range(len(word)):
        xnext, ynext = x, y
        if xdir == 1: # increase
            xnext = x + k
        elif xdir == -1: # decrease
            xnext = x - k
        if ydir == 1: # increase
            ynext = y + k
        elif ydir == -1: # decrease
            ynext = y - k

        nextl = list[ynext][xnext]
        # print ("Next: ", nextl)
        if nextl != '-' and nextl != w[k]:
            return False
    return True

def fill_word(w, x, y, xdir, ydir):
    for k in range(len(w)):
        xnext, ynext = x, y
        if xdir == 1:  # increase
            xnext = x + k
        elif xdir == -1:  # decrease
            xnext = x - k
        if ydir == 1:  # increase
            ynext = y + k
        elif ydir == -1:  # decrease
            ynext = y - k

        nextl = list[ynext][xnext]

        list[ynext][xnext] = w[k]




# initialize list
for i in range(n):
    l = [ "-" for j in range(m)]
    list.append(l)


dir_counter = [0 for i in range(8)]

# populate the list

for w in words:

    #for i in range(n):
     #   print(list[i])

    length = len(w)


    loop = True
    count = 0

    while loop:


        # we are picking a random starting point, then direction for each iteration
        x = random.randint(0, m - 1)
        y = random.randint(0, n - 1)
        count += 1
        #print("Word: ", w, ", Length: ", length, ", X: ", x, ", Y: ", y)

        clean = True
        # 0 is left, 1 is up, 2 is right, 3 is down
        # 4 is nw, 5 is ne, 6 is se, 7 is sw
        dir = random.randint(0,7)
        #print ("dir: ", dir)

        dir_counter[dir] += 1
        if dir == 0:
            if outof_bounds(x-length, 0, 1):
                continue
            else:

                if is_path_clear(w, x, y, -1, 0):
                    fill_word(w, x, y, -1, 0)
                    loop = False

        elif dir == 1:
            if outof_bounds(y-length, 0, 1):
                continue
            else:
                if is_path_clear(w, x, y, 0, -1):
                    fill_word(w, x, y, 0, -1)
                    loop = False

        elif dir == 2:
            if outof_bounds(x+length, m, 0):
                continue
            else:
                if is_path_clear(w, x, y, 1, 0):
                    fill_word(w, x, y, 1, 0)
                    loop = False
        elif dir == 3:
            if outof_bounds(y+length, n, 0):
                continue
            else:
               if is_path_clear(w, x, y, 0, 1):
                   fill_word(w, x, y, 0, 1)
                   loop = False

        # nw
        elif dir == 4:
            endx = x - length
            endy = y - length
            if outof_bounds(endx, 0, 1) or outof_bounds(endy, 0, 1):
                continue
            else:
                if is_path_clear(w, x, y, -1, -1):
                    fill_word(w, x, y, -1, -1)
                    loop = False

        # ne
        elif dir == 5:
            endx = x + length
            endy = y - length
            #if endx > n - 1 or endy < 0:
            if outof_bounds(endx, n, 0) or outof_bounds(endy, 0, 1):
                continue
            else:
                if is_path_clear(w, x, y, 1, -1):
                    fill_word(w, x, y, 1, -1)
                    loop = False

        # se
        elif dir == 6:
            endx = x + length
            endy = y + length
            if outof_bounds(endx, m, 0) or outof_bounds(endy, n, 0):
                continue
            else:
                if is_path_clear(w, x, y, 1, 1):
                    fill_word(w, x, y, 1, 1)
                    loop = False

        # sw
        elif dir == 7:
            endx = x - length
            endy = y + length
            #if endx < 0 or endy >  n - 1:
            if outof_bounds(endx, 0, 1) or outof_bounds(endy, n, 0):
                continue
            else:
                if is_path_clear(w, x, y, -1, 1):
                    fill_word(w, x, y, -1, 1)
                    loop = False

# print the contents
#for i in range(n):
#    print (list[i])
    #print ("Word: ", w, ", Attempts: ", count)

print ("Dir counter: ", dir_counter)

for i in range(n):
    a = "".join(list[i])
    print (a)
print ("")
#for w in words:
#    print (w)
#for i in words:
#    print (i)



