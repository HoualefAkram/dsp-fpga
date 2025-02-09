import constants.numbers
import sounddevice as sd
from utils.file_picker import FilePicker
import constants


class AudioPlayer:
    @staticmethod
    def play(file_path: str, samplerate=constants.numbers.SAMPLE_RATE):
        with open(file=file_path, mode="r") as file:
            lines = file.readlines()
            audio_data = [float(line.strip()) for line in lines]
        sd.play(audio_data, samplerate=samplerate)

    @staticmethod
    def pick_and_play(samplerate=constants.numbers.SAMPLE_RATE):
        file_path = FilePicker.csv()
        print(f"FILE PATH: {file_path}")
        if not file_path:
            return;
        AudioPlayer.play(file_path=file_path, samplerate=samplerate)
        return file_path
