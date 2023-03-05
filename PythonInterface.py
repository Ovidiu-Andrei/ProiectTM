# Import the required Libraries
import cv2
from tkinter import * 
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import tkinter.messagebox
from PIL import ImageTk
from PIL import Image
from scipy.interpolate import UnivariateSpline
import numpy as np
import easygui
import os

# Create an instance of tkinter frame
FirstWindow = tk.Tk()
FirstWindow.title('ImageProcessing - UI')
FirstWindow.geometry("1280x1080")
FirstWindow.config(background="#5cfcff")
CreateLogo = Image.open(r"C:\Users\Ovidiu\Desktop\ProiectTM\ImageProcessing.png")
CreateLogo.save(r"C:\Users\Ovidiu\Desktop\ProiectTM\ImageProcessing.ico", format='ICO',
          sizes=[(40, 40)])
FirstWindow.iconbitmap(r'C:\Users\Ovidiu\Desktop\ProiectTM\ImageProcessing.ico')
global img_o
global pathToImage
global SaveImage
SaveImage = None
global ResizeImage
ResizeImage = None
def open_file():
  global img_o
  global pathToImage
  pathToImage = filedialog.askopenfile(mode='r', title = 'Select a image', filetypes=[("jpeg","*.jpg"),
              ("png", "*.png"),("jpg", "*.jpg"),("tiff", "*.tiff"),("bmp", "*.bmp"),("gif", "*.gif")])
  img_o=cv2.imread(pathToImage.name)
  scaling=(int(img_o.shape[1]*0.5),int(img_o.shape[0]*0.5))
  img_o=cv2.resize(img_o,scaling,interpolation=cv2.INTER_AREA)
  img_o=cv2.cvtColor(img_o,cv2.COLOR_BGR2RGB)
  img_o=Image.fromarray(img_o)
  img_o=ImageTk.PhotoImage(img_o)
  label_o=tk.Label(image=img_o) 
  label_o.grid(row=0,column=0,sticky=tk.E + tk.W + tk.N + tk.S) 
  root = Tk()
  root.destroy()
  root.mainloop()
  
def ShowAMessage():
  tkinter.messagebox.showinfo('Be aware!',"Be carefully, the following commands will work just if you added a photo")

def spreadLookupTable(x, y):
    spline= UnivariateSpline(x, y)
    return spline(range(256))

def warm(image):
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    return cv2.merge((red_channel, green_channel, blue_channel))

def save():
    pass

def grayFilter():
  pass   

def rgbFilter(image):
	(B, G, R) = cv2.split(image) #spliting the img into RGB components
	# find the maximum pixel intensity values for each
	# (x, y)-coordinate,, then set all pixel values less
	# than M to zero
	M = np.maximum(np.maximum(R, G), B)
	R[R < M] = 0
	G[G < M] = 0
	B[B < M] = 0
	# merge the channels back together and return the image
	return cv2.merge([B, G, R])

def resize_func():
    global width,height,disp_img,ResizeImage
    if ResizeImage is None:
      image = Image.open(pathToImage.name)
      image = Image.fromarray(image)
    else:
      image = Image.fromarray(ResizeImage)
    w = int(width.get())
    h = int(height.get())

    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img


