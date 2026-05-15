# DAN-EXT-73-Assignment-3
Software Now HIT137

## Group Name
DAN/EXT 73

## Group Member
Patrick Burzynski - 399755

## Assignment 3
This program creates a desktop application using Tkinter and OpenCV. It allows the user to load an image, generates random differences, and lets the user find those differences by clicking on the image.

## Current Features
- Tkinter desktop GUI.
- OpenCV image loading and processing.
- Supports JPG, JPEG, PNG and BMP image files.
- Original image displayed on the left.
- Modified image displayed on the right.
- Exactly 5 random differences generated for each loaded image.
- Difference regions are checked to reduce overlap.
- Three image alteration types are used: blended colour patch, adaptive blur patch and invert patch.
- Each image uses all three alteration types at least once.
- Player clicks the modified image to find differences.
- Found differences are marked with red circles and contrast outlines.
- Revealed differences are marked with blue circles and contrast outlines.
- Remaining differences, mistakes and total score are displayed.
- Maximum of 3 mistakes per image.
- Reveal button shows all unfound differences.
- Win and game-over messages are shown.
- Total score carries across multiple loaded images.

## How to Run

1. Install required libraries if needed:

```bash
pip install opencv-python pillow
```

2. Run the Python file.
3. Click **Load Image**.
4. Select a JPG, JPEG, PNG or BMP image.
5. Compare the original image on the left with the modified image on the right.
6. Click the differences on the modified image.

## Required Libraries

- tkinter
- cv2
- random
- PIL

tkinter and random are standard Python libraries.  
cv2 comes from OpenCV and PIL comes from Pillow.

## OOP Design Summary
The program uses multiple classes to organise the application:
- GameApp controls the Tkinter interface, game state, scoring, clicks, reveal, win and game-over logic.
- ImageProcessor loads images, copies the original image, generates differences and applies OpenCV image alterations.
- DifferenceMarker is the parent marker class.
- FoundMarker inherits from DifferenceMarker and draws red circles with contrast outlines for found differences.
- RevealMarker inherits from DifferenceMarker and draws blue circles with contrast outlines for revealed differences.
The marker classes demonstrate inheritance and polymorphism because both child classes use the same draw() method with different marker colours.

## Testing Summary
The program was tested for:
- Loading supported image files
- Displaying original and modified images side by side
- Generating 5 differences
- Reducing overlap between difference regions
- Detecting correct clicks
- Preventing duplicate clicks from counting as mistakes
- Tracking mistakes up to 3
- Showing win and game-over messages
- Revealing unfound differences
- Carrying total score across multiple images

## Display Note
Images are displayed in a fixed 550 x 550 canvas. This keeps the displayed image size and click detection consistent during gameplay. Some non-square images may appear slightly stretched, but this approach helps maintain accurate click detection between the visible image and the generated difference coordinates.

## Update History
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

Update 12 
- Added mistake limit, game over popup, and disabled clicks after 3 incorrect guesses.

Update 13 
- Added win condition detection and completion message when all differences are found.

Update 14 
- Added side by side image display and corrected click detection scaling.

Update 15 
- Added permanent visual markers on both images when differences are found.

Update 16
- Implemented functional Reveal Differences button. The game now reveals all remaining differences, refreshes both images, and disables further gameplay after reveal.

Update 17 
- Replaced temporary red circle markers with three OpenCV alteration types: colour patch, blur patch and invert patch.

Update 18 
- Added overlap checking to prevent generated difference regions from being placed too close together.

Update 19
- Updated visual markers so found differences show red circles and revealed differences show blue circles, with remaining counter updated after reveal.

Update 20 
- Added marker classes using inheritance and polymorphism to improve OOP structure for found and revealed differences.

Update 21 
- Added safety checks to prevent gameplay actions before an image is loaded.

Update 22 
- Updated click logic so already found differences are recognised without increasing the mistake counter.

Update 23 
- Increased window size and added canvas borders to improve side by side image display.

Update 24 
- Updated image loading with file type filtering and error handling for unsupported or unreadable image files.

Update 25 
- Improved on-screen feedback for correct clicks, duplicate clicks, reveal, win and game over states.

Update 26 
- Removed debugging print statements and cleaned minor formatting before final testing.

Update 27 
- Added a cumulative total score counter that tracks found differences across multiple loaded images.

Update 28 
- Updated difference generation so each loaded image uses colour, blur and invert alterations at least once.

Update 29 
- Refined colour and blur alterations for better visibility and increased the image display area to make gameplay easier to view.

Update 30
- Added final README sections including current features, how to run the program, required libraries, OOP design summary, testing summary and display note.

Update 31
- Improved blur differences and marker contrast so differences remain visible on light and dark image areas.
- Added final amendments to README ready for submission.

  
