import tkinter as tk

from constants.colors import Colors


class Widget:
    @staticmethod
    def Button(master, command, text, background=Colors.WHITE,
               foreground=Colors.FUCHSIA):
        return tk.Button(
            master=master,
            command=command,
            text=text,
            height=2,
            width=30,
            background=background,
            activebackground=background,
            bg=background,
            foreground=foreground,
            activeforeground=foreground,
            fg=foreground,
        )
