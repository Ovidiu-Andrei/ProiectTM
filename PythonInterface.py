# Import the required Libraries
import cv2
from tkinter import * 
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk
from PIL import Image





# Create an instance of tkinter frame
FirstWindow = tk.Tk()
FirstWindow.title('ImageProcessing - UI')
FirstWindow.geometry("1280x1080")
FirstWindow.config(background="#5cfcff")
CreateLogo = Image.open(r"C:\Users\Ovidiu\Desktop\ProiectTM\ImageProcessing.png")
CreateLogo.save(r"C:\Users\Ovidiu\Desktop\ProiectTM\ImageProcessing.ico", format='ICO',
          sizes=[(40, 40)])
FirstWindow.iconbitmap(r'C:\Users\Ovidiu\Desktop\ProiectTM\ImageProcessing.ico')


# Adding widgets to the root FirstWindow
Label(FirstWindow, text = 'Click on the bellow button to add a new picture on the canvas', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:\Users\Ovidiu\Desktop\ProiectTM\Folder.png")
  
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
  


def open_file():
  
  pathToImage = filedialog.askopenfile(mode='r', title = 'Select a image', filetypes=[('jpeg', '*.jpg')])
  
  

  # display an image label
  # image = Image.open(pathToImage.name)
  # photo = tk.PhotoImage(file=image)
  # ttk.Label(
  #     FirstWindow,
  #     image=photo,
  #     padding=5
  # ).pack()
  
  #ttk.Label(self, image=self.python_image).pack()

  #SecondWindow = tk.Tk()
  #SecondWindow.geometry("1280x1080")

  #SelectedImage=cv2.imread(pathToImage.name)

  # dim=(int(SelectedImage.shape[1]*0.5),int(SelectedImage.shape[0]*0.5))
  # SelectedImage=cv2.resize(SelectedImage,dim,interpolation=cv2.INTER_AREA)
  # SelectedImage=cv2.cvtColor(SelectedImage,cv2.COLOR_BGR2RGB)
  # SelectedImage=Image.fromarray(SelectedImage)
  


  #SelectedImage = PIL.Image.open(pathToImage)
  #ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2image))

  #SelectedImage=ImageTk.PhotoImage(image=Image.fromarray(SelectedImage))
  #label_o=ttk.Label(image=SelectedImage) 
  #label_o.grid(row=0,column=0,rowspan=5) #afisam imaginea originala
  #print(label_o)


  #cv2.imshow('image', SelectedImage)
  print(pathToImage.name)
  #SecondWindow.mainloop()



  
# Create the Browse button
Button(FirstWindow, text = 'Browse Me !', image = photoimage,
                    compound = LEFT, command=lambda:[FirstWindow.quit(),open_file()]).pack(side = TOP)

FirstWindow.mainloop()



