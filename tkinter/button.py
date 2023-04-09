from tkinter import *
window = Tk()
window.title("SUNIL BISWAKARMA")
window.geometry('500x700')
def log_entry():
    print("Logged In")
button = Button(window, text="Login", command=log_entry, width=12, font=('bold', 12), activebackground="red", activeforeground="black")

button.pack()
mainloop()