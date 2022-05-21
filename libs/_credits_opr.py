# Copyright (c) 2022 IotaHydrae
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.VideoClip import ImageClip, TextClip

class credits_opr:
    def __init__(self, creditfile, width, stretch=30, color='white', stroke_color='black',
                 stroke_width=2, font='Impact-Normal', fontsize=60, gap=0):
        self.creditfile = creditfile
        self.width = width
        self.stretch = stretch
        self.color = color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.font = font
        self.fontsize = fontsize
        self.gap = gap

        self.texts = []
        pass

    def get_credits(self):
        with open(self.creditfile, 'r') as f:
            for line in f:
                # skip comment lines
                if line.startswith(('\n', '#', '//')):
                    continue
                # blank lines
                elif line.startswith(".blank"):
                    for i in range(int(line.split(" ")[1])):
                        self.texts.append(['\n', '\n'])
                # job
                elif line.startswith(".job"):
                    #print(line)
                    self.texts.append([line.split(".job")[1], '\n'])
                # name
                elif line.startswith(".name"):
                    #print(line)
                    self.texts.append([line.split(".name")[1], '\n'])
                # image
                elif line.startswith(".image"):
                    #print(line)
                    self.texts.append([line.split(".image")[1], '\n'])
            
            left, right = ("".join(l) for l in zip(*self.texts))
            print(left,right)
            

def main():
    cdopr = credits_opr(creditfile="./authors.cd", width=1080, stretch=30, color='white', stroke_color='black',font="./msyh.ttc")
    cdopr.get_credits()
    pass

if __name__ == "__main__":
    main()