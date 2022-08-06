import pymongo
client = pymongo.MongoClient("mongodb+srv://Ashis:Ashisskp123@cluster0.v5lrjko.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"ashis",
    "email":"pashiskumar035@gmail.com",
    "surname":"kanha"
}
d1 = {
    "name":"ashis",
    "email":"pashiskumar035@gmail.com",
    "surname":"kanha"
}
d2 = {
    "name":"ashis",
    "email":"pashiskumar035@gmail.com",
    "surname":"kanha"
}
d3 = {
    "name":"ashis",
    "email":"pashiskumar035@gmail.com",
    "surname":"kanha"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)