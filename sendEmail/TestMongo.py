from pymongo import MongoClient
client = MongoClient("mongodb+srv://username:password@cluster0-XYZURL.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('covid19DB')
records = db.chat_records
print(records.count_documents({}))
new_chat = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}


records.remove()


