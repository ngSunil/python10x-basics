
from tkinter import *
window = Tk()
window.geometry('500x500')
check_bx1 = IntVar()
check_bx2 = IntVar()
check_bx3 = IntVar()
chk_btn1 = Checkbutton(window, text='apple', onvalue=1, offvalue=0, height=2, width=10)
chk_btn2 = Checkbutton(window, text='mango', onvalue=1, offvalue=0, height=2, width=10)
chk_btn3 = Checkbutton(window, text='plum', onvalue=1, offvalue=0, height=2, width=10)
chk_btn1.pack()
chk_btn2.pack()
chk_btn3.pack()
window.mainloop()