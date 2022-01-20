import argparse
import sys
from MaxFreqs import MaxFreqs
from NCD import NCD
from audioUtils import add_noise

class Main:
    def __init__(self) -> None:
        sample, noise, music_dir, compressor =  self.check_arguments()
        
        if noise:
            add_noise(sample)

        self.max_freqs = MaxFreqs(music_dir, sample)

        self.max_freqs.calc_max_freqs()
        
        self.NCD = NCD(sample, compressor)

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

        arg_parser.add_argument('-sample', nargs=1, default=["./../wav_files/sample03.wav"])
        arg_parser.add_argument('-noise', action="store_true", default=False)
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
        noise = args.noise
        music_dir = args.music_dir[0]
        compressor = args.compressor[0]

        return sample, noise, music_dir, compressor


if __name__ =="__main__":
    main = Main()
