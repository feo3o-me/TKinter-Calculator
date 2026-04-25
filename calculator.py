from tkinter import *
from tkinter import ttk

# ============== #
#   constants

grey_color = "#c0c0c0"
white_color = "#ffffff"
red_color = "#ff0000"
blue_color = "#0000FF"
black_color = "#000000"
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

memory_label = Label(frame_mem, bg=grey_color, highlightbackground=black_color, highlightthickness=1)
memory_label.place(x=4, y=4, width=30, height=25)

mc_btn = Button(frame_mem, bg=grey_color, text="MC", font=('Tahoma', 8), fg=red_color)
mc_btn.place(x=0, y=35, width=40, height=30)

mr_btn = Button(frame_mem, bg=grey_color, text="MR", font=('Tahoma', 8), fg=red_color)
mr_btn.place(x=0, y=70, width=40, height=30)

ms_btn = Button(frame_mem, bg=grey_color, text="MS", font=('Tahoma', 8), fg=red_color)
ms_btn.place(x=0, y=105, width=40, height=30)

madd_btn = Button(frame_mem, bg=grey_color, text="M+", font=('Tahoma', 8), fg=red_color)
madd_btn.place(x=0, y=140, width=40, height=30)

# ============== #
# BTN FRAME

frame_btn = Frame(window, width=190, height=40, bg=grey_color)
frame_btn.place(x=58, y=40)

backspace_btn = Button(frame_btn, text="Backspace", font=('Tahoma', 8), bg=grey_color, fg=red_color)
backspace_btn.place(x=2, y=5, width=59, height=30)

ce_btn = Button(frame_btn, text="CE", font=('Tahoma', 8), bg=grey_color, fg=red_color)
ce_btn.place(x=65, y=5, width=59, height=30)

c_btn = Button(frame_btn, text="C", font=('Tahoma', 8), bg=grey_color, fg=red_color)
c_btn.place(x=127, y=5, width=59, height=30)

# ============== #
# NUMBERS FRAME

frame_num = Frame(window, width=190, height=135, bg=grey_color)
frame_num.place(x=60, y=80)

num_7 = Button(frame_num, text="7", bg=grey_color, fg=blue_color)
num_7.place(x=5, y=0, width=40, height=28)

num_8 = Button(frame_num, text="8", bg=grey_color, fg=blue_color)
num_8.place(x=50, y=0, width=40, height=28)

num_9 = Button(frame_num, text="9", bg=grey_color, fg=blue_color)
num_9.place(x=95, y=0, width=40, height=28)

div_btn = Button(frame_num, text="÷", bg=grey_color, fg=red_color)
div_btn.place(x=140, width=40, height=28)

num_4 = Button(frame_num, text="4", bg=grey_color, fg=blue_color)
num_4.place(x=5, y=35, width=40, height=28)

num_5 = Button(frame_num, text="5", bg=grey_color, fg=blue_color)
num_5.place(x=50, y=35, width=40, height=28)

num_6 = Button(frame_num, text="6", bg=grey_color, fg=blue_color)
num_6.place(x=95, y=35, width=40, height=28)

mul_btn = Button(frame_num, text="X", bg=grey_color, fg=red_color)
mul_btn.place(x=140, y = 35, width=40, height=28)

num_1 = Button(frame_num, text="1", bg=grey_color, fg=blue_color)
num_1.place(x=5, y=70, width=40, height=28)

num_2 = Button(frame_num, text="2", bg=grey_color, fg=blue_color)
num_2.place(x=50, y=70, width=40, height=28)

num_3 = Button(frame_num, text="3", bg=grey_color, fg=blue_color)
num_3.place(x=95, y=70, width=40, height=28)

sub_btn = Button(frame_num, text="-", bg=grey_color, fg=red_color)
sub_btn.place(x=140, y = 70, width=40, height=28)

num_0 = Button(frame_num, text="0", bg=grey_color, fg=blue_color)
num_0.place(x=5, y=105, width=40, height=28)

negative_btn = Button(frame_num, text="±", bg=grey_color, fg=red_color)
negative_btn.place(x=50, y=105, width=40, height=28)

float_btn = Button(frame_num, text=".", bg=grey_color, fg=red_color)
float_btn.place(x=95, y=105, width=40, height=28)

result_btn = Button(frame_num, text="=", bg=grey_color, fg=red_color)
result_btn.place(x=140, y = 105, width=40, height=28)

# ============== #

center_window(window, WIDTH, HEIGHT) # center window
window.mainloop() # runs the main widget