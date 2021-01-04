from collections import Counter
import math


# left_right = [(26, 22), (26, 22), (28, 20), (30, 24), (28, 24), (28, 24)]
# Counted with 60 frames
left = [26, 26, 28, 30, 28, 28]
right = [22, 22, 20, 24, 24, 24]

min_h1 = min(left)
min_h2 = min(right)

max_h1 = max(left)
max_h2 = max(right)

hand1 = Counter(left)
hand2 = Counter(right)
print(f'{hand1}\n{hand2}\nThe min and max values of left and right are:\nmin: {min_h1}, {min_h2}\nmax: {max_h1}, {max_h2}')
