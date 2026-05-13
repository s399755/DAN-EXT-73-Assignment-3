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

# marker parent class
class DifferenceMarker:
    def __init__(self, radius, thickness):
        self.radius = radius
        self.thickness = thickness

    def draw(self, image, x, y):
        pass

# marker for found differences
class FoundMarker(DifferenceMarker):
    def __init__(self):
        super().__init__(25, 3)

    def draw(self, image, x, y):
        cv2.circle(
            image,
            (x, y),
            self.radius,
            (0, 0, 255),
            self.thickness
        )

# marker for revealed differences
class RevealMarker(DifferenceMarker):
    def __init__(self):
        super().__init__(25, 3)

    def draw(self, image, x, y):
        cv2.circle(
            image,
            (x, y),
            self.radius,
            (255, 0, 0),
            self.thickness
        )
        
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

    def is_overlapping(self, x, y, size):
        for old_x, old_y in self.differences:

            if abs(x - old_x) < size * 3 and abs(y - old_y) < size * 3:
                return True

        return False

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

        attempts = 0

        while len(self.differences) < 5 and attempts < 100:
            attempts += 1

            x = random.randint(size, width - size)
            y = random.randint(size, height - size)

            if not self.is_overlapping(x, y, size):

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
        self.image_loaded = False
        
        # marker objects
        self.found_marker = FoundMarker()
        self.reveal_marker = RevealMarker()
        
        # game state tracking
        self.found_differences = []
        self.mistakes = 0
        self.remaining = 5
      
        # window setup
        self.root.title("Find the Differences")
        self.root.geometry("900x650")

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
        self.frame_images.pack(pady=10)

        self.canvas_original = tk.Canvas(
            self.frame_images,
            width=400,
            height=400,
            bg="grey",
            highlightthickness=1,
            highlightbackground="black"
        )
        self.canvas_original.pack(side="left", padx=10)

        self.canvas_modified = tk.Canvas(
            self.frame_images,
            width=400,
            height=400,
            bg="grey",
            highlightthickness=1,
            highlightbackground="black"
        )
        self.canvas_modified.pack(side="right", padx=10)
        
        # click detection
        self.canvas_modified.bind("<Button-1>", self.check_difference) 

    # Load image 
    def load_image(self):
    
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
                ("All Files", "*.*")
            ]
        )
 
        print(file_path)

        if file_path:
            success = self.processor.load_image(file_path)
 
            if success:  
                self.image_loaded = True
            
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
                
                self.label_info.config(
                    text="Game started! Find all 5 differences."
                )
            
                self.processor.generate_differences()
                self.display_image()

                # re-enable clicking for new game
                self.canvas_modified.bind("<Button-1>", self.check_difference)

                print("Image loaded and differences generated")

            else:
                messagebox.showerror(
                    "Image Load Error",
                    "The selected file could not be loaded. Please choose a JPG, JPEG, PNG or BMP image."
            )
    
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
        self.found_marker.draw(self.processor.original_image, x, y)
        self.found_marker.draw(self.processor.modified_image, x, y)
        
    def draw_reveal_circle(self, x, y):
        self.reveal_marker.draw(self.processor.original_image, x, y)
        self.reveal_marker.draw(self.processor.modified_image, x, y)
    
    def reveal_differences(self):
        
        if not self.image_loaded:
            messagebox.showwarning(
                "No Image Loaded",
                "Please load an image before revealing differences."
            )
            return

        for dx, dy in self.processor.differences:

            if (dx, dy) not in self.found_differences:
                self.draw_reveal_circle(dx, dy)

        self.remaining = 0

        self.label_remaining.config(
            text="Remaining: 0"
        )
        
        self.label_info.config(
            text="Differences revealed. Load another image to play again."
        )

        self.display_image()
 
        # disable further clicks
        self.canvas_modified.unbind("<Button-1>")

        messagebox.showinfo(
            "Reveal Differences",
            "All remaining differences have been revealed."
        )
    
    def check_difference(self, event):
        
        if not self.image_loaded:
            messagebox.showwarning(
                "No Image Loaded",
                "Please load an image before playing."
            )
            return

        # scale click position back to original image size
        image_width = self.processor.original_image.shape[1]
        image_height = self.processor.original_image.shape[0]

        click_x = int(event.x * image_width / 400)
        click_y = int(event.y * image_height / 400)

        print("Clicked:", click_x, click_y)

        hit = False

        for dx, dy in self.processor.differences:

            if abs(click_x - dx) < 20 and abs(click_y - dy) < 20:

                hit = True

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
                    
                    self.label_info.config(
                        text="Correct! Difference found."
                    )

                    if self.remaining == 0:

                        self.label_info.config(
                            text="You found all differences!"
                        )

                        messagebox.showinfo(
                            "You Win",
                            "All differences found!"
                        )

                         # disable further clicks
                        self.canvas_modified.unbind("<Button-1>")

                else:
                    self.label_info.config(
                        text="This difference has already been found."
                    )

                break
            
        if not hit:
            self.mistakes += 1
            self.label_mistakes.config(
                text=f"Mistakes: {self.mistakes} / 3"
            )
            
            self.label_info.config(
                text="Wrong guess! Try again."
            )
            
            if self.mistakes >= 3:

                found_count = len(self.found_differences)

                self.label_info.config(
                    text=f"Game over! You found {found_count} out of 5 differences."
                )          

                messagebox.showinfo(
                   "Game Over",
                   f"Too many mistakes! You found {found_count} out of 5 differences. Load a new image to try again."
                )

                # disable further clicks
                self.canvas_modified.unbind("<Button-1>")

# run program
root = tk.Tk()
app = GameApp(root)
root.mainloop()



