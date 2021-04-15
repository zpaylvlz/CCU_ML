import random
import numpy as np
import matplotlib.pyplot as plt  
import csv
import time


def checkPLA (wt,x_c,y_c,l_c):
    result = None
    for i in range(len(x_c)):
        datap = [float(x_c[i]), float(y_c[i])]
        datap = np.array(datap)
        if int(np.sign(wt.T.dot(datap))) != l_c[i]:
            result =  datap, l_c[i]
            return result
    return result
    
if __name__ == '__main__':
    current = time.time()
    x_coor = []
    y_coor = []
    label = []
    with open('data_Q3.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            x_coor.append(float(row[0]))
            y_coor.append(float(row[1]))
            label.append(int(row[2]))
    iteration = 0
    w = np.array([0.0,0.0])
    while checkPLA(w,x_coor,y_coor,label) is not None:
        
        
        datas,lr = checkPLA(w,x_coor,y_coor,label)
        w += datas * lr
        iteration+=1
        if(iteration > 100000):
            break;
    end = time.time()
    print(end - current,"seconds")
    print("iterations:",iteration)
    pla_x = np.arange(600)
    pla_y,pla_b = -w[0]/w[1], -1/w[1]
    plt.plot(pla_x, pla_y*pla_x + pla_b)
    plt.plot(x_coor[:1000], y_coor[:1000], 'o', color='blue')
    plt.plot(x_coor[1000    :], y_coor[1000:], 'o', color='red')
    plt.show()
