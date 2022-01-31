import argparse
import sys
from tkinter import N
from MaxFreqs import MaxFreqs
from NCD import NCD
from audioUtils import add_noise, trim_audio_file
from consts import SAMPLE_MAX_FREQS
from Tests import Tests
class Main:
    def __init__(self) -> None:
        sample, noise, trim_start, trim_duration,  music_dir, compressor, tests =  self.check_arguments()
        
        if tests:
            test_obj = Tests(music_dir)
            test_obj.trim_tests()
            test_obj.noise_tests()
            test_obj.compressor_tests()
            test_obj.all_tests()
            exit(0)

        sample_name = sample.split(".")[-2].split("/")[-1] + "." + sample.split(".")[-1]

        if trim_duration:
            sample, sample_name = trim_audio_file(sample, trim_start, trim_duration, sample_name)

        if noise:
            sample, sample_name = add_noise(sample, sample_name, noise)

        self.max_freqs = MaxFreqs(music_dir)
        sample, sample_name = self.max_freqs.calc_max_freqs(sample, sample_name)
        
        self.NCD = NCD(sample_name, compressor)
        music = self.NCD.recognize_music()
        print(f"Guessed Music: {music}" )



    def usage(self):
        print("Usage: python3 main.py\
            \n\t-s <Sample file path to be identified: str>\
            \n\t-m <Directory for music database: str>\
            \n\t-c <Compressor to be used (gzip, bzip2 or lzma): str>\
            \n\t-n <Noise level to add to the sample: float>\
            \n\t-t <Time of sample to start triming: float>\
            \n\t-d <Duration of the trim: float>\
            \n\t-r <Run tests>\n")



    def check_arguments(self):
        arg_parser = argparse.ArgumentParser(
            prog="Finite Context Model",
            usage=self.usage
        )

        arg_parser.add_argument('-sample', nargs=1, default=["./../wav_files/J_Cole-WHO_DAT.wav"])
        arg_parser.add_argument('-noise', nargs=1, type=float, default=[0])
        arg_parser.add_argument('-trim_start', nargs=1, type=float, default=[0])
        arg_parser.add_argument('-duration', nargs=1, type=float, default=[0])
        arg_parser.add_argument('-music_dir', nargs=1, default=["./../wav_files/"])
        arg_parser.add_argument('-compressor', nargs=1, default=["gzip"], choices=["gzip", "bzip2", "lzma"])
        arg_parser.add_argument('-run_tests', action="store_true")
        args = None
        try:
            args = arg_parser.parse_args()
        except:
            self.usage()
            sys.exit(0)

        sample = args.sample[0]
        noise = args.noise[0]
        trim_start = args.trim_start[0]
        trim_duration = args.duration[0]
        music_dir = args.music_dir[0]
        compressor = args.compressor[0]
        tests = args.run_tests

        return sample, noise, trim_start, trim_duration, music_dir, compressor, tests


if __name__ =="__main__":
    main = Main()
