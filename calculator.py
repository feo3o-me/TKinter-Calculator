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
window.geometry("320x240") # window width and heigth 
window.configure(background=grey_color)
window.iconbitmap("C:/Users/feo3o/Desktop/Calculator/TKinter-Calculator/resources/Calculator.ico")

# ============== #

frame_visor = Frame(window, width="280", height="25", bg=white_color)
frame_visor.pack(padx = 3, pady = 8)

# ============== #

frame_btn = Frame(window, width=320, bg=grey_color)
frame_btn.pack()

# ============== #

window.mainloop() # runs the main widget