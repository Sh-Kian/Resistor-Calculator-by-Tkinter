# Siavash Kianimehr
# RESISTOR CALCULATOR (5BAND) #

from tkinter import *
import platform
from lib.util import *

def for_three():
    main_screen.destroy()
    open_three()

def for_four():
    main_screen.destroy()
    open_four()

def for_six():
    main_screen.destroy()
    open_six()

def for_help():
    main_screen.destroy()
    open_help()

main_screen = Tk()
main_screen.configure(bg='#9EC8B9')
main_screen.geometry(five_scr)
main_screen.resizable(FALSE, FALSE)
main_screen.title("محاسبگر مقاومت")
if "Windows" in platform.system():
    main_screen.iconbitmap("D:/Project Class mft 2/Resistor Calculator/images/ohm.ico")


hex_one = StringVar()
hex_two = StringVar()
hex_three = StringVar()
hex_multiplier = StringVar()
hex_tolerance = StringVar()
hex_temperature = StringVar()
temperature_var = StringVar()
value_keeper(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature)

draw_line(30, 20, 150, 30, bg_canvas) 
draw_line(100, 20, 150, 30, bg_canvas) 
draw_line(170, 20, 150, 30, bg_canvas)
draw_line(240, 20, 150, 30, bg_canvas) 
draw_line(310, 20, 150, 30, bg_canvas) 

first_menu = make_menu("1. باند", "one", hex_one, 30, bg_menu, fg_color, 20, 190, 20, 50)
second_menu = make_menu("2. باند", "two", hex_two, 100, bg_menu, fg_color, 85, 190, 20, 50) 
third_menu = make_menu("3. باند", "three", hex_three, 170, bg_menu, fg_color, 150, 190, 20, 50) 
fourth_menu = make_menu("ضریب", "multiplier", hex_multiplier, 240, bg_menu, fg_color, 208, 190, 20, 70) 
fifth_menu = make_menu("تلورانس", "tolerance", hex_tolerance, 310, bg_menu, fg_color, 288, 190, 20, 70) 

touch_button("سه باند", bg_button, fg_color, for_three, 380, 20, 40, 140)
touch_button("چهار باند", bg_button, fg_color, for_four, 380, 70, 40, 140)
touch_button("شش باند", bg_button, fg_color, for_six, 380, 120, 40, 140)
touch_button("راهنما", bg_button, fg_color, for_help, 410, 170, 20, 80)

enter_button = Button(bd=0, bg=bg_button, fg=fg_color, text="محاسبه", activebackground=bg_button, activeforeground=fg_color, command=lambda: calc_result(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature, value_var, temperature_var, 2))
enter_button.pack()
enter_button.place(x=40, y=230, height=40, width=280)

value_var = StringVar()
think_entry(value_var, bg_entry, fg_color, 370, 200, 60, 160)
value_var.set("مقدار")

main_screen.mainloop()
