# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 12:12:06 2022

@author: cs166
"""
from Algorithms.bubbleSort import bubble_Sort
from Algorithms.MergeSort import merge_sort
from tkinter import *
from tkinter import ttk

#import random to generate array 

import random 
#import colors to use it in tkinter functions 
from colors import *

#creating a window 

window = Tk()
window.title("SORTING ALGORITHMS VISUALIZER")
window.maxsize(1000,700)
window.config(bg = WHITE)


algorithm_name = StringVar()
algo_list = ['BubbleSort','MergeSort']


speed_name = StringVar()
speed_list = ['Slow','Medium','Fast']


data = []

#This function will convert elements of data into vertical bars and draw them into the window
def drawData(Data,colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width/(len(data)+1)
    offset = 4
    spacing = 2
    normalizedData = [i/max(data) for i in data]
    
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()
    
    

#this function will generate random value 
def generate():
    global data
    data = []
    for i in range(0,100):
        random_value = random.randint(0,150)
        data.append(random_value)
        
        drawData(data,[PINK for x in range(len(data))])
    

#This function will set the sorting speed 
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    #return 0.3
    
    elif speed_menu.get() == 'Medium':
        return 0.1
    #return 0.1
     
    else:
        return 0.001


#This function will select a sorting algorithm and start sorting 
def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'BubbleSort':
        bubble_Sort(data, drawData, timeTick)
        
    elif algo_menu.get() == 'MergeSort':
        merge_sort(data,0,len(data)-1, drawData, timeTick)



#user interface here
UI_frame = Frame(window,width=900,height=300,bg=WHITE)
UI_frame.grid(row =0,column=0,padx=10,pady=5)

#Dropdown menu to select sorting algorithm
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

#Dropdown menu to select sorting speed 

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)


#Sorting Button on UI
b1 = Button(UI_frame,text="Sort",command=sort,bg = LIGHT_GREEN)
b1.grid(row=2,column=1,padx=5,pady=5)

#Button For Generating Array
b2 = Button(UI_frame,text="Generate Array",command = generate,bg=LIGHT_GREEN )
b2.grid(row=2,column=0,padx=5,pady=5)

#Canvas to draw the array 
canvas = Canvas(window,width=800,height=400,bg=WHITE)
canvas.grid(row=1,column=0,padx=10,pady=5)


window.mainloop()

#basic UI is done




