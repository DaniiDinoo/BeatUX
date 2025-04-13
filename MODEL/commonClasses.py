from MODEL.jsonOperations import jsonOperations
import random
import string


class Register:
    def __init__(self, patientID: int, DI:list, DII: list, DIII: list, date = None):
        self.patientID = patientID
        self.registerID = self.createRegisterID()
        self.DIvector = DI
        self.DIIvector = DII
        self.DIIIvector = DIII


        self.updatePatientID()
        self.saveSignalTxt()

    def updatePatientID(self):
        identJson = jsonOperations('IDENTIFIERS', "IDS")
        identJson.addID(self.patientID)

    def createRegisterID(self)-> str:
        registerIDJson = jsonOperations("REGISTER_ID", "registerIDs")
        usedRegisterIDs = registerIDJson.getIDs()
        
        a = 0
        while(a == 0):
            codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if codigo not in usedRegisterIDs:
                a = 1
                registerIDJson.addID(codigo)

        return codigo
            
    def saveSignalTxt(self):
        DIString = "DI " + self.registerID + '.txt'
        DIIString = "DII " + self.registerID + '.txt'
        DIIIString = "DIII " + self.registerID + '.txt'
        with open(DIString, 'w') as f:
            for item in self.DIvector:
                f.write(f"{item},\n")

        with open(DIIString, 'w') as f:
            for item in self.DIIvector:
                f.write(f"{item},\n")
                
        with open(DIIIString, 'w') as f:
            for item in self.DIIIvector:
                f.write(f"{item},\n")
        

