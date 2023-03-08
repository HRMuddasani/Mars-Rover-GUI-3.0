from tkinter import *
import customtkinter
from PIL import ImageTk, Image

#make a window
root = Tk()
root.wm_attributes('-fullscreen', 'True')
canvas = Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

#get wigth & height of screen
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.resizable(False, False)

# put image in a label and place label as background
imgTemp = Image.open("maininfo.jpg")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)
canvas.create_image(width/2,height/2, image=img)

#ADD BUTTONS
#to edit button background it is just background
quit_button = customtkinter.CTkButton(master=root, text="Quit", command=root.quit, width=150, height=50)
quit_button_window = canvas.create_window(1150, 690, anchor='nw', window=quit_button)

game1_button = customtkinter.CTkButton(master=root, text="Learn About Mars", command=root.quit, width=150, height=50)
game1_button_window = canvas.create_window(1150, 510, anchor='nw', window=game1_button)

game2_button = customtkinter.CTkButton(master=root, text="Explore Mars", command=root.quit, width=150, height=50)
game2_button_window = canvas.create_window(1150, 600, anchor='nw', window=game2_button)

#Center Text
canvas.create_text(width/2, height/3, text="Mars Rover", fill="white", font=('Helvetica 40 bold'))
canvas.pack()

root.mainloop()