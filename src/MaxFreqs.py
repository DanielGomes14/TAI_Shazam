import os
import subprocess
from consts import *

class MaxFreqs:
    def __init__(self, music_dir) -> None:
        self.music_dir = music_dir
        self.calc_max_freqs()


    def calc_max_freqs(self, sample=None, sample_name=None):
        # execute binary to get max frequencies of musics and for the sample
        
        if sample:
            sample_musics = { f.name for f in os.scandir(SAMPLE_MAX_FREQS) }

            n_sample_name = f"freqs_{sample_name}"
        
            if n_sample_name not in sample_musics:
                subprocess.run([f"./GetMaxFreqs -w {SAMPLE_MAX_FREQS}{n_sample_name} {sample}"], shell=True)
                if sample_name in sample_musics:
                    os.remove(f"{SAMPLE_MAX_FREQS}{sample_name}")

            sample = f"{SAMPLE_MAX_FREQS}{n_sample_name}"

            return sample, n_sample_name
        else:
            musics = { f.name for f in os.scandir(MUSIC_MAX_FREQS) }
            for file in os.scandir(self.music_dir):
                if file.name not in musics:
                    subprocess.run([f"./GetMaxFreqs -w {MUSIC_MAX_FREQS}{file.name} {self.music_dir}{file.name}"], shell=True)
