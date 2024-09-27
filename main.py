# Siavash Kianimehr

from tkinter import *
import platform
from lib.util import *
from src.lib.config import *

main_screen = Tk()
main_screen.configure(bg='#9EC8B9')
main_screen.geometry(main_scr)
main_screen.resizable(FALSE, FALSE)
main_screen.title("محاسبگر مقاومت")
if "Windows" in platform.system():
    main_screen.iconbitmap("D:/Project Class mft 2/Resistor Calculator/images/ohm.ico")


def for_three():
    main_screen.destroy()
    open_three()

def for_four():
    main_screen.destroy()
    open_four()

def for_five():
    main_screen.destroy()
    open_five()

def for_six():
    main_screen.destroy()
    open_six()

def for_help():
    main_screen.destroy()
    open_help()

write_label("محاسبگر مقاومت", "center", 20, bg_color, fg_color, 0, 20, 40, 516)
draw_line(0, 60, 2, 516, fg_color)

touch_button("سه باند", bg_button, fg_color, for_three, 60, 80, 50, 180)
touch_button("چهار باند", bg_button, fg_color, for_four, 286, 80, 50, 180)
touch_button("پنج باند", bg_button, fg_color, for_five, 60, 150, 50, 180)
touch_button("شش باند", bg_button, fg_color, for_six, 286, 150, 50, 180)

touch_button("راهنما", bg_button, fg_color, for_help, 0, 0, 30, 80)
draw_line(0, 30, 1, 80, bg_color)
draw_line(80, 0, 30, 1, bg_color) 

write_label(" Development Siavash", "center", 14, bg_color, fg_color, 0, 235, 40, 200)
draw_line(0, 280, 1, 210, fg_color)
draw_line(210, 280, 30, 1, fg_color)
 
main_screen.mainloop()
