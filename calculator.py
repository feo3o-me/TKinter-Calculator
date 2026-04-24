from tkinter import *
from tkinter import ttk

# ============== #
#   constants

grey_color = "#c0c0c0"
white_color = "#ffffff"
red_color = "#ff0000"
blue_color = "#000080"

# ============== #

window = Tk() # creates the tk widget
window.title("Calculadora")
window.geometry("260x225") # window width and heigth 
window.configure(background=grey_color)
window.iconbitmap("C:/Users/feo3o/Desktop/Calculator/TKinter-Calculator/resources/Calculator.ico")

# ============== #

frame_visor = Frame(window, width="240", height="25", bg=white_color)
frame_visor.pack(padx = 3, pady = 8)

# ============== #

frame_btn = Frame(window, width=320, bg=grey_color)
frame_btn.pack()

# ============== #

backspace_btn = Button(frame_btn, text="Backspace", width=8, height=1)
backspace_btn.pack(side='left', padx=2)

clear_btn = Button(frame_btn, text="C", width=8, height=1)
clear_btn.pack(side='right', padx=2)

eclear_btn = Button(frame_btn, text="CE", width=8, height=1)
eclear_btn.pack(side='right', padx=2)


window.mainloop() # runs the main widget