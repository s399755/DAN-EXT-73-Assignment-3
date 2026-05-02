# Group Name: [DAN/EXT 73]

# Group Member:
# Patrick Burzynski - [399755]

# Assignment 3
"""This program creates a desktop application using Tkinter and OpenCV. 
It allows the user to load an image, generates random differences,
and lets the user find those differences by clicking on the image."""

import tkinter as tk

# Create window
root = tk.Tk()
root.title("Find the Differences")
root.geometry("800*600")

# Label
label_info = tk.label(root, text="Load an image to start")
label_info.pack()

#Buttons
btn_load + tk.Button(root, text="Load Image")
btn_load.pack()

btn_reveal = tk.Button(root, text="Reveal Differences")
btn_reveal.pack()

#canvas
canvas = tk.Canvas(root, width=400, height=400, bg="grey")
canvas.pack()

# run program
root.mainloop()



