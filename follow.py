import time
import os


def follow(thefile):
    thefile.seek(0, os.SEEK_END)
    while True:
        time.sleep(10)
        line = thefile.readlines()
        if not line:
            continue
        yield line



if __name__ == "__main__":
    f = open("newlines.txt", 'r')
    fls = follow(f)
    for l in fls:
        print(l)