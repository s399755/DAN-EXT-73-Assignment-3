# Group Name: [DAN/EXT 73]

# Group Member:
# Patrick Burzynski - [399755]

# Assignment 3
"""This program creates a desktop application using Tkinter and OpenCV. 
It allows the user to load an image, generates random differences,
and lets the user find those differences by clicking on the image."""

import tkinter as tk
from tkinter import filedialog 

#Main Class
class GameApp:
   def __init__(self, root):
       self.root = tk.Tk()
      
       # window setup
       self.root.title("Find the Differences")
       self.root.geometry("800*600")

       # Label
       self.label_info = tk.Label(root, text="Load an image to start")
       self.label_info.pack()

       #Buttons
       self.btn_load + tk.Button(root, text="Load Image")
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

self.btn_load = tk.Button(root,text="Load Image", command=self.load_image)   

# run program
root = tk.Tk()
app = GameApp(root)
root.mainloop()



