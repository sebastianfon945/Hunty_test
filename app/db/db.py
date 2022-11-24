# from motor import motor_asyncio

# MONGO_DETAILS = "mongodb://localhost:27017"

from mongoengine import connect

client = connect(host="mongodb://127.0.0.1:27017/hunty_db")
