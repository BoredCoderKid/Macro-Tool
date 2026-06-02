import pyautogui as py
import customtkinter as ct
import keyboard as ky
import os

window = ct.CTk()
window.geometry("325x300")
window.title("Helpful Macro Tool")
window.resizable(False, False)

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

button_mouse_xy = ct.CTkButton(window, width=10, height=30, corner_radius=5, text="Mouse Tracker", border_width=1, border_color="#000000", command=trigger_position_mouse)
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
times = 0

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

click_recorder = ct.CTkButton(window, width=10, height=30, corner_radius=5, text="Click Recorder", border_width=1, border_color="#000000", command=click_record)
click_recorder.place(x=25, y=115)

clicks_recorded = ct.CTkLabel(window, width=5, height=15, corner_radius=5, text="Recorded: No Clicks")
clicks_recorded.place(x=15, y=90)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Opener UI

def fetch_data_file():
    global config_path
    try:
        os.startfile(config_path)
    except Exception as error:
        print("An error has occured!:   ", error)

fetch_data_button = ct.CTkButton(window, width=0, height=20, corner_radius=5, text="Open file", border_width=1, border_color="#000000", command=fetch_data_file, fg_color="#07CA00", hover_color="#058A00")
fetch_data_button.place(x=38.5, y=175)

#Deleter UI

def fetch_file_delete():
    global config_path
    try:
        os.remove(config_path)
    except Exception as error:
        print("An error has occured!:   ", error)

fetch_file_delete = ct.CTkButton(window, width=0, height=20, corner_radius=5, text="Delete file", border_width=1, border_color="#000000", command=fetch_file_delete, fg_color="#CA0000", hover_color="#8A0000")
fetch_file_delete.place(x=35, y=150)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Keybinds UI

import tkinter as tk
from tkinter import ttk

tkinter_bool = False

#Keybind 1 set
keybind1_label = None
keybind1_button = None

#Keybind 2 set
keybind2_label = None
keybind2_button = None

#Keybind 3 set
keybind3_label = None
keybind3_button = None

#Save button
save_keybinds = None

def read_hotkeys():
    global keybind1, keybind2, keybind3, hotkey1_position, hotkey2_color, hotkey3_data
    try:
        hotkey1_position = ky.remove_hotkey(hotkey1_position)
        hotkey2_color = ky.remove_hotkey(hotkey2_color)
        hotkey3_data = ky.remove_hotkey(hotkey3_data)

        new_keybind1 = keybind1_button.get()
        new_keybind2 = keybind2_button.get()
        new_keybind3 = keybind3_button.get()

        if new_keybind1 == None or "" or new_keybind2 == None or "" or new_keybind3 == None or "":
            print("Invalid hotkey")
            new_keybind1 = "ctrl+1"
            new_keybind2 = "ctrl+2"
            new_keybind3 = "ctrl+3"
        else:
            keybind1 = new_keybind1
            keybind2 = new_keybind2
            keybind3 = new_keybind3

            hotkey1_position = ky.add_hotkey(keybind1, position_mouse)
            hotkey2_color = ky.add_hotkey(keybind2, color_track)
            hotkey3_data = ky.add_hotkey(keybind3, save_data)

    except Exception as error:
        print(f"Error while trying to set hotkey or remove hotkey: {error}")

def keybinds_open():
    global tkinter_bool, keybind1_label, keybind1_button, keybind2_label, keybind2_button, keybind3_label, keybind3_button, save_keybinds
    try:
        root = tk.Tk()
        root.geometry("200x150")
        root.title("Keybinds")
        root.resizable(False, False)

        #-------- UI --------
        #TitlE
        tkinter_title = tk.Label(root, width=20, height=1, text="KeyBinds", font="fredoka")
        tkinter_title.place(x=0, y=5)

        #Keybind 1
        keybind1_label = tk.Label(root, width=10, height=2, text="Keybind 1")
        keybind1_label.place(x=10, y=25)

        keybind1_button = ttk.Entry(root, width=10)
        keybind1_button.place(x=92.5, y=31)

        #Keybind 2
        keybind2_label = tk.Label(root, width=10, height=2, text="Keybind 2")
        keybind2_label.place(x=10, y=50)

        keybind2_button = ttk.Entry(root, width=10)
        keybind2_button.place(x=92.5, y=56)

        #Keybind 3
        keybind3_label = tk.Label(root, width=10, height=2, text="Keybind 3")
        keybind3_label.place(x=10, y=75)

        keybind3_button = ttk.Entry(root, width=10)
        keybind3_button.place(x=92.5, y=81)

        #Save button
        save_keybinds = ttk.Button(root, width=10, text="Save", command=read_hotkeys)
        save_keybinds.place(x=58, y=125)

        root.mainloop()

    except Exception as error:
        print("Error setting up 2nd ui:     ", error)

#Keybind UI Opener
Keybind_ui_opener = ct.CTkLabel(window, width=0, height=10, corner_radius=5, text="Keybinds", bg_color="#242424")
Keybind_ui_opener.place(x=175, y=280)
Keybind_ui_opener.bind("<Button-1>", lambda open: keybinds_open())

#Hotkeys
keybind1 = "ctrl+1"
keybind2 = "ctrl+2"
keybind3 = "ctrl+3"

hotkey1_position = ky.add_hotkey(keybind1, position_mouse)
hotkey2_color = ky.add_hotkey(keybind2, color_track)
hotkey3_data = ky.add_hotkey(keybind3, save_data)

window.mainloop()
