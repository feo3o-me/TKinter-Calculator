from tkinter import *
from tkinter import ttk

# ============== #
#   constants

grey_color = "#c0c0c0"
white_color = "#ffffff"
red_color = "#ff0000"
blue_color = "#000080"
WIDTH = 260
HEIGHT = 225

# ============== #

window = Tk() # creates the tk widget
window.title("Calculadora")
window.configure(background=grey_color)
window.iconbitmap("C:/Users/feo3o/Desktop/Calculator/TKinter-Calculator/resources/Calculator.ico")
window.resizable(False, False)

def center_window(window, width=WIDTH, height=HEIGHT):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

# ============== #

frame_visor = Frame(window, width="240", height="25", bg=white_color, highlightbackground="blue", highlightthickness=1)
frame_visor.grid(padx=10, pady=5)

# ============== #
# MEMORY FRAME
# MEMORY CLEAR = MC ; limpa o visor de memória
# MEMORY RECALL = MR ; retorna o valor da memória
# MEMORY ADD = M+ ; adiciona o que está no visor com o que está na memória
# MEMORY SUB = MS ; subtrai do valor da memória com o visor

frame_mem = Frame(window, width=40, height=175, bg=grey_color, highlightbackground="blue", highlightthickness=1)
frame_mem.place(x=15, y=40)

# ============== #
# BTN FRAME

frame_btn = Frame(window, width=170, height=40, bg=grey_color, highlightbackground="blue", highlightthickness=1)
frame_btn.place(x=70, y=40)

# ============== #
# NUMBERS FRAME

frame_num = Frame(window, width=170, height=125, bg=grey_color, highlightbackground="blue", highlightthickness=1)
frame_num.place(x=70, y=90)

center_window(window, WIDTH, HEIGHT) # center window
window.mainloop() # runs the main widget