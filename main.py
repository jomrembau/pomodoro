from tkinter import *
import tkinter as tk
from PIL import ImageTk

timer_on = False
work_time = 10
break_time = 5
long_break = 7
cycle_count = 3
short_breaks_done = 0

def reset_clock():
    global timer_on, cycle_count
    timer_on = False
    canvas.itemconfig(clock_text, text="00:00")
    canvas.itemconfig(cycle_text, text="")
    cycle_count = 3
    canvas.itemconfig(title_text, text="P O M O D O R O")

def countdown(count):
    global timer_on, cycle_count
    if timer_on and count >= 0:
        canvas.itemconfig(title_text, text="Work! Work!")
        timer_on = True
        minutes = count // 60
        secs = count % 60
        canvas.itemconfig(clock_text, text=f"{minutes:02d}:{secs:02d}")
        if count > 0:
            win.after(1000, countdown, count - 1)
        else:
            global short_breaks_done
            if short_breaks_done < 3:
                short_breaks_done += 1
                break_countdown(break_time)
            else:
                long_break_countdown(long_break)

def long_break_countdown(count):
    global timer_on, cycle_count
    if timer_on and count >= 0:
        canvas.itemconfig(title_text, text="Long Break!")
        timer_on = True
        minutes = count // 60
        secs = count % 60
        canvas.itemconfig(clock_text, text=f"{minutes:02d}:{secs:02d}")
        if count > 0:
            win.after(1000, long_break_countdown, count - 1)
        else:
            global short_breaks_done
            if count <= 0:
                canvas.itemconfig(cycle_text, text="")
                cycle_count = 3
                short_breaks_done = 0
                countdown(work_time)

def break_countdown(count):
    global timer_on, cycle_count
    if timer_on and count >= 0:
        canvas.itemconfig(title_text, text="Have a KitKat!")
        timer_on = True
        minutes = count // 60
        secs = count % 60
        canvas.itemconfig(clock_text, text=f"{minutes:02d}:{secs:02d}")
        if count > 0:
            win.after(1000, break_countdown, count - 1)
        else:
            txt = canvas.itemcget(cycle_text, 'text')
            canvas.itemconfig(cycle_text, text=txt + "✔️")
            if cycle_count > 0:
                countdown(work_time)

def start_timer():
    global timer_on
    timer_on = True
    countdown(work_time)

win = tk.Tk()
win.title("Pomodoro App")
win.geometry("500x500")
win.configure(bg="light green")

canvas = Canvas(width = 200, height = 200, bg = 'light green')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = "tomato.png")
canvas.create_image(150, 120, image = image, anchor = NW)


title_text = canvas.create_text(250, 100, text="P O M O D O R O", font=("Roboto", 30), fill="#006400")
clock_text = canvas.create_text(250, 250, text="00:00", font=("Roboto", 30), fill="white")
cycle_text = canvas.create_text(250, 400, font=("Roboto", 16), fill="#006400")

start_button = tk.Button(win, text="Start", command= start_timer)
reset_button = tk.Button(win, text="Reset", command= reset_clock)

canvas.create_window(100, 400, window=start_button)
canvas.create_window(400, 400, window=reset_button)


win.mainloop()
