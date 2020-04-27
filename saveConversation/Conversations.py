from datetime import datetime
class Log:
    def __init__(self):
        pass

    def saveConversations(self, sessionID, usermessage,botmessage,intent,dbConn):

        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")

        #db = dbConn['Covid-19DB']  # connecting to the database called crawlerD
        mydict = {"sessionID":sessionID,"User Intent" : intent ,"User": usermessage, "Bot": botmessage, "Date": str(self.date) + "/" + str(self.current_time)}

        #table = db[sessionID]
        records = dbConn.chat_records
        records.insert_one(mydict)

        #table.insert_one(mydict)


    def saveCases(self, search,botmessage,dbConn):
        myquery = {"search": search}

        cases_dict = {"search":search,"cases": botmessage}
        newvalues = {"$set": cases_dict}

        records = dbConn.cases_records
        records.update_one(myquery, newvalues)
        #records.insert_one(cases_dict)

    def getcasesForEmail(self, search,botmessage,dbConn):
        records = dbConn.cases_records
        return records.find_one({'search': search})

