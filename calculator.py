from tkinter import *
from tkinter import ttk

# FALTA ADICIONAR O BOTÃO DE ADD (NÃO SEI COMO ESQUECI DISSO) E AJUSTAR O LAYOUT PARA ALINHAR OS NOVOS ITENS

# ============== #
#   constants

grey_color = "#c0c0c0"
white_color = "#ffffff"
red_color = "#ff0000"
blue_color = "#0000FF"
black_color = "#000000"
idle_color = "#6e6e6e"
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

frame_visor = Frame(window, width="240", height="28", bg=white_color)
frame_visor.grid(padx=10, pady=5)

# HOLD INPUT
btn_input = StringVar()
mem_input = StringVar()

label_visor = Label(frame_visor, bg=white_color, textvariable=btn_input, relief=SUNKEN, anchor="e", padx=5)
label_visor.place(x=0, y=0, width=240, height=28)

# ============== #
# LOGIC
hold_numbers = ''

def visor_output(value):
    global hold_numbers
    hold_numbers = hold_numbers + str(value)
    btn_input.set(hold_numbers)

def result():
    global hold_numbers
    # DEBUG
    result = eval(hold_numbers)
    btn_input.set(result)
    print(result)

def clear():
    global hold_numbers
    hold_numbers = ""
    btn_input.set(hold_numbers)
    print(hold_numbers)

def backspace():
    global hold_numbers
    hold_numbers = hold_numbers[:-1]
    btn_input.set(hold_numbers)

# ============== #

# MEMORY FRAME
# MEMORY CLEAR = MC ; clears memory value
# MEMORY RECALL = MR ; returns memory value
# MEMORY ADD = M+ ; add the memory value to the variable value
# MEMORY SUB = MS ; sub the memory value to the variable value

frame_mem = Frame(window, width=40, height=175, bg=grey_color)
frame_mem.place(x=10, y=40)

memory_label = Label(frame_mem, bg=grey_color, relief=SUNKEN)
memory_label.place(x=4, y=4, width=30, height=25)

mc_btn = Button(frame_mem, bg=grey_color, text="MC", font=('Tahoma', 8), fg=idle_color, activebackground=grey_color)
mc_btn.place(x=0, y=35, width=40, height=30)

mr_btn = Button(frame_mem, bg=grey_color, text="MR", font=('Tahoma', 8), fg=idle_color, activebackground=grey_color)
mr_btn.place(x=0, y=70, width=40, height=30)

ms_btn = Button(frame_mem, bg=grey_color, text="MS", font=('Tahoma', 8), fg=red_color, activebackground=grey_color)
ms_btn.place(x=0, y=105, width=40, height=30)

madd_btn = Button(frame_mem, bg=grey_color, text="M+", font=('Tahoma', 8), fg=red_color, activebackground=grey_color)
madd_btn.place(x=0, y=140, width=40, height=30)

# ============== #
# BTN FRAME

frame_btn = Frame(window, width=190, height=40, bg=grey_color)
frame_btn.place(x=58, y=40)

backspace_btn = Button(frame_btn, text="Backspace", font=('Tahoma', 8), bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: backspace())
backspace_btn.place(x=2, y=5, width=59, height=30)

ce_btn = Button(frame_btn, text="CE", font=('Tahoma', 8), bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: clear())
ce_btn.place(x=65, y=5, width=59, height=30)

c_btn = Button(frame_btn, text="C", font=('Tahoma', 8), bg=grey_color, fg=red_color, activebackground=grey_color)
c_btn.place(x=127, y=5, width=59, height=30)

# ============== #
# NUMBERS FRAME

frame_num = Frame(window, width=190, height=135, bg=grey_color)
frame_num.place(x=60, y=80)

num_7 = Button(frame_num, text="7", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("7"))
num_7.place(x=5, y=0, width=40, height=28)

num_8 = Button(frame_num, text="8", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("8"))
num_8.place(x=50, y=0, width=40, height=28)

num_9 = Button(frame_num, text="9", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("9"))
num_9.place(x=95, y=0, width=40, height=28)

div_btn = Button(frame_num, text="÷", bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: visor_output("/"))
div_btn.place(x=140, width=40, height=28)

num_4 = Button(frame_num, text="4", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("4"))
num_4.place(x=5, y=35, width=40, height=28)

num_5 = Button(frame_num, text="5", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("5"))
num_5.place(x=50, y=35, width=40, height=28)

num_6 = Button(frame_num, text="6", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("6"))
num_6.place(x=95, y=35, width=40, height=28)

mul_btn = Button(frame_num, text="X", bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: visor_output("*"))
mul_btn.place(x=140, y = 35, width=40, height=28)

num_1 = Button(frame_num, text="1", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("1"))
num_1.place(x=5, y=70, width=40, height=28)

num_2 = Button(frame_num, text="2", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("2"))
num_2.place(x=50, y=70, width=40, height=28)

num_3 = Button(frame_num, text="3", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("3"))
num_3.place(x=95, y=70, width=40, height=28)

sub_btn = Button(frame_num, text="-", bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: visor_output("-"))
sub_btn.place(x=140, y = 70, width=40, height=28)

num_0 = Button(frame_num, text="0", bg=grey_color, fg=blue_color, activebackground=grey_color, command = lambda: visor_output("0"))
num_0.place(x=5, y=105, width=40, height=28)

add_btn = Button(frame_num, text="+", bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: visor_output("+"))
add_btn.place(x=50, y=105, width=40, height=28)

float_btn = Button(frame_num, text=".", bg=grey_color, fg=red_color, activebackground=grey_color, command = lambda: visor_output("."))
float_btn.place(x=95, y=105, width=40, height=28)

result_btn = Button(frame_num, text="=", bg=grey_color, fg=red_color, activebackground=grey_color, command= lambda: result())
result_btn.place(x=140, y = 105, width=40, height=28)

# ============== #

center_window(window, WIDTH, HEIGHT) # center window
visor_output(hold_numbers)
window.mainloop() # runs the main widget