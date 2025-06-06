from PySide6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QDockWidget, QToolBar, QWidget, QSizePolicy,QSplitter,
                               QStatusBar, QMessageBox, QInputDialog, QPushButton, QTreeView)
from PySide6.QtCore import Qt, QTimer
from pathlib import Path
from PySide6.QtGui import QPixmap, QIcon, QAction, QGuiApplication, QMovie
from qt_material import apply_stylesheet
import qtawesome as qta  #https://fontawesome.com/v5/search?o=r&m=free&s=solid
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt



from VIEW.viewClasses import Splash, Boton, Box, IDLabel, textEdition, plotable, ComboBoxi, Hierarchy




class BeatWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("BeatLink")
        self.resize(1400,700)
        gifPath = self.controller.rightPathCall('transparentGif.gif')
        self.splash = Splash('#1c1f2a', gifPath) 
        self.setCentralWidget(self.splash)
        self.heartIcon = QIcon(self.controller.rightPathCall('heartIcon.png'))
        self.setWindowIcon(self.heartIcon)
        QTimer.singleShot(3000, self.realApp)    #Modify the splash time



    def realApp(self):

        self.splash.heartGif.stop()
        self.setStatusBar(QStatusBar(self))
        self.menuBuilder()
        self.toolBuilder()
        self.layoutBuilder()


    def menuBuilder(self):
        menuBar = self.menuBar()

        #FILE TAB CREATION
        fileTab = menuBar.addMenu("   &File   ")

        self.selectRegister = QAction('Select Register', self)
        self.selectRegister.setShortcut('Ctrl+R')
        openRegistericon = qta.icon('fa5s.file-medical-alt', color = '#65dfd5')
        self.selectRegister.setIcon(openRegistericon)
        self.selectRegister.setStatusTip("Select electrocardiographical register")
        self.selectRegister.triggered.connect(self.controller.openRegisterPressed)

        self.selectPacient = QAction("Select a Pacient", self)
        self.selectPacient.setShortcut('Ctrl+P')
        pacienteIcon = qta.icon('fa5s.id-badge', color = '#65dfd5')
        self.selectPacient.setIcon(pacienteIcon)
        self.selectPacient.setStatusTip('Select a pacient to access them data')
        self.selectPacient.triggered.connect(self.controller.selectPacientPressed)


        self.generateReport = QAction('Generate report', self)
        self.generateReport.setShortcut('')


        fileTab.addAction(self.selectPacient)
        fileTab.addAction(self.selectRegister)

        #VIEW TAB CREATION
        viewTab = menuBar.addMenu("   &View   ")


        #HELP TAB CREATION
        helpTab = menuBar.addMenu("   &Help   ")

        self.openUserGuide = QAction("Open User Guide", self)
        self.openUserGuide.setShortcut("Ctrl+D")
        openUGIcon = qta.icon('fa5s.file-alt', color = '#65dfd5')
        self.openUserGuide.setIcon(openUGIcon)
        self.openUserGuide.setStatusTip("Detailed guide for users")
        self.openUserGuide.triggered.connect(self.controller.openDocumentation)

        welcome = QAction("Welcome", self)
        welcomeIcon = qta.icon('fa5s.medkit', color = '#65dfd5')
        welcome.setIcon(welcomeIcon)
        welcome.setStatusTip('Open Welcome message')
        welcome.triggered.connect(self.controller.launchWelcome)

        helpTab.addAction(welcome)
        helpTab.addAction(self.openUserGuide)

    def toolBuilder(self):
        tools = QToolBar("Utilities")
        tools.setOrientation(Qt.Vertical)
        tools.addAction(self.selectPacient)
        tools.addAction(self.selectRegister)
        tools.addAction(self.openUserGuide)

        self.addToolBar(Qt.LeftToolBarArea, tools)

    def layoutBuilder(self):
        self.idAndName = Box("#373D43")
        self.patientRegisterBox = Hierarchy("#373D43")
        self.idLabel = IDLabel("#####", "#373D43")
        self.refreshButton = Boton('fa5s.sync-alt')
        self.refreshButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.refreshButton.setToolTip("Refresh Database")
        self.refreshButton.setStatusTip("Refresh the available data")
        self.refreshButton.pressed.connect(self.controller.refreshButtonPressed)
        leftVPane = QVBoxLayout()
        leftVPane.addWidget(self.idAndName, 7)
        leftVPane.addWidget(self.idLabel, 7)
        leftVPane.addWidget(self.patientRegisterBox, 77)
        leftVPane.addWidget(self.refreshButton, 9)
        dockDummy = QWidget()
        dockDummy.setMinimumWidth(250)
        dockDummy.setLayout(leftVPane)

        self.leftVPaneDock = QDockWidget()
        self.leftVPaneDock.setWindowTitle("Pacient Data")
        self.leftVPaneDock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.leftVPaneDock.setWidget(dockDummy)

        self.upArrowButton = Boton("fa5s.angle-double-up")
        self.upArrowButton.setStatusTip("Change view to next signal")
        self.upArrowButton.setToolTip("Previous Signal")
        self.upArrowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.downArrowButton = Boton("fa5s.angle-double-down")
        self.downArrowButton.setStatusTip("Change view to previous signal")
        self.downArrowButton.setToolTip("Next Signal")
        self.downArrowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.upArrowButton.pressed.connect(self.controller.upArrowPressed)
        self.downArrowButton.pressed.connect(self.controller.downArrowPressed)

        verticalButtons = QVBoxLayout()
        verticalButtons.addWidget(self.upArrowButton, 1)
        verticalButtons.addWidget(self.downArrowButton, 1)


 
        self.ecgSignalBoxDI = plotable()
        self.ecgSignalBoxDI.plot([],0,'cyan')
        self.ecgSignalBoxDII = plotable()
        self.ecgSignalBoxDII.plot([],0,'cyan')
        self.ecgSignalBoxDIII = plotable()
        self.ecgSignalBoxDIII.plot([],0,'cyan')

        vertiSignals = QVBoxLayout()
        vertiSignals.addWidget(self.ecgSignalBoxDI)
        vertiSignals.addWidget(self.ecgSignalBoxDII)
        vertiSignals.addWidget(self.ecgSignalBoxDIII)

        
        horiSignal = QHBoxLayout()
        horiSignal.addLayout(verticalButtons, 2)
        horiSignal.addLayout(vertiSignals, 15)

        #   self.filtersLabel = Box()
        self.firstDateFilter  = ComboBoxi('Select first Date')
        self.secondDateFilter = ComboBoxi('Select second Date')
        self.devFilter        = ComboBoxi('Cyan Waveform')
        self.devFilter.updateData(['Green Waveform', 'White Waveform'])
        self.horiFilters = QHBoxLayout()
        self.horiFilters.addWidget(self.firstDateFilter, 20)
        self.horiFilters.addWidget(self.secondDateFilter, 20)
        self.horiFilters.addWidget(self.devFilter, 15)

        



        leftStat = Box("#373d43")
        mediumStat = Box("#373d43")
        rightStat = Box("#373d43")
        horiStats = QHBoxLayout()
        horiStats.addWidget(leftStat)
        horiStats.addWidget(mediumStat)
        horiStats.addWidget(rightStat)


        self.historical = textEdition('#373d43', 'Relevant Medical History of the Pacient')
        self.historical.textChanged.connect(self.controller.historicalTextChanged)
        self.signalInfo = textEdition('#373d43', 'Signal relevant findings')
        self.signalInfo.textChanged.connect(self.controller.signalInfoTextChanged)

        self.buttonsCorner = QVBoxLayout()
        self.saveData = Boton('fa5s.save')
        self.saveData.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.saveData.setToolTip('Save Data')
        self.saveData.setStatusTip('Save auxiliar data')
        self.clearData = Boton('fa5s.trash')
        self.clearData.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.clearData.setToolTip('Erase Data')
        self.clearData.setStatusTip('Erase current auxiliar data')
        self.buttonsCorner.addWidget(self.saveData)
        self.buttonsCorner.addWidget(self.clearData)
        horiInfo = QHBoxLayout()
        splitterInfo =  QSplitter(Qt.Horizontal)
        splitterInfo.addWidget(self.historical)
        splitterInfo.addWidget(self.signalInfo)
        horiInfo.addWidget(splitterInfo, 95)
        horiInfo.addLayout(self.buttonsCorner, 5)

        rightVPane = QVBoxLayout()
        rightVPane.addLayout(horiSignal, 40)
        rightVPane.addLayout(self.horiFilters, 13)
        rightVPane.addLayout(horiStats, 27)
        rightVPane.addLayout(horiInfo, 20)
        


        self.addDockWidget(Qt.LeftDockWidgetArea, self.leftVPaneDock)

        dummyWidget = QWidget()
        dummyWidget.setLayout(rightVPane)

        self.setCentralWidget(dummyWidget)
        self.controller.launchActions()

