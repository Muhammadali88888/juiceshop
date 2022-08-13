from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

root = Tk()
root.geometry("600x400")








def play_gif():
    while True:
        global img
        img = Image.open("persn.gif")

        lbl = Label(root)
        lbl.place(x=0,y=0)

        for img in ImageSequence.Iterator(img):

            img = img.resize((300,300))
            img = ImageTk.PhotoImage(img)
            lbl.config(image = img)

            root.update()


def exit():
    root.destroy()


    root.after(0, play_gif)
Button(root, text="play", bd=0, command=play_gif).place(x = 500, y = 300)
Button(root, text="exit", bd=0, command=exit).place(x = 450, y = 300)


root.mainloop()