from collections import Counter
import math
from playsound import playsound

bad = playsound('/home/magnus/GitHub/ASAA/Sounds/bad.wav')
okay = playsound('/home/magnus/GitHub/ASAA/Sounds/okay.wav')
good = playsound('/home/magnus/GitHub/ASAA/Sounds/good.wav')

left_right = [(26, 22), (26, 22), (28, 20), (30, 24), (28, 24), (28, 24)]
# Counted with 60 frames
left = [26, 26, 28, 30, 28, 28]
right = [22, 22, 20, 24, 24, 24]

lcomp = [good if l <= 24 else okay if l >=30 else bad for l in left]