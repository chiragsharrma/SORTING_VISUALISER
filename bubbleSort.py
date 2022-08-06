# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 12:13:15 2022

@author: cs166
"""

import time       #to make some time difference between comparisons importing time
                  #module
from colors import *

def bubble_Sort(data,drawData,timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]= data[j+1],data[j]
                drawData(data,[PURPLE if x==j or x==j+1 else PINK for x in range(len(data))])
                time.sleep(timeTick)
                
      
    drawData(data,[PINK for x in range(len(data))])
    