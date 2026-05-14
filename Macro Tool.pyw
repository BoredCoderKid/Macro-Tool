import pyautogui as py
import customtkinter as ct
import keyboard as ky
import os

window = ct.CTk()
window.geometry("400x300")
window.title("Helpful Macro Tool")
window.resizable(width=False, height=False)

pathb = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(pathb, "RecordedClicksData(Macro Tool).txt")

#Mouse UI & Functions
bool_mouse = False
timescolor = 1

def position_mouse():
    global bool_mouse, location_text, config_path, timescolor
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

location_text = ct.CTkLabel(window, width=0, height=0, bg_color="#242424", text=f"Location: Not Checked")
location_text.place(x=15, y=25)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Color tracking UI & Functions
color_bool = False
color_detect = None

def color_track():
    global color_text, color_bool, color_detect, color_box
    x, y = py.position()
    color_detect = py.pixel(x=x, y=y)
    color_detect = '#{:02x}{:02x}{:02x}'.format(*color_detect) #i cant lie, i used ai for this 1 line cus i aint know what "{:02x}" means
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

color_text = ct.CTkLabel(window, width=0, height=0, bg_color="#242424", text=f"Color: Not Checked")
color_text.place(x=200, y=25)


my_canvas  = ct.CTkCanvas(window, width=30, height=20, bg="#242424", highlightthickness=0)
my_canvas.place(x=285, y=40) 
color_box = my_canvas.create_aa_circle(x_pos=10, y_pos=10, radius=10, fill='red')

#info ui
want_more_info = ct.CTkLabel(window, width=0, height=0, bg_color="#242424", text="Want more info? Click Me!")
want_more_info.place(x=5, y=280)
want_more_info.bind("<Button-1>", lambda info: py.mouseInfo())

#---------------------------------------------------------------------------------------------------------------------------------------------

#Record UI & Functions
record_bool = True
times = 1

def save_data():
    global record_bool, times, pathb, config_path
    x, y = py.position()
    color_detect = py.pixel(x=x, y=y)
    color_detect = '#{:02x}{:02x}{:02x}'.format(*color_detect)
    clicks_recorded.configure(text = f"Recorded: {times}")
    clicks_recorded.place(x=35, y=90)
    times += 1
    
    with open(config_path, "a") as file:
        file.write(f"---------------------------------------------------\n")
        file.write(f"Mouse POS {times}: {py.position()}\n")
        file.write(f"Color {times}: {color_detect}\n")

def click_record():
    global click_recorder, record_bool
    click_recorder.configure(fg_color="#ff0000", text="""Now Recording!
Click to stop!""")
    click_recorder.place(x=25, y=110)
    window.after(1000, save_data)

def record_bool():
    global record_bool
    if record_bool == False:
        record_bool = True
    elif record_bool == True:
        record_bool = False
        click_record()

click_recorder = ct.CTkButton(window, width=10, height=30, corner_radius=5, text="Click Recorder", border_width=1, border_color="#000000")
click_recorder.bind("<Button-1>", lambda click: click_record())
click_recorder.place(x=25, y=115)

clicks_recorded = ct.CTkLabel(window, width=5, height=15, corner_radius=5, text="Recorded: No Clicks")
clicks_recorded.place(x=15, y=90)

#Hotkeys
ky.add_hotkey("ctrl+1", position_mouse)
ky.add_hotkey("ctrl+2", color_track)
ky.add_hotkey("ctrl+3", save_data)

window.mainloop()
