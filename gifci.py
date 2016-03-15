from __future__ import print_function

from PIL import Image

if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        print("GIFMAKER -- create GIF animations")
        print("Usage: gifmaker infile outfile")
        sys.exit(1)

    im = Image.open(sys.argv[1])
    im.save(sys.argv[2], save_all=True)
