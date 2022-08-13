
import json
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time


def register():
    root = Tk()
    root.geometry("400x400")
    root.title("Tkinter widgets ! ")
    root.config(bg='#34eb9b')
    root.resizable(0, 0)




    def ochir():
        b = {
            "name": entry1.get(),
            "last_name": entry4.get(),
            "phone": entry6.get(),
            "email": entry8.get(),
            "Pin": entry9.get()
        }
        with open('register.json', 'w') as a:
            json.dump(b, a)
        root.destroy()
        oyna()
        
    root.geometry("1100x600")

    label1 = Label(root, text="Assalomu aluykum ", bg='#34eb9b', foreground='black', font=('Helvatica', 15, 'bold'))
    label1.pack()
    label1 = Label(root, text="Huw kelibsiz Registrationdan oting", bg='#34eb9b', foreground='black', font=('Helvatica', 15, 'bold'))
    label1.pack()

    label2 = Label(root, text="First Name", bg='#34eb9b', foreground='white', font=('Helvatica', 12, 'bold'))
    label2.pack(padx=4)

    entry1 = Entry(root)
    entry1.pack(padx=5)

    label3 = Label(root, text="Last Name", bg='#34eb9b', foreground='white', font=('Helvatica', 12, 'bold'))
    label3.pack(padx=6)

    entry4 = Entry(root)
    entry4.pack(padx=7)

    label5 = Label(root, text="Phone Number", bg='#34eb9b', foreground='white', font=('Helvatica', 12, 'bold'))
    label5.pack(padx=8)

    entry6 = Entry(root)
    entry6.pack(padx=9)

    label7 = Label(root, text='E-Mail', bg='#34eb9b', foreground='white', font=('Helvatica', 12, 'bold'))
    label7.pack(padx=10)

    entry8 = Entry(root)
    entry8.pack(padx=11)

    label8 = Label(root, text='Pin', bg='#34eb9b', foreground='white', font=('Helvatica', 12, 'bold'))
    label8.pack(padx=10)

    entry9 = Entry(root, show='*')
    entry9.pack(padx=12)
    
    btn = Button(root,text="Next",font=('Helvatica',10,'normal'), command=ochir)
    btn.pack(pady=10)
    root.mainloop()
#

