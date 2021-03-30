import math
def zad7(x):
    index = 0
    tmp1 = []
    tmp2 = []
    tmp3 = []
    a1 = 0
    a2 = 0
    a3 = 0
    b1 = 0
    for i in range(len(x)):
        if len(x) % 2 !=0:
            index = math.floor(len(x)/2)
            #print(x[:index]) 
            tmp1.append(x[:index])
            tmp2.append(x[index+1:])
            for i2 in tmp1:
                a1 = sum(i2)
            for i3 in tmp2:
                a2 = sum(i3)

            tmp3.append(x[:-1])
            for i4 in tmp3:
                a3 = sum(i4)

    print("Punkt rownowagi: " + str(x[index]) + " i " + str(sum(i4)))
    print("Suma liczb po lewiej: " + str(a1))
    print("Suma liczb po prawiej: " + str(a2))
    # a = 3.5
    # print(math.floor(a))
tmp = [-7, 1, 5, 2, -4, 3, 0]
zad7(tmp)