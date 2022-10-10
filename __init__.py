import tkinter as tk
from tkinter import filedialog

ROOT_SCREEN_WIDTH = 300
ROOT_SCREEN_HEIGHT = 200

def onOpen():
    print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Img files",".png"),("Img files",".jpg"))))

def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Img files",".png"),("Img files",".jpg"))))


root_window = tk.Tk()

root_window.geometry("{}x{}".format(ROOT_SCREEN_HEIGHT,ROOT_SCREEN_WIDTH))
root_window.title("Image")

menubar = tk.Menu(root_window)

filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open Image", command=onOpen)
filemenu.add_command(label = "Save", command=onSave)
filemenu.add_command(label = "Exit")

menubar.add_cascade(label = "File", menu=filemenu)

root_window.config(menu=menubar)
root_window.mainloop()