import time
import os


def follow(i):
    thefile = open("newlines.txt", 'r')
    thefile.seek(i)
    line = thefile.readlines()
    if not line:
        return
    yield line


if __name__ == "__main__":

    fls = follow(n)
    print(fls)