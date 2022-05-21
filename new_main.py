# Copyright (c) 2022 IotaHydrae
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np
from moviepy.editor import *
from libs import _credits_opr


def main():
    clip1 = VideoFileClip("./tech_1920-1080.mp4").margin(10)
    clip2 = VideoFileClip("./test.avi").resize(0.6)

    final_clip = clips_array([[clip1, clip2]])

    final_clip.resize(width=1080).write_videofile("./test.mp4", fps=24)
    pass

if __name__ == "__main__":
    main()
    pass