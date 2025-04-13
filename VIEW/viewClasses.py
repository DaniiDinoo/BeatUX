
from PySide6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QDockWidget, QToolBar, QWidget, QSizePolicy,
                               QStatusBar, QMessageBox, QInputDialog, QPushButton, QLineEdit, QTextEdit, QComboBox, QTreeWidget)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QIcon, QAction, QGuiApplication, QMovie
from qt_material import apply_stylesheet
import qtawesome as qta  #https://fontawesome.com/v5/search?o=r&m=free&s=solid
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np






class Splash(QLabel):
    def __init__(self, bgColor: str, gifPath: str):
        super().__init__()
        
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f'background-color: {bgColor}')
        self.heartGif = QMovie(gifPath)
        self.setMovie(self.heartGif)
        self.heartGif.start() 

class Boton(QPushButton):
    def __init__(self, iconID: str):
        super().__init__()
        auxIcon = qta.icon(iconID, color = '#65dfd5')
        self.setIcon(auxIcon)


class Box(QLabel):
    def __init__(self, color: str):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')

    def setBoxText(self, newText: str):
        self.setText(newText)




class IDLabel(QLabel):
    def __init__(self, id: str, color: str):
        super().__init__()
        self.setText(id)
        self.setStyleSheet(f'background-color: {color}')



class textEdition(QTextEdit):
    def __init__(self, color: str, placeHolder: str):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setPlaceholderText(placeHolder)




class plotable(QWidget):
    def __init__(self):
        super().__init__()
        self.signal: list = []
        self.linewidth: int = 1
        self.lineColor: str = ''

        self.figure, self.ax = plt.subplots()
        self.ax.grid(True)
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, data: list, fs: int, lineColor: str):
        self.ax.clear()
        self.ax.plot(data, linestyle='-', color = lineColor, linewidth = 0.5)
        # self.ax.set_xlabel("Índice")
        # self.ax.set_ylabel("Valor")
        self.ax.set_facecolor('#373d43')
        self.ax.set_position([0, 0, 1, 1]) #ADJUST THE PLOT TO FILL THE AVAILABLE SPACE IN THE WIDGET
        self.ax.set_xlim(left=0, right=len(data) - 1) #TAKE INTO ACCOUNT THIS LINE ENSURES THE DATA STARTS FROM ZERO EVEN WHEN NOT
        self.canvas.draw()
    


class ComboBoxi(QComboBox):
    def __init__(self, placeHolder: str = ''):
        super().__init__()
        self.addItem(placeHolder) # Placeholder
        self.setStyleSheet("QComboBox { color: white; }")
        self.data: list = []
        self.addItems(self.data)

    def updateData(self, newData: list):
        self.data = newData
        self.addItems(self.data)


class Hierarchy(QTreeWidget):
    def __init__(self, color: str):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')
        self.setHeaderLabels(["Patients"])