
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys
from CONTROLLER.mainController import MainController

import os
import shutil


def delete_pycache_dirs(path='.'):
    """
    Elimina todas las carpetas __pycache__ recursivamente desde el directorio dado (por defecto, el actual).
    """
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if dir_name == '__pycache__':
                full_path = os.path.join(root, dir_name)
                print(f"Eliminando: {full_path}")
                shutil.rmtree(full_path)

if __name__ == '__main__':
    delete_pycache_dirs()
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_cyan.xml')  
    controller = MainController()
    controller.mainWindow.show()
    sys.exit(app.exec())






# Llamar a la función
