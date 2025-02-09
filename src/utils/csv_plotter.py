import matplotlib.pyplot as plt
import constants
import constants.numbers

class CsvPlotter:
    @staticmethod
    def plot(file_path,xlabel, ylabel,frequency=constants.numbers.SAMPLE_RATE):
        if not file_path:
            return;
        with open(file=file_path, mode="r") as file:
            lines = file.readlines()
            output = [float(line.strip()) for line in lines]
            x = [i/frequency for i in range(len(output))]
            plt.plot(x,output)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
