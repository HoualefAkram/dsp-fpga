import sounddevice as sd
import numpy as np
import csv

from utils.file_picker import FilePicker


class AudioPlayer:
    @staticmethod
    def play(file_path: str, samplerate=44100):
        with open(file=file_path, mode="r") as file:
            lines = file.readlines()
            audio_data = [float(line.strip()) for line in lines]
        sd.play(audio_data, samplerate=samplerate)

    @staticmethod
    def pick_and_play(samplerate=44100):
        file_path = FilePicker.csv()
        print(f"FILE PATH: {file_path}")
        AudioPlayer.play(file_path=file_path, samplerate=samplerate)
        return file_path
