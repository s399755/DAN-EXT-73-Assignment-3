# DAN-EXT-73-Assignment-3
Software Now HIT137

## Group Name
DAN/EXT 73

## Group Member
Patrick Burzynski - 399755

## Assignment 3
This program creates a desktop application using Tkinter and OpenCV. It allows the user to load an image, generates random differences, and lets the user find those differences by clicking on the image.

Update 1 
- Initial setup of program structure. Created basic Tkinter window with title, size and main loop.

Update 2 
- Added basic GUI components including label, buttons and canvas layout.

Update 3 
- Converted GUI into a class structure using GameApp to begin applying object-oriented programming.

Update 4 
- Connected load image button to a function. Currently prints a message when clicked.

Update 5 
- Implemented file selection using file dialog for image loading.

Update 6 
- Added ImageProcessor class to handle image loading using OpenCV. Basic image loading connected to GUI button and tested successfully.

Update 7 
- Corrected image loading structure and implemented random difference generation. 
- Differences are currently shown as visible markers for testing.

Update 8 
- Added image display functionality using Tkinter canvas, PIL image conversion, and OpenCV RGB conversion.

Update 9 
- Refactored GUI layout by introducing a Tkinter frame and separating image display into two canvases for original and modified images.
- Updated display function to render processed images using OpenCV BGR to RGB conversion and PIL format for Tkinter canvas display.

Update 10 
- Added mouse click event handling on the modified image canvas and implemented basic coordinate proximity detection for identifying difference regions.
- Added game state tracking and click detection logic implemented.

Update 11 
- Added remaining difference and mistake counters with live GUI updates and game state reset functionality.
