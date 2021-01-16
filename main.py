from collections import Counter
import math
import pymongo
import pprint

client = pymongo.MongoClient("mongodb+srv://Magnus-Peters-Munzo:Magnus2008!@cluster0.edcxs.mongodb.net/LIKE?retryWrites=true&w=majority")
db = client.LIKE
asaa = db.asaa


# Sound Variables
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


left_right = int(input("Are you left handed or right handed? 0 for left, 1 for right: "))

if left_right == 0:
    left_right = 0
    print("Times should be posted in 60 fps. To convert 30 fps to 60 fps, take your number and multiply it by two.")
    
    while True:
        left = int(input(
            "Name one throwing time you have. When you have entered in all your times, type in 0: "))
        aleft.append(left)

        if left == 0:
            False
            aleft.pop(-1)
            dbleft = {
                "handiness": "left",
                "numbers": aleft
            }
            break
    left_id = asaa.insert_one(dbleft).inserted_id









elif left_right == 1:
    left_right = 1
    print("Times should be posted in 60 fps. To convert 30 fps to 60 fps, take your number and multiply it by two.")
    
    while True:
        right = int(input(
            "Name one throwing time you have. When you have entered in all your times, type in 0: "))
        aright.append(right)
        if right == 0:
            aright.pop(-1)
            False
            dbright = {
                "handiness": "right",
                "numbers": aright
            }
            break
    right_id = asaa.insert_one(dbright).inserted_id
else:
    pass

