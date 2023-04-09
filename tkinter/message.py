
from tkinter import *
window = Tk()
window.geometry('500x500')
message = Message(window, text='Python', relief=RAISED, padx=20, pady=20)
var = StringVar()
ent_var = StringVar()
message1 = Message(window, textvariable=var, relief=RAISED, padx=50, pady=50)
entry = Entry(window, textvariable=ent_var)
def insert():
    result = ent_var.get()
    var.set(result)
button = Button(window, text='OK', command = insert)
message1.pack()
entry.pack()
button.pack()
window.mainloop()