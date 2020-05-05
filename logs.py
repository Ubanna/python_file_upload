import pymongo
from flask import Flask
import datetime

app = Flask(__name__)
myClient = None
dataBase = None
nyColl = None

@app.route("/logs",methods=['GET'])
@app.route("/index",methods=['GET'])
def fetchData():
    #Connect to DB
    myClient = pymongo.MongoClient("mongodb+srv://test:123@cluster0-iiyzw.mongodb.net/test?retryWrites=true&w=majority")
    dataBase = myClient["pytest"]
    appLogs = dataBase["applogs"]
    #Return all data
    retData = []
    for row in appLogs.find():
        retData.append(row)
    return str(retData)