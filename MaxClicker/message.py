from tkinter import messagebox as msg
from client_util import client_version, client_name


def create_info(text):
    msg.showinfo(client_name + client_version, text)    # create a info box
