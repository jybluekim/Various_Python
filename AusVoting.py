

# input: list of candidates and list of results
def ausvoting(result_list):

    DBG  =  0
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

        if DBG:
            print ("counter: ", counter)

        max, maxind = 0, 0
        maxlist = []

        min = num_voters

        # find who is the max
        for i in range(1, num_cand+1):
            if counter[i] > max:
                max = counter[i]
                #maxind = i
            if counter[i] <= min and counter[i] != -1:
                min = counter[i]

        # find who is the bottom (list)
        for i in range(1, num_cand+1):
            if counter[i] == min:
                minlist.append(i)
            if counter[i] == max:
                maxlist.append(i)

        if max >= num_voters / 2:
            if len(maxlist) == 2:
                if DBG:
                    print ("There is a 50:50 tie between these two: ", maxlist)
            else:
                if DBG:
                    print ("Winner is: ", maxind)
                    print ("Total cand: ", num_cand, ", eliminated cand: ", len(minlist) - 1, "votes earned: ", counter[maxlist[0]])
            return maxlist, iter
        else: # no clear winner

            iter += 1
            if DBG:
                print("No winner in iteration # ", iter)
                print ("Eliminated list: ", minlist)
            # get rid of bottom candidate(s)



if __name__ == "__main__":

    import random

    num_cand = 10
    num_voters = 10000

    for x in range (10):

        list = []
        for i in range(num_voters):
            slist = [j for j in range(1, num_cand + 1)]
            random.shuffle(slist)
            list.append(slist[:])

    #print(list)

        win, iter = ausvoting(list)
        print ("Winner: ", win, "# of iterations: ", iter)

