# Import the required Libraries
import cv2
from tkinter import * 
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import tkinter.messagebox
from PIL import ImageTk
from PIL import Image
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

def open_file():
  pathToImage = filedialog.askopenfile(mode='r', title = 'Select a image', filetypes=[("jpeg","*.jpg"),
              ("png", "*.png"),("jpg", "*.jpg"),("tiff", "*.tiff"),("bmp", "*.bmp"),("gif", "*.gif")])
  img_o=cv2.imread(pathToImage.name)
  dim=(int(img_o.shape[1]*0.5),int(img_o.shape[0]*0.5))
  img_o=cv2.resize(img_o,dim,interpolation=cv2.INTER_AREA)
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

def ActivateMenu():
  DestroyMenuBtn = Button(FirstWindow, text = 'Activate the Menu', bg= 'yellow', 
                    compound = RIGHT , command = lambda:[DestroyMenuBtn.destroy(), ActivateMenu()])
  DestroyMenuBtn.place(relx = 1, x =-2, y = 2, anchor = NE)
  
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
                    compound = RIGHT , command = lambda:[DestroyMenuBtn.destroy(), ActivateMenu(), ShowAMessage()])
DestroyMenuBtn.place(relx = 1, x =-2, y = 2, anchor = NE)

FirstWindow.mainloop()