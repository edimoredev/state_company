from pymongo import MongoClient

# variables
URL_MONGO =  'mongodb://localhost:27017/'
MONGO_DB = 'state_company'

# Connection to the database
client = MongoClient(URL_MONGO)
conn = client[MONGO_DB]