def oyna():
    root = Tk()
    root.geometry("1300x750")



    root.configure(bg='whitesmoke')
    look = Image.open('888.png').resize((1300,700)) # rasimga=razmer beriqw
    image1 = ImageTk.PhotoImage(look)
    l1 = Label(root, image=image1, bg='whitesmoke', font=('Arial',100,'bold'))
    l1.place(x=0, y=0)

    def next():
        root.destroy()
        rasim()

    b2 = Button(root, text="""   Shop   """, bd=0,
    bg="#3D5A23", fg="white", font=('Helvatica', 17, 'bold'), command=next, activebackground='#3D5A23')
    b2.place(x=210, y=497)
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='whitesmoke', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bd=0, cursor='hand2', bg='whitesmoke', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bd=0, cursor='hand2', bg='whitesmoke', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us',  bd=0, cursor='hand2',bg='whitesmoke', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bd=0, cursor='hand2', bg='whitesmoke', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bd=0, cursor='hand2',bg="whitesmoke", font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    root.mainloop()
#
def rasim():
    root = Tk()
    root.geometry('1300x750')
    root.configure(bg="#EBECF0")

    def poisk():
        w = entry1.get()
        if w == 'Pink': 
            root.destroy()
            birinci()
        elif w == "Ginger":
            root.destroy()
            ikinchi()
        elif w == "Raspberry":
            root.destroy()
            uchinchi()
        elif w == "Orange":
            root.destroy()
            tortinchi()
        elif w == "Apple":
            root.destroy()
            bewinchi()
        elif w == "Light":
            root.destroy()
            oltinchi()
            
    entry1 = Entry(root, width=30, highlightbackground='red')
    entry1.place(x=900,y=30)
    button = Button(root, text='Enter', command=poisk)
    button.place(x=1095,y=28)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0",bd=0,  cursor='hand2', fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    l18 = Label(root, text="""
    Cold-pressed, 100% organic, packed with vitamins, nutrients,
    and natural goodness.""", justify=LEFT, fg="black",bg="#EBECF0",bd=0,  cursor='hand2',font=("Arial", 10, "bold"))
    l18.place(x=190, y=80)

    def bir():
        root.destroy()
        birinci()

    rasm1 = Image.open('qizil-su.webp').resize((200,200)) # rasimga=razmer beriqw
    image1 = ImageTk.PhotoImage(rasm1)
    l1 = Button(root, image=image1, command=bir, bd=0)
    l1.place(x=200, y=150)
    b3 = Label(root, text="""
    Pink Grapefruit $6.00""", fg="black", bg="#EBECF0")
    b3.place(x=220, y=355)
    def iki():
        root.destroy()
        ikinchi()
    rasm2 = Image.open('olovrang-su.webp').resize((200,200)) # rasimga=razmer beriqw
    image2 = ImageTk.PhotoImage(rasm2)
    l2 = Button(root, image=image2, command=iki, bd=0)
    l2.place(x=500, y=150)
    b4 = Label(root, text="""
    Ginger Tangerine $6.00""", fg="black", bg="#EBECF0")
    b4.place(x=500, y=355)
    def uch():
        root.destroy()
        uchinchi()

    rasm3 = Image.open('raspberry-su.webp').resize((200,200)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rasm3)
    l3 = Button(root, image=image3, command=uch, bd=0)
    l3.place(x=800, y=150)
    b5 = Label(root, text="""
    Raspberry Lime $6.00""", fg="black", bg="#EBECF0")
    b5.place(x=800, y=355)
    def tor():
        root.destroy()
        tortinchi()

    rasm4 = Image.open('sarig-su.webp').resize((200,200)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(rasm4)
    l4 = Button(root, image=image4, command=tor, bd=0)
    l4.place(x=200, y=400)
    b6 = Label(root, text="""
    Orange juice $6.00""", fg="black", bg="#EBECF0")
    b6.place(x=210, y=605)
    def bew():
        root.destroy()
        bewinchi()

    rasm5 = Image.open('yashil-su.webp').resize((200,200)) # rasimga=razmer beriqw
    image5 = ImageTk.PhotoImage(rasm5)
    l5 = Button(root, image=image5, command=bew, bd=0)
    l5.place(x=500, y=400) 
    b7 = Label(root, text="""
    Green punch $6.00""", fg="black", bg="#EBECF0")
    b7.place(x=500, y=605)
    def olti():
        root.destroy()
        oltinchi()

    rasm6 = Image.open('yawil-su.webp').resize((200,200)) # rasimga=razmer beriqw
    image6 = ImageTk.PhotoImage(rasm6)
    l6 = Button(root, image=image6, command=olti, bd=0)
    l6.place(x=800, y=400)
    b8 = Label(root, text="""
    Light orange juice $6.00""", fg="black", bg="#EBECF0")
    b8.place(x=800, y=605)
    root.mainloop()
#
def birinci():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    bu = Image.open('qizil-su.webp').resize((500,700)) # rasimga=razmer beriqw
    image1 = ImageTk.PhotoImage(bu)
    n1 = Label(root, image=image1, bd=0)
    n1.place(x=300, y=50)

    
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Pink Grapefruit

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0",bd=0,  fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i1 = Label(root, text="""PRODUCT INFO


I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.

_______________________

RETURN & REFUND POLICY
_______________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i1.place(x=850, y=320)
    def f1():
        root.destroy()
        fff()
    r3 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=f1)
    r3.place(x=850, y=300)
    root.mainloop()

