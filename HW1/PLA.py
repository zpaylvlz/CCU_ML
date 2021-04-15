import random
import numpy as np
import matplotlib.pyplot as plt  


it = 0
def rand_seed(m, b, num=2):
    # create empty list
    x_coor = []
    y_coor = []
    label = []
    # positive and negtive point number
    pos_num = int(num / 2)
    neg_num = num - pos_num
    # random create point
    for i in range(pos_num):
        x = random.randint(0, 30)
        r = random.randint(1, 30)
        y = m * x + b - r
        # save the coordinate of x and y
        x_coor.append(x)
        y_coor.append(y)
        # save label, right=1, left=0
        label.append(1 if m >= 0 else -1)

    for i in range(neg_num):
        x = random.randint(0, 30)
        r = random.randint(1, 30)
        y = m * x + b + r
        x_coor.append(x)
        y_coor.append(y)
        label.append(-1 if m >= 0 else 1)
    return x_coor, y_coor, label


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
    # set value of m and b 
    #m, b = 4, 3
    m = random.randint(-4.0,4.0)
    b = random.randint(0, 5)
    # plot the function curve
    x = np.arange(30)   # x = [0, 1,..., 29]
    y = m * x + b
    # plot the random point
    # blue for positive and red for negative
    x_coor, y_coor, label = rand_seed(m, b, num=30)
    w = np.array([0.0,0.0])
    iteration = 0
    while checkPLA(w,x_coor,y_coor,label) is not None:
        datas,lr = checkPLA(w,x_coor,y_coor,label)
        w += datas * lr
        iteration+=1
        if(iteration > 300):
            break;
    
    print("iterations:",iteration)
    pla_x = np.arange(30)
    pla_y,pla_b = -w[0]/w[1], -1/w[1]
    plt.plot(pla_x, pla_y*pla_x + pla_b)
    plt.plot(x_coor[:15], y_coor[:15], 'o', color='blue')
    plt.plot(x_coor[15:], y_coor[15:], 'o', color='red')
    plt.show()
