# goal: given 2 words, check if they are anagrams of each other and find a sequence that will convert the first one
# to the other
#
# e.g.
# eric and rice
# we can do push, push, pop, push, pop, etc



from collections import deque


w1 = "madam"
w2 = "adamm"

# given a length of a string, come up with all possible sequences

seq = []
temp = []
#npush, npop = 0, 0



final_seq = []
seq2 = []
def gen_seq2(seq, wl):

    numi = seq.count("i")
    numo = seq.count("o")

    if numi == wl and numo == wl:
        print (seq)
        final_seq.append(seq[:])
        return

    if numi == numo:
        seq.append("i")
        gen_seq2(seq, wl)
        seq.pop()
    elif numi == wl : # max # of pushes
        seq.append("o")
        gen_seq2(seq, wl)
        seq.pop()
    else: # numi > numo
        if numi < wl :
            seq.append("i")
            gen_seq2(seq, wl)
            seq.pop()
        if numo < wl :
            seq.append("o")
            gen_seq2(seq, wl)
            seq.pop()


gen_seq2(seq2, len(w1))

#gen_seq(len(w1))
for x in seq:
    print (x)



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


print ("w1: ", w1, "w2: ", w2)
for i in final_seq:
    ret = check_seq(w1, w2, i)
    #print (ret)
    if ret == w2:
        print ("Good seq: ", i)



















x = check_seq(w1, w2, ["i", "i", "o", "i", "o", "i", "o", "o"])
#print (x)
x = check_seq(w1, w2, ["i", "o", "i", "o", "i", "o", "i", "o"])
#print (x)
