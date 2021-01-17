


'''
This is the main.py file. ASAA is under the BSD 3-Clause License, 
which states that no one can use my base code to create closed source copies. You also cannot
promote this product without my permission. I did this to ensure companies like Adidas and 
Nike aren't using my product for their gain.
'''

from collections import Counter
import math
from pydub import AudioSegment
import pymongo
import pprint


client = pymongo.MongoClient(
    "mongodb+srv://Magnus-Peters-Munzo:Magnus2008!@cluster0.edcxs.mongodb.net/LIKE?retryWrites=true&w=majority")
db = client.LIKE
asaa = db.asaa


# Sound Variables
# bad = AudioSegment.from_wav("Sounds/bad.wav")
# okay = AudioSegment.from_wav("Sounds/okay.wav")
# good= AudioSegment.from_wav("Sounds/good.wav")



# Input 
dbvar = []
left_right = ''
dbobj = {}

# left = [26, 26, 28, 30, 28, 28]
# right = [22, 22, 20, 24, 24, 24]


def author():
    global auth
    auth = input("What is your name?(Used for access purposes)\n")


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
                "author": auth,
                "handiness": left_or_right,
                "numbers": dbvar
            }
            break
    lr_id = asaa.insert_one(dbobj).inserted_id

def find_docs():
    for query in asaa.find({"author": auth}):
        pprint.pprint(query)


author()

big_question = input(
    "Do you want to enter in new data(y) or see old data(n)?: ")

if big_question.startswith('y') == True:
    while left_right.startswith('r') or left_right.startswith('l') == False:
        left_right = input(
            "Are you left handed or right handed? l for left, r for right: ")

        if left_right.startswith('r') or left_right.startswith('l') == True:
            questions(left_right[0])

            break
    another_question = input(
        "Do you want to see your data after you enter in more data? (y/n): ")
    if another_question.startswith('y') == True:
        find_docs()
    else:
        pass
else:
    find_docs()
