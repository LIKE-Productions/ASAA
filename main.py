from collections import Counter
import math
from playsound import playsound

# Sound Variables
bad = playsound('Sounds/bad.wav')
okay = playsound('Sounds/okay.wav')
good = playsound('Sounds/good.wav')
# Hand variables
left = [26, 26, 28, 30, 28, 28]
right = [22, 22, 20, 24, 24, 24]


left_right = int(input("Are you left handed or right handed? 0 for left, 1 for right."))

while left_right >=2:
    left_right

if left_right:
    lcomp = [good if l <= 24 else okay if l >=28 else bad for l in left]
else:
    rcomp = [good if r <= 22 else okay if r >=24 else bad for r in right]
# Juicy sweet code
# Counted with 60 frames





ileft = iter(left)
iright = iter(right)

print("Left hand")
for i in ileft:
    print(i)
print("")
print("Right hand")
for i in iright:
    print(i)