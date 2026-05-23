import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer", fg=GREEN)
    reps = 0
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    reps += 1
    work_sec = WORK_MIN * 60 # 1, 3, 5, 7 round
    short_break_sec = SHORT_BREAK_MIN * 60 # 2, 4, 6 round
    long_break_sec = LONG_BREAK_MIN * 60 # 8 round

    if reps % 8 == 0:
        count_down(long_break_sec)
        text.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text.config(text="BREAK", fg=RED)
    else:
        count_down(work_sec)
        text.config(text="STUDY", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    mins = count // 60
    secs = count % 60
    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else: # count = 0
        if reps % 2 == 1:
            marks = ""
            work_sessions = (reps + 1) // 2
            for _ in range(work_sessions):
                marks += "✓"
            check_marks.config(text=marks)
        start_pomodoro()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("🍅 POMODORO TIMER 🍅")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

text = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
text.grid(row=1, column=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=4, column=2)

start_button = tk.Button(text="START", command=start_pomodoro, highlightthickness=0)
start_button.grid(row=3, column=1)
reset_button = tk.Button(text="RESET", command=reset_pomodoro, highlightthickness=0)
reset_button.grid(row=3, column=3)

window.mainloop()