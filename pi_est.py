# estimate the value of pi
#
# given a small set of integers (call it n)
# the # of pairs is: n choose 2
# of those, the ratio of pairs that have only 1 has common factor to all pairs should be =~ 6/pi^2
# i.e. pi =~ sqrt (6 / the ratio)

NUM_INT = 10
import random

bigl = [i for i in range(2,30)]
l = random.sample(bigl, NUM_INT)


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime




def prime_fact(n):
    dict = {}
    div = 2
    if n < 1:
        return dict
    while True:
        if n == 1:
            break
        if n % div == 0 and is_prime(div):
            n = n / div
            if div in dict:
                dict[div] += 1
            else:
                dict[div] = 1
        else:
            div += 1
    return dict

#d = prime_fact(125)
#print (d)

total = 0
noint = 0
for i in range(len(l) - 1):
    for j in range(i, len(l) ):
        print ("i, j = ", l[i], l[j])
        total += 1

        x, y = 0, 0
        if l[i] < l[j]:
            x = l[i]
            y = l[j]
        else:
            x = l[j]
            y = l[i]
        d1 = prime_fact(x)
        d2 = prime_fact(y)
        print (d1, d2)
        s1 = set(d1.keys())
        s2 = set(d2.keys())
        intersection = s1 & s2
        if len(intersection) != 0:
            print ("\nIntersection: ", intersection)
            noint += 1
        else:
            print ("No intersection")

print ("List is: ", l)
print ("Total, Noint = ", total, noint)
print ("Pi is: ", (6 / (noint/total)) ** .5)

#for i in range(1,12):
    #d = prime_fact(i)
    #print (i, d)