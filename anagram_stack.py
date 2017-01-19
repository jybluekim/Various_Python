# goal: given 2 words, check if they are anagrams of each other and find a sequence that will convert the first one
# to the other
#
# e.g.
# eric and rice
# we can do push, push, pop, push, pop, etc



from collections import deque
import random

w1 = "kim"

l = list(w1)
random.shuffle(l)
w2 = "".join(l)

#w2 = "eric"

# given a length of a string, come up with all possible sequences

seq = []

# global data
final_seq = []

def gen_seq(seq, wl):

    numi = seq.count("i")
    numo = seq.count("o")

    if numi == wl and numo == wl:
        #print (seq)
        final_seq.append(seq[:])
        return

    if numi == numo:
        seq.append("i")
        gen_seq(seq, wl)
        seq.pop()
    elif numi == wl : # max # of pushes
        seq.append("o")
        gen_seq(seq, wl)
        seq.pop()
    else: # numi > numo
        if numi < wl :
            seq.append("i")
            gen_seq(seq, wl)
            seq.pop()
        if numo < wl :
            seq.append("o")
            gen_seq(seq, wl)
            seq.pop()






def check_seq(w1, w2, seq):
    S = list()
    T = list()
    ptr = 0
    for i in seq:
        if i == "i":
            S.append(w1[ptr])
            ptr += 1
        elif i == "o":
            pop = S.pop()
            T.append(pop)
    return "".join(T)



gen_seq(seq, len(w1))

print ("w1: ", w1, "w2: ", w2)
for i in final_seq:
    ret = check_seq(w1, w2, i)
    #print (ret)
    if ret == w2:
        print ("Good seq: ", i)



