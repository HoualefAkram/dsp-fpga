import tkinter as tk

from constants.colors import Colors


class Widget:
    @staticmethod
    def Button(master, command, text):
        return tk.Button(
            master=master,
            command=command,
            text=text,
            height=2,
            width=30,
            background=Colors.BLUE,
            activebackground=Colors.BLUE,
            foreground=Colors.WHITE,
            activeforeground=Colors.WHITE,
        )
