# Group Name: [DAN/EXT 73]

# Group Member:
# Patrick Burzynski - [399755]

# Assignment 3
"""This program creates a desktop application using Tkinter and OpenCV. 
It allows the user to load an image, generates random differences,
and lets the user find those differences by clicking on the image."""

import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import random
from PIL import Image, ImageTk

# image processor 
class ImageProcessor:
    def __init__(self):
        self.original_image = None
        self.modified_image = None
        self.differences = []

    def load_image(self, path):
        self.original_image = cv2.imread(path)

        if self.original_image is None:
            print("Error loading image")
            return False

        self.modified_image = self.original_image.copy()
        print("Image copied for modification")
        return True

    def get_region(self, x, y, size):
        height, width, _ = self.modified_image.shape

        x1 = max(0, x - size)
        x2 = min(width, x + size)

        y1 = max(0, y - size)
        y2 = min(height, y + size)

        return x1, y1, x2, y2

    def add_colour_patch(self, x, y, size):
        x1, y1, x2, y2 = self.get_region(x, y, size)

        # yellow patch in BGR format
        self.modified_image[y1:y2, x1:x2] = (0, 255, 255)

    def add_blur_patch(self, x, y, size):
        x1, y1, x2, y2 = self.get_region(x, y, size)

        area = self.modified_image[y1:y2, x1:x2]

        if area.size > 0:
            blurred_area = cv2.GaussianBlur(area, (21, 21), 0)
            self.modified_image[y1:y2, x1:x2] = blurred_area

    def add_invert_patch(self, x, y, size):
        x1, y1, x2, y2 = self.get_region(x, y, size)

        area = self.modified_image[y1:y2, x1:x2]

        if area.size > 0:
            self.modified_image[y1:y2, x1:x2] = 255 - area

    # Generate differences
    def generate_differences(self):
        self.differences = []

        height, width, _ = self.modified_image.shape

        size = 20
        alteration_types = ["colour", "blur", "invert"]

        for i in range(5):
            x = random.randint(size, width - size)
            y = random.randint(size, height - size)

            self.differences.append((x, y))

            alteration = random.choice(alteration_types)

            if alteration == "colour":
                self.add_colour_patch(x, y, size)

            elif alteration == "blur":
                self.add_blur_patch(x, y, size)

            elif alteration == "invert":
                self.add_invert_patch(x, y, size)

        print("Differences:", self.differences)   

# Main Class
class GameApp:
    def __init__(self, root):
        self.root = root
        self.processor = ImageProcessor()

        # game state tracking
        self.found_differences = []
        self.mistakes = 0
        self.remaining = 5
      
        # window setup
        self.root.title("Find the Differences")
        self.root.geometry("800x600")

        # Label
        self.label_info = tk.Label(root, text="Load an image to start")
        self.label_info.pack()
        
        # score labels
        self.label_remaining = tk.Label(root, text="Remaining: 5")
        self.label_remaining.pack()

        self.label_mistakes = tk.Label(root, text="Mistakes: 0 / 3")
        self.label_mistakes.pack()

        # Buttons
        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.btn_load.pack()

        self.btn_reveal = tk.Button(
            root,
            text="Reveal Differences",
            command=self.reveal_differences
        )
        
        self.btn_reveal.pack()

        # image frame
        self.frame_images = tk.Frame(root)
        self.frame_images.pack()

        self.canvas_original = tk.Canvas(self.frame_images, width=400, height=400, bg="grey")
        self.canvas_original.pack(side="left", padx=10)

        self.canvas_modified = tk.Canvas(self.frame_images, width=400, height=400, bg="grey")
        self.canvas_modified.pack(side="right", padx=10)
        
        # click detection
        self.canvas_modified.bind("<Button-1>", self.check_difference) 

    # Load image 
    def load_image(self):
        
        file_path = filedialog.askopenfilename()
        print(file_path)

        if file_path:
            success = self.processor.load_image(file_path)

            if success:
                
                # reset game state
                self.found_differences = []
                self.mistakes = 0
                self.remaining = 5

                self.label_remaining.config(
                    text="Remaining: 5"
                )

                self.label_mistakes.config(
                    text="Mistakes: 0 / 3"
                )
                
                self.processor.generate_differences()
                self.display_image()
                # re-enable clicking for new game
                self.canvas_modified.bind("<Button-1>", self.check_difference)
                print("Image loaded and differences generated")
    
    def display_image(self):

        # original image
        original = self.processor.original_image

        # modified image
        modified = self.processor.modified_image

        # convert BGR to RGB
        original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
        modified = cv2.cvtColor(modified, cv2.COLOR_BGR2RGB)

        # convert to PIL format
        original = Image.fromarray(original)
        modified = Image.fromarray(modified)

        # resize images
        original = original.resize((400, 400))
        modified = modified.resize((400, 400))

        # convert for tkinter
        self.tk_original = ImageTk.PhotoImage(original)
        self.tk_modified = ImageTk.PhotoImage(modified)

        # clear old images
        self.canvas_original.delete("all")
        self.canvas_modified.delete("all")

        # display original image
        self.canvas_original.create_image(
            0,
            0,
            anchor="nw",
            image=self.tk_original
        )

        # display modified image
        self.canvas_modified.create_image(
            0,
            0,
            anchor="nw",
            image=self.tk_modified
        )
    
    def draw_found_circle(self, x, y):     
        cv2.circle(self.processor.original_image, (x, y), 25, (0, 255, 0), 3)
        cv2.circle(self.processor.modified_image, (x, y), 25, (0, 255, 0), 3)
        
    def reveal_differences(self):

        for dx, dy in self.processor.differences:
            self.draw_found_circle(dx, dy)

        self.display_image()

        # disable further clicks
        self.canvas_modified.unbind("<Button-1>")

        messagebox.showinfo(
            "Reveal Differences",
            "All differences have been revealed."
    )  
    
    def check_difference(self, event):

        # scale click position back to original image size
        image_width = self.processor.original_image.shape[1]
        image_height = self.processor.original_image.shape[0]

        click_x = int(event.x * image_width / 400)
        click_y = int(event.y * image_height / 400)

        print("Clicked:", click_x, click_y)

        hit = False

        for dx, dy in self.processor.differences:

            if abs(click_x - dx) < 20 and abs(click_y - dy) < 20:

                if (dx, dy) not in self.found_differences:
                    self.found_differences.append((dx, dy))
                    self.remaining -= 1

                    # draw permanent visual marker
                    self.draw_found_circle(dx, dy)

                    # refresh images
                    self.display_image()

                    self.label_remaining.config(
                        text=f"Remaining: {self.remaining}"
                    )

                    hit = True
                    
                    if self.remaining == 0:

                        messagebox.showinfo(
                            "You Win",
                            "All differences found!"
                        )

                        # disable further clicks
                        self.canvas_modified.unbind("<Button-1>")
                break
            
        if not hit:
            self.mistakes += 1
            self.label_mistakes.config(
                text=f"Mistakes: {self.mistakes} / 3"
            )
            
            print("Wrong guess")

            if self.mistakes >= 3:

                messagebox.showinfo(
                    "Game Over",
                    "Too many mistakes! Load a new image to try again."
                )

                # disable further clicks
                self.canvas_modified.unbind("<Button-1>")

# run program
root = tk.Tk()
app = GameApp(root)
root.mainloop()
