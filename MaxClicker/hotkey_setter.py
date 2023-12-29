import tkinter as tk
import hotkey_setter_util
import file_util
# with this program can you change the hot keys


w = tk.Tk()
w.geometry(hotkey_setter_util.app_size)
e1 = tk.Entry(w)
e2 = tk.Entry(w)
e3 = tk.Entry(w)

entry_list = [e1, e2, e3]
text_unchanged_list = ["left hotkey",
                       "right hotkey",
                       "stop hotkey"]


def make_ready():
    for elm in entry_list:
        elm.pack()
    for elm2 in entry_list:
        elm2.config(font=(hotkey_setter_util.font, hotkey_setter_util.font_size))
    for elm3 in entry_list:
        if elm3 == entry_list[0]:
            elm3.insert("0", "left hotkey")
        if elm3 == entry_list[1]:
            elm3.insert("0", "right hotkey")
        if elm3 == entry_list[2]:
            elm3.insert("0", "stop hotkey")


def write():
    text = ""
    if entry_list[0].get() == text_unchanged_list[0]:
        text = f"LEFT = '{hotkey_setter_util.get_left_hotkey()}'"
    if entry_list[1].get() == text_unchanged_list[1]:
        text += f"\nRIGHT = '{hotkey_setter_util.get_right_hotkey()}'"
    if entry_list[2].get() == text_unchanged_list[2]:
        text += f"\nSTOP = '{hotkey_setter_util.get_stop_hotkey()}'"
    if entry_list[0].get() != text_unchanged_list[0]:
        text = f"LEFT = '{entry_list[0].get()}'"
    if entry_list[1].get() != text_unchanged_list[1]:
        text += f"\nRIGHT = '{entry_list[1].get()}'"
    if entry_list[2].get() != text_unchanged_list[2]:
        text += f"\nSTOP = '{entry_list[2].get()}'"
    file_util.write(hotkey_setter_util.file_name, text)


make_ready()
tk.Button(w, text="Save Hotkeys", command=write, font=(hotkey_setter_util.font, hotkey_setter_util.font_size)).pack()
w.mainloop()
