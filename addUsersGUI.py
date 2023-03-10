# -*- coding: utf-8 -*-
import csv
import json

# Form implementation generated from reading ui file 'addUsers.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog


class Ui_add_users(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, add_users):
        add_users.setObjectName("add_users")
        add_users.resize(561, 437)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/facebook (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_users.setWindowIcon(icon)
        add_users.setStyleSheet("background:rgb(22, 33, 62)")
        self.verticalLayout = QtWidgets.QVBoxLayout(add_users)
        self.verticalLayout.setObjectName("verticalLayout")
        self.users_names_txt = QtWidgets.QPlainTextEdit(add_users)
        self.users_names_txt.setStyleSheet("background:white;")
        self.users_names_txt.setObjectName("users_names_txt")
        self.verticalLayout.addWidget(self.users_names_txt)
        self.buttons_wgt = QtWidgets.QWidget(add_users)
        self.buttons_wgt.setObjectName("buttons_wgt")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons_wgt)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_btn = QtWidgets.QPushButton(self.buttons_wgt)
        self.import_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.import_btn.setStyleSheet("QPushButton { \n"
                                      "    background:rgb(160, 132, 202); \n"
                                      "    color:white;\n"
                                      "    border: 2px solid rgb(164, 136, 207);\n"
                                      "      border-radius: 5px;\n"
                                      "    height:20px;\n"
                                      "    width:50px;\n"
                                      " }\n"
                                      "QPushButton:hover { \n"
                                      "    background:rgb(164, 136, 207);\n"
                                      "border: 2px solid rgb(160, 132, 202);\n"
                                      "      border-radius: 5px;\n"
                                      "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_btn.setIcon(icon1)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout.addWidget(self.import_btn)
        self.save_btn = QtWidgets.QPushButton(self.buttons_wgt)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setStyleSheet("QPushButton { \n"
                                    "    background:rgb(160, 132, 202); \n"
                                    "    color:white;\n"
                                    "    border: 2px solid rgb(164, 136, 207);\n"
                                    "      border-radius: 5px;\n"
                                    "    height:20px;\n"
                                    "    width:50px;\n"
                                    " }\n"
                                    "QPushButton:hover { \n"
                                    "    background:rgb(164, 136, 207);\n"
                                    "border: 2px solid rgb(160, 132, 202);\n"
                                    "      border-radius: 5px;\n"
                                    "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon2)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout.addWidget(self.buttons_wgt)

        self.retranslateUi(add_users)
        QtCore.QMetaObject.connectSlotsByName(add_users)
        self.setup_buttons()

    def setup_buttons(self):
        self.save_btn.clicked.connect(self.save)
        self.import_btn.clicked.connect(self.import_data)

    def openFileNameDialog(self):
        dialog = QFileDialog()
        options = dialog.Options()
        dialog.setStyleSheet("QFileDialog{background:white;color:white}")
        file_name, _ = dialog.getOpenFileName(self, "Import Users", "",
                                              "CSV Files (*.csv)", options=options)
        if file_name:
            with open(file_name) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                csv_data = ''
                try:
                    for row in csv_reader:
                        if not len(row[0].strip()) == 0:
                            csv_data += row[0].strip() + ',\n'
                    self.users_names_txt.appendPlainText(csv_data)
                except Exception:
                    QtWidgets.QMessageBox(title='Error', text='File Error', parent=dialog)

    def merge_data(self, new_data: dict) -> dict:
        try:
            previous_data = open('users.json', 'r')
            data = dict(json.load(previous_data))
            return data | new_data
        except FileNotFoundError:
            return new_data

    def save(self):
        data = self.users_names_txt.toPlainText().replace('\n', '').strip().split(',')
        new_data = {}
        for value in data:
            if not len(value) == 0:
                new_data[value] = {True: []}
        new_data = self.merge_data(new_data)
        with open('users.json', 'w') as file:
            file.write(json.dumps(new_data, indent=4))
        self.accept()

    def import_data(self):
        self.openFileNameDialog()

    def retranslateUi(self, add_users):
        _translate = QtCore.QCoreApplication.translate
        add_users.setWindowTitle(_translate("add_users", "Add Users"))
        self.import_btn.setText(_translate("add_users", "Import CSV"))
        self.save_btn.setText(_translate("add_users", "Save User"))
