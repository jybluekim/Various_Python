

def num2lcd(num, s):
    # x_x  x0x
    # |x|  1x2
    # x_x  x3x
    # |x|  4x5
    # x_x  x6x

    list = [0 for i in range (10)]
    list[0] = "1110111"
    list[1] = "0010010"
    list[2] = "1011101"
    list[3] = "1011011"
    list[4] = "0111010"
    list[5] = "1101011"
    list[6] = "1101111"
    list[7] = "1010010"
    list[8] = "1111111"
    list[9] = "1111011"

    outlist = [ []  for i in range(2*s + 3)]


    num = int(num)

    index = 0
    for i in range(2*s + 3):
        # first row
        if i == 0:
            if list[num][index] == "1":
                outlist[i] = " " + "_" * s  + " "
            else:
                outlist[i] = " " * (s + 2)
            index += 1
        # middle row
        elif i == int( (2*s + 3)/2 ):
            index += 2
            if list[num][index] == "1":
                outlist[i] = " " + "_" * s  + " "
            else:
                outlist[i] = " " * (s + 2)
            index += 1
        # last row
        elif i == 2*s + 2:
            index += 2
            if list[num][index] == "1":
                outlist[i] = " " + "_" * s  + " "
            else:
                outlist[i] = " " * (s + 2)
        # vertical rows - don't increment the index
        else:

            if list[num][index] == "1" and list[num][index+1] == "1":
                outlist[i] = "|" + " " * s + "|"
            elif list[num][index] == "1" and list[num][index+1] == "0":
                outlist[i] = "|" + " " * s + " "
            elif list[num][index] == "0" and list[num][index + 1] == "1":
                outlist[i] = " " + " " * s + "|"
    return outlist





def print_numstring(instr, s):

    x = ["" for i in range (2*s + 3)]
    for i in instr:

        a = num2lcd(i, s)

        for j in range(2*s + 3):
            x[j] = x[j] + " " + a[j]

    for i in range(2*s + 3):
        print (x[i])


print_numstring("0123456789", 2)
print_numstring("0123456789", 10)







