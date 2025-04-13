from pathlib import Path

class Common:
    @staticmethod
    def rightPath(imageName: str):
        currenDir = Path(__file__).parent.parent
        rightPath: str = str(currenDir/'VIEW/images'/imageName)
        return rightPath



class fetchData:
    def __init__(self): #Aquí se le deben pasar los parámetros para poder encontrar los datos, como el link, contraseña de acceso o algo así..
        pass

    def getNewData(self) -> dict:
        print("se buscó nueva data")
        #Por ahora se va a buscar la información en los txt
        baseRoute = 'C:/Users/Gerardo/Desktop/MODULAR DEVELOPMENT/BeatUX/private'
        DIroute = baseRoute + '/DI.txt'
        DIIroute = baseRoute + '/DII.txt'
        DIIIroute = baseRoute + '/DIII.txt'
        signalFileDI = open(DIroute, 'r')
        DI = signalFileDI.readlines()

        signalFileDII = open(DIIroute, 'r')
        DII = signalFileDII.readlines()

        signalFileDIII = open(DIIIroute, 'r')
        DIII = signalFileDIII.readlines()


        ecgReturnableSignals: dict = {}
        ecgReturnableSignals['DI'] = DI
        ecgReturnableSignals['DII'] = DII
        ecgReturnableSignals['DIII'] = DIII
        
        return ecgReturnableSignals

       


            