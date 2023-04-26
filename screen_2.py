from PyQt5.QtWidgets import *
from results import Ui_Form
from main import Motor

class Results(QWidget):
        def __init__(self) -> None:
            super().__init__()
            self.screen_2 = Ui_Form()
            self.screen_2.setupUi(self)
            self.motor = Motor()
            self.motor.title_signal.connect(self.title_change)
            self.motor.date_signal.connect(self.date_change)
            self.motor.overview_signal.connect(self.overview_change)
            self.title = ''
            self.date = ''
            self.overview = ''
            
        def title_change(self,title_1):
            self.screen_2.title.setText(title_1)
        def date_change(self,date_1):
            self.screen_2.date.setText(date_1)
        def overview_change(self,overview_1):
            self.screen_2.overview.setText(overview_1)
            
