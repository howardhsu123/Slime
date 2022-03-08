from re import X
from xmlrpc.client import FastUnmarshaller
import numpy as np
import math

def update_weight(n, data, now_weight):
    x = 0.2
    for i in range(n):
        for j in range(n):
            if(data[i][j] < 0):
                print("here " + str(i) + " " + str(j))
            numerator = []
            denominator = data[i][j]
            numerator.append(0)
            numerator.append(0)            
            numerator.append(0)
            numerator.append(0)
            if (i != 0 and i != n-1 and j != 0 and j != n-1):
                numerator[0] = data[i][j - 1]
                denominator += data[i][j - 1]
                numerator[1] = data[i][j + 1]
                denominator += data[i][j + 1]
                numerator[2] = data[i - 1][j]
                denominator += data[i - 1][j]
                numerator[3] = data[i + 1][j]
                denominator += data[i + 1][j]
                now_weight[i][j][0] = numerator[0] / (denominator + 0.01)
                now_weight[i][j][1] = numerator[1] / (denominator + 0.01)
                now_weight[i][j][2] = numerator[2] / (denominator + 0.01)
                now_weight[i][j][3] = numerator[3] / (denominator + 0.01)
            elif (i == 0):
                if (j == 0):
                    #numerator[0] = data[i][j - 1]
                    #denominator += data[i][j - 1]
                    #numerator[1] = data[i][j + 1]
                    #denominator += data[i][j + 1]
                    #numerator[2] = data[i - 1][j]
                    #denominator += data[i - 1][j]
                    #numerator[3] = data[i + 1][j]
                    #denominator += data[i + 1][j]
                    now_weight[i][j][0] = x
                    numerator[1] = 0
                    now_weight[i][j][2] = x
                    numerator[3] = 0
                    denominator += data[i + 1][j]
                    denominator += data[i][j + 1]
                    #now_weight[i][j][0] = 0.4 * numerator[0] / (denominator + 0.01)
                    now_weight[i][j][1] = 0.4 * numerator[1] / (denominator + 0.01)
                    #now_weight[i][j][2] = 0.4 * numerator[2] / (denominator + 0.01)
                    now_weight[i][j][3] = 0.4 * numerator[3] / (denominator + 0.01)
                elif (j == n - 1):
                    #numerator[0] = data[i][j - 1]
                    #denominator += data[i][j - 1]
                    #numerator[1] = data[i][j + 1]
                    #denominator += data[i][j + 1]
                    #numerator[2] = data[i - 1][j]
                    #denominator += data[i - 1][j]
                    #numerator[3] = data[i + 1][j]
                    #denominator += data[i + 1][j]
                    numerator[0] = 0
                    now_weight[i][j][1] = x
                    now_weight[i][j][2] = x
                    numerator[3] = 0
                    denominator += data[i + 1][j]
                    denominator += data[i][j - 1]
                    now_weight[i][j][0] = 0.4 * numerator[0] / (denominator + 0.01)
                    #now_weight[i][j][1] = 0.4 * numerator[1] / (denominator + 0.01)
                    #now_weight[i][j][2] = 0.4 * numerator[2] / (denominator + 0.01)
                    now_weight[i][j][3] = 0.4 * numerator[3] / (denominator + 0.01)
                else:
                    numerator[0] = data[i][j - 1]
                    denominator += data[i][j - 1]
                    numerator[1] = data[i][j + 1]
                    denominator += data[i][j + 1]
                    #numerator[2] = data[i - 1][j]
                    #denominator += data[i - 1][j]
                    #numerator[3] = data[i + 1][j]
                    #denominator += data[i + 1][j]
                    now_weight[i][j][2] = x
                    numerator[3] = 0
                    denominator += data[i + 1][j]
                    now_weight[i][j][0] = 0.7 * numerator[0] / (denominator + 0.01)
                    now_weight[i][j][1] = 0.7 * numerator[1] / (denominator + 0.01)
                    #now_weight[i][j][2] = 0.7 * numerator[2] / (denominator + 0.01)
                    now_weight[i][j][3] = 0.7 * numerator[3] / (denominator + 0.01)
            elif (i == n - 1):
                if (j == 0):
                    #numerator[0] = data[i][j - 1]
                    #denominator += data[i][j - 1]
                    #numerator[1] = data[i][j + 1]
                    #denominator += data[i][j + 1]
                    #numerator[2] = data[i - 1][j]
                    #denominator += data[i - 1][j]
                    #numerator[3] = data[i + 1][j]
                    #denominator += data[i + 1][j]
                    now_weight[i][j][0] = x
                    numerator[1] = 0
                    numerator[2] = 0
                    now_weight[i][j][3] = x
                    denominator += data[i - 1][j]
                    denominator += data[i][j + 1]
                    #now_weight[i][j][0] = 0.4 * numerator[0] / (denominator + 0.01)
                    now_weight[i][j][1] = 0.4 * numerator[1] / (denominator + 0.01)
                    now_weight[i][j][2] = 0.4 * numerator[2] / (denominator + 0.01)
                    #now_weight[i][j][3] = 0.4 * numerator[3] / (denominator + 0.01)
                elif (j == n - 1):
                    #numerator[0] = data[i][j - 1]
                    #denominator += data[i][j - 1]
                    #numerator[1] = data[i][j + 1]
                    #denominator += data[i][j + 1]
                    #numerator[2] = data[i - 1][j]
                    #denominator += data[i - 1][j]
                    #numerator[3] = data[i + 1][j]
                    #denominator += data[i + 1][j]
                    numerator[0] = 0
                    now_weight[i][j][1] = x
                    numerator[2] = 0
                    now_weight[i][j][3] = x
                    denominator += data[i - 1][j]
                    denominator += data[i][j - 1]
                    now_weight[i][j][0] = 0.4 * numerator[0] / (denominator + 0.01)
                    #now_weight[i][j][1] = 0.4 * numerator[1] / (denominator + 0.01)
                    now_weight[i][j][2] = 0.4 * numerator[2] / (denominator + 0.01)
                    #now_weight[i][j][3] = 0.4 * numerator[3] / (denominator + 0.01)
                else:
                    numerator[0] = data[i][j - 1]
                    denominator += data[i][j - 1]
                    numerator[1] = data[i][j + 1]
                    denominator += data[i][j + 1]
                    #numerator[2] = data[i - 1][j]
                    #denominator += data[i - 1][j]
                    #numerator[3] = data[i + 1][j]
                    #denominator += data[i + 1][j]
                    now_weight[i][j][3] = x
                    numerator[2] = 0
                    denominator += data[i - 1][j]
                    now_weight[i][j][0] = 0.7 * numerator[0] / (denominator + 0.01)
                    now_weight[i][j][1] = 0.7 * numerator[1] / (denominator + 0.01)
                    #now_weight[i][j][2] = 0.7 * numerator[2] / (denominator + 0.01)
                    now_weight[i][j][3] = 0.7 * numerator[3] / (denominator + 0.01)
            else:
                if (j == 0):
                    #numerator[0] = data[i][j - 1]
                    #denominator += data[i][j - 1]
                    #numerator[1] = data[i][j + 1]
                    #denominator += data[i][j + 1]
                    numerator[2] = data[i - 1][j]
                    denominator += data[i - 1][j]
                    numerator[3] = data[i + 1][j]
                    denominator += data[i + 1][j]
                    now_weight[i][j][0] = x
                    numerator[1] = 0
                    denominator += data[i][j + 1]
                    #now_weight[i][j][0] = 0.7 * numerator[0] / (denominator + 0.01)
                    now_weight[i][j][1] = 0.7 * numerator[1] / (denominator + 0.01)
                    now_weight[i][j][2] = 0.7 * numerator[2] / (denominator + 0.01)
                    now_weight[i][j][3] = 0.7 * numerator[3] / (denominator + 0.01)
                elif (j == n - 1):
                    #numerator[0] = data[i][j - 1]
                    #denominator += data[i][j - 1]
                    #numerator[1] = data[i][j + 1]
                    #denominator += data[i][j + 1]
                    numerator[2] = data[i - 1][j]
                    denominator += data[i - 1][j]
                    numerator[3] = data[i + 1][j]
                    denominator += data[i + 1][j]
                    now_weight[i][j][1] = x
                    numerator[0] = 0
                    denominator += data[i][j - 1]
                    now_weight[i][j][0] = 0.7 * numerator[0] / (denominator + 0.01)
                    #now_weight[i][j][1] = 0.7 * numerator[1] / (denominator + 0.01)
                    now_weight[i][j][2] = 0.7 * numerator[2] / (denominator + 0.01)
                    now_weight[i][j][3] = 0.7 * numerator[3] / (denominator + 0.01)             

            #print(now_weight[i][j][0] + now_weight[i][j][1] + now_weight[i][j][2] + now_weight[i][j][3])

