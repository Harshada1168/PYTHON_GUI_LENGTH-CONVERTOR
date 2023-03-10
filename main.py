from tkinter import *
App=Tk()
App.title("Length Convertor")
App.geometry("300x300")
scales=['meters', 'inches', 'foot']

_from=StringVar()
from_menu=OptionMenu(App, _from, *scales)
from_menu.grid(row=0, column=0)

msg=Label(App, text='Convert to')
msg.grid(row=0, column=1)

to_=StringVar()
to_menu=OptionMenu(App, to_, *scales)
to_menu.grid(row=0, column=2)

msg1=Label(App, text="Enter your length ")
msg1.grid(row=1, column=0)
input=Entry()
input.grid(row=1, column=1)

def convertor():
    fro= _from.get()
    to=to_.get()
    num=int(input.get())
    if fro=='meters' and to=='inches':
        conv_num=num*39.37
    elif fro=='meters' and to=='foot':
        conv_num=num*3.28
    elif fro=='inches' and to=='meters':
        conv_num=num/39.37
    elif fro=='inches' and to=='foot':
        conv_num=num/12
    elif fro=='foot' and to=='meters':
        conv_num=num/3.28
    elif fro=='foot' and to=='inches':
        conv_num=num*12
    else:
        conv_num=num
    msg2=Label(App, text=round(conv_num, 2))
    msg2.grid(row=1, column=2)

b=Button(App, text="Convert", command=convertor)
b.grid(row=2, column=0)
App.mainloop()