def ikinchi():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    tit = Image.open('olovrang-su.webp').resize((500,700)) # rasimga=razmer beriqw
    image2 = ImageTk.PhotoImage(tit)
    n2 = Label(root, image=image2, bd=0)
    n2.place(x=300, y=70)
    r = Label(root, text=" New ", bd=0, bg="#3D5A23", fg="white", font=("Arial", 15, "normal"))
    r.place(x=370,y=100)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Pink Grapefruit

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bd=0, bg="#EBECF0", font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0", bd=0, fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i2 = Label(root, text="""PRODUCT INFO

I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.
________________________

RETURN & REFUND POLICY
________________________

SHIPPING INFO

    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i2.place(x=850, y=320)
    def f2():
        root.destroy()
        f2f2()
    r4 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=f2)
    r4.place(x=850, y=300)
    root.mainloop()


    
def uchinchi():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg='#EBECF0')
    rere = Image.open('raspberry-su.webp').resize((500,700)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rere)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=300, y=60)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Raspberry Lime

    SKU:003

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact',  bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bd=0, bg="#EBECF0", font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0", bd=0, fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i3 = Label(root, text="""PRODUCT INFO

I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.

_________________________

RETURN & REFUND POLICY
_________________________

SHIPPING INFO
    

    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i3.place(x=850, y=320)
    def f3():
        root.destroy()
        f3f3()
    r5 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=f3)
    r5.place(x=850, y=300)
    root.mainloop()

def tortinchi():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    pip = Image.open('sarig-su.webp').resize((500,700)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pip)
    n4 = Label(root, image=image4, bd=0)
    n4.place(x=300, y=60)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Orange juice    

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop',  bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bd=0,  bg="#EBECF0",  font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0", bd=0, fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i2 = Label(root, text="""PRODUCT INFO

I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.
________________________

RETURN & REFUND POLICY
________________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i2.place(x=850, y=320)
    def f4():
        root.destroy()
        f4f4()
    r4 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=f4)
    r4.place(x=850, y=300)
    root.mainloop()

def bewinchi():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    rere = Image.open('yashil-su.webp').resize((500,700)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rere)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=300, y=60)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Green punch 

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop',  bg="#EBECF0", bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us',  bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bd=0,  bg="#EBECF0", font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0", bd=0, fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i4 = Label(root, text="""PRODUCT INFO   

I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.
_________________________

RETURN & REFUND POLICY
_________________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i4.place(x=850, y=320)
    def f5():
        root.destroy()
        f5f5()
    r6 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=f5)
    r6.place(x=850, y=300)
    root.mainloop()
    
def oltinchi():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    bibi = Image.open('yawil-su.webp').resize((500,700)) # rasimga=razmer beriqw
    image5 = ImageTk.PhotoImage(bibi)
    n5 = Label(root, image=image5, bd=0)
    n5.place(x=300, y=60)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Light orange juice

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg="#EBECF0",  bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bd=0, bg="#EBECF0",  font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0", bd=0,  fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i5 = Label(root, text="""PRODUCT INFO

I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.
________________________

RETURN & REFUND POLICY
________________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i5.place(x=850, y=320)

    def f6():
        root.destroy()
        f6f6()
    r4 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=f6)
    r4.place(x=850, y=300)
    root.mainloop()
