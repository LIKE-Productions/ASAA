from collections import Counter
import math
from typing import Collection
from pydub import AudioSegment
import spow
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://Magnus-Peters-Munzo:vB0$12!G!WAi@asaafun.zjiyv.mongodb.net/ASAAfun?retryWrites=true&w=majority")
db = client.asaa
asaa = db.asaa


# Sound Variables
good = AudioSegment.from_wav("/home/magnus/GitHub/ASAA/Sounds/good.wav")
okay = AudioSegment.from_wav("/home/magnus/GitHub/ASAA/Sounds/okay.wav")
bad = AudioSegment.from_wav("/home/magnus/GitHub/ASAA/Sounds/bad.wav")
# DB Variables
aleft = []
aright = []
# input variables
left_right = 2

# Hand variables
# left = [26, 26, 28, 30, 28, 28]
# right = [22, 22, 20, 24, 24, 24]
dbleft = {}
dbright = {}


left_right = int(input("Are you left handed or right handed? 0 for left, 1 for right(-1 to end): "))

if left_right == 0:
    left_right = 0
    print("Times should be posted in 60 fps. To convert 30 fps to 60 fps, take your number and multiply it by two.")
    while True:
        left = int(input(
            "Name one throwing time you have. When you have entered in all your times, type in 0: "))
        aleft.append(left)

        if left == 0:
            False
            dbleft = {
                "handiness": "left",
                "numbers": aleft
            }
            break
elif left_right == 1:
    left_right = 1
    while True:
        print("Times should be posted in 60 fps. To convert 30 fps to 60 fps, take your number and multiply it by two.")
        right = float(input(
            "Name one throwing time you have. When you have entered in all your times, type in 0: "))
        aright.append(right)
        if right == 0:
            False
            dbright = {
                "handiness": "right",
                "numbers": aright
            }
        break
else:
    pass

left_id = asaa.insert_one(dbleft).inserted_id
right_id = asaa.insert_one(dbright).inserted_id
