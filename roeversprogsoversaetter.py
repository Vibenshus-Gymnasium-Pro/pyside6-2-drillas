import os
import sys

import roeversprog

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader


loader = QUiLoader()


class Roeversprogsoversaetter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("roeversprogsoversaetter.ui", None)
        self.ui.setWindowTitle("Oversætter yayayayay")
        self.ui.oversaet_knap.clicked.connect(self.oversaet)
        # self.ui.show()

    def oversaet(self):
        input_text = self.ui.danskinput.toPlainText()
        output_fra_oversaetteren = roeversprog.oversaet_til_roeversprog(input_text)
        self.ui.roever_output.setPlainText(output_fra_oversaetteren)


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
roeversprogsoversaetter = Roeversprogsoversaetter()
roeversprogsoversaetter.ui.show()
program.exec()
