import matplotlib.pyplot as plt


class CsvPlotter:
    @staticmethod
    def plot(file_path):
        with open(file=file_path, mode="r") as file:
            lines = file.readlines()
            output = [float(line.strip()) for line in lines]
            plt.plot(output)
            plt.show()
