from tkinter import *

root = Tk()
root.geometry('400x500')



frame = Frame(root, width=400, height=250, bg='red')
frame.pack()

frame1 = Frame(root, width=400, height=250, bg='grey')
frame1.pack()

button = Button(frame1, text='click')
button.place(x=100, y=50)


root.mainloop()