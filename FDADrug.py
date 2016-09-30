import ijson
from urllib.request import urlopen


labelList = []
eventList = []
enforceList = []

class FDADrugAdv():

    def getName(self):
        return self.name

    def getAll(self):
        return self.name


    # Path example: results.item.description.item
    def getLabel(self, path):


        url = "https://api.fda.gov/drug/label.json?api_key=M7uGvaUUJYvv3s5JwUmSqYPfGHauJWqHAZ0VwgGI&search=" + self.name

        labelDump = urlopen(url)




        ret = ""
        for i in ijson.items(labelDump, path):
            ret = i
        return ret

    def getEvent(self, path):

        url = "https://api.fda.gov/drug/event.json?api_key=M7uGvaUUJYvv3s5JwUmSqYPfGHauJWqHAZ0VwgGI&search=" + self.name

        eventDump = urlopen(url)




        ret = ""
        for i in ijson.items(eventDump, path):
            ret = i
        return ret

    def getEnforce(self, path):

        url = "https://api.fda.gov/drug/enforcement.json?api_key=M7uGvaUUJYvv3s5JwUmSqYPfGHauJWqHAZ0VwgGI&search=" + self.name

        enforceDump = urlopen(url)



        ret = ""
        for i in ijson.items(enforceDump, path):
            ret = i
        return ret

    def __init__(self, name):
        self.name = name



class FDADrugEasy():

    def getName(self):
        return self.name


    # Path example: results.item.description.item
    def getLabel(self, path):


        url = "https://api.fda.gov/drug/label.json?api_key=M7uGvaUUJYvv3s5JwUmSqYPfGHauJWqHAZ0VwgGI&search=" + self.name

        labelDumpE = urlopen(url)




        ret = ""
        for i in ijson.items(labelDumpE, "results.item." + path + ".item"):
            ret = i
        return ret

    def getEvent(self, path):
        url = "https://api.fda.gov/drug/event.json?api_key=M7uGvaUUJYvv3s5JwUmSqYPfGHauJWqHAZ0VwgGI&search=" + self.name

        eventDumpE = urlopen(url)



        ret = ""
        for i in ijson.items(eventDumpE, "results.item." + path + ".item"):
            ret = i
        return ret

    def getEnforce(self, path):

        url = "https://api.fda.gov/drug/enforcement.json?api_key=M7uGvaUUJYvv3s5JwUmSqYPfGHauJWqHAZ0VwgGI&search=" + self.name

        enforceDumpE = urlopen(url)



        ret = ""
        for i in ijson.items(enforceDumpE, "results.item." + path + ".item"):
            ret = i
        return ret

    def __init__(self, name):
        self.name = name
