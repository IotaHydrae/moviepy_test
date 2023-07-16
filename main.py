# Copyright (c) 2023 iotah
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
import argparse
from moviepy.editor import *
from libs import _credits_opr

DEFAULT_X_RES = 1920
DEFAULT_Y_RES = 1080
DEFAULT_FRAMERATE = 60

DEFAULT_DURATION = 19
DEFAULT_OUTPUT_NAME = "./output.mp4"
DEFAULT_OUTPUT_CODEC = "mpeg4"

def if_not_none(v, d):
    return v if v is not None else d

def gen_cast(path, duration):
    cdopr = _credits_opr.credits_opr(creditfile=path, height=1920, width=1080, gap=100, font="./fonts/msyh.ttc")
    scrolling_credits = cdopr.gen_credits().set_position(lambda t: ('center', -int((cdopr.h_sum / duration) * t)))
    return scrolling_credits

def main():
    filename = "./credits.txt"

    parser = argparse.ArgumentParser(
        prog='python3 main.py',
        description='used to generate a credits for movie',
        epilog='Text at the bottom of help',
    )

    parser.add_argument('credits')
    parser.add_argument('-d', '--duration')
    parser.add_argument('-o', '--output')
    parser.add_argument('-r', '--framerate')
    parser.add_argument('-x', '--xres')
    parser.add_argument('-y', '--yres')
    parser.add_argument('-c', '--codec')


    args = parser.parse_args()

    print(args.credits, args.duration, args.output,
          args.framerate, args.xres, args.yres, args.codec)

    if os.path.exists(args.credits):
        filename = args.credits
    else:
        exit("PATH ERROR! abort.")

    duration  = if_not_none(args.duration, DEFAULT_DURATION)
    framerate = if_not_none(args.framerate, DEFAULT_FRAMERATE)
    xres = if_not_none(args.xres, DEFAULT_X_RES)
    yres = if_not_none(args.yres, DEFAULT_Y_RES)
    output = if_not_none(args.output, DEFAULT_OUTPUT_NAME)
    codec = if_not_none(args.codec, DEFAULT_OUTPUT_CODEC)

    print(duration, framerate, xres, yres, output, codec)

    cast = gen_cast(filename, duration)
    final = CompositeVideoClip([cast], size=(xres, yres))
    final.duration = duration

    final.write_videofile(output, fps=int(framerate), codec=codec)
    pass

if __name__ == "__main__":
    main()
    pass
