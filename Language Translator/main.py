from tkinter import *
from translate import Translator
def convert():
    v1=lang1.get()
    v2=lang2.get()
    v3=var1.get()
    T=Translator(from_lang=v1,to_lang=v2)
    output=T.translate(v3)
    var2.set(output)

root=Tk()
root.title("Language Translator")
root.geometry("700x360+100+200")
root.minsize(700,360)
root.maxsize(700,360)
root.config(bg="black")
Label(root,text="TRANSLATOR",font="comicsans 20 bold",fg="white",bg="gray20").pack(side=TOP,fill=X)
f1=Frame(root,bg="gray10",padx=45,pady=15,relief=RAISED)
f1.pack(side=TOP,pady=10)

Label(f1,text="Select input Language",fg="white",font="arial 14 bold",bg="gray22",pady=5).grid(row=1,column=0,pady=5)
Label(f1,text="Select output Language",fg="white",font="arial 14 bold",bg="gray22",pady=5).grid(row=1,column=2,pady=5)
lang1=StringVar()
lang2=StringVar()
lang1.set("Choose")
lang2.set("Choose")
choices=["English", "German", "French" , "Hindi"]
menu1=OptionMenu(f1,lang1,*choices)
menu1.grid(row=2,column=0,padx=5,pady=5,ipadx=4,ipady=4)
menu2=OptionMenu(f1,lang2,*choices)
menu2.grid(row=2,column=2,padx=5,pady=5,ipadx=4,ipady=4)

Label(f1,text="Enter Text",font="arial 14 bold",fg="white",bg="gray").grid(row=3,column=0,padx=8,pady=8,ipadx=10,ipady=10)
Label(f1,text="Output Text",font="arial 14 bold",fg="white",bg="gray").grid(row=3,column=2,padx=8,pady=8,ipadx=10,ipady=10)

var1=StringVar()
var2=StringVar()
Entry(f1,textvariable=var1, font="comicsans 15 bold").grid(row=4,column=0,ipadx=12,ipady=12,padx=4,pady=4)
Entry(f1,textvariable=var2, font="comicsans 15 bold").grid(row=4,column=2,ipadx=12,ipady=12,padx=4,pady=4)
Button(f1,text="Submit",fg="white",bg="gray22",command=convert).grid(row=5,column=1,padx=5,pady=5,ipadx=10,ipady=10)


root.mainloop()