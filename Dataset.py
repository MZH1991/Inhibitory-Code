import numpy as np
import matplotlib.pyplot as plt
import math
import os

Allomatrix = np.array([[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]])
def move(direction, img):
    assert direction in [-1, 0, 1], "direction should be in [-1, 0, 1]"
    if direction == 0:
        return img
    elif direction == 1: #move up 1 block
        return np.concatenate((img[1:], np.zeros(img.shape[1]).reshape(1, -1)), axis = 0)
    elif direction == -1:
        return np.concatenate((np.zeros(img.shape[1]).reshape(1, -1), img[:-1]), axis = 0)
ims = 32 #imagesize
gap = 3
sugap = ims - gap 
pixstart = 1
pixend = 1
pixa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,32]
# for pix in range(pixstart,pixend+1):
for pix in range(1,33):

    folder1 = 'G:/Data Base17/learning/' + str(pix) + '/before/'
    folder2 = 'G:/Data Base17/learning/' + str(pix) + '/after/' 
    folder3 = 'G:/Data Base17/learning/' + str(pix) + '/label/'
    if not os.path.exists(folder1):
        os.makedirs(folder1)
    if not os.path.exists(folder2):
        os.makedirs(folder2)
    if not os.path.exists(folder3):
        os.makedirs(folder3)

    numo = 501
    for numk in range(1,numo):
        a = np.zeros((ims,ims))
        i = np.random.randint(gap,sugap)
        j = np.random.randint(gap,sugap)
        a[i][j] = 1
        indexQ = [[i,j],[i,j]]
        indexQ = np.array(indexQ)
        num = 1
        rownum = indexQ.shape[0]
        while rownum < pix + 1 :    
            m = np.random.randint(-1,2)
            n = np.random.randint(-1,2)

            k = np.random.randint(1,rownum)
            mn = indexQ[k,:]
            i = mn[0]
            j = mn[1]
            i = i + m
            j = j + n      
            mn = [i,j]
            judge = mn in indexQ.tolist()       
            if  judge or i < gap or i > sugap or j < gap or j > sugap :
                pix = pix
            else:
                indexQ = np.row_stack((indexQ, mn))
                a[i][j] = 1
            rownum = indexQ.shape[0]
        b = a
        Matran = np.random.randint(0,8)
        ODC = Allomatrix[Matran,:]
        ODA = Matran
        b = move(ODC[0], b)  # move in straight direction
        b = b.T 
        b = move(-ODC[1], b)  # move in horizonal direction
        b = b.T   

        OD = np.zeros((1,8))
        OD[:,Matran] = 1

        file1 = 'G:/Data Base17/learning/' + str(pix) + '/before/' + str(numk) + '.txt'
        file2 = 'G:/Data Base17/learning/' + str(pix) + '/after/' + str(numk) + '.txt'
        file3 = 'G:/Data Base17/learning/' + str(pix) + '/label/' + str(numk) + '.txt'
        np.savetxt(file1,a,fmt='%d',delimiter=' ')
        np.savetxt(file2,b,fmt='%d',delimiter=' ')
        np.savetxt(file3,OD,fmt='%d',delimiter=' ')