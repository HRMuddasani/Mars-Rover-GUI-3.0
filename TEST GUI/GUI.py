# Packages needed: pyserial, customtkinter, opencv-python, Pillow, pygame, pip, 
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import time
import cv2
import serial
from serial import SerialException
import pygame
from pygame.locals import *

# make a window
root = Tk()
root.wm_attributes('-fullscreen', 'True')
canvas = Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

# get width & height of screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# COMMENT OUT FOR MAC ONLY
root.resizable(False, False)
buttons = []
count = 0
career_count = 0
life_count = 0
move_count = 0

Community_pages = ["Image Assets/Curiosity/Slide4.jpg", "Image Assets/Curiosity/Slide5.jpg",
                   "Image Assets/Curiosity/Slide6.jpg", "Image Assets/Curiosity/Slide7.jpg",
                   "Image Assets/Curiosity/Slide8.jpg", "Image Assets/Curiosity/Slide9.jpg"]

Career_pages = ["Image Assets/Career/Slide19.jpg", "Image Assets/Career/Slide20.jpg",
                "Image Assets/Career/Slide21.jpg", "Image Assets/Career/Slide22.jpg",
                "Image Assets/Career/Slide23.jpg", "Image Assets/Career/Slide24.jpg",
                "Image Assets/Career/Slide25.jpg"]

life_pages = ["Image Assets/Life/Slide28.jpg", "Image Assets/Life/Slide29.jpg", "Image Assets/Life/Slide30.jpg",
              "Image Assets/Life/Slide31.jpg", "Image Assets/Life/Slide32.jpg", "Image Assets/Life/Slide33.jpg",
              "Image Assets/Life/Slide34.jpg", "Image Assets/Life/Slide35.jpg", "Image Assets/Life/Slide36.jpg",
              "Image Assets/Life/Slide37.jpg"]

# Bluetooth connection to Rover
serialPort1 = serial.Serial()

def bleConnect():
    try:
        if not serialPort1.is_open:
            serialPort1.port = 'COM8' # Set the port name
            serialPort1.open() # Open the serial port
            #serialPort1.baudrate = 9600 # Set the baud rate
    except SerialException as e:
        print(f"Failed to connect to serial port: {e}")


# SWAP FUNCTIONS changes background to represent slide for specific mode
def swap(event):
    global count
    if not count == len(Community_pages) - 1:
        new_background(Community_pages[count])
        count += 1
    if count == len(Community_pages) - 1:
        count = 0
        main_page()


def swap_career(event):
    global career_count
    if not career_count == len(Career_pages) - 1:
        new_background(Career_pages[career_count])
        career_count += 1
    if career_count == len(Career_pages) - 1:
        career_count = 0
        main_page()


def swap_life(event):
    global life_count
    if not life_count == len(life_pages) - 1:
        new_background(life_pages[life_count])
        life_count += 1
    if life_count == len(life_pages) - 1:
        life_count = 0
        main_page()


# END SWAP FUNCTIONS


# Hover Functions for main page swap between buttons
def move_up(event):
    global buttons
    global move_count
    buttons[move_count].configure(fg_color="#F69220")
    if move_count == 0:
        move_count = len(buttons) - 1
    else:
        move_count -= 1
    buttons[move_count].configure(fg_color="#4169E1")


def move_down(event):
    global buttons
    global move_count
    buttons[move_count].configure(fg_color="#F69220")
    if move_count == len(buttons) - 1:
        move_count = 0
    else:
        move_count += 1
    buttons[move_count].configure(fg_color="#4169E1")


# END MOVE FUNCTIONS


# Select Function invokes button function in main with left or right arrow key
def select_button(event):
    global buttons
    global move_count
    buttons[move_count].invoke()


# END SELECT FUNCTION


# Clear screen function removes buttons
def clear_screen():
    global buttons
    for b in buttons:
        b.place_forget()
    buttons.clear()


# END CLEAR_SCREEN


# Resize and make image fill screen as background
def new_background(path):
    # needs to be global otherwise won't be displayed on canvas IDK why, but it works with it global
    global img
    temp = Image.open(path)
    img2 = temp.resize((width, height))
    img = ImageTk.PhotoImage(img2)
    canvas.create_image(width / 2, height / 2, image=img)


# END NEW_BACKGROUND()


