
CREDITS Generator
====================

Usage
--------------------
This script read from a special format file to generate the credits like:

```shell
creditsusage: python3 main.py [-h] [-d DURATION] [-o OUTPUT] [-r FRAMERATE] [-x XRES] [-y YRES] [-c CODEC] credits
```

A credits should be like this:
```
# This is a comment
# The next line says : leave 4 blank lines

.blank 4
.blank 4
.blank 4

.blank 1
.title,CREDITS,center,72
.blank 1

.job,主要贡献者,center
.name,@iotah,center

.blank 1
.title,MUSIC,center,72
.blank 1

.job,插曲,center
.name,Daniel Powter - Song 6,center

.blank 1

.job,插曲,center
.name,Daft Punk & Panda Bear - Doin' it Right,center

.blank 1

.job,插曲,center
.name,Bonfeel Electro Band - Play Again (Original Mix),center

.blank 1

.job,插曲,center
.name,aesttc - wait for u,center

.blank 1

.job,插曲,center
.name,Avicii & Joakim Berg - I Be Gone (Original Mix),center

.blank 1
.title,THANKS,center,72
.blank 1

.job,屏幕提供方,center
.name,老王电子,center

.blank 1

.job,芯片提供方,center
.name,全志科技、树莓派、STC等,center

.blank 1

.image,./assets/kid.jpg,center
.name,摘下无敌了啊,center

.job,个人仓库,center
.name,https://github.com/iotahydrae,center

.blank 1

.job,组织仓库,center
.name,https://github.com/embeddedboys,center

.image,./assets/embeddedboys-256x256.png,center

.job,组织官网（建设中）,center
.name,https://embeddedboys.github.io/,center

.job,玩的开心！,center

.blank 2
.name,Built with @MoviePy,center

.blank 4
.blank 4
.blank 4
.blank 4
```

License
--------------------
MIT