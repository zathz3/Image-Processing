import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import cv2

ROOT_WINDOW_HEIGHT = 500
ROOT_WINDOW_WIDTH = 400

# função executada ao selecionar a opção "File > Open Image"
def onOpenImage():
    imagePath = filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Img files",".png"),("Img files",".jpg")))
    printImage(imagePath)

# função responsável pela exibição da imagem carregada na janela do programa.
def printImage(imagePath):
    if(len(imagePath) > 0):
        image = ImageTk.PhotoImage(file=imagePath)
        imagebox.config(image=image)
        imagebox.image = image

        image = cv2.imread(imagePath)
        oriImage = image.copy()

def onSaveImage():
    filename_save = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Img files",".png"),("Img files",".jpg")))

def main():
    root_window = tk.Tk()

    root_window.geometry("{}x{}".format(ROOT_WINDOW_HEIGHT,ROOT_WINDOW_WIDTH))
    root_window.title("Diagnosis of femorotibial osteoarthritis")

    menubar = tk.Menu(root_window)

    # Opções do menu superior
    filemenu = tk.Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Open Image", command=onOpenImage)
    filemenu.add_command(label = "Save", command=onSaveImage)
    filemenu.add_command(label = "Exit")

    menubar.add_cascade(label = "File", menu=filemenu)

    root_window.config(menu=menubar)

    imagebox = tk.Label(root_window)
    imagebox.pack()

    root_window.mainloop()

if __name__ == "__main__":
    main()