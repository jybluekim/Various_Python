import random


NUM_TUR = 5

weight = []
strength = []

#weight = [37, 47, 67, 83, 15]
#strength = [39, 181, 109, 187, 28]


def randomize():
    for i in range(NUM_TUR):
        w = random.randint(1,100)
        s = random.randint(w+1, 200)
        weight.append(w)
        strength.append(s)


randomize()


print (weight)
print (strength)

diff = []
for i in range(len(weight)):
    diff.append(strength[i] - weight[i])

print(diff)

def dfs(index):

    visited = [False for i in range(NUM_TUR)]

    stack = []
    stack.append(index)
    visited[index] = True


    ctr = 0
    while len(stack) > 0:
        i = stack.pop()
        print ("i: ", i)

        slack = strength[i] - weight[i]
        for j in range(NUM_TUR):
            if j == index:
                continue

            if weight[j] < slack and visited[j] == False:
                stack.append(j)
                visited[j] = True
                if len(stack) > 10:
                    exit(1)
                print (stack)
                print (visited)
                ctr += 1
        visited[i] = False

        if ctr > 10:
            break
dfs(0)


# find the one with largest slack (strength - own weight)
# function...
#    for each turtle that has NOT been used AND who weight <= current slack
#          pick 