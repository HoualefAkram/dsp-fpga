import sounddevice as sd
from numpy import concatenate
import csv
import time
import os


class AudioRecorder:
    def __init__(self):
        self.__output = []
        self.__is_recording = False
        self.__stream = sd.Stream(channels=1, callback=self.__callback)

    @property
    def is_recording(self) -> bool:
        return self.__is_recording

    def __callback(self, indata, outdata, frames, time, status):
        self.__output.append(indata.copy())

    def start(self):
        if not self.__is_recording:
            self.__output.clear()
            self.__is_recording = True
            self.__stream.start()
            print("Recording started.")

    def stop(self):
        if self.__is_recording:
            self.__is_recording = False
            self.__stream.stop()
            result = concatenate(self.__output, axis=0)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_dir = os.path.join(os.path.dirname(__file__), "../output")
            os.makedirs(output_dir, exist_ok=True)
            filename = f"{timestamp}.csv"
            file_path = os.path.join(output_dir, filename)
            print(file_path)
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(result)
            print(f"Recording stopped. Data saved to {filename}.")
            return file_path
