# Group Name: [DAN/EXT 73]

# Group Member:
# Patrick Burzynski - [399755]

# Assignment 3
"""This program creates a desktop application using Tkinter and OpenCV. 
It allows the user to load an image, generates random differences,
and lets the user find those differences by clicking on the image."""

import tkinter as tk
from tkinter import filedialog 
import cv2

#image processor 
class ImageProcessor:
    def __init__(self):
        self.original_image = None
        self.modified_image = None

    def load_image(self,path):
        self.orginal_image = cv2.imread(path)

        if self.original_image is None:
            print("Error loading image")
            return False

        self.modified_image = self.original_image.copy()
        print("Image copied for modification")
        return True
           
       
#Main Class
class GameApp:
   def __init__(self, root):
       self.root = root
       self.processor = ImageProcessor()
      
       # window setup
       self.root.title("Find the Differences")
       self.root.geometry("800x600")

       # Label
       self.label_info = tk.Label(root, text="Load an image to start")
       self.label_info.pack()

       #Buttons
       self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
       self.btn_load.pack()

       self.btn_reveal = tk.Button(root, text="Reveal Differences")
       self.btn_reveal.pack()

       #canvas
       self.canvas = tk.Canvas(root, width=400, height=400, bg="grey")
       self.anvas.pack()   

#Load image 
def load_image(self):
    file_path = filedialog.askopenfilename()
    print(file_path)

    if file_path:
        success = self.processor.load_image(file_path)

        if success:
            print("Image loaded successfully")

# run program
root = tk.Tk()
app = GameApp(root)
root.mainloop()



