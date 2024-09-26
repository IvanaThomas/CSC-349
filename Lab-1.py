#Lab 1 
#Ivana Thomas
#Goal: Find the singleton in a sorted list of duplicates

import numpy as np
sorted_list = np.genfromtxt('/Users/ivanathomas/Downloads/unique-64')

def findSingleton(array, low, high ):
    #define the middle
    middle = (low + high) // 2

    #look left for the pair
    left = middle - 1
    right = middle + 1

    if array[left] == array[middle]:
        pair_side = 'right'

    #look right
    elif array[right] == array[middle]:
        pair_side = 'left'
    
    #case where it is the middle of the array
    else: 
        print("singleton:")
        print(array[middle])
        return middle

    #determine which side the singleton is on
    if pair_side == 'right':
        left_len = (middle - low - 1)
        low = middle + 2
        right_len = (high - low)
        
    
    elif pair_side == 'left':
        right_len = (high - middle - 1)
        high = middle - 1
        left_len = (high - low)
    
    if (right_len > left_len):
        findSingleton(array, middle + 2, high )
    elif (left_len > right_len):
        findSingleton(array, low, middle-1)

findSingleton(sorted_list, 0, len(sorted_list) -1 )
    




    