# MAIN PAGE FUNCTION START
def main_page():
    global buttons
    global move_count
    move_count = 0
    # Create background
    new_background("Image Assets/MainScreen].jpg")

    # Add buttons to canvas and button array
    # to edit button background it is just background
    life_button = customtkinter.CTkButton(master=root, text="Life Mode", command=life_mode, width=250, height=50,
                                          corner_radius=10, bg_color='#E05035', fg_color='#F69220',
                                          font=('Helvetica bold', 16))
    life_button.place(relx=0.42, rely=0.825)

    career_button = customtkinter.CTkButton(master=root, text="Career Mode", command=career_mode, width=250,
                                            height=50, fg_color='#F69220', corner_radius=10, bg_color='#E05035',
                                            font=('Helvetica bold', 16))
    career_button.place(relx=0.42, rely=0.675)

    community_button = customtkinter.CTkButton(master=root, text="Community Mode", command=community_mode, width=250,
                                               height=50, corner_radius=10, bg_color='#E05035', fg_color='#F69220',
                                               font=('Helvetica bold', 16))
    community_button.place(relx=0.42, rely=0.75)

    main_button = customtkinter.CTkButton(master=root, text="Main Game", command=main_game, width=250, height=50,
                                          corner_radius=10, bg_color='#E05035', fg_color='#F69220',
                                          font=('Helvetica bold', 16))
    main_button.place(relx=0.42, rely=0.9)

    buttons.append(main_button)
    buttons.append(career_button)
    buttons.append(community_button)
    buttons.append(life_button)
    move_up(None)
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)
    root.bind("<Left>", select_button)
    root.bind("<Right>", select_button)
    root.update()
# Main loop for reading joystick input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Get axis values
                axis_x = joystick.get_axis(0)
                axis_y = joystick.get_axis(1)
                if (abs(axis_x) > 0.75) or (abs(axis_y) >= 0.75):
                    # Check for axis X
                    if axis_x >= 0.75:
                        # Do something for right direction
                        select_button(None)
                        break
                    elif axis_x <= -0.75:
                        # Do something for left direction
                        select_button(None)
                        break
                    # Check for axis Y
                    if axis_y >= 0.75:
                        # Do something for down direction
                        move_down(None)
                    elif axis_y <= -0.75:
                        # Do something for up direction
                        move_up(None)
                root.update()
                pygame.time.delay(50)
                pygame.event.pump()

# END OF MAIN_PAGE()


