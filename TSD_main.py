# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TSD.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from importlib.resources import path
import pyttsx3
import speech_recognition as sr #input speech module
import datetime
import wikipedia 
import webbrowser
import os   #for playing music and other stuff
import random
from playsound import playsound
from mic_Py_window import Ui_Mic_window  # importing new window py class
import icon_rc
import images_rc
import time


############################################## MAIN CODE ###########################################################




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.backPic = QtWidgets.QLabel(self.mainFrame)
        self.backPic.setGeometry(QtCore.QRect(0, 0, 771, 421))
        self.backPic.setText("")
        self.backPic.setPixmap(QtGui.QPixmap("Images/tech.jpg"))
        self.backPic.setScaledContents(True)
        self.backPic.setObjectName("backPic")
        self.frame_1 = QtWidgets.QFrame(self.mainFrame)
        self.frame_1.setGeometry(QtCore.QRect(420, -10, 351, 441))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.getStarted = QtWidgets.QPushButton(self.frame_1)
        self.getStarted.setGeometry(QtCore.QRect(180, 290, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.getStarted.setFont(font)
        self.getStarted.setStyleSheet(
"background-color: transparent ;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"padding: 4px;\n"
"color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);"

)          
        self.getStarted.setObjectName("getStarted")
        self.frame_2 = QtWidgets.QFrame(self.mainFrame)
        self.frame_2.setGeometry(QtCore.QRect(10, -11, 411, 441))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.mainTitle = QtWidgets.QLabel(self.frame_2)
        self.mainTitle.setGeometry(QtCore.QRect(110, 160, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(51)
        self.mainTitle.setFont(font)
        self.mainTitle.setStyleSheet("color: rgb(170, 170, 255);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(170, 170, 255);")
        self.mainTitle.setObjectName("mainTitle")
        self.title_1 = QtWidgets.QLabel(self.frame_2)
        self.title_1.setGeometry(QtCore.QRect(110, 180, 291, 141))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(24)
        self.title_1.setFont(font)
        self.title_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_1.setObjectName("title_1")
        self.title_2 = QtWidgets.QLabel(self.frame_2)
        self.title_2.setGeometry(QtCore.QRect(110, 260, 281, 131))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_2.setObjectName("title_3")
        
        self.title_3 = QtWidgets.QLabel(self.frame_2)
        self.title_3.setObjectName("title_1")
        self.title_3.setGeometry(10, 0, 281, 131)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(8)
        self.title_3.setFont(font)
        self.title_3.setStyleSheet("color: white")
        self.horizontalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                                        
                               #######Main Button logic..........

        self.getStarted.clicked.connect(self.Intro_start)


        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', self.voices[0].id)


    def speak(self, audio):           #take a string argument and speak that string argument
        self.engine.say(audio)
        self.engine.runAndWait()



    def takeCommand(self):            #Funtion to take command from user and return it as string 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=5)
            audio = r.listen(source)

        try:
            print("Recognizing")
            """
            app = QtWidgets.QApplication(sys.argv)
            new_window = QtWidgets.QMainWindow()
            new_window.setObjectName("AnotherWindow")
            new_window.setWindowTitle("Command")
            new_window.setGeometry(784, 438, 0,0)
            win2_label1 = QtWidgets.QLabel(new_window)
            win2_label1.setText("TSD is Listening")
            win2_label1.setGeometry(110, 260, 281, 131)
            new_window.show()
            sys.exit(app.exec_())
            """
            

            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except:
            say = "say that again"
            self.speak(say)
            print(say)
            return None
        return query



    def Intro_start(self):

        self.open_micWindow()

        intro = "Hello Rishav, how can I help you"
        self.speak(intro)
        query = self.takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia....")
            query = query.replace("wikipedia", "") # replaces wikipedia with null for the next iteration
            results = wikipedia.summary(query, sentences=5) # store wikipedia summary in result by using summary function
            self.speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("youtube.com")
    
        elif "google" or "browser" in query:
            webbrowser.open("google.com")

        elif "instagram" in query:
            webbrowser.open("instagram.com")

        elif "the time" in query:                               
            strTime = datetime.datetime.now().strftime("%H:%M:%S") # return time in string format and store in 'strTime'
            speak(f"Sir the time is {strTime}")

        elif "notepad" in query:
            cmd = "notepad"
            os.startfile(cmd)



    def open_micWindow(self):

        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Mic_window()
        self.ui.setupUi(self.window)
        
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TSD"))
        self.title_3.setText("HOME")
        self.getStarted.setText(_translate("MainWindow", "SPEAK"))
        self.mainTitle.setText(_translate("MainWindow", "TSD."))
        self.title_1.setText(_translate("MainWindow", "THINK SPEAK DONE."))
        self.title_2.setText(_translate("MainWindow", "TSD is an artificial intelligence that \n"

"offers an alternate apps control\n"
"system through user voice"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
