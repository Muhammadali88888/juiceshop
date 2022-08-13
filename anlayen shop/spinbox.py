from tkinter import *


root = Tk()
root.geometry("400x400")



def och():
    spin.pack()



def next():
    a = spin.get()
    sok.configure(text=a)

sok = Button(root, text="Sok", command=och)
sok.pack()
spin = Spinbox(root, from_=1, to=10, width=4)
spin.pack()

nex = Button(root, text="Next", command=next)
nex.pack()



root.mainloop()