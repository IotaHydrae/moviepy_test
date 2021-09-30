from moviepy.editor import *

from moviepy.video.tools.credits import credits1
from skimage.filters import gaussian

RES_HOR_MAX = 1920
RES_VER_MAX = 1080
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
def blur(image):
    return gaussian(image.astype(float), sigma=1)

print("starting...", 3 * RES_HOR_MAX / 4)
credits = credits1(creditfile="./credits.txt", width=480, gap=100,
                   font="/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf")
#  font="微软雅黑")
scrolling_credits = credits.set_pos(lambda t: ('center', -int((RES_VER_MAX / VIDEO_DURATION) * t)))

final = CompositeVideoClip([scrolling_credits], size=(800, 480))
final.duration = 5
# final.fps=24

final_blurred = final.fl_image(blur)
final_blurred.preview(fps=24)

# final.preview(fps=24, audio=False)


# final.write_videofile("../../test.avi", fps=24, codec='mpeg4')
# cvc.write_videofile("../../test.avi", fps=25, codec="mpeg4")
# final_clip = concatenate_videoclips(cvc)
# final_clip.write_videofile("../../test.avi", fps=12, codec="mpeg4")
# ipython_display(final)
