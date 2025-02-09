import tkinter as tk
from constants.strings import Txt
from utils.audio_player import AudioPlayer
from utils.audio_recorder import AudioRecorder
from utils.csv_plotter import CsvPlotter
from widgets.widgets import Widget


class AudioApp:

    def __init__(self):
        self.__root_tk = tk.Tk()
        self.__root_tk.geometry(Txt.WINDOW_SIZE)
        self.__root_tk.title(Txt.TITLE)
        self.__recorder = AudioRecorder()
        self.__record_button = Widget.Button(
            master=self.__root_tk,
            command=self.__record,
            text=Txt.START_RECORD,
        )
        self.__record_button.pack(pady=20)

        play_button = Widget.Button(
            master=self.__root_tk,
            text=Txt.SELECT_FILE,
            command=self.__pick,
        )
        play_button.pack()
        self.__root_tk.mainloop()

    def __pick(self):
        file_path = AudioPlayer.pick_and_play()
        CsvPlotter.plot(file_path=file_path,xlabel=Txt.TIME,ylabel=Txt.AMPLITUDE)

    def __record(self):
        if not self.__recorder.is_recording:
            self.__recorder.start()
            self.__record_button.configure(text=Txt.STOP_RECORD)
        else:
            file_path = self.__recorder.stop()
            AudioPlayer.play(file_path=file_path)
            CsvPlotter.plot(file_path=file_path, xlabel=Txt.TIME, ylabel=Txt.AMPLITUDE)
            self.__record_button.configure(text=Txt.START_RECORD)


app = AudioApp()
