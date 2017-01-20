import random

NUM_SLOTS = 100
NUM_FILLED = 13
NUM_PPL = 7
master = [ ]



for i in range(NUM_PPL):
    l = [0 for k in range(NUM_SLOTS)]
    l2 = [k for k in range(NUM_SLOTS)]
    l3 = random.sample(l2, NUM_FILLED)
    for k in l3:
        l[k] = 1

    master.append(l[:])

def dump_master():
    for i in range(NUM_PPL):
        print (master[i])


def find_slot(length):
    for i in range(NUM_SLOTS - length + 1):
        avail = True
        for j in range(NUM_PPL):
            if avail == False:
                break

            for k in range(length):
                if master[j][i+k] == 0:
                    pass
                else:
                    avail = False
                    break

        if avail == True:
            # mark the slots now
            for j in range(NUM_PPL):
                for k in range(length):
                    master[j][i+k] = 1
            return i
    return -1

dump_master()

for i in [1, 2, 3, 4]:

    print (find_slot(i))
    dump_master()
