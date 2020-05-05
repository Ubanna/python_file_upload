import pymongo
import os
import csv

myclient = pymongo.MongoClient("mongodb+srv://test:123@cluster0-iiyzw.mongodb.net/test?retryWrites=true&w=majority")
"""dblist = myclient.list_database_names()"""
mydb = myclient["pytest"]
myColl = mydb["csvcoll"]
myData = []

if os.path.isfile("task_data.csv"):
    with open("task_data.csv", "r") as filePtr:
        fileData = csv.DictReader(filePtr)
        for row in fileData:
            myData.append(row)
        """Clear the data and reupload"""
        myColl.delete_many({})
        print("Deleted old data")
        num = myColl.insert_many(myData)
        print("{0} new records inserted".format(len(num.inserted_ids)))
else:
    print("task_data.csv not found, exiting!!!")
