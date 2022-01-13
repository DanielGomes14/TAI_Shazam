import os
import subprocess
from consts import *

class MaxFreqs:
    def __init__(self, music_dir, sample) -> None:
        self.music_dir = music_dir
        self.sample = sample
        self.sample_name = sample.split(".")[-2].split("/")[-1] + "." + sample.split(".")[-1]


    def calc_max_freqs(self):
        # execute binary to get max frequencies of musics and for the sample
        for file in os.scandir(self.music_dir):
            subprocess.run([f"./GetMaxFreqs -w {MUSIC_MAX_FREQS}{file.name} {self.music_dir}{file.name}"], shell=True)
        subprocess.run([f"./GetMaxFreqs -w {SAMPLE_MAX_FREQS}{self.sample_name} {self.sample}"], shell=True)