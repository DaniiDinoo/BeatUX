from VIEW.beatWindow import BeatWindow
from MODEL.common import Common
from MODEL.common import fetchData
import webbrowser
from VIEW.viewClasses import Box

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
        self.ecgData: dict = self.fetchData.getNewData()
        for signal in self.ecgData:
            print(signal)
        


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
        