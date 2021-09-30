# 

## Official

Take look a typical example.

```python

# Check the `credits1` defined where have all thing you want to know.
credits = credits1(creditfile="./credits.txt", width=480, gap=100,
                   font="/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf")

# After did this, credits could be srolling.
scrolling_credits = credits.set_position(lambda t: ('center', -int((RES_VER_MAX / VIDEO_DURATION) * t)))

final = CompositeVideoClip([scrolling_credits], size=(800, 480))
final.duration = 5

# write to a file
final.write_videofile("../../test.avi", fps=24, codec='mpeg4')
```

## DIY