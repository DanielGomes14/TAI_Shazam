import argparse
import sys
from MaxFreqs import MaxFreqs
from NCD import NCD
from audioUtils import add_noise,trim_audio_file
from consts import SAMPLE_MAX_FREQS

class Main:
    def __init__(self) -> None:
        sample, noise, trim,  music_dir, compressor =  self.check_arguments()
        
        sample_name = sample.split(".")[-2].split("/")[-1] + "." + sample.split(".")[-1]
        
        if trim:
            trim_audio_file(sample,trim, sample_name)
            sample= f"{SAMPLE_MAX_FREQS}trim_{sample_name}"
            sample_name = f"trim_{sample_name}"


        noise = None
        if noise:
            add_noise(sample, sample_name, noise)
            sample = f"{SAMPLE_MAX_FREQS}noise_{noise}_{sample_name}"
            sample_name = f"noise_{noise}_{sample_name}"

        self.max_freqs = MaxFreqs(music_dir, sample, sample_name)

        self.max_freqs.calc_max_freqs()

        self.NCD = NCD(sample, sample_name, compressor)

        music = self.NCD.recognize_music()
        print(f"Guessed Music: {music}" )



    def usage(self):
        print("Usage: python3 main.py \n\t-f <file name for data set:str> \n\t-k <context size:int>" +\
            "\n\t-a <alpha:int> \n\t-g <generate text> \n\t-t <number of characters to generate:int>\n")


    def check_arguments(self):
        arg_parser = argparse.ArgumentParser(
            prog="Finite Context Model",
            usage=self.usage
        )

        arg_parser.add_argument('-sample', nargs=1, default=["./../wav_files/sample02.wav"])
        arg_parser.add_argument('-noise', nargs=1, type=float, default=[0.02])
        arg_parser.add_argument('-trim', nargs=1, type=float, default=[5])
        arg_parser.add_argument('-music_dir', nargs=1, default=["./../wav_files/"])
        # meter outros
        arg_parser.add_argument('-compressor', nargs=1, default=["gzip"], choices=["gzip", "bzip2"])
        args = None
        try:
            args = arg_parser.parse_args()
        except:
            self.usage()
            sys.exit(0)

        sample = args.sample[0]
        noise = args.noise[0]
        trim = args.trim[0]
        music_dir = args.music_dir[0]
        compressor = args.compressor[0]

        return sample, noise,trim, music_dir, compressor


if __name__ =="__main__":
    main = Main()
