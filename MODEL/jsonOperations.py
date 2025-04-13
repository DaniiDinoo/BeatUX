import json
import os


import json
import os

class jsonOperations:
    def __init__(self, jsonName: str, container: str):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.jsonName = os.path.join(base_path, jsonName + '.json')
        self.container = container

    def getIDs(self):
        if not os.path.exists(self.jsonName):
            return set()
        with open(self.jsonName, 'r') as f:
            data = json.load(f)
            return set(data.get(self.container, []))  # leer lista de IDS si existe

    def saveUsedIDs(self, usedIds):
        with open(self.jsonName, 'w') as f:
            json.dump({self.container: list(usedIds)}, f, indent=4)

    def addID(self, newID):
        usedIDs = self.getIDs()
        if newID in usedIDs:
            print("This ID already exists")
        else:
            usedIDs.add(newID)
            self.saveUsedIDs(usedIDs)
            print("The ID has been successfully added")

        