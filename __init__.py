import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import cv2
import numpy as np
import os

ROOT_WINDOW_HEIGHT = 500
ROOT_WINDOW_WIDTH = 400

img_name = ""
image_path = ""

IS_CROPPED = False
CROPPING_EVENT_FINISHED = False
LOADED_IMG = None
CROP_IMG = None

x_start, y_start, x_end, y_end = 0, 0, 0, 0
cropping = False
image = None
oriImage = None

# função executada ao selecionar a opção "File > Open Image"
def onOpenImage():
    global imagePath
    imagePath = filedialog.askopenfilename(initialdir = "./tests",title = "Open file",filetypes = (("Img files",".png"),("Img files",".jpg")))
    global img_name
    img_name = imagePath[-12::]
    printImage(imagePath)


# def getCropDirectory(crop_name):
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     crop_path = dir_path + crop_name

# função responsável pela exibição da imagem carregada na janela do programa.
def printImage(imagePath):
    if(len(imagePath) > 0):
        global oriImage, LOADED_IMG
        LOADED_IMG = ImageTk.PhotoImage(file=imagePath)
        imagebox.config(image=LOADED_IMG)
        imagebox.image = LOADED_IMG

        LOADED_IMG = cv2.imread(imagePath)
        oriImage = LOADED_IMG.copy()
        menubar.entryconfig("Crop", state="active")


def printCrop(cropPath):
    if (len(imagePath) > 0):
        global LOADED_IMG, CROP_IMG


def onOpenCrop():
    cropPath = filedialog.askopenfilename(initialdir="./crops", title="Open file",
                                           filetypes=(("Img files", ".png"), ("Img files", ".jpg")))
    imgcrop = cv2.imread(cropPath)
    cv2.namedWindow("crop")
    cv2.imshow("crop", imgcrop)
    cv2.waitKey(5)
    cv2.destroyWindow("crop")


# Funcao para detectar os movimentos do mouse e realizar o crop
def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, cropping, pathImagemRecortada, cropped, i
    if event == cv2.EVENT_LBUTTONDOWN:
        # Ao pressionar o mouse, armazena posicao inicial e final
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
    elif event == cv2.EVENT_MOUSEMOVE:
        # movimentacao do mouse
        if cropping == True:
            x_end, y_end = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        # soltar left click
        x_end, y_end = x, y
        # finaliza o crop
        cropping = False
        refPoint = [(x_start, y_start), (x_end, y_end)]
        if len(refPoint) == 2:
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            crop_name = "crops/" + img_name
            cv2.imwrite(crop_name,roi)
            cropped = True
            res = cv2.matchTemplate(LOADED_IMG,roi,cv2.TM_CCOEFF_NORMED)
            threshold = 0.99
            loc = np.where (res >= threshold)
            x_coordinate = list(loc[0])
            y_coordinate = list(loc[1])

            im = Image.open(crop_name)
            width, height = im.size
            xstart = x_coordinate[0]
            ystart = y_coordinate[0]

            xend = xstart + width
            yend = ystart + height

            print(xstart,ystart,xend,yend)

            i = LOADED_IMG.copy()

            cv2.namedWindow("image2")
            cv2.imshow("image2", i)
            cv2.rectangle(i, (xstart, ystart), (xend, yend), (255, 0, 0), 2)
            cv2.imshow("image2", i)
            cv2.waitKey(5)
            cv2.destroyWindow("image2")







def crop():
    global cropped, img
    cropped = False
    cv2.namedWindow("image")

    while not cropped:
        try:
            cv2.setMouseCallback("image", mouse_crop)
        except:
            print("Window Closed")
            cropped = True

        img = LOADED_IMG.copy()
        if not cropping:
            #mostra imagem na janela
            cv2.imshow("image", LOADED_IMG)
        if cropping:
            #imagem, ponto inicial, ponto final, cor, largura
            cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
            cv2.imshow("image", img)
        cv2.waitKey(1)
    cv2.destroyWindow("image")



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
filemenu.add_command(label = "Open crop ...", command=onOpenCrop)
filemenu.add_command(label = "Save", command=onSaveImage)
filemenu.add_command(label = "Exit", command=closeWindow)

menubar.add_cascade(label = "File", menu=filemenu)
menubar.add_command(label = "Crop", state= "disabled", command=crop)

root.config(menu=menubar)

imagebox = tk.Label(root)
imagebox.pack()

root.mainloop()