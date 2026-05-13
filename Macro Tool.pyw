import pyautogui as py
import customtkinter as ct
import os

window = ct.CTk()
window.geometry("400x300")
window.title("Helpful Macro Tool")
window.resizable(width=False, height=False)

#Mouse POS
bool_mouse = False

def position_mouse():
    global bool_mouse, location_text
    x, y = py.position()
    location_text.configure(text = f"Location: x = {x}, y = {y}")
    bool_mouse = True
    
def trigger_position_mouse():
    global bool_mouse
    bool_mouse = False
    if bool_mouse == False:
        window.after(2500, position_mouse)

button_mouse_xy = ct.CTkButton(window, width=10, height=30, corner_radius=5, text="Mouse Tracker", border_width=1, border_color="#000000")
button_mouse_xy.bind("<Button-1>", lambda track: trigger_position_mouse())
button_mouse_xy.place(x=25, y=50)

location_text = ct.CTkLabel(window, width=98, height=50, bg_color="#242424", text=f"Location: Not Checked")
location_text.place(x=20, y=0)
#---------------------------------------------------------------------------------------------------------------------------------------------

color_bool = False
color_detect = None

def color_track():
    global color_text, color_bool, color_detect, color_box
    x, y = py.position()
    color_detect = py.pixel(x=x, y=y)
    color_detect = '#{:02x}{:02x}{:02x}'.format(*color_detect) #i cant lie, i used ai for this 1 line cus i aint know what #{:02x} means
    color_text.configure(text = f"Color: {color_detect}")
    my_canvas.itemconfig(color_box, fill=color_detect)
    color_bool = True
            
def trigger_color_track():
    global color_bool
    color_bool = False
    if color_bool == False:
        window.after(2500, color_track)

button_color = ct.CTkButton(window, width=10, height=30, corner_radius=5, text="Color Finder", border_width=1, border_color="#000000", command=trigger_color_track)
button_color.place(x=200, y=50)

color_text = ct.CTkLabel(window, width=98, height=50, bg_color="#242424", text=f"Color: Not Checked")
color_text.place(x=195, y=0)


my_canvas  = ct.CTkCanvas(window, width=100, height=100, bg="#242424", highlightthickness=0)
my_canvas.place(x=200, y=100) 
color_box = my_canvas.create_aa_circle(x_pos=40, y_pos=10, radius=10, fill='red')


want_more_info = ct.CTkLabel(window, width=98, height=50, bg_color="#242424", text="Want more info? Click Me!")
want_more_info.place(x=20, y=250)
want_more_info.bind("<Button-1>", lambda info: py.mouseInfo())
#---------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()