# COMMUNITY MODE FUNCTION
def community_mode():
    # clear screen
    clear_screen()
    # Create background
    new_background("Image Assets/Curiosity/Slide3.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Get axis values
                axis_x = joystick.get_axis(0)
                axis_y = joystick.get_axis(1)
                if (abs(axis_x) > 0.75) or (abs(axis_y) >= 0.75):
                    # Check for axis X
                    if axis_x >= 0.75:
                        # Do something for right direction
                        swap(None)
                    elif axis_x <= -0.75:
                        # Do something for left direction
                        swap(None)

                    # Check for axis Y
                    if axis_y >= 0.75:
                        # Do something for down direction
                        swap(None)
                    elif axis_y <= -0.75:
                        # Do something for up direction
                        swap(None)
                root.update()
                pygame.time.delay(50)
                pygame.event.pump()


# END CAREER MODE FUNCTION


# Career Mode function
def career_mode():
    # clear screen
    clear_screen()
    # Create background
    new_background("Image Assets/Career/Slide18.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Get axis values
                axis_x = joystick.get_axis(0)
                axis_y = joystick.get_axis(1)
                if (abs(axis_x) > 0.75) or (abs(axis_y) >= 0.75):
                    # Check for axis X
                    if axis_x >= 0.75:
                        # Do something for right direction
                        swap_career(None)
                    elif axis_x <= -0.75:
                        # Do something for left direction
                        swap_career(None)

                    # Check for axis Y
                    if axis_y >= 0.75:
                        # Do something for down direction
                        swap_career(None)
                    elif axis_y <= -0.75:
                        # Do something for up direction
                        swap_career(None)
                root.update()
                pygame.time.delay(50)
                pygame.event.pump()


# END Career Mode


# Life Mode Function
def life_mode():
    # clear screen
    clear_screen()
    # Create background
    new_background("Image Assets/Life/Slide27.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Get axis values
                axis_x = joystick.get_axis(0)
                axis_y = joystick.get_axis(1)
                if (abs(axis_x) > 0.75) or (abs(axis_y) >= 0.75):
                    # Check for axis X
                    if axis_x >= 0.75:
                        # Do something for right direction
                        swap_life(None)
                    elif axis_x <= -0.75:
                        # Do something for left direction
                        swap_life(None)

                    # Check for axis Y
                    if axis_y >= 0.75:
                        # Do something for down direction
                        swap_life(None)
                    elif axis_y <= -0.75:
                        # Do something for up direction
                        swap_life(None)
                root.update()
                pygame.time.delay(50)
                pygame.event.pump()


# END LIFE MODE


# MAIN GAME WRITES
def write_left(event):
    print("Left\n")
    # serial_port.write("l")


# End Write Left


def write_front(event):
    print("front\n")
    # serial_port.write("f")


# End Write Front


def write_right(event):
    print("right\n")
    # serial_port.write("r")


# End Write Front


def write_back(event):
    print("back\n")
    # serial_port.write("b")


# End Write Front


# Main Game Mode Start
def main_game():
    root.bind("<Left>", write_left)
    root.bind("<Right>", write_right)
    root.bind("<Up>", write_front)
    root.bind("<Down>", write_back)

    clear_screen()
    # Use image as background
    bg = PhotoImage(file="Image Assets/Surface.png")
    # Use secondary image for frame under camera feed
    image = Image.open('Image Assets/GUI icons.png')
    img2 = image.resize((930, 300))
    test = ImageTk.PhotoImage(img2)

    # Create Frame with background of image
    frame1 = Frame(root, bg="white")

    # Add background image to fill screen
    label1 = Label(frame1, image=bg)
    label1.pack()
    # Add secondary frame under camera feed
    label2 = Label(frame1, image=test)
    label2.place(x=0, y=575)

    # Add text to frame
    Label(frame1, text="MISSION", bg="black", foreground="white", font=('Helvetica bold', 35)).place(x=1150, y=50)
    frame1.pack(side="top", fill=BOTH, expand=False)
    Label(frame1, text="1. Use the joystick to move the robot", bg="black", foreground="white",
          font=('Helvetica bold', 20)).place(x=1050, y=125)
    Label(frame1, text="2. Explore Mars to your hearts content", bg="black", foreground="white",
          font=('Helvetica bold', 20)).place(x=1050, y=175)
    Label(frame1, text="3. You will have 90 seconds", bg="black", foreground="white",
          font=('Helvetica bold', 20)).place(x=1050, y=225)

    # Add Countdown Label
    timer_label = Label(frame1, text="Time remaining: 90 seconds", bg="black", foreground="white",
                        font=('Helvetica bold', 30))
    timer_label.place(x=1000, y=800)

    # forget canvas to allow frame to show in entirety
    canvas.pack_forget()

    # Captures video feed from stream. MUST BE ON ROVER WI-FI:
    # Put in videocapture: 'rtsp://admin:MarsRover23!@192.168.2.99:88/videoMain' or in ""
    cap = cv2.VideoCapture(0)
    start = time.time()
    timer_duration = 90
    last_elapsed_time = 0

    # Camera Feed Loop
    while time.time() - start < 5:
        # Capture frame of feed
        ret, frame = cap.read()
        if not ret:
            break
        # Resize the frame and then show
        small_frame = cv2.resize(frame, (930, 550))
        cv2.imshow("MARS FEED", small_frame)
        root.focus_force()
        # Calculate elapsed time
        elapsed_time = int(time.time() - start)
        # Update timer label only if a whole second has elapsed
        if elapsed_time > last_elapsed_time:
            remaining_time = int(timer_duration - elapsed_time)
            timer_label.config(text=f"Time remaining: {remaining_time} seconds")
            # Store current elapsed time for comparison in next iteration
            last_elapsed_time = elapsed_time
        # Call the main event loop of Tkinter
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Get axis values
                axis_x = joystick.get_axis(0)
                axis_y = joystick.get_axis(1)
                #print(axis_x)
                if (abs(axis_x) > 0.75) or (abs(axis_y) >= 0.75):
                    # Check for axis X
                    if axis_x >= 0.75:
                        # Do something for right direction
                        write_right(None)
                    elif axis_x <= -0.75:
                        # Do something for left direction
                        write_left(None)
                    # Check for axis Y
                    if axis_y >= 0.75:
                        # Do something for back direction
                        write_back(None)
                    elif axis_y <= -0.75:
                        # Do something for front direction
                        write_front(None)
        pygame.time.delay(50)
        pygame.event.pump()
        root.update()
        #root.update_idletasks()

    # Close video capture
    cap.release()
    cv2.destroyAllWindows()
    # Set focus back to root because video feed causes popup that will alt tab, it so need to set focus
    root.focus_force()
    Label(frame1, text="MISSION COMPLETE!!!\nReturning to Main Menu", bg="black", fg="red",
          font=('Helvetica bold', 50)).place(x=200, y=200)
    # Adds the label to screen and gets rid of camera feed and pauses for 3 seconds
    root.update()
    time.sleep(3)
    # Repack canvas to allow for slides and main screen
    canvas.pack(fill=BOTH, expand=True)
    # Get rid of Frame
    frame1.pack_forget()
    frame1.destroy()
    # Call main page
    main_page()

# END MAIN GAME


# Call the ble_connect() function to establish the serial port connection
bleConnect()

# Initialize pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# I TESTED THIS WITH AN XBOX CONTROLLER. I DO NOT KNOW IF IT WORKS WITH CONSOLE ITSELF
# Check for connected joysticks
if pygame.joystick.get_count() > 0:
    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # Print joystick information
    print("Joystick Name:", joystick.get_name())
    print("Joystick Axes:", joystick.get_numaxes())
    print("Joystick Buttons:", joystick.get_numbuttons())


main_page()

root.mainloop()
