# Copyright (c) 2022 IotaHydrae
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
from moviepy.editor import *
from libs import _credits_opr

ASSETS_TITBITS_DIR="./assets/titbits"
ASSETS_IMAGES_DIR="./assets/images"
ASSETS_SOUNDS_DIR="./assets/sounds"

def gen_titbit() -> None:
    titbit_resources = []
    titbit_clips = []
    screensize=(1920,1080)

    # 获取所有的titbit资源
    if os.path.exists(ASSETS_TITBITS_DIR) and len(os.listdir(ASSETS_TITBITS_DIR)) > 0:
        resources = os.listdir(ASSETS_TITBITS_DIR)
        for resource in resources:
            if resource.endswith(".mp4") or resource.endswith(".avi"):
                titbit_resources.append(resource)
    
    print(titbit_resources)

    # 从资源中生成video clip
    titbit_clips = [VideoFileClip(os.path.join(ASSETS_TITBITS_DIR, resource)).subclip(0,6) for resource in titbit_resources]

    # 花絮字幕
    txt_title = (TextClip("花絮", fontsize=60,
                color='white', font="./msyh.ttc")
                .margin(top=15, opacity=0)
                .set_position(('center', 'top')))
    title = (CompositeVideoClip([txt_title])
            .fadein(.5)
            .set_duration(3.5))

    final_clip = concatenate_videoclips([title,titbit_clips])

    final_clip.write_videofile("./final.mp4", fps=30)

    pass

def gen_cast():
    cdopr = _credits_opr.credits_opr(creditfile="./authors.cd", width=1080, stretch=30, color='white', stroke_color='black',font="./msyh.ttc")
    cdopr.get_credits()
    pass

def main():
    clip1 = VideoFileClip("./tech_1920-1080.mp4").margin(10)
    clip2 = VideoFileClip("./test.avi").resize(0.6)

    final_clip = clips_array([[clip1, clip2]])

    final_clip.resize(width=1080).write_videofile("./final.mp4", fps=24)
    pass

def debug():
    gen_titbit()
    # gen_cast()
    pass

if __name__ == "__main__":
    # main()
    debug()
    pass