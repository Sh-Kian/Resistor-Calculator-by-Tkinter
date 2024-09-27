# Siavash Kianimehr
# RESISTOR CALCULATOR (HELP) #

from tkinter import *
import platform
from lib.util import *
from src.lib.config import *

main_screen = Tk()
main_screen.configure(bg=bg_color)
main_screen.geometry(help_scr)
main_screen.resizable(FALSE, FALSE)
main_screen.title("محاسبگر مقاومت")
if "Windows" in platform.system():
    main_screen.iconbitmap("D:/Project Class mft 2/Resistor Calculator/images/ohm.ico")


def for_main():
    main_screen.destroy()
    open_main()

three_band_label = "باند اول = رقم اول\nباند دوم = رقم دوم\nباند سوم = ضریب مقاومت"
four_band_label = "باند اول = رقم اول\nباند دوم = رقم دوم\nباند سوم = ضریب مقاومت\nباند چهارم = تلرانس"
five_band_label = "باند اول = رقم اول\nباند دوم = رقم دوم\nباند سوم = رقم سوم\nباند چهارم = ضریب مقاومت\nباند پنجم = تلرانس"
six_band_label = "باند اول = رقم اول\nباند دوم = رقم دوم\nباند سوم = رقم سوم\nباند چهارم = ضریب مقاومت\nباند پنجم = تلرانس\nباند ششم = ضریب دمایی"
information = "مقاومت قطعه‌ای است که یک مقاومت الکتریکی مشخص و معمولاً ثابت دارد\nمقاومت الکتریکی جریان الکترون‌های یک مدار را محدود می‌کند. \nمقاومت‌ها قطعاتی پسیو هستند؛ به این معنی که فقط توان مصرف می‌کنند و نمی‌توانند آن را تولید کنند\nاین قطعات معمولاً به قسمت‌های اکتیو مدار مانند آپ‌امپ‌ها، میکروکنترلرها و سایر مدارهای مجتمع نیز اضافه می‌شوند\nاز مهم‌ترین نقش‌های مقاومت‌ها در مدار می‌توان به محدود کردن جریان، تقسیم ولتاژ و خطوط ورودی/خروجی اشاره کرد"

write_label("محاسبگر مقاومت", "center", 20, bg_color, fg_color, 0, 20, 52, 852)
draw_line(0, 70, 2, 852, fg_color) 
touch_button("صفحه اصلی", bg_button, fg_color, for_main, 0, 0, 30, 80)
draw_line(0, 30, 1, 80, bg_color)
draw_line(80, 0, 30, 1, bg_color)

write_label("سه باند", "center", 15, bg_color, fg_color, 60, 102, 25, 110)
draw_line(40, 130, 2, 150, fg_color)
write_label(three_band_label, "center", 13, bg_color, fg_color, 10, 135, 90, 230)

write_label("چهار باند", "center", 15, bg_color, fg_color, 150, 102, 25, 362)
draw_line(256, 130, 2, 150, fg_color)
write_label(four_band_label, "center", 13, bg_color, fg_color, 216, 135, 110, 230)

write_label("پنج باند", "center", 15, bg_color, fg_color, 472, 102, 25, 110)
draw_line(452, 130, 2, 150, fg_color)
write_label(five_band_label, "center", 13, bg_color, fg_color, 412, 135, 125, 230)

write_label("شش باند", "center", 15, bg_color, fg_color, 675, 102, 25, 110)
draw_line(655, 130, 2, 150, fg_color)
write_label(six_band_label, "center", 13, bg_color, fg_color, 615, 135, 125, 230)

draw_line(0, 270, 2, 852, fg_color)
write_label(information , "center", 14, bg_color, fg_color, 10, 275, 200, 832)

main_screen.mainloop()
