from collections import Counter
import math
from pydub import AudioSegment
import pymongo
import pprint
import csv

client = pymongo.MongoClient("mongodb+srv://Magnus-Peters-Munzo:Magnus2008!@cluster0.edcxs.mongodb.net/LIKE?retryWrites=true&w=majority")
db = client.LIKE
asaa = db.asaa


# Sound Variables
# bad = AudioSegment.from_wav("Sounds/bad.wav")
# okay = AudioSegment.from_wav("Sounds/okay.wav")
# good= AudioSegment.from_wav("Sounds/good.wav")
# DB Variables
dbvar = []
# input variables
left_right = 'w'

# Hand variables
# left = [26, 26, 28, 30, 28, 28]
# right = [22, 22, 20, 24, 24, 24]
dbobj = {}


def author():
    global author
    author = input()
    

def questions(left_or_right):
    left_or_right = left_right
    print("Times should be posted in 60 fps. To convert 30 fps to 60 fps, take your number and multiply it by two.")

    while True:
        throwing_time = int(input(
            "Name one throwing time you have. When you have entered in all your times, type in 0: "))
        dbvar.append(throwing_time)

        if throwing_time == 0:
            False
            dbvar.pop(-1)
            dbobj = {
                "handiness": left_or_right,
                "numbers": dbvar
            }
            break
    lr_id = asaa.insert_one(dbobj).inserted_id
        

while left_right.startswith('r') or left_right.startswith('l') == False:
    left_right = input("Are you left handed or right handed? r for left, l for right: ")
    
    if left_right.startswith('r') or left_right.startswith('l') == True:
        questions(left_right[0])
    break