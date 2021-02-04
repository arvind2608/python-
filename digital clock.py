
#import whole module
from tkinter import *
from tkinter.ttk import *

#import time and stringfunction 
from time import strftime 

#create root window
root = Tk() 
root.title('DIGITAL CLOCK') 


def time(): 
	string = strftime('%H:%M:%S %p   %d/%m/%Y %a') 
	lbl.config(text = string) 
	lbl.after(1000, time) 

#giving color and style to font
lbl = Label(root, font = ('arial', 30, 'italic'),background = 'blue', 
			foreground = 'white') 
#placing clock
lbl.pack(anchor = 'c') 
time() 

mainloop() 
