# Copyright (c) 2022 IotaHydrae
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.VideoClip import ImageClip, TextClip

JOB_HEAD   = ".job"
NAME_HEAD  = ".name"
TITLE_HEAD = ".title"
IMAGE_HEAD = ".image"
MOVIE_HEAD = ".movie"

class credit_line:
    def __init__(self, txt="", type="normal", align="center",
                 font="", fontsize="24", color="white", oneline=True,
                 img_path=""):
        self.txt = txt
        self.type = type
        self.align = align
        self.font = font
        self.fontsize = fontsize
        self.color = color
        self.oneline = oneline
        self.img_path = img_path

class credits_opr:
    def __init__(self, creditfile, width, height, stretch=30, color='white', stroke_color='black',
                 stroke_width=1, font='Impact-Normal', fontsize=48, gap=0):
        self.creditfile = creditfile
        self.width = width
        self.height = height
        self.stretch = stretch
        self.color = color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.font = font
        self.fontsize = fontsize
        self.gap = gap

        self.texts = []
        self.clips = []
        self.online = True
        
        self.h_sum = 0
        self.w_sum = 0
        pass

    def gen_credits(self):

        credit_lines = []
        oneline = True
        
        with open(self.creditfile) as f:
            for l in f:
                line = ''
                if l.startswith(('\n', '#', "//")):
                    # exclude blank lines or comments
                    continue
                elif l.startswith('.blank'):
                    # ..blank n  
                    line = credit_line(
                        txt="\n"*int(l.split(' ')[1]),
                        type="text",
                        font=self.font,
                        fontsize=self.fontsize,
                    )

                    
                elif l.startswith(JOB_HEAD):
                    line = credit_line(
                        txt = l.split(',')[1],
                        type = "text",
                        align = l.split(',')[2].strip(),
                        oneline = False,
                        # font = self.font,
                        font = "./fonts/NotoSansSC-Light.otf",
                        fontsize = 56,
                    )
                    
                elif l.startswith(TITLE_HEAD):
                    # self.texts.append(l.split(' '))
                    # oneline = False
                    line = credit_line(
                        txt = l.split(',')[1],
                        type = "text",
                        align = l.split(',')[2].strip(),
                        oneline = True,
                        font = "./fonts/FiraCode-Bold.ttf",
                        fontsize = 72,
                    )
                elif l.startswith(NAME_HEAD):
                    line = credit_line(
                        txt = l.split(',')[1],
                        type = "text",
                        align = l.split(',')[2].strip(),
                        oneline = True,
                        font = "./fonts/NotoSansSC-Medium.otf",
                        fontsize=self.fontsize
                    )
                # TODO: add image support
                elif l.startswith(IMAGE_HEAD):
                    line = credit_line(
                        type = "image",
                        img_path=l.split(',')[1]
                    )
                    pass
                # TODO: add movie support
                elif l.startswith(MOVIE_HEAD):
                    pass
                else:
                    line = credit_line("\n")
                 
                credit_lines.append(line)
            

            for i in range(len(credit_lines)):
                this_line = credit_lines[i]
                
                font = self.font
                fontsize = self.fontsize
                offset_y = 0
                clip = TextClip("\n")
                if this_line.type == "text":
                    font = this_line.font
                    fontsize = this_line.fontsize
                    print(i, this_line.type, this_line.txt)
                    
                    clip = TextClip(this_line.txt, color=self.color, stroke_color=self.stroke_color,
                                        stroke_width=self.stroke_width,
                                        font=font,
                                        fontsize=fontsize)
                
                elif this_line.type == "image":
                    print(i, this_line.type, this_line.img_path)
                    clip = ImageClip(img=this_line.img_path)
        
            
                else:
                    print("Unsupported type!!!!!!!!!")
                
                clip = clip.set_position((this_line.align, self.h_sum + offset_y))
                self.h_sum += clip.h
                self.w_sum += clip.w
                
                self.clips.append(clip)
                    
            cc = CompositeVideoClip(self.clips,
                                    size=(self.width, self.h_sum),
                                    bg_color=None)
            
            # SCALE TO THE REQUIRED SIZE
            
            scaled = resize(cc, width=self.width)
            
            # TRANSFORM THE WHOLE CREDIT CLIP INTO AN ImageCLip
            
            imclip = ImageClip(scaled.get_frame(0))
            amask = ImageClip(scaled.mask.get_frame(0), ismask=True)
            
            return imclip.set_mask(amask)
            

def main():
    cdopr = credits_opr(creditfile="./authors.cd", width=1080, gap=100,font="./msyh.ttc")
    cdopr.gen_credits()
    pass

if __name__ == "__main__":
    main()