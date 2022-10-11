import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import cv2

ROOT_WINDOW_HEIGHT = 500
ROOT_WINDOW_WIDTH = 400

IS_CROPPED = False
CROPPING_EVENT_FINISHED = False
LOADED_IMG = None

# função executada ao selecionar a opção "File > Open Image"
def onOpenImage():
    imagePath = filedialog.askopenfilename(initialdir = "./tests",title = "Open file",filetypes = (("Img files",".png"),("Img files",".jpg")))
    printImage(imagePath)

# função responsável pela exibição da imagem carregada na janela do programa.
def printImage(imagePath):
    if(len(imagePath) > 0):
        LOADED_IMG = ImageTk.PhotoImage(file=imagePath)
        imagebox.config(image=LOADED_IMG)
        imagebox.image = LOADED_IMG

        LOADED_IMG = cv2.imread(imagePath)
        oriImage = LOADED_IMG.copy()
        menubar.entryconfig("Crop", state="active")

def cropImage():
    IS_CROPPED = False
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouseCrop)

def mouseCrop():
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        CROPPING_EVENT_FINISHED = True

def onSaveImage():
    filename_save = filedialog.asksaveasfilename(initialdir = "./tests",title = "Save as",filetypes = (("Img files",".png"),("Img files",".jpg")))

def closeWindow():
    root.destroy()

root = tk.Tk()

root.geometry("{}x{}".format(ROOT_WINDOW_HEIGHT,ROOT_WINDOW_WIDTH))
root.title("Diagnosis of femorotibial osteoarthritis")

menubar = tk.Menu(root)

# Opções do menu superior
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open image ...", command=onOpenImage)
filemenu.add_command(label = "Save", command=onSaveImage)
filemenu.add_command(label = "Exit", command=closeWindow)

menubar.add_cascade(label = "File", menu=filemenu)
menubar.add_command(label = "Crop", state= "disabled", command=cropImage)

root.config(menu=menubar)

imagebox = tk.Label(root)
imagebox.pack()

root.mainloop()