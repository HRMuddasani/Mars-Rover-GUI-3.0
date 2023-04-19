# Packages needed: pyserial, customtkinter, opencv-python, Pillow, pygame, pip, 
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import time
import cv2
import serial
import pygame

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


# Create a Serial object
serial_port = serial.Serial()

# Joystick
#pygame.init()

# Set up joystick
#pygame.joystick.init()
#joystick = pygame.joystick.Joystick(0)
#joystick.init()

# Define joystick axis constants
JOY_AXIS_X = 0
JOY_AXIS_Y = 1
JOYAXISMOTION = 7

# Bluetooth connection to Rover
def ble_connect():
    # Set the port name
    serial_port.port = "COM8"  # Replace with the desired port name
    try:
        if not serial_port.is_open:
            # Open the serial port
            serial_port.open()
            # Perform your communication with the serial port here
            # e.g., send/receive data
    except Exception as e:
        print(f"Error: {e}")


# SWAP FUNCTIONS changes background to represent slide for specific mode
def swap(event):
    global count
    if not count == len(Community_pages) - 1:
        new_background(Community_pages[count])
        count += 1
    if count == len(Community_pages) - 1:
        main_page()
        count = 0


def swap_career(event):
    global career_count
    if not career_count == len(Career_pages) - 1:
        new_background(Career_pages[career_count])
        career_count += 1
    if career_count == len(Career_pages) - 1:
        main_page()
        career_count = 0


def swap_life(event):
    global life_count
    if not life_count == len(life_pages) - 1:
        new_background(life_pages[life_count])
        life_count += 1
    if life_count == len(life_pages) - 1:
        main_page()
        life_count = 0


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

# END OF MAIN_PAGE()


# COMMUNITY MODE FUNCTION
def community_mode():
    # clear screen
    clear_screen()
    # Create background
    new_background("Image Assets/Curiosity/Slide3.jpg")
    root.bind("<Left>", swap)
    root.bind("<Right>", swap)
    root.bind("<Up>", swap)
    root.bind("<Down>", swap)


# END CAREER MODE FUNCTION


# Career Mode function
def career_mode():
    # clear screen
    clear_screen()
    # Create background
    new_background("Image Assets/Career/Slide18.jpg")
    root.bind("<Left>", swap_career)
    root.bind("<Right>", swap_career)
    root.bind("<Up>", swap_career)
    root.bind("<Down>", swap_career)
# END Career Mode


# Life Mode Function
def life_mode():
    # clear screen
    clear_screen()
    # Create background
    new_background("Image Assets/Life/Slide27.jpg")
    root.bind("<Left>", swap_life)
    root.bind("<Right>", swap_life)
    root.bind("<Up>", swap_life)
    root.bind("<Down>", swap_life)
# END LIFE MODE


# MAIN GAME WRITES
def write_left(event):
    print("Left\n")
    #serial_port.write("l")
# End Write Left


def write_front(event):
    serial_port.write("f")
# End Write Front


def write_right(event):
    serial_port.write("r")
# End Write Front


def write_back(event):
    serial_port.write("b")
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
    # Put in videocapture: rtsp://admin:MarsRover23!@192.168.2.99:88/videoMain
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
        # Handle joystick input
        #for event in pygame.event.get():
         #   if event.type == JOYAXISMOTION:
          #      if event.axis == JOY_AXIS_X:
           #         if event.value > 0:
                        # Handle right joystick movement
                        # Do something for right movement
            #            pass
             #       elif event.value < 0:
                        # Handle left joystick movement
                        # Do something for left movement
               #         pass
              #  elif event.axis == JOY_AXIS_Y:
               #     if event.value > 0:
                        # Handle down joystick movement
                        # Do something for down movement
                #        pass
                 #   elif event.value < 0:
                        # Handle up joystick movement
                        # Do something for up movement
                  #      pass
        # Calculate elapsed time
        elapsed_time = int(time.time() - start)
        # Update timer label only if a whole second has elapsed
        if elapsed_time > last_elapsed_time:
            remaining_time = int(timer_duration - elapsed_time)
            timer_label.config(text=f"Time remaining: {remaining_time} seconds")
            # Store current elapsed time for comparison in next iteration
            last_elapsed_time = elapsed_time
        # Call the main event loop of Tkinter
        root.update_idletasks()
        root.update()

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
ble_connect()

main_page()

root.mainloop()