#
def fff():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('qizil-su.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Pink Grapefruit
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('uzcard.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)

    root.mainloop()

def f2f2():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    yu = Image.open('olovrang-su.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(yu)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Green Tangerine
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p2():
        root.destroy()
        pp2()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p2)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=65)
    entry1 = Entry(root)
    entry1.place(x=100,y=90)

    label2 = Label(root, text="name juice", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=165)

    entry1 = Entry(root)
    entry1.place(x=100,y=190)
    root.mainloop()


def f3f3():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    pip = Image.open('raspberry-su.webp').resize((300,400)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pip)
    n4 = Label(root, image=image4, bd=0)
    n4.place(x=750, y=60)
    b6 = Label(root, text="""
    Raspberry Lime 
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b6.place(x=1000, y=70)


    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p3():
        root.destroy()
        pp3()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p3)
    r9.place(x=1018, y=300)
    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=65)
    entry1 = Entry(root)
    entry1.place(x=100,y=90)

    label2 = Label(root, text="name juice", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=165)

    entry1 = Entry(root)
    entry1.place(x=100,y=190)
    root.mainloop()

def f4f4():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    rere = Image.open('sarig-su.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rere)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Orange juice
    $6.00""", fg="black", bg='#EBECF0',justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p4():
        root.destroy()
        pp4()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p4)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=65)
    entry1 = Entry(root)
    entry1.place(x=100,y=90)
    label2 = Label(root, text="name juice", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=165)

    entry1 = Entry(root)
    entry1.place(x=100,y=190)
    root.mainloop()

def f5f5():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    bibi = Image.open('yashil-su.webp').resize((300,400)) # rasimga=razmer beriqw
    image5 = ImageTk.PhotoImage(bibi)
    n5 = Label(root, image=image5, bd=0)
    n5.place(x=750, y=60)
    b6 = Label(root, text="""
    Green Punch
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b6.place(x=1000, y=70)
 
    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p5():
        root.destroy()
        pp5()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p5)
    r9.place(x=1018, y=300)
    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=65)
    entry1 = Entry(root)
    entry1.place(x=100,y=90)

    label2 = Label(root, text="name juice", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=110,y=165)

    entry1 = Entry(root)
    entry1.place(x=100,y=190)
    root.mainloop()

def f6f6():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    rere = Image.open('yawil-su.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rere)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Light green juice
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=800, y=450)
    def p6():
        root.destroy()
        pp6()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p6)
    r9.place(x=800, y=500)
    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=1018,y=300)
    entry1 = Entry(root)
    entry1.place(x=1018,y=310)

    label2 = Label(root, text="name juice", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=999,y=700)

    entry1 = Entry(root)
    entry1.place(x=999,y=710)
    root.mainloop()


def pp1():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#A7BD4E")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#A7BD4E", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    
    
    "Thank you for your purchase"
    
    
    """, bd=0, bg="#A7BD4E", font=("Arial", 15, "bold"))
    roo.place(x=450,y=200)
    root.mainloop()

def pp2():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#A7BD4E")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#A7BD4E", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    
    
    "Thank you for your purchase"
    
    
    
    """, bd=0, bg="#A7BD4E", font=("Arial", 15, "bold"))
    roo.place(x=450,y=200)
    root.mainloop()

def pp3():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#A7BD4E")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#A7BD4E", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    
    
    "Thank you for your purchase"
    
    
    
    """, bd=0, bg="#A7BD4E", font=("Arial", 15, "bold"))
    roo.place(x=450,y=200)
    root.mainloop()

def pp4():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#A7BD4E")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#A7BD4E", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    
    
    "Thank you for your purchase"
    
    
    
    """, bd=0, bg="#A7BD4E", font=("Arial", 15, "bold"))
    roo.place(x=450,y=200)
    root.mainloop()

def pp5():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#A7BD4E")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#A7BD4E", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    
    
    "Thank you for your purchase"
    
    
    
    """, bd=0, bg="#A7BD4E", font=("Arial", 15, "bold"))
    roo.place(x=450,y=200)
    root.mainloop()

