import matplotlib.pyplot as plt


class CsvPlotter:
    @staticmethod
    def plot(file_path,xaxis=None):
        if not file_path:
            return;
        with open(file=file_path, mode="r") as file:
            lines = file.readlines()
            output = [float(line.strip()) for line in lines]
            if xaxis:
                plt.plot(xaxis,output)
            else:
                plt.plot(output)
            plt.show()
