
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys
from CONTROLLER.mainController import MainController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_cyan.xml')  
    controller = MainController()
    controller.mainWindow.show()
    sys.exit(app.exec())



