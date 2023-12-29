import tkinter as tk
import config_creator_util
import message
import file_util
# with this program you can create your on config is
# sorry for this bad design
w = tk.Tk()
w.geometry("300x200")
e1 = tk.Entry(w)
e2 = tk.Entry(w)
e3 = tk.Entry(w)
e4 = tk.Entry(w)
e1.pack()
e2.pack()


def set_desc():
    e1.insert("0", "max cps")
    e1.config(font=(config_creator_util.font, config_creator_util.font_size))
    e2.insert("0", "min cps")
    e2.config(font=(config_creator_util.font, config_creator_util.font_size))
    e3.insert("0", "x")
    e3.config(font=(config_creator_util.font, config_creator_util.font_size))
    e4.insert("0", "y")
    e4.config(font=(config_creator_util.font, config_creator_util.font_size))


def write():

    try:
        el = int(e1.get())  # Useless var only for try  xd
        el2 = int(e2.get())  # useless var only for try xd
    except TypeError:
        message.create_info("Cps can't converted")
        return

    file_util.write(config_creator_util.file_name, config_creator_util.string + f"c = cps.create({int(e1.get())}, {int(e2.get())})")
    if e3.get() != "x" and e4.get() != "y":
        try:
            el3 = int(e3.get())
            el4 = int(e4.get())
        except TypeError:
            message.create_info("Position can't converted")
            return
        file_util.write("pos_config.py", f"x = {int(e3.get())}\ny = {int(e4.get())}")


btn = tk.Button(w, text="Write Config", command=write, font=(config_creator_util.font, config_creator_util.font_size))

btn.pack()
set_desc()
w.mainloop()