from tkinter import *

import backendDesktopbased

def view_command():
    list1.delete(0,END)
    for row in backendDesktopbased.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backendDesktopbased.select(oredr_text.get(),Consigner_text.get(),Cname_text.get(),Caddress_text.get(),Contact_text.get(),Package_text.get()):
        list1.insert(END,row)


def add_command():
    backendDesktopbased.insert(oredr_text.get(),Consigner_text.get(),Cname_text.get(),Caddress_text.get(),Contact_text.get(),Package_text.get())
    list1.delete(0,END)
    list1.insert(END,(oredr_text.get(),Consigner_text.get(),Cname_text.get(),Caddress_text.get(),Contact_text.get(),Package_text.get()))

window=Tk()

l1=Label(window,text="ORDER NO")
l1.grid(row=1,column=1)

l2=Label(window,text="CONSIGNER ID")
l2.grid(row=1,column=6)

l3=Label(window,text="CONSIGNEE NAME")
l3.grid(row=2,column=1)

l4=Label(window,text="SHIPPING ADDRESS")
l4.grid(row=3,column=1)

l5=Label(window,text="CONSIGNEE CONTACT")
l5.grid(row=4,column=1)

l6=Label(window,text="PACKAGE WEIGHT")
l6.grid(row=5,column=1)

oredr_text=StringVar()
e1=Entry(window,textvariable=oredr_text)
e1.grid(row=1,column=2,columnspan=2)

Consigner_text=StringVar()
e2=Entry(window,textvariable=Consigner_text)
e2.grid(row=1,column=8,columnspan=2)

Cname_text=StringVar()
e3=Entry(window,textvariable=Cname_text)
e3.grid(row=2,column=2,columnspan=2)

Caddress_text=StringVar()
e4=Entry(window,textvariable=Caddress_text)
e4.grid(row=3,column=2,columnspan=2)

Contact_text=StringVar()
e5=Entry(window,textvariable=Contact_text)
e5.grid(row=4,column=2,columnspan=2)

Package_text=StringVar()
e6=Entry(window,textvariable=Package_text)
e6.grid(row=5,column=2,columnspan=2)

list1=Listbox(window,height=10,width=50)
list1.grid(row=6,column=1,rowspan=6,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=6,column=7,rowspan=6)

#list1.configure(yscrollcommand=sb1.set)
#sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=15,command=view_command)
b1.grid(row=6,column=9)

b2=Button(window,text="Search Entry",width=15,command=search_command)
b2.grid(row=7,column=9)

b3=Button(window,text="Add Entry",width=15,command=add_command)
b3.grid(row=8,column=9)

b4=Button(window,text="Update",width=15)
b4.grid(row=9,column=9)

b5=Button(window,text="Delete",width=15)
b5.grid(row=10,column=9)

b6=Button(window,text="Close",width=15)
b6.grid(row=11,column=9)


window.mainloop()
