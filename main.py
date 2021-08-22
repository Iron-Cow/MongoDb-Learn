from pymongo import MongoClient
from random import randint
from decouple import config

DB_USER = config('DB_USER')
DB_PASS = config('DB_PASS')
DB_COLLECTION = config('DB_COLLECTION')
DB_STANDARD_COLLECTION = config('DB_COLLECTION')

client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_COLLECTION}.lhhtw.mongodb.net/{DB_STANDARD_COLLECTION}?retryWrites=true&w=majority")
db = client['testdata']  # any name of database you want
collection = db['testcoll']  # any name of table (collection) you want
name = input("Insert name to save >>> ")
cash = randint(1, 10)

# add one record to db
post1 = {"_id": 1, "name": name, "balance": cash}
collection.insert_one(post1)

# add many records at the same time
post2 = {"_id": 2, "name": name, "balance": cash}  # _id should be unique
post3 = {"_id": 3, "name": name, "balance": cash}

posts_collection = [post2, post3]
collection.insert_many(posts_collection)

print('finished successfully')
