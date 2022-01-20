import matplotlib.pyplot as plt
import librosa
import math
import numpy as np

def add_noise(sample):
    signal, _ = librosa.load(sample)
    plt.plot(signal)

    RMS = STD_n = math.sqrt(np.mean(signal**2))
    noise = np.random.normal(0, STD_n, signal.shape[0])

    signal_noise = signal+noise
    plt.plot(signal_noise)
