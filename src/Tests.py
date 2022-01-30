
from cProfile import label
import matplotlib.pyplot as plt
from MaxFreqs import MaxFreqs
from NCD import NCD
from audioUtils import add_noise, trim_audio_file
import os
from tabulate import tabulate
import time
class Tests():
    def __init__(self, music_dir):
        self.music_dir = music_dir
        self.noises = [0, 0.1, 0.5, 1]
        self.trim_durations = [0, 1, 3, 5]
        self.compressors = ['gzip','bzip2','lzma']
        self.max_freqs = MaxFreqs(music_dir)


    def run_precision_tests(self, trim = 0, noise=0, compressor="gzip"):
        precision = 0
        for i, file in enumerate(os.scandir(self.music_dir)):
            music_sample = sample_name = file.name

            sample = f"{self.music_dir}{music_sample}"
            if trim:
                sample, sample_name = trim_audio_file(sample, 0, trim, sample_name)
            if noise:
                sample, sample_name = add_noise(sample, sample_name, noise)
                
            sample, sample_name = self.max_freqs.calc_max_freqs(sample, sample_name)

            self.NCD = NCD(sample_name, compressor)
            music = self.NCD.recognize_music()

            if music == music_sample:
                precision += 1

        precision /= (i + 1)
        return precision


    def trim_tests(self):
        precisions = []
        for duration in self.trim_durations:
            precision = self.run_precision_tests(trim=duration)
            precisions.append(precision * 100)
            print(f"Trim Duration: {duration}\nPrecision: {precision:.2%}")
        
        plt.plot(self.trim_durations, precisions, label="Precision (%)")
        plt.xlabel("Trim Duration (s)")
        plt.ylabel("Precision (%)")
        plt.yticks(precisions)
        plt.xticks(self.trim_durations)
        plt.legend()
        plt.title("Music Identification Precision with Several Trim Durations")
        plt.show()

    def noise_tests(self):
        precisions = []
        for noise in self.noises:
            precision = self.run_precision_tests(noise=noise)
            precisions.append(precision * 100)
            print(f"Noise Level: {noise}\nPrecision: {precision:.2%}")

        plt.plot(self.noises, precisions, label="Precision (%)")
        plt.xlabel("Noise Level")
        plt.ylabel("Precision (%)")
        plt.yticks(precisions)
        plt.xticks(self.noises)
        plt.legend()
        plt.title("Music Identification Precision with Several Noises Durations")
        plt.show()


    def compressor_tests(self):
        times = []
        precisions = []
        x = []
        for i, compressor in enumerate(self.compressors):
            x.append(i+1)
            start = time.time()
            precision = self.run_precision_tests(compressor=compressor)
            exec_time = time.time() - start
            times.append(exec_time)
            precisions.append(precision * 100)
            print(f"Compressor: {compressor}\nPrecision: {precision:.2%}")

        plt.plot(x, precisions, label="Precision (%)")
        plt.xlabel("Compressor")
        plt.ylabel("Precision (%)")
        plt.yticks(precisions)
        plt.xticks(x, self.compressors)
        plt.legend()
        plt.title("Music Identification Precision with Several Compressors")
        plt.show()
        
        plt.plot(x, times, label="Execution Time (s)")
        plt.xlabel("Compressor")
        plt.ylabel("Execution time (s)")
        plt.yticks(times)
        plt.xticks(x, self.compressors)
        plt.legend()
        plt.title("Music Identification Execution Time with Several Compressors")
        plt.show()


    def all_tests(self):
        headers = ["Trim Duration (s)", "Noise Level", "Compressor", "Execution Time (s)", "Precision"]
        data = []
        for duration in self.trim_durations:
            for noise in self.noises:
                for compressor in self.compressors[:2]:
                    start = time.time()
                    precision = self.run_precision_tests(duration, noise, compressor)
                    exec_time = time.time() - start
                    data.append([duration, noise, compressor, f"{exec_time:.2f}", f"{precision:.2%}"])
                    print(f"Trim Duration (s): {duration}")
                    print(f"Noise Level: {noise}")
                    print(f"Compressor: {compressor}")
                    print(f"Execution Time (s): {exec_time:.2f}")
                    print(f"Precision: {precision:.2%}\n")

        print(tabulate(data, headers,  tablefmt="latex"))