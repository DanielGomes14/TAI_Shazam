from consts import *

class NCD:
    def __init__(self, sample, compressor="gzip") -> None:
        self.sample_name = sample.split(".")[-2].split("/")[-1] + "." + sample.split(".")[-1]

        if compressor == "gzip":
            import gzip as compressor
        elif compressor == "bzip2":
            
        self.compressor = compressor
    
    def recognize_music(self) -> str:
        pass

