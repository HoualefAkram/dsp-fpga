import matplotlib.pyplot as plt
from math import log10
import constants
import numpy
import constants.numbers
from constants.strings import Txt


class CsvPlotter:
    @staticmethod
    def plot(file_path, frequency=constants.numbers.SAMPLE_RATE, use_decibel=True):
        if not file_path:
            return
        with open(file=file_path, mode="r") as file:
            lines = file.readlines()
            output = [float(line.strip()) for line in lines]
            db = [
                20 * log10(abs(output[i]) + constants.numbers.EPSILON)
                for i in range(len(output))
            ]
            x = [i / frequency for i in range(len(output))]
            plt.subplot(2, 1, 1)
            plt.plot(x, db if use_decibel else output)
            plt.xlabel(Txt.TIME)
            ylabel = Txt.AMPLITUDE + " (dB)" if use_decibel else Txt.AMPLITUDE
            plt.ylabel(ylabel)
            fft = numpy.fft.fft(output)
            fft_shifted = numpy.fft.fftshift(fft)
            fft_magnitude = [abs(f) for f in fft_shifted]
            f_line = numpy.linspace(-frequency / 2, frequency / 2, len(fft_magnitude))
            plt.subplot(2, 1, 2)
            plt.plot(f_line, fft_magnitude)

            plt.show()
