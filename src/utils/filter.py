from scipy.signal import butter, lfilter


class Filter:
    def __init__(self):
        pass

    def coeff(self, cutoff, fs, order=5):
        return butter(order, cutoff, fs=fs, btype="low")

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.coeff(cutoff, fs, order=order)
        y = lfilter(b, a, data)
        return y
