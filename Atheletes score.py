# You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

# image

# Note that  is indexed from  to , where  is the number of attributes.

# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

# Input Format

# The first line contains  and  separated by a space.
# The next  lines each contain  elements.
# The last line contains .

# Constraints



# Each element 

# Output Format

# Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

# Sample Input 0

# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# Sample Output 0

# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# Explanation 0

# The details are sorted based on the second attribute, since  is zero-indexed.











#!/bin/python3

import math
import os
import random
import re



import sys
from operator import itemgetter


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    # minm=arr[0][k]
    # a=[]
    # a.append(arr[0])
    # for i in range(n):
    #     if a[i][k]>arr[i][k]:
    #         t=a[i]
    #         a[i]=arr[i]
    #         # print(t)
    #         a.append(t)
    #     else:
    #         a.append(arr[i])
    #     # if i==1:
    #         # a=a[1:]
    # print(a[1:])
    # sorted(arr,key=itemgetter(k))
    arr.sort(key=lambda x: x[k])
    for i in range (n):
        arr[i]=map(str,arr[i])
        print(' '.join(arr[i]))
            