def update_food_impact(n, data, now_weight, initial_food):
    sum = 0
    flag = False
    food = []
    food_num = 0
    tmp = []
    
    for i in range(n):
        for j in range(n):
            if (initial_food[i][j] != 0):
                if (data[i][j] != 0):
                    flag = True
                    sum += initial_food[i][j]
                    food.append([])
                    food[food_num].append(initial_food[i][j])
                    food[food_num].append(i)
                    food[food_num].append(j)
                    food_num += 1
    for k in range(n):
        tmp.append([])
        for l in range(n):
            tmp[k].append([])
            for s in range(4):
                tmp[k][l].append([])
                for f in range(food_num):
                    tmp[k][l][s].append(0)            

    if(flag):
        for f in range(food_num):
            how_much = food[f][0]
            i = food[f][1]
            j = food[f][2]
            for k in range(n):
                for l in range(n):
                    dx = i - k
                    dy = j - l
                    xdirection = dx**2/(dx**2 + dy**2 + 0.0001) 
                    ydirection = dy**2/(dx**2 + dy**2 + 0.0001)
                    prop = 0.95
                    distant_coefficient = 1 - math.exp(-n**2/10/(dx**2 + dy**2 + 0.0001))
                    if (i - k > 0 and j - l > 0):
                        tmp[k][l][0][f] = distant_coefficient * prop * ydirection + (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = distant_coefficient * prop * xdirection + (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = (1-distant_coefficient) * now_weight[k][l][3]
                    elif (i - k > 0 and j - l < 0):
                        tmp[k][l][0][f] = (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = distant_coefficient * prop * ydirection + (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = distant_coefficient * prop * xdirection + (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = (1-distant_coefficient) * now_weight[k][l][3]
                    elif (i - k < 0 and j - l > 0):
                        tmp[k][l][0][f] = distant_coefficient * prop * ydirection + (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = distant_coefficient * prop * xdirection + (1-distant_coefficient) * now_weight[k][l][3]
                    elif (i - k < 0 and j - l < 0):
                        tmp[k][l][0][f] = (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = distant_coefficient * prop * ydirection + (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = distant_coefficient * prop * xdirection + (1-distant_coefficient) * now_weight[k][l][3]
                    elif ( i - k == 0 and j - l < 0):
                        tmp[k][l][0][f] = (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = distant_coefficient * prop * ydirection + (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = (1-distant_coefficient) * now_weight[k][l][3]
                    elif ( i - k == 0 and j - l > 0):
                        tmp[k][l][0][f] = distant_coefficient * prop * ydirection + (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = (1-distant_coefficient) * now_weight[k][l][3]
                    elif ( i - k < 0 and j - l == 0):
                        tmp[k][l][0][f] = (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = distant_coefficient * prop * xdirection + (1-distant_coefficient) * now_weight[k][l][3]
                    elif ( i - k > 0 and j - l == 0):
                        tmp[k][l][0][f] = (1-distant_coefficient) * now_weight[k][l][0]
                        tmp[k][l][1][f] = (1-distant_coefficient) * now_weight[k][l][1]
                        tmp[k][l][2][f] = distant_coefficient * prop * xdirection + (1-distant_coefficient) * now_weight[k][l][2]
                        tmp[k][l][3][f] = (1-distant_coefficient) * now_weight[k][l][3]

    if(flag):
        for k in range(n):
            for l in range(n):
                for s in range(4):
                    tmp2 = 0
                    for f in range(food_num):
                        tmp2 += food[f][0]/sum * tmp[k][l][s][f]
                    now_weight[k][l][s] = tmp2

def output(n, initial_food, now_slime_state, now_weight):
    data = []
    to_use = []
    for i in range(n):
        data.append([])
        to_use.append([])
        for j in range(n):
            data[i].append(0)
            to_use[i].append(0)
    
    for i in range(n):
        for j in range(n):
            to_use[i][j] = now_slime_state[i][j]
            
   
    sigma = 0.01
    shorten = 0.8 
    for i in range(n):
        for j in range(n):

            if(j + 1 < n):
                rand = np.random.randn()
                if (now_weight[i][j][0] + sigma * rand < 0):
                    weight = 0
                else:
                    weight = now_weight[i][j][0] + sigma * rand
                if (now_slime_state[i][j] - shorten * weight * to_use[i][j] <= 0):
                    data[i][j + 1] += now_slime_state[i][j]
                    now_slime_state[i][j] = 0
                else:     
                    data[i][j + 1] += shorten * weight * to_use[i][j]
                    now_slime_state[i][j] -= shorten * weight * to_use[i][j]
            
            if(j - 1 >= 0):
                rand = np.random.randn()
                if (now_weight[i][j][1] + sigma * rand < 0):
                    weight = 0
                else:
                    weight = now_weight[i][j][1] + sigma * rand
                if (now_slime_state[i][j] - shorten * weight * to_use[i][j] <= 0):
                    data[i][j - 1] += now_slime_state[i][j]
                    now_slime_state[i][j] = 0
                else:     
                    data[i][j - 1] += shorten * weight * to_use[i][j]
                    now_slime_state[i][j] -= shorten * weight * to_use[i][j] 

            if(i + 1 < n):
                rand = np.random.randn()
                if (now_weight[i][j][2] + sigma * rand < 0):
                    weight = 0
                else:
                    weight = now_weight[i][j][2] + sigma * rand
                if (now_slime_state[i][j] - shorten * weight * to_use[i][j] <= 0):
                    data[i + 1][j] += now_slime_state[i][j]
                    now_slime_state[i][j] = 0
                else:     
                    data[i + 1][j] += shorten * weight * to_use[i][j]
                    now_slime_state[i][j] -= shorten * weight * to_use[i][j]

            if(i - 1 >= 0):
                rand = np.random.randn()
                if (now_weight[i][j][3] + sigma * rand < 0):
                    weight = 0
                else:
                    weight = now_weight[i][j][3] + sigma * rand
                if (now_slime_state[i][j] - shorten * weight * to_use[i][j] <= 0):
                    data[i - 1][j] += now_slime_state[i][j]
                    now_slime_state[i][j] = 0
                else:     
                    data[i - 1][j] += shorten * weight * to_use[i][j]
                    now_slime_state[i][j] -= shorten * weight * to_use[i][j]
            
            data[i][j] += now_slime_state[i][j]
    
    '''
    for i in range(n):
        for j in range(n):
            if(data[i][j] != 0):
                now_weight[i][j][0] = 1/5
                now_weight[i][j][1] = 1/5
                now_weight[i][j][2] = 1/5
                now_weight[i][j][3] = 1/5
    '''
    update_weight(n, data, now_weight)
    update_food_impact(n, data, now_weight, initial_food)


    
    return [data, now_weight]

'''
now_slime_state = []
now_weight = []
initial_food = []
n = 4
for i in range(n):
    now_slime_state.append([])
    now_weight.append([])
    for j in range(n):
        now_slime_state[i].append(0)
        now_weight[i].append([])
        for k in range(4):
            now_weight[i][j].append(1/5)

now_slime_state[0][0] = 300

ans = output(n, initial_food, now_slime_state, now_weight)
print(ans[0])
'''


