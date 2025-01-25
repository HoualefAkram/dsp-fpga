from tkinter import filedialog


class FilePicker:
    @staticmethod
    def csv():
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
        )
        return file_path
