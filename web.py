import pymongo
from flask import Flask
import datetime

app = Flask(__name__)
myClient = None
dataBase = None
nyColl = None

@app.route("/",methods=['GET'])
@app.route("/index",methods=['GET'])
def fetchData():
    #Connect to DB
    myClient = pymongo.MongoClient("mongodb+srv://test:123@cluster0-iiyzw.mongodb.net/test?retryWrites=true&w=majority")
    dataBase = myClient["pytest"]
    csvData = dataBase["csvcoll"]
    appLogs = dataBase["applogs"]
    #Log current time against each GET-request
    appLogs.insert_one({"type":"GET", "timestamp":datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")})
    #Return all data
    retData = []
    for row in csvData.find():
        retData.append(row)
    return str(retData)