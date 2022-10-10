import tkinter as tk
from tkinter import filedialog

def onOpen():
    print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Img files",".png"),("Img files",".jpg"))))

def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Img files",".png"),("Img files",".jpg"))))


window = tk.Tk()

window.geometry('300x200')
window.title("Lula Preso")

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open Image", command=onOpen)
filemenu.add_command(label = "Save", command=onSave)
filemenu.add_command(label = "Exit")



menubar.add_cascade(label = "File", menu=filemenu)


window.config(menu=menubar)
window.mainloop()