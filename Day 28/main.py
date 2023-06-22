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
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    title_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    window.after_cancel(TIMER)
    tracker.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_secs  =WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    # Testing conf
    # work_secs = 1
    # short_break_secs= 1
    # long_break_secs = 30
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        title_text.config(text="Break", fg=RED)
        countdown(long_break_secs)
    elif REPS % 2 == 0:
        title_text.config(text="Break", fg=PINK)
        countdown(short_break_secs)
    else:
        title_text.config(text="Work", fg=GREEN)
        countdown(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✓"
        tracker.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


# Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Timer title
title_text = Label(text="Timer", font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
title_text.grid(column=1, row=0)
# Tomato to the screen
TOMATO = PhotoImage(file="./tomato.png")
canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103,112, image=TOMATO)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Start button; Start timer on click
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

# Tracker label
tracker = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
tracker.grid(column=1, row=4)

window.mainloop()