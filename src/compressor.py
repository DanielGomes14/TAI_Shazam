class Compressor:
    def __init__(self, compressor) -> None:
        if compressor == 'gzip':
            import gzip as compressor
        elif compressor == "bzip2":
            import bz2 as compressor

    

    