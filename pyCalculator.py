import tkinter as tk
from tkinter import *

# creates the window
master = Tk()

# this contains all the design of the application

# this is of the variable class
# What is the variable class?
# we create an instance of this 
equation = StringVar()

# this is the reuslt bar that is at the top
# it spans 4 columns
# try to see if you can make it taller and longer 
resultBar = Entry( master, textvariable=equation )
resultBar.grid( columnspan = 4 )


button1 = tk.Button(  text="1", height=10, width = 10 )
button1.grid( row=1, column=1 )

button2 = tk.Button(  text="2" )
button2.grid( row=1, column=2 )

button3 = tk.Button(  text="3" )
button3.grid( row=1, column=3 )


button4 = tk.Button(  text="4" )
button4.grid( row=2, column=1 )

button5 = tk.Button(  text="5" )
button5.grid( row=2, column=2 )

button6 = tk.Button(  text="6" )
button6.grid( row=2, column=3 )


button7 = tk.Button(  text="7" )
button7.grid( row=3, column=1 )

button8 = tk.Button(  text="8" )
button8.grid( row=3, column=2 )

button9 = tk.Button(  text="9" )
button9.grid( row=3, column=3 )


button0 = tk.Button(  text="0" )
button0.grid( row=4, column=2 )

master.mainloop() 
