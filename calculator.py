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

frame_visor = Frame(window, width="240", height="28", bg=white_color, highlightbackground="black", highlightthickness=1, relief="raised")
frame_visor.grid(padx=10, pady=5)

# ============== #
# MEMORY FRAME
# MEMORY CLEAR = MC ; limpa o visor de memória
# MEMORY RECALL = MR ; retorna o valor da memória
# MEMORY ADD = M+ ; adiciona o que está no visor com o que está na memória
# MEMORY SUB = MS ; subtrai do valor da memória com o visor

frame_mem = Frame(window, width=40, height=175, bg=grey_color)
frame_mem.place(x=10, y=40)

memory_label = Label(frame_mem, bg=grey_color, highlightbackground=red_color, highlightthickness=1)
memory_label.place(x=4, y=4, width=30, height=25)

mc_btn = Button(frame_mem, bg=grey_color, text="MC", font=('Tahoma', 8))
mc_btn.place(x=0, y=35, width=40, height=30)

mr_btn = Button(frame_mem, bg=grey_color, text="MR", font=('Tahoma', 8))
mr_btn.place(x=0, y=70, width=40, height=30)

ms_btn = Button(frame_mem, bg=grey_color, text="MS", font=('Tahoma', 8))
ms_btn.place(x=0, y=105, width=40, height=30)

madd_btn = Button(frame_mem, bg=grey_color, text="M+", font=('Tahoma', 8))
madd_btn.place(x=0, y=140, width=40, height=30)

# ============== #
# BTN FRAME

frame_btn = Frame(window, width=190, height=40, bg=grey_color)
frame_btn.place(x=60, y=40)

backspace_btn = Button(frame_btn, text="Backspace", font=('Tahoma', 8), bg=grey_color)
backspace_btn.place(x=2, y=5, width=59, height=30)

ce_btn = Button(frame_btn, text="CE", font=('Tahoma', 8), bg=grey_color)
ce_btn.place(x=65, y=5, width=59, height=30)

c_btn = Button(frame_btn, text="C", font=('Tahoma', 8), bg=grey_color)
c_btn.place(x=127, y=5, width=59, height=30)

# ============== #
# NUMBERS FRAME

frame_num = Frame(window, width=190, height=135, bg=grey_color, highlightbackground="blue", highlightthickness=1)
frame_num.place(x=60, y=80)

# ============== #

center_window(window, WIDTH, HEIGHT) # center window
window.mainloop() # runs the main widget