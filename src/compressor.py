class Compressor:
    def __init__(self, compressor) -> None:
        if compressor == 'gzip':
            import gzip as compressor
        elif compressor == "bzip2":
            import bz2 as compressor
        elif compressor == "lzma":
            import lzma as compressor
        self.compressor = compressor

    
    # Returns number of bytes
    def compress(self, data):
        return len(self.compressor.compress(data))