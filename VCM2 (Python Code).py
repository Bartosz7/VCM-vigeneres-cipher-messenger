# VCM Vigenere's Cipher Messenger v.2.0
# Developed and programmed by Bartosz Grabek
# Using: PyQt 5 and Python Programming Language
# All rights reserved
# License info: ...

# Properties
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'vc_guiv2.ui'
# Created by: PyQt5 UI code generator 5.12.1
# WARNING! Save is for saving the report, whereas save_text is for saving message/ciphergram

import os, time
from PyQt5 import QtCore, QtGui, QtWidgets

# Cosmetic addings
interval = "".join(["#" for i in range(0,122)]) + "\n"
appStyle="""
QMainWindow{
background-color: lightgray;
}
"""

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 315)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 315))
        MainWindow.setMaximumSize(QtCore.QSize(640, 315))
        MainWindow.setWindowIcon(QtGui.QIcon('key_icon.png'))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # for customizing background color
        MainWindow.setStyleSheet(appStyle)
        ######################################
        # New Label for Font size
        self.label_fs = QtWidgets.QLabel(MainWindow)
        self.label_fs.setText("Font size: 8")
        self.label_fs.move(180,24)
        self.label_fs.show()
        #####################################
        # New slider for Font size
        self.slider = QtWidgets.QSlider(MainWindow)
        self.slider.setFixedWidth(100)
        self.slider.setFixedHeight(17)
        self.slider.setMaximum(30)
        self.slider.setMinimum(8)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.move(250,32)
        self.slider.show()
        ######################################
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 401, 231))
        self.textBrowser.setFontPointSize(8)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_Control_Panel = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Control_Panel.setGeometry(QtCore.QRect(420, 10, 211, 251))
        self.groupBox_Control_Panel.setObjectName("groupBox_Control_Panel")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_Control_Panel)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 22, 199, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_open = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_2.addWidget(self.btn_open)
        self.btn_save = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 5, 0, -1)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radiobtn_encrypt = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radiobtn_encrypt.setChecked(True)
        self.radiobtn_encrypt.setObjectName("radiobtn_encrypt")
        self.horizontalLayout.addWidget(self.radiobtn_encrypt)
        self.radiobtn_decrypt = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radiobtn_decrypt.setObjectName("radiobtn_decrypt")
        self.horizontalLayout.addWidget(self.radiobtn_decrypt)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_start = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_2.addWidget(self.btn_start)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.checkBox_report = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_report.setObjectName("checkBox_report")
        self.verticalLayout.addWidget(self.checkBox_report)
        ######################################
        # New Checkbox for reporting
        self.checkBox_test_report = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_test_report.setObjectName("checkBox_test_report")
        self.checkBox_test_report.setText("Test Report")
        self.verticalLayout.addWidget(self.checkBox_test_report)
        ######################################
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 621, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(360, 9, 51, 21))
        self.btn_clear.setObjectName("btn_clear")
        self.groupBox_Control_Panel.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        self.btn_clear.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuAutor = QtWidgets.QMenu(self.menubar)
        self.menuAutor.setObjectName("menuAutor")
        MainWindow.setMenuBar(self.menubar)
        self.actionGuide = QtWidgets.QAction(MainWindow)
        self.actionGuide.setObjectName("actionGuide")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionEncrypt = QtWidgets.QAction(MainWindow)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionDecrypt = QtWidgets.QAction(MainWindow)
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.actionHack = QtWidgets.QAction(MainWindow)
        self.actionHack.setObjectName("actionHack")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAutor.addAction(self.actionGuide)
        self.menuAutor.addAction(self.actionAuthor)
        self.menuAutor.addAction(self.actionExit)
        self.menubar.addAction(self.menuAutor.menuAction())

        # SIGNALS
        self.btn_clear.clicked.connect(self.textBrowser.clear)
        self.btn_start.clicked.connect(self.start)
        self.actionGuide.triggered.connect(self.open_docs)
        self.actionAuthor.triggered.connect(self.open_author)
        self.btn_open.clicked.connect(self.open_text)
        self.btn_save.clicked.connect(self.save_text)
        self.actionExit.triggered.connect(MainWindow.close)
        #self.checkBox_report.stateChanged.connect(self.isreport)
        self.slider.valueChanged.connect(self.change_font_size)
        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save(self, texty, title):
        file = open(str(title) + '.txt', 'w')
        file.write(str(texty))
        file.close()

    def change_font_size(self):
        size = self.slider.value()
        copy = self.textBrowser.toPlainText()
        self.textBrowser.clear()
        self.textBrowser.setFontPointSize(size)
        self.textBrowser.setText(copy)
        self.label_fs.setText("Font size: "+str(size))

    def error_box(self, info):
        self.error = QtWidgets.QMessageBox(MainWindow)
        self.error.setWindowTitle("Error")
        self.error.setIcon(3)
        self.error.setText(info)
        self.error.show()
        return

    def open_author(self):
        try:
            os.startfile("LICENSE.txt")
        except Exception as e:
            self.error_box("Error: Document not found")

    def open_docs(self):
        try:
            os.startfile("Guide to Vigenere's Cipher by Bartosz Grabek.pdf")
        except Exception as e:
            self.error_box("Error: Document not found")

    def start(self):
        # taking out values
        text = self.textBrowser.toPlainText()
        password = str(self.lineEdit_password.text())
        auto_save = self.checkBox_report.isChecked()

        # FOR TESTING ONLY
        create_report = self.checkBox_test_report.isChecked()

        if password == "" and text == "":
            self.error_box("Write your message and password!")
            return

        elif password == "":
            self.error_box("Write your password!")
            return

        elif text == "":
            self.error_box("There is no message to be transformed.")
            return

        # checking the password
        try:
            for el in password:
                if (ord(el) >= 65 and ord(el)<=90) or (ord(el)>=97 and ord(el)<=122):
                    None
                else:
                    self.error_box("Password must include ONLY English letters")
                    return
        except Exception as e:
            self.error_box("An error occured: "+str(e))

        # clearing the table
        self.textBrowser.clear()
        self.lineEdit_password.clear()

        # checking Encryption or Decryption
        encrypt = self.radiobtn_encrypt.isChecked()
        if encrypt == True:
            self.crypt("encrypt",text,password,create_report,AutoSave=auto_save)
        else:
            self.crypt("decrypt",text,password,create_report,AutoSave=auto_save)

    def crypt(self,mode,text,password,create_report,AutoSave):
        try:
            self.progressBar.show()
            # s - what user wants to crypt
            s = text

            # list_1 for result text
            list_1 = []

            # getting the key word
            key_word = password.lower()
            key_word_len = int(len(key_word))

            # num_space for preventing non-letters from being transcribed
            num_space = 0

            # for testing purposes only
            if create_report == True:
                report = ("Mode: "+str(mode))
                report += "\n"+interval + "Text: " + "\n" + s + "\n" + interval
                report += ("Length of your messagge: " + str(len(s)) + "\n")
                report += ("Password:                " + key_word + "\n")
                report += ("Length of password:      " + str(key_word_len) + "\n")
                report += interval

            # boolean for controlling upper- and lowercase
            change = False

            for index in range(0, int(len(s))):

                # number in the ASCII table
                char_ascii = ord(s[index])

                # checking if the char is a small letter
                if (char_ascii >= 65 and char_ascii <= 90) or (char_ascii >= 97 and char_ascii <= 122):

                    # if capital letter
                    if char_ascii >= 65 and char_ascii <= 90:
                        # making capitals lowercase
                        char_ascii += 32
                        change = True

                    # attributing number of password transformations to positions of prime message
                    rest = int((index - num_space)% key_word_len)

                    # transforming letters with succesive chars of key_word within the alphabet
                    if mode == "encrypt":
                        n = (int(char_ascii + ord(key_word[rest])-1) - 96)
                        # if it doesn't fit to the alphabet
                        if not (n >= 97 and n <= 122):
                            n %= 122
                            n += 96

                    elif mode == "decrypt":
                        #shift = (ord(key_word[rest]) - 97)
                        n = char_ascii - (ord(key_word[rest]) - 97)
                        # if it doesn't fit to the alphabet
                        if not (n >= 97 and n <= 122):
                            n = 96 - n
                            n = 122 - n

                    # for testing only
                    # Rest index = value of shift/relocation
                    if create_report == True:
                        report += ("Char of password:        " + key_word[rest] + "\n")
                        report += ("Old index:               " + str(char_ascii) + "\n")
                        report += ("New index:               " + str(n) + "\n")
                        report += ('"' + str(s[index]) + '"' + ' changed with "' + str(chr(n)) + '"' + "\n")
                        report += interval

                    # checking if change to lowercase was executed and converting back to uppercase
                    if change == True:
                        n -= 32
                        change = False

                    # add new transformed char to the result list
                    list_1.append(str(chr(n)))

                # if char is not a letter
                else:
                    list_1.append(str(chr(char_ascii)))
                    num_space += 1

                # for progress bar
                loading = index / int(len(s)) * 100
                self.progressBar.setValue(loading)

            # saving newly transcribed message
            # connecting succesive chars to form complete ciphergram
            ciphergram = "".join(list_1)

            # reporting (for testing only)
            if create_report == True:
                if mode == "encrypt":
                    report += ("Ciphergram: " + "\n" + ciphergram + "\n")
                elif mode == "decrypt":
                    report += ("Deciphered text: " + "\n" + ciphergram + "\n")

                report += interval

                if int(len(ciphergram)) == int(len(s)):
                    report += ("TEST: Successful" + "\n")
                else:
                    report += ("TEST: Failure" + "\n" + "Probable cause: ValueError" + "\n")

            # Automatic save option
            time_1 = time.strftime("%d-%m-%Y %H-%M", time.localtime())

            if AutoSave == True:
                if mode == "encrypt":
                    self.save(ciphergram, 'Encrypted Message '+str(time_1))
                elif mode == "decrypt":
                    self.save(ciphergram, 'Decrypted Message '+str(time_1))

            if create_report == True:
                self.save(report, 'Report ' + str(mode) + 'ion' + " "+str(time_1))

            self.textBrowser.setPlainText(ciphergram)
            self.progressBar.setValue(0)
            self.progressBar.hide()

        except Exception as e:
            self.progressBar.setValue(0)
            self.progressBar.hide()
            self.error_box("Process failed due to: "+ str(e) +"."+"\n"+"Try again.")

    def open_text(self):
        try:
            self.filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Otwórz dokument', "Users\dggt\Desktop\Vigenere's Cipher v.2.0", "*.txt;*.rtf")
            if self.filename != None:
                f = open(self.filename[0], 'r')  # New line
                data = f.read()
                f.close()

            self.textBrowser.clear()
            self.textBrowser.insertPlainText(data)
        except Exception as e:
            None

    def save_text(self):
        try:
            data = self.textBrowser.toPlainText()
            name = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', ('.txt'))
            file = open(name[0] + ".txt", 'w')
            file.writelines(data)
            file.close()
        except Exception as e:
            None

# retranslating GUI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VCM Vigenere\'s Cipher Messenger by Bartosz Grabek"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Your message:"))
        self.groupBox_Control_Panel.setTitle(_translate("MainWindow", "Control Panel"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Enter your password"))
        self.label_1.setText(_translate("MainWindow", "Password:"))
        self.lineEdit_password.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Enter the key word to be used to encrypt your message. Any person who knows this password will be able to decrypt and read your message.</span></p></body></html>"))
        self.lineEdit_password.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Choose function"))
        self.radiobtn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.radiobtn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Settings:"))
        self.checkBox_report.setText(_translate("MainWindow", "Auto Save"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.menuAutor.setTitle(_translate("MainWindow", "Help"))
        self.actionGuide.setText(_translate("MainWindow", "Guide to Vigenere\'s Cipher"))
        self.actionAuthor.setText(_translate("MainWindow", "Author/License"))
        self.actionEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.actionEncrypt.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.actionDecrypt.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionHack.setText(_translate("MainWindow", "Hack"))
        self.actionHack.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))

# Running app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
