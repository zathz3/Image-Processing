import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import cv2

ROOT_SCREEN_WIDTH = 400
ROOT_SCREEN_HEIGHT = 500

def onOpenImage():
    imagePath = filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Img files",".png"),("Img files",".jpg")))
    printImage(imagePath)

def printImage(imagePath):
    if(len(imagePath) > 0):
        image = ImageTk.PhotoImage(file=imagePath)
        imagebox.config(image=image)
        imagebox.image = image

        image = cv2.imread(imagePath)
        oriImage = image.copy()

def onSaveImage():
    filename_save = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Img files",".png"),("Img files",".jpg")))


root_window = tk.Tk()

root_window.geometry("{}x{}".format(ROOT_SCREEN_HEIGHT,ROOT_SCREEN_WIDTH))
root_window.title("Diagnosis of femorotibial osteoarthritis")

menubar = tk.Menu(root_window)

filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open Image", command=onOpenImage)
filemenu.add_command(label = "Save", command=onSaveImage)
filemenu.add_command(label = "Exit")

menubar.add_cascade(label = "File", menu=filemenu)

root_window.config(menu=menubar)

imagebox = tk.Label(root_window)
imagebox.pack()

root_window.mainloop()
