import pymongo as pm 

client = pm.MongoClient("mongodb://localhost:27017")
myDB = client['VisitorDB']

count = 0

while True:

    print("Person - ", count + 1)

    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    query = input("Enter your query: ")

    data = {
        "name" : name,
        "phone" : phone,
        "query" : query
    }

    myDB['Info'].insert_one(data)
    count += 1