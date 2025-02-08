from VIEW.beatWindow import BeatWindow
from MODEL.common import Common
import webbrowser
from VIEW.viewClasses import Box

class MainController:
    def __init__(self):
        self.mainWindow = BeatWindow(self)


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
        pass

    def upArrowPressed(self):
        # print("Hola")
        # color = '#4fff44'
        # self.mainWindow.registerBox.setStyleSheet(f'background-color: {color}')
        pass
    def downArrowPressed(self):
        pass