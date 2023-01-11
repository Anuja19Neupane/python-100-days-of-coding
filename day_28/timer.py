from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min=math.floor(count/60)
    # .floor le 4.8 ko 4 matra dinxa
    count_sec=count%60
    timer_text.config(text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)
# after will Call function once after given time, time in milisecond

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.minsize(width=600, height=400)






my_label = Label(window, text="Timer", fg=RED,
                 bg=YELLOW, font=("Arial", 24, "bold"))
my_label.grid(column=10, row=0)

timer_text = Label(window, text="00:00", fg=PINK,
                 bg=YELLOW, font=("Arial", 24, "bold"))
timer_text.grid(column=10, row=1)


start_button = Button(text="start")
start_button.grid(column=1, row=2)



check_mark=Label(text="✔️",fg=GREEN,bg=YELLOW,font=("Arial", 24, "bold"))
check_mark.grid(column=1,row=3)


window.mainloop()