def pp6():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#A7BD4E")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#A7BD4E', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#A7BD4E", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    
    
    "Thank you for your purchase"
    
    
    """, bd=0, bg="#A7BD4E", font=("Arial", 15, "bold"))
    roo.place(x=450,y=200)
    root.mainloop()


def tt3():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)
    roo = Label(root, text="""
    Subscribe to and of our plans and select how often you want 
    them delivered
    """, justify=LEFT, bd=0, cursor='hand2', bg="#EBECF0", font=("Arial", 15, "bold"))
    roo.place(x=100, y=50)
    
    def kom():
        root.destroy()
        komkom()
    rere1 = Image.open('mixkom.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rere1)
    n6 = Button(root, image=image3, bd=0, command=kom)
    n6.place(x=100, y=150)
    u5 = Label(root, text="""
    Total Care
    $50.00""", justify=LEFT, bg="#EBECF0", bd=0, cursor="hand2", font=("Arial", 13, "normal"))
    u5.place(x=150, y=500)
    def kom2():
        root.destroy()
        kom2kom2()
    rere2 = Image.open('mixkombo.webp').resize((300,400)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(rere2)
    n7 = Button(root, image=image4, bd=0, command=kom2)
    n7.place(x=450, y=150)
    u4 = Label(root, text="""
    Detox Plan
    $30.00""", justify=LEFT, bg="#EBECF0", bd=0, cursor="hand2", font=("Arial", 13, "normal"))
    u4.place(x=500, y=500)
    def kom3():
        root.destroy()
        kom3kom3()
    rere3 = Image.open('mixkomplekt.webp').resize((300,400)) # rasimga=razmer beriqw
    image5 = ImageTk.PhotoImage(rere3)
    n8 = Button(root, image=image5, bd=0, command=kom3)
    n8.place(x=800, y=150)
    u3 = Label(root, text="""
    Full-Day Cleanses
    $30.00""",  justify=LEFT,bg="#EBECF0", bd=0, cursor="hand2", font=("Arial", 13, "normal"))
    u3.place(x=850, y=500)
    root.mainloop()
    
    def och():
        spin.pack()
    def next():
        a = spin.get()
        sok.configure(text=a)

    sok = Button(root, text="""     Sok     """, command=och)
    sok.place(x=850,y=200)
    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=220)

    nex = Button(root, text="""     Next    """, command=next)
    nex.place(x=850,y=240)
def tt4():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    rere4 = Image.open('sok.webp').resize((400,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(rere4)
    n4 = Label(root, image=image3, bd=0)
    n4.place(x=750, y=70)
    
    rere5 = Image.open('sok1.webp').resize((400,400)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(rere5)
    n3 = Label(root, image=image4, bd=0)
    n3.place(x=680, y=200)

    l2 = Label(root, text="""
About Us


Bringing 100% 
natural juices 
straight to your door


I'm a paragraph. Click here to add your own text and edit 
me. It’s easy. Just click “Edit Text” or double click me to add 
your own content and make changes to the font. I’m a 
great place for you to tell a story and let your users know 
a little more about you
""", fg="black", justify=LEFT, bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 15, "normal"))
    l2.place(x=100, y=50)
    root.mainloop()

def tt5():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)


    l1 = Label(root, text="""
    Get in Touch

    Fill in the form with your questions, comments and concerns, and 
    we will get right back to you.


    ________________________

    Other ways to reach us
    Wholesale enquiries:

    info@mysite.com

    PR, press or partnerships:

    info@mysite.com

    Address:

    500 Terry Francois St. San Francisco,

    CA 94158""", bg="#EBECF0",  justify=LEFT,font=("Arial", 14, "normal"))

    label2 = Label(root, text="Comlaints", bg='#EBECF0',bd=0, fg='black', font=('Helvatica', 10, 'bold'))
    label2.place(x=700,y=75)
    entry1 = Entry(root)
    entry1.place(x=700,y=100)

    label2 = Label(root, text="limitation", bg='#EBECF0',bd=0, fg='black', font=('Helvatica', 10, 'bold'))
    label2.place(x=900,y=75)
    entry1 = Entry(root)
    entry1.place(x=900,y=100)

    label2 = Label(root, text="What do you like", bg='#EBECF0',bd=0, fg='black', font=('Helvatica', 10, 'bold'))
    label2.place(x=700,y=175)
    entry1 = Entry(root)
    entry1.place(x=700,y=200)

    label2 = Label(root, text="What would you like ", bg='#EBECF0',bd=0, fg='black', font=('Helvatica', 10, 'bold'))
    label2.place(x=900,y=175)
    entry1 = Entry(root)
    entry1.place(x=900,y=200)
    l1.place(x=100, y=40)
    def life():
        root.destroy()
        oppo2()
    l15 = Button(root, text='next window', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=life)
    l15.place(x=900, y=300)
    root.mainloop()

def tt6():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0", bd=0, font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    roo = Label(root, text="""
    Demo Mode

    To make this template yours, start editing it.
    """, bg="#EBECF0",font=("Arial", 15, "bold"))
    roo.place(x=400, y=100)
    def main():
        root.destroy()
        rasim()
    r9 = Button(root, text="   Ok   ", bg="green", fg="white", font=('Arial', 15, 'bold'), command=main)
    r9.place(x=600, y=220)
    
    root.mainloop()

def oppo2():
        
    root = Tk()
    root.geometry("1300x750")
    def play_gif():
        while True:
            global img
            img = Image.open("pochtaa.gif")

            lbl = Label(root)
            lbl.place(x=0,y=0)

            for img in ImageSequence.Iterator(img):

                img = img.resize((1250,700))
                img = ImageTk.PhotoImage(img)
                lbl.config(image = img)

                root.update()


    def exit():
        root.destroy()


        root.after(0, play_gif)
    Button(root, text="play", bd=0, command=play_gif).place(x = 1000, y = 600)
    Button(root, text="exit", bd=0, command=exit).place(x = 950, y = 600)
    root.mainloop()

def komkom():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    bu = Image.open('mixkom.webp').resize((500,700)) # rasimga=razmer beriqw
    image1 = ImageTk.PhotoImage(bu)
    n1 = Label(root, image=image1, bd=0)
    n1.place(x=300, y=50)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Pink Grapefruit

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0",bd=0,  fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i1 = Label(root, text="""PRODUCT INFO


I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.

_______________________

RETURN & REFUND POLICY
_______________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i1.place(x=850, y=320)
    def x1():
        root.destroy()
        xxx1()
    r3 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=x1)
    r3.place(x=850, y=300)
    root.mainloop()

def kom2kom2():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    bu = Image.open('mixkombo.webp').resize((500,700)) # rasimga=razmer beriqw
    image1 = ImageTk.PhotoImage(bu)
    n1 = Label(root, image=image1, bd=0)
    n1.place(x=300, y=50)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Pink Grapefruit

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0",bd=0,  fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i1 = Label(root, text="""PRODUCT INFO


I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.

_______________________

RETURN & REFUND POLICY
_______________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i1.place(x=850, y=320)
    def x2():
        root.destroy()
        xx2()
    r3 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=x2)
    r3.place(x=850, y=300)
    root.mainloop()

