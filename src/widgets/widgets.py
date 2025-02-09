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
            background=Colors.BLACK,
            activebackground=Colors.BLACK,
            foreground=Colors.BLUE,
            activeforeground=Colors.BLUE,
        )