def ApplyFilter(mode):
    global img_o
    global pathToImage
    global SaveImage
    global ResizeImage
    if mode==warm:
       img_o=cv2.imread(pathToImage.name)
       img_o=cv2.cvtColor(img_o,cv2.COLOR_BGR2RGB)
       img_o=warm(img_o)
       SaveImage=img_o
       ResizeImage=img_o
       scaling=(int(img_o.shape[1]*0.5),int(img_o.shape[0]*0.5))
       img_o=cv2.resize(img_o,scaling,interpolation=cv2.INTER_AREA)
       img_o=Image.fromarray(img_o)
       img_o=ImageTk.PhotoImage(img_o)
       label2_img=tk.Label(image=img_o)
       label2_img.grid(row=0,column=0,sticky=tk.E + tk.W + tk.N + tk.S)
    elif mode==grayFilter:
       img_o=cv2.imread(pathToImage.name)
       img_o = cv2.cvtColor(img_o, cv2.COLOR_BGR2GRAY )
       SaveImage=img_o
       ResizeImage=img_o
       scaling=(int(img_o.shape[1]*0.5),int(img_o.shape[0]*0.5))
       img_o=cv2.resize(img_o,scaling,interpolation=cv2.INTER_AREA)
       img_o=Image.fromarray(img_o)
       img_o=ImageTk.PhotoImage(img_o)
       label2_img=tk.Label(image=img_o)
       label2_img.grid(row=0,column=0,sticky=tk.E + tk.W + tk.N + tk.S)         
    elif mode==rgbFilter:
       img_o=cv2.imread(pathToImage.name)
       img_o=rgbFilter(img_o)
       SaveImage=img_o
      #  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
      #  img=Image.fromarray(img)
      #  img=ImageTk.PhotoImage(img)
       label2_img=tk.Label(image=img_o)
       label2_img.grid(row=0,column=0,sticky=tk.E + tk.W + tk.N + tk.S)       
    elif mode==save:
      if SaveImage is None:
        easygui.msgbox("You need to modify an upload photo in order to save an image!", title="Inform message")
      else:    
        name = filedialog.asksaveasfilename(title="Save as...", filetypes=(('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')), defaultextension=".png")
      if name:
        cv2.imwrite(name, SaveImage)
        easygui.msgbox("The modified image has been saved!", title="Inform message")
      else:
        easygui.msgbox("Wrong Path!", title="Inform message")
        

def ShowMenu():
  global width,height,disp_img
  WarmBtn = Button(FirstWindow, text = 'Warm', bg= 'yellow', 
                    compound = RIGHT , command = lambda:[ApplyFilter(warm)])
  WarmBtn.place(relx = 1, x =-2, y = 2, anchor = NE)

  GrayBtn = Button(FirstWindow, text = 'GrayFilter', bg= 'gray', 
                    compound = RIGHT , command = lambda:[ApplyFilter(grayFilter)])
  GrayBtn.place(relx = 1, x =-2, y = 50, anchor = NE)

  RGBBtn = Button(FirstWindow, text = 'RGB-Filter', bg= 'green', 
                    compound = RIGHT , command = lambda:[ApplyFilter(rgbFilter)])
  RGBBtn.place(relx = 1, x =-2, y = 98, anchor = NE)

  SaveBtn = Button(FirstWindow, text = 'Save', bg= 'red', 
                    compound = RIGHT , command = lambda:[ApplyFilter(save)])
  SaveBtn.place(relx = 1, x =-2, y = 146, anchor = NE)

  frame = Frame(FirstWindow)
  frame.grid()

  Label(
      frame,
      text='Width'
      ).grid(column= 0)
  width = Entry(frame, width=10)
  width.insert(END, 300)
  width.grid(column= 0)

  Label(
      frame,
      text='Height'
      ).grid(column=0)

  height = Entry(frame, width=10)
  height.insert(END, 350)
  height.grid(column= 0)

  disp_img = Label()
  disp_img.grid(pady=1)

  resize_btn = Button(
      frame,
      text='Resize',
      command=resize_func
  )
  resize_btn.grid(column= 0)


# Adding widgets to the root FirstWindow
BrowseLabel = Label(FirstWindow, text = 'Click on the below button to pick a new image on the canvas\n - After you pick a photo this text will disappear\n - And a lot of buttons will apeer', font =(
                     'Verdana', 15)).grid(row=0, column=0, pady=10, ipadx = 250, ipady = 180 )
  
# Creating a photoimage object to use folder image
photo = PhotoImage(file = r"C:\Users\Ovidiu\Desktop\ProiectTM\Images\Folder.png")
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)

# Creating a photoimage object to use folder image
menuImg = PhotoImage(file = r"C:\Users\Ovidiu\Desktop\ProiectTM\Images\menu.png")
# Resizing image to fit on button
ResizedMenuImg = menuImg.subsample(15, 15)

# Create the Browse button
BrowseBtn = Button(FirstWindow, text = 'Browse Me !', image = photoimage, bg='#ffb3fe',
                    compound = LEFT, command = lambda:[open_file()]).grid(row=1, column=0, ipadx = 10, ipady = 10,)
# Create a button which will disapper
DestroyMenuBtn = Button(FirstWindow, text = 'Activate the Menu',image = ResizedMenuImg, bg= 'yellow', 
                    compound = RIGHT , command = lambda:[DestroyMenuBtn.destroy(), ShowMenu(), ShowAMessage()])
DestroyMenuBtn.place(relx = 1, x =-2, y = 2, anchor = NE)

FirstWindow.mainloop()