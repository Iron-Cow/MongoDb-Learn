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
# name = input("Insert name to save >>> ")
name = "TestUser"
cash = randint(1, 10)

# add one record to db
post1 = {"_id": 1, "name": name, "balance": cash}
if collection.count_documents({"_id": 1}) == 0:
    collection.insert_one(post1)
    print('Added successfully')
else:
    print('Post with such id already exist')

# add many records at the same time
post2 = {"_id": 2, "name": name, "balance": cash}  # _id should be unique
post3 = {"_id": 3, "name": name, "balance": cash}

posts_collection = [post2, post3]

if collection.count_documents({"_id": 2}) == 0 and collection.count_documents({"_id": 3}) == 0:
    collection.insert_many(posts_collection)
    print('Added successfully')
else:
    print('Posts with such id already exist')

# -> dict with keys as a cols
balance1 = collection.find_one({'_id': 1})['balance']
print(f'id 1 balance = {balance1}')

# iterable with full record information
record1 = collection.find({'_id': 1})
[print(record) for record in record1]

# -> dict with keys as a cols
balance2 = collection.find_one({'_id': 1})['balance']
print(f'id 1 balance = {balance1}')

print('Finished successfully')
