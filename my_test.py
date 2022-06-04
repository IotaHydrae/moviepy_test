# coding:utf-8
from moviepy.editor import *

from moviepy.video.tools.credits import credits1

# from skimage.filters import gaussian

RES_HOR_MAX = 2560
RES_VER_MAX = 1440
VIDEO_DURATION = 5

# txtClip = TextClip('txtClip', color='white', font='/usr/share/fonts/chinese/TrueType/msyh.ttf',
#                    kerning=5, fontsize=48)
#
# txtClip2 = TextClip('txtClip2', color='white', font='/usr/share/fonts/chinese/TrueType/msyh.ttf',
#                     kerning=5, fontsize=48)
#
# txtClip3 = TextClip('txtClip3', color='white', font='/usr/share/fonts/chinese/TrueType/msyh.ttf',
#                     kerning=5, fontsize=48)
#
# txtClip4 = TextClip('txtClip4', color='white', font='/usr/share/fonts/chinese/TrueType/msyh.ttf',
#                     kerning=5, fontsize=48)
#
# screensize = (RES_HOR_MAX, RES_VER_MAX)
#
# cvc = CompositeVideoClip(
#     [txtClip, txtClip4.set_position(lambda t: (RES_HOR_MAX / 1.5, int((RES_VER_MAX / VIDEO_DURATION) * t)))],
#     size=screensize)
#
# cvc.duration = 5

# def blur(image):
#     return gaussian(image.astype(float), sigma=1)


print("starting...")
credits = credits1(creditfile="./credits.txt", width=1440, gap=100,
                   #    font="/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf")
                   font=".\msyh.ttc")
scrolling_credits = credits.set_position(lambda t: ('center', -int((RES_VER_MAX / 4) * t)))

# Music
audio_clips = AudioFileClip("./bgm.mp3")
# scrolling_credits.set_audio(audio_clips.subclip(55, 65))

scrolling_credits.audio = audio_clips.subclip(55,61)


final = CompositeVideoClip([scrolling_credits], size=(2560, 1440))
final.duration = 6

# final_blurred = final.fl_image(blur)
# final_blurred.preview(fps=24)

final.write_videofile("./test.avi", fps=60, codec='mpeg4')
# final_blurred.write_videofile("../../test.avi", fps=24, codec='mpeg4')
