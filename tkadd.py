from tkinter import *
from tkinter import ttk
def get_sum():
    num_1_value=float(num_1.get())
    num_2_value = float(num_2.get())
    solution.set(num_1_value+num_2_value)
root = Tk()
root.title("Calculator")
frame=ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
num_1=StringVar()
num_2=StringVar()
solution=StringVar()
num_1_entry=ttk.Entry(frame,width=7,textvariable=num_1)
num_1_entry.grid(column=1,row=1,sticky=("W,E"))
ttk.Label(frame,text="+").grid(column=2,row=1,sticky=(W,E))
num_2_entry=ttk.Entry(frame,width=7,textvariable=num_2)
num_2_entry.grid(column=3,row=1,sticky=("W,E"))
ttk.Button(frame,text="Add",command=get_sum).grid(column=4,row=1,sticky=(W,E))

solution_entry=ttk.Entry(frame,width=9,textvariable=solution)
solution_entry.grid(column=5,row=1,sticky=(W,E))
num_1_entry.focus()
root.bind('<Return>',get_sum)
root.mainloop()