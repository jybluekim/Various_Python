

k = 0
for i in range(10):
    for j in range(10):
        x = '8' + str(i) + '65' + str(j)
        y = int(x)
        if y % 24 == 0:
            print (k, ": ", y)
        k += 1