def kom3kom3():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")
    bu = Image.open('mixkomplekt.webp').resize((500,700)) # rasimga=razmer beriqw
    image1 = ImageTk.PhotoImage(bu)
    n1 = Label(root, image=image1, bd=0)
    n1.place(x=300, y=50)
    def och():
        spin.pack()

    def next():
        a = spin.get()
        price = int(a) * 6
        narx.configure(text=price)

    spin = Spinbox(root, from_=0, to=10, width=8)
    spin.place(x=850,y=245)

    nex = Button(root, text="""     Calc    """, bg="blue", fg="white", command=next)
    nex.place(x=850,y=270)
    b3 = Label(root, text="""
    Pink Grapefruit

    SKU:001

    $       .0
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 14, "normal"))
    b3.place(x=830, y=30)

    narx = Label(root, text='6.00', font=("Arial", 14, "normal"), bg='#EBECF0')
    narx.place(x=870, y=139)

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    l17 = Button(root, text="SHOP FLAVES", justify=LEFT, bg="#EBECF0",bd=0,  fg="black", font=("Arial", 15, "bold"))
    l17.place(x=200, y=50)
    i1 = Label(root, text="""PRODUCT INFO


I'm a product detail. I'm a great place to add 
more information about your product such 
as sizing, material, care and cleaning 
instructions. This is also a great space to 
write what makes this product special and 
how your customers can benefit from this 
item.

_______________________

RETURN & REFUND POLICY
_______________________

SHIPPING INFO
    
    """, fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 10, "bold"))
    i1.place(x=850, y=320)
    def x3():
        root.destroy()
        xxx3()
    r3 = Button(root, text="Add to Cart", bg="green", fg="white", font=('Arial', 15, 'bold'), command=x3)
    r3.place(x=850, y=300)
    root.mainloop()

def xxx1():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('mixkom.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Pink Grapefruit
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('carad image.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)


    root.configure(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('mixkombo.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Total Care
    $50.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('carad image.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)
    root.mainloop()

def xx2():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('mixkom.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Pink Grapefruit
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('uzcard.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)
    root.mainloop()

    root.config(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('mixkomplekt.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Detox Plan
    $30.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('uzcard.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)
    root.mainloop()

def xxx3():
    root = Tk()
    root.geometry("1300x750")
    root.config(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('mixkom.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Pink Grapefruit
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('uzcard.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)
    root.mainloop()

    root.config(bg="#EBECF0")

    def t1():
        root.destroy()
        oyna()
    poco5 = Button(root, text='Pure Flave', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t1)
    poco5.place(x=200, y=10)
    def t2():
        root.destroy()
        rasim()
    poco4 = Button(root, text='Shop', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t2)
    poco4.place(x=300, y=10)
    def t3():
        root.destroy()
        tt3()
    poco3 = Button(root, text='Subscription', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t3)
    poco3.place(x=400, y=10)
    def t4():
        root.destroy()
        tt4()
    l14 = Button(root, text='About Us', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t4)
    l14.place(x=500, y=10)
    def t5():
        root.destroy()
        tt5()
    l15 = Button(root, text='Contact', bg='#EBECF0', bd=0, cursor='hand2', font=('Helvatica',10,'normal'), command=t5)
    l15.place(x=600, y=10)
    def t6():
        root.destroy()
        tt6()
    l16 = Button(root, text="Log in", bg="#EBECF0", bd=0, cursor='hand2', font=("Arial", 10, "bold"), command=t6)
    l16.place(x=800, y=10)

    uy = Image.open('mixkombo.webp').resize((300,400)) # rasimga=razmer beriqw
    image3 = ImageTk.PhotoImage(uy)
    n3 = Label(root, image=image3, bd=0)
    n3.place(x=750, y=60)
    b5 = Label(root, text="""
    Full-Day Cleanses
    $6.00""", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 13, "normal"))
    b5.place(x=1000, y=70)

    b6 = Label(root, text="Subtatal", fg="black", bg='#EBECF0', justify=LEFT, font=("Arial", 12, "normal"))
    b6.place(x=1020, y=250)
    def p1():
        root.destroy()
        pp1()
    r9 = Button(root, text="View Cart", bg="#EBECF0", bd=0, font=('Arial', 13, 'bold'), command=p1)
    r9.place(x=1018, y=300)

    label2 = Label(root, text="karta raqami", bg='#EBECF0', font=('Helvatica', 12, 'bold'))
    label2.place(x=150,y=220)
    entry1 = Entry(root)
    entry1.place(x=140,y=245)

    pp = Image.open('uzcard.jpg').resize((200,150)) # rasimga=razmer beriqw
    image4 = ImageTk.PhotoImage(pp)
    p = Label(root, image=image4, bd=0)
    p.place(x=100, y=60)
    root.mainloop()


register()