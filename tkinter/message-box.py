
from tkinter import *
import tkinter.messagebox
window = Tk()
tkinter.messagebox.showerror("Info", "Running of time")
question = tkinter.messagebox.askyesno("Yesno", 'Are you sure?')
if question == True:
    print('Great')
else:
    print('Sorry to hear that')
window.mainloop()