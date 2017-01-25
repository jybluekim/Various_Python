


x = eval(input("Give me x: "))
y = eval(input ("Give me y: "))

z = x + y

print (z)


xs = str(x)
ys = str(y)

lx = len(xs)
ly = len(ys)

print ("# of digits for x: ", lx)
print ("# of digits for y: ", ly)

length = 0
if lx >= ly:
    length = lx
else:
    length = ly

carry = 0
num_carry = 0

for i in range(1, length + 1):
    ind = -1 * i
    print ("Index: ", ind)

    xv = 0
    yv = 0

    if i <= lx:
        xv = int(xs[ind])
    if i <= ly:
        yv = int(ys[ind])

    sum = xv + yv + carry
    if sum > 9:
        carry = 1
        num_carry += 1
    else:
        carry = 0

print ("num_carry: ", num_carry)

