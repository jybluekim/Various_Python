import random

num_cand = 5
num_voters = 10

list = []
for i in range (num_voters):
    slist = [ j for j in range(1, num_cand + 1 )]
    random.shuffle(slist)
    list.append(slist[:])


print (list)


# input: list of candidates and list of results
def ausvoting(result_list):

    # check if we have a clear winner - just count #1 and see if it is 50% or higher
    #   If not... need to eliminate bottom vote getters. Identify them first
    #       then re-count while ignoring the bottom vote getters



    counter = [ 0 for i in range (num_cand + 1)]


    for i in result_list:
        counter[i[0]] += 1

    print ("counter: ", counter)

    max, maxind = 0, 0
    min = num_voters
    minlist = []

    for i in range(1, num_cand+1):
        if counter[i] > max:
            max = counter[i]
            maxind = i
        if counter[i] <= min:
            min = counter[i]

    for i in range(1, num_cand+1):
        if counter[i] == min:
            minlist.append(i)


    if max >= num_voters / 2:
        print ("Winner is: ", maxind)
        return
    else: # no clear winner
        # get rid of bottom candidate(s)
        for i in minlist:
            for j in result_list:
                topop = 0
                for k in range(len(j)):
                    if j[k] == i:
                        topop = k
                j.pop(topop)




    print ("max ind: ", maxind)
    print ("min list: ", minlist)


    print(result_list)
    ausvoting(result_list)



ausvoting(list)
