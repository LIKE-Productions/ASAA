'''
This is the main.py file. ASAA is under the BSD 3-Clause License, 
which states that no one can use my base code to create closed source copies. You also cannot
promote this product without my permission. I did this to ensure companies like Adidas and 
Nike aren't using my product for their gain.
'''
from numpy import append
import pymongo
import pandas as pd
import pprint
import pdb
import csv
import os
import platform

client = pymongo.MongoClient(
    "mongodb+srv://Magnus-Peters-Munzo:Magnus2008!@cluster0.edcxs.mongodb.net/LIKE?retryWrites=true&w=majority")
db = client.LIKE
asaa = db.asaa

# left = [26, 26, 28, 30, 28, 28]
# right = [22, 22, 20, 24, 24, 24]
# Distance = 449 cm


dbvar = []
left_right = ''
throwing_time = ""
dbobj = {}
fi_in = 0




class AsaaObj:

        # Input
    def author(self):
        global auth
        auth = input("What is your name?(Used for access purposes)\n")

    def b_setup(self):
        # sysname = platform.system()
        if os.path.exists("asaa_logs"):
            pass
        else:            
            os.mkdir("asaa_logs")



    def questions(self, left_or_right):
        left_or_right = left_right
        print("Times should be posted in 60 fps. To convert 30 fps to 60 fps, take your number and multiply it by two.")

        distance = float(input("What is the distance you threw your throws from? Use meters(to convert cm to m, divide by 100): "))
        while True:
            time = float(input(
                "Name one throwing time you have. When you have entered in all your times, type in 0: "))

            if time == 0:
                dfobj = {
                    "author": auth,
                    "handiness": left_or_right,
                    "distance": distance,
                    "numbers": dbvar
                }

                df = pd.DataFrame.from_dict(dfobj)
                pdb.set_trace()
                df.to_csv(f"./asaa_logs/thr_time{len([name for name in os.listdir('asaa_logs') if os.path.isfile(name)])}.csv")
                print(df)


                
                dbobj = {
                    "author": auth,
                    "handiness": left_or_right,
                    "distance": distance,
                    "numbers": dbvar.pop(-1)
                }
                break
            else:
                tcon = 16.67*time/1000
                throwing_time = distance / tcon * 3.6
            dbvar.append(throwing_time)

        lr_id = asaa.insert_one(dbobj).inserted_id

    def find_docs(self):
        for query in asaa.find({"author": auth}):
            pprint.pprint(query)
            
    
asaaobj = AsaaObj()










asaaobj.author()

big_question = input(
    "Do you want to enter in new data(y) or see old data(n)?: ")

if big_question.startswith('y') == True:
    while left_right.startswith('r') or left_right.startswith('l') == False:
        left_right = input(
            "Are you left handed or right handed? l for left, r for right: ")

        if left_right.startswith('r') or left_right.startswith('l') == True:
            # pdb.set_trace()
            asaaobj.questions(left_right[0])

            break
else:
    asaaobj.find_docs()
