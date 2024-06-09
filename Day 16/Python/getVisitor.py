import pymongo as pm 

client = pm.MongoClient("mongodb://localhost:27017")

myDB = client['VisitorDB']

for i in myDB['Info'].find():
    print(i)