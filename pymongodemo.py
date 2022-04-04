import pymongo

client = pymongo.MongoClient() # MongoDB connection
database = client['mydb'] # Create Database
collection = database['people'] # Create Collection

post1 = {'_id':8, 'name': 'Mew'} # always include '_id'
post2 = {'_id':9, 'name': 'Sand'}
post3 = {'_id':10, 'name': 'Jo'}
post4 = {'_id':11, 'name': 'Ant'}

collection.insert_many([post1,post2,post3,post4])


results = collection.find({"name":"Jo"})

for result in results:
    print(result["_id"])