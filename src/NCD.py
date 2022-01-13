from consts import *
from compressor import Compressor
import os


class NCD:
    def __init__(self, sample, compressor="gzip") -> None:
        self.sample_name = sample.split(".")[-2].split("/")[-1] + "." + sample.split(".")[-1]

        self.compressor = Compressor(compressor)

        self.music_ndc = {}


    # Kolmogorov distance
    def calc_NCD(self, cx, cy, cxy):
        return (cxy - min(cx, cy)) / max(cx, cy)


    def recognize_music(self) -> str:
        sample_freqs_file = open(f"{SAMPLE_MAX_FREQS}{self.sample_name}",mode="rb")
        sample_freqs = sample_freqs_file.read()

        cx = self.compressor.compress(sample_freqs)

        for music_file in os.scandir(MUSIC_MAX_FREQS):
            music_freqs_file = open(f"{MUSIC_MAX_FREQS}{music_file.name}",mode ="rb")

            music_freqs = music_freqs_file.read()

            cy = self.compressor.compress(music_freqs)

            cxy = self.compressor.compress(sample_freqs + music_freqs)
            
            self.music_ndc[music_file.name.split(".")[-2]] = self.calc_NCD(cx, cy, cxy)

        music = min(self.music_ndc, key=self.music_ndc.get)
        print(self.music_ndc)
        return music
