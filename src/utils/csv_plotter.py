import matplotlib.pyplot as plt
from math import log10
import constants
import numpy
import constants.numbers
from constants.strings import Txt
from utils.filter import Filter


class CsvPlotter:
    @staticmethod
    def plot(file_path, frequency=constants.numbers.SAMPLE_RATE, use_decibel=True):
        if not file_path:
            return
        with open(file=file_path, mode="r") as file:
            flt = Filter()
            lines = file.readlines()
            output = [float(line.strip()) for line in lines]
            db = [
                20 * log10(abs(output[i]) + constants.numbers.EPSILON)
                for i in range(len(output))
            ]
            output = output if not use_decibel else db
            x = [i / frequency for i in range(len(output))]
            plt.subplot(3, 1, 1)
            plt.plot(x, db if use_decibel else output)
            plt.xlabel(Txt.TIME)
            ylabel = Txt.AMPLITUDE + " (dB)" if use_decibel else Txt.AMPLITUDE
            plt.ylabel(ylabel)
            fft = numpy.fft.fft(output)
            fft_shifted = numpy.fft.fftshift(fft)
            fft_magnitude = [abs(f) for f in fft_shifted]
            f_line = numpy.linspace(-frequency / 2, frequency / 2, len(fft_magnitude))
            plt.subplot(3, 1, 2)
            plt.plot(f_line, fft_magnitude)
            plt.subplot(3, 1, 3)
            plt.plot(
                x,
                flt.butter_lowpass_filter(output, 500, frequency),
            )
            plt.show()
