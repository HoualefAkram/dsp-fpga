import tkinter as tk
from constants.strings import Txt
from utils.audio_recorder import AudioRecorder
from utils.csv_plotter import CsvPlotter
from widgets.widgets import Widget


class AudioApp:

    def __init__(self):
        self.__root_tk = tk.Tk()
        self.__root_tk.geometry(Txt.WINDOW_SIZE)
        self.__root_tk.title(Txt.TITLE)
        self.__recorder = AudioRecorder()
        self.__button = Widget.Button(
            master=self.__root_tk,
            command=self.__record,
            text=Txt.START_RECORD,
        )
        self.__button.pack(pady=20)
        self.__root_tk.mainloop()

    def __record(self):
        if not self.__recorder.is_recording:
            self.__recorder.start()
            self.__button.configure(text=Txt.STOP_RECORD)
        else:
            file_path = self.__recorder.stop()
            CsvPlotter.plot(file_path=file_path)
            self.__button.configure(text=Txt.START_RECORD)


app = AudioApp()
