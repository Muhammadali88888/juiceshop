from tkinter import *
import time
tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()

fish_obj = PhotoImage(file="")
id_img = canvas.create_image(50,50,anchor=NW, image=fish_obj)
print(id_img)



for i in range(1,100):
    canvas.move(id_img, 2,0)
    tk.update()
    time.sleep(0.02)

input()