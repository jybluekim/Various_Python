import random

num_cand = 10
num_voters = 100

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

    minlist = []

    done = False


    iter = 1
    while done == False:

        counter = [0 for i in range(num_cand + 1)]

        # populate counter - do this again after each iter.
        for i in result_list:
            for j in i:
                if j in minlist:
                    pass
                else:
                    counter[j] += 1
                    break
        for i in minlist:
            counter[i] = -1

        print ("counter: ", counter)

        max, maxind = 0, 0
        min = num_voters

        # find who is the max
        for i in range(1, num_cand+1):
            if counter[i] > max:
                max = counter[i]
                maxind = i
            if counter[i] <= min and counter[i] != -1:
                min = counter[i]

        # find who is the bottom (list)
        for i in range(1, num_cand+1):
            if counter[i] == min:
                minlist.append(i)


        if max >= num_voters / 2:
            print ("Winner is: ", maxind)
            return
        else: # no clear winner
            print ("No winner in iteration # ", iter)
            iter += 1
            print ("Eliminated list: ", minlist)
            # get rid of bottom candidate(s)





ausvoting(list)
