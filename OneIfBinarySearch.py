# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
np.random.seed(0)
n = sorted(np.random.randint(0, 100, 70))

def search(arr, target):
    low = 0
    high = len(arr) - 1
    greater = True
    result = -1
    while (low < high or greater):
        greater = False
        mid = (low + high) // 2
        
        guess = arr[mid]
        
        if target > guess:
            #greater - get rid of the left side
            low = mid + 1
            greater = True
        else:
            #less than or equal 
            high = mid
    if(target != guess):
       # print("not found")
        result = -1
    else:
        #print(f'{target} is equal to {guess} at {mid}')
        result = mid
    return result

def test_all_numbers(arr, high):
    answer = -1
    for i in range(high):
        answer = search(n, i)
        if answer != -1:
            print(i, answer, n[answer])
        else:
            print(i, answer)