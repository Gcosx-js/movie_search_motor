from PyQt5.QtWidgets import *
from search_motor import Ui_Form
import json
import requests
from deep_translator import GoogleTranslator
from PyQt5.QtCore import pyqtSignal
import ctypes
from screen_2 import Ui_Form as Ui_ResultsForm
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt 

        
class Results(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.screen_2 = Ui_ResultsForm()
        self.screen_2.setupUi(self)
        self.title = ''
        self.date = ''
        self.overview = ''
        
    def title_change(self, new_text):
        self.screen_2.title.setText(new_text)

    def date_change(self, new_text):
        self.screen_2.date.setText(new_text)

    def overview_change(self, new_text):
        self.screen_2.overview.setText(new_text)


class Motor(QWidget):
    title_signal = pyqtSignal(str)
    date_signal = pyqtSignal(str)
    overview_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.motor = Ui_Form()
        self.motor.setupUi(self)
        self.sc_next = Results()
        self.status = None
        self.motor.search_button.clicked.connect(self.search_on_db)
        self.motor.learn_button.clicked.connect(self.learn_about)
        self.api_key = "a79c5c396bf5cd4305fdd5f11bf194f3"

    def search_on_db(self):
        self.text = self.motor.search_lineedit.text()
        if self.text != '':
            try:
                self.motor.status.setText("Searching..")
                self.motor.status.setStyleSheet("color: rgb(255, 170, 127)")
                self.url = f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={self.text}"
                response = requests.get(self.url)
                json_data = json.loads(response.text)
            except:
                MB_ICONERROR = 0x10
                MB_SETFOREGROUND = 0x100
                message = "Xəta Baş Verdi!"
                title = "Movie Database has stopped!"
                ctypes.windll.user32.MessageBoxW(None, message, title, MB_ICONERROR | MB_SETFOREGROUND, 500, 300)
                json_data = None

            if json_data is not None and json_data["total_results"] > 0:
                movie = json_data["results"][0]
                self.t_t = movie['title']
                self.d_t = movie['release_date']
                self.o_v = movie['overview']
                self.status = True
                self.motor.status.setStyleSheet("color:green;")
                self.motor.status.setText("True")
                self.motor.learn_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.motor.learn_button.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(170, 0, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px solid green;\n"
"    border-radius: 15px;\n"
"    \n"
"    background-color: rgb(56, 0, 85);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(113, 113, 56);\n"
"}")
            else:
                self.motor.status.setStyleSheet("color:red;")
                self.motor.status.setText("False")
                self.motor.learn_button.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.status = False
                self.motor.learn_button.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(170, 0, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px solid red;\n"
"    border-radius: 15px;\n"
"    \n"
"    background-color: rgb(56, 0, 85);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(113, 113, 56);\n"
"}")
                
                


    def learn_about(self):
        self.close()
        if hasattr(self, 't_t') and hasattr(self, 'd_t') and hasattr(self, 'o_v'):
            if self.status == True:
                self.sc_next.title_change(self.t_t)
                self.sc_next.date_change(self.d_t)
                self.sc_next.overview_change(self.o_v)
                self.sc_next.show()
        else:
            QMessageBox.critical(self, "Error", "Please make sure you enter the name of the movie correctly.")

app = QApplication([])
ekran = Motor()
ekran.show()
app.exec_()