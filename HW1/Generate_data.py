import random
import numpy as np
import matplotlib.pyplot as plt  
import csv

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
        x = random.randint(0, 600)
        r = random.randint(3, 600)
        y = m * x + b - r
        # save the coordinate of x and y
        x_coor.append(x)
        y_coor.append(y)
        # save label, right=1, left=0
        label.append(1 if m >= 0 else -1)

    for i in range(neg_num):
        x = random.randint(0, 600)
        r = random.randint(3, 600)
        y = m * x + b + r
        x_coor.append(x)
        y_coor.append(y)
        label.append(-1 if m >= 0 else 1)

    with open('data_Q3.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(2000):
            writer.writerow([x_coor[i],y_coor[i],label[i]])

    #return x_coor, y_coor, label

if __name__ == '__main__':
    # set value of m and b 
    #m, b = 4, 3
    m = random.randint(-4,4)
    b = random.randint(0, 5)
    # plot the function curve
    x = np.arange(500)   # x = [0, 1,..., 29]
    y = m * x + b
    
    # plot the random point
    # blue for positive and red for negative
    rand_seed(m, b, num=2000)
    
    
    
