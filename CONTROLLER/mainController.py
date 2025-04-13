from VIEW.beatWindow import BeatWindow
from PySide6.QtWidgets import QTreeWidgetItem
from MODEL.common import Common
from MODEL.common import fetchData
import webbrowser
from VIEW.viewClasses import Box

from MODEL.jsonOperations import jsonOperations

class MainController:
    def __init__(self):
        self.mainWindow = BeatWindow(self)
        self.fetchData = fetchData()


    def rightPathCall(self, imageName: str):
        returnablePath = Common.rightPath(imageName= imageName)
        return returnablePath
    
    def openDocumentation(self):
        # url = ''
        # webbrowser.open(url)
        pass


    def selectPacientPressed(self):
        pass

    def openRegisterPressed(self):
        pass

    def launchWelcome(self):
        pass

    def refreshButtonPressed(self):
        self.fetchData.getNewData()
        # DI = self.ecgData['DI']
        # DII = self.ecgData['DII']
        # DIII = self.ecgData['DIII']
        # self.mainWindow.ecgSignalBoxDI.plot(DI,1000, 'cyan')
        # self.mainWindow.ecgSignalBoxDII.plot(DII,1000, 'cyan')
        # self.mainWindow.ecgSignalBoxDIII.plot(DIII,1000, 'cyan')

        identJson= jsonOperations("IDENTIFIERS", "IDS")
        ides = identJson.getIDs()
        self.mainWindow.patientRegisterBox.clear()
        # self.mainWindow.patientRegisterBox
        for id in ides:
            patient = QTreeWidgetItem([str(id)])
            self.mainWindow.patientRegisterBox.addTopLevelItem(patient)
            #CORREGIR QUE SE ESCRIBAN DE NUEVO EN LA jerarquía.
        

        


    def upArrowPressed(self):
        # print("Hola")
        # color = '#4fff44'
        # self.mainWindow.registerBox.setStyleSheet(f'background-color: {color}')
        pass
    def downArrowPressed(self):
        pass


    def historicalTextChanged(self):
        testo = self.mainWindow.historical.toPlainText()
        print(type(testo))


    def signalInfoTextChanged(self):
        pass


    def launchActions(self):
        identJson= jsonOperations("IDENTIFIERS", "IDS")
        ides = identJson.getIDs()
        for id in ides:
            patient = QTreeWidgetItem([str(id)])
            self.mainWindow.patientRegisterBox.addTopLevelItem(patient)