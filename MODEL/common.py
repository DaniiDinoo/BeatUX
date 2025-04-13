from pathlib import Path
from scipy.signal import butter, filtfilt, iirnotch
from MODEL.jsonOperations import jsonOperations

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

        for i in range(0, len(DI)):
            DI[i] = float(DI[i])
            DII[i] = float(DII[i])
            DIII[i] = float(DIII[i])

        DI = self.filter_ecg_signal(DI, 1000, 60 , 30,80 , 5)
        DII = self.filter_ecg_signal(DII, 1000, 60 , 30,80 , 5)
        DIII = self.filter_ecg_signal(DIII, 1000, 60 , 30, 80, 5)
        # ecgReturnableSignals: dict = {}
        # ecgReturnableSignals['DI'] = DI
        # ecgReturnableSignals['DII'] = DII
        # ecgReturnableSignals['DIII'] = DIII


        #Debería recibir una estructura con: (la estructura podría ser una lista de objetos)
        #ID PACIENTE
            #DI vector
            #DII vector
            #DIII vector
            #Fecha de registro (posiblemente)
        
        identJson = jsonOperations('IDENTIFIERS')
        identJson.addID(2512)
        identJson.addID(1511)
        #Y para cada objeto, revisar si ya existe su identificador en el .json IDENTIFIERS.json
        #Si no exixte, agregarlo




        # return ecgReturnableSignals





    def filter_ecg_signal(self, signal, fs, notch_freq, q, lowpass_cutoff, lowpass_order):
        """
        Filtra una señal ECG aplicando un filtro notch para eliminar 60 Hz y
        un filtro pasa-bajos para eliminar altas frecuencias.

        :param signal: Lista o array de la señal de entrada
        :param fs: Frecuencia de muestreo en Hz
        :param notch_freq: Frecuencia del filtro notch (por defecto 60 Hz)
        :param q: Factor de calidad del filtro notch
        :param lowpass_cutoff: Frecuencia de corte del filtro pasa-bajos
        :param lowpass_order: Orden del filtro pasa-bajos
        :return: Señal filtrada
        """
        # Filtro notch
        b_notch, a_notch = iirnotch(notch_freq, q, fs)
        signal_notched = filtfilt(b_notch, a_notch, signal)

        # Filtro pasa-bajos
        nyq = 0.5 * fs
        normal_cutoff = lowpass_cutoff / nyq
        b_low, a_low = butter(lowpass_order, normal_cutoff, btype='low', analog=False)
        signal_filtered = filtfilt(b_low, a_low, signal_notched)

        return signal_filtered


       


            