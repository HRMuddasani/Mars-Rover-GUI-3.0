from tkinter import *
import customtkinter
from PIL import ImageTk, Image

# make a window
root = Tk()
root.wm_attributes('-fullscreen', 'True')
canvas = Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

# get width & height of screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
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

life_pages = ["Image Assets/Life/Slide28.jpg", "Image Assets/Life/Slide29.jpg", "Image Assets/Life/Slide30.jpg"
              "Image Assets/Life/Slide31.jpg", "Image Assets/Life/Slide32.jpg", "Image Assets/Life/Slide33.jpg"
              "Image Assets/Life/Slide34.jpg", "Image Assets/Life/Slide35.jpg", "Image Assets/Life/Slide36.jpg"
              "Image Assets/Life/Slide37.jpg"]


# SWAP FUNCTIONS changes background to represent slide for specific mode
def swap(event):
    global count
    if not count == len(Community_pages) - 1:
        new_background(Community_pages[count])
        count += 1
    if count == len(Community_pages) - 1:
        root.bind("<Up>", move_up)
        root.bind("<Down>", move_down)
        root.bind("<Left>", select_button)
        root.bind("<Right>", select_button)
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
        root.unbind("<Right>")
        root.unbind("<Left>")
        root.unbind("<Up>")
        root.unbind("<Down>")
        main_page()
        life_count = 0
# END SWAP FUNCTIONS


# Hover Functions for main page swap between buttons
def move_up(event):
    global buttons
    global move_count
    buttons[move_count].configure(fg_color="blue")
    if move_count == 0:
        move_count = len(buttons) - 1
    else:
        move_count -= 1
    buttons[move_count].configure(fg_color="white")


def move_down(event):
    global buttons
    global move_count
    buttons[move_count].configure(fg_color="blue")
    if move_count == len(buttons) - 1:
        move_count = 0
    else:
        move_count += 1
    buttons[move_count].configure(fg_color="white")
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
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)
    root.bind("<Left>", select_button)
    root.bind("<Right>", select_button)
    # Add buttons to canvas and button array
    # to edit button background it is just background
    quit_button = customtkinter.CTkButton(master=root, text="Quit", command=root.quit, width=150, height=50)
    quit_button.place(relx=0.5, rely=0.85)

    game1_button = customtkinter.CTkButton(master=root, text="Career Mode", command=career_mode, width=150,
                                           height=50, fg_color='#F69220')
    game1_button.place(relx=0.5, rely=0.65)

    game2_button = customtkinter.CTkButton(master=root, text="Community Mode", command=community_mode, width=150,
                                           height=50)
    game2_button.place(relx=0.5, rely=0.75)
    buttons.append(quit_button)
    buttons.append(game1_button)
    buttons.append(game2_button)
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


main_page()

root.mainloop()
