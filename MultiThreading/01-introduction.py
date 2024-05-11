
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:14:46 2024

@author: Ahmed Elsheikh
"""
#This is sequential program

import time

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)


print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")