# Mars-Rover-GUI-3.0
Converting GUI 2.0 to Python 

# Necessary Editors: 
  Pycharm Community to run this version of the GUI. Otherwise you need Visual Studio Code/Visual Studio for the older versions if needed.

# Pycharm:
  To set up you will need to have an interpreter. You should get a prompt to set up an interpreter on launch or you can look up "Python Interpreter setup on Pycharm" on Youtube. 
  
  You will need to import python packages. This you can also lookup how to do on Youtube. You will need to look up the following packages and install: "customtkinter", "Pillow", "pygame", "opencv-python", "pyserial", and you might need "pip". Install the packages and then restart Pycharm by closing it out and then relaunching it. This should make all the red lines on the imports disappear and you should be able to run it. 
  
# How It Works
  The way this works is that I created a canvas which is used as a background. I have a resize() and new_image() funcation used to replace the image of the canvas. The way that it works is that I used a buttons over the image for each mode. If you look at the functions, each mode: life or career they use a swap function that changes the image and resumes to the main page. 
  
  The main_game() function is the one with a camera feed. The way this is used is that I used cv2.VideoCapture(0). The 0 means it uses the devices camera, so your laptop's camera. You want to replace the 0 with the stream link. This should be in the mode itself as a comment. You also need to make sure you are connected to the console's wifi to use the stream. 
  
# Joystick 
  I implemented joystick functionality which works with the joystick of a xbox controller, but does not work with the console itself as of Spring 2023. You might need to check the previous way it is used or ask Tim for help. Asking Tim would make it go faster. 
  
# Rover Connection
  We could not test rover connection, but looking at the previous GUI version, they used a serialPort and did serialPort.name = "COM8" and then did serialPort.open(). This is how they did it in the previous GUI and I have added this to the code, but I commented it out. You will need to write the serialPort in the Main_game() if the joystick goes up, right, left, or down. You need to change the write_left() functions to write to the serial port the letter "f", "l", "r", or "b". Right now it just prints the direction and the write is commented out. 
  
  This still needs to be tested and as of writing this README, I do not think it works. 
  
# What you need to do
  I belive you just have to fix joystick and rover connection. This should be simple to do, and if you have any issues just ask Timothy Prichette. He knows a lot and can help you get this done really quickly. 

# Extra Help
  If you need any help, there are a lot of options availabel online. Youtube is a great help and typing it into google or ChatGPT can help with certain issues or how stuff works. If you have any questions ask Tim or you can call me on this number (770)-330-7552. My name is Hruthin Muddasani and I would be cool with helping out early in the semester. 
