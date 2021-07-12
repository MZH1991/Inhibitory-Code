import numpy as np
import matplotlib.pyplot as plt
import math
Allomatrix = np.array([[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]])
Direction = ['up', 'upright', 'right', 'downright','down','downleft','left','upleft']
Direction0 = ['up', 'upright', 'right', 'downright','down','downleft','left','upleft']
Allo = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4])

total = 0
correct = 0
incorrect = 0
random_va = 0
pixa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,32]
pixB = [1,2,4,8,16,32]
for pix in range(1,33):

    for numk in range(1,501):

        random_va = np.random.randint(0,16)  #随机1~100的值

        total = total + 1   
        # random_va = np.random.randint(1,7001)  #随机1~100的值

        bkgrate = 8
        oripixel1 = np.random.randint(1,5)
        oripixel= np.power(2, oripixel1)



        k01 = 6
        k02 = Allo[k01]
        noipixel = math.ceil(oripixel*k02) 




        file1 = 'G:/Data Base17/learning/' + str(pix) + '/before/' + str(numk) + '.txt'
        file2 = 'G:/Data Base17/learning/' + str(pix) + '/after/' + str(numk) + '.txt'
        file3 = 'G:/Data Base17/learning/' + str(pix) + '/label/' + str(numk) + '.txt'
        # file1 = 'G:/Data Base/learning/shift40160/before/' + str(numk) + '.txt'
        # file2 = 'G:/Data Base/learning/shift40160/after/' + str(numk) + '.txt'
        # file3 = 'G:/Data Base/learning/shift40160/label/' + str(numk) + '.txt'
        a = np.loadtxt(file1,dtype = int)
        b = np.loadtxt(file2,dtype = int)
        c = np.loadtxt(file3,dtype = int)
        loc = np.nonzero(b)
        loc = np.array(loc)
        nums = loc.shape[1]
        K = 0
        c1 = 0

        for num1 in range(8):
            Direction[num1] = 0
            for num2 in range(nums):
                E1 = a[loc[:,num2][0]-Allomatrix[num1][0],loc[:,num2][1]+Allomatrix[num1][1]]    #因为坐标是从左上角开始的，所以需要横坐标加1，纵坐标减1.
                E2 = a[loc[:,num2][0]+Allomatrix[num1][0],loc[:,num2][1]-Allomatrix[num1][1]]

                if (E2 == 1)&(E1 != 1):
                    Direction[num1] = Direction[num1] + 1
                else:
                    K = 0

                # if E2 == 1:
                #     Direction[num1] = Direction[num1] + 1
                # else:
                #     K = 0
        aao = np.argmax(Direction)
        OD = np.zeros((1,8))
        OD[:,aao] = 1

        if (OD == c).all():
            correct = correct + 1
        else:
            incorrect = incorrect + 1


print(total)
print(correct)
print(incorrect)
