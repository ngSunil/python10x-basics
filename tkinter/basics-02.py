from tkinter import *
window = Tk()
window.title("SUNIL BISWAKARMA")
window.geometry('500x700')
# window.config(bg='yellow')
# frame1 = Frame(window, bg='red', width=300, height=300, cursor='dot')
# frame2 = Frame(window, bg='green', width=300, height=300, cursor='dotbox')
# button1 = Button(frame1, text="Test Button", bg="blue")
# button2 = Button(frame2, text="Button2", bg="green")
# button3 = Button(frame1, text="Button 3", fg="red")
# frame1.pack(side=TOP)
# frame2.pack(side=BOTTOM)
# button1.pack()
# button2.pack()
# button3.pack()

# INPUT BOXES
label1 = Label(window, text="Mail")
label2 = Label(window, text="Password")
el = Entry(window, width=40, borderwidth=0)
el2 = Entry(window, width=40, borderwidth=0)
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
el.grid(row=0, column=2)
el2.grid(row=1, column=2)

mainloop()