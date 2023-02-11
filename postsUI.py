# -*- coding: utf-8 -*-
import json

# Form implementation generated from reading ui file 'posts.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from addPosts import Ui_add_posts
from removePosts import Ui_remove_post


class Ui_posts_ui(QDialog):
    def __init__(self, parent, data: str):
        super(Ui_posts_ui, self).__init__(parent)
        self.user = data
        self.setupUi(self)

    def setupUi(self, posts_ui):
        posts_ui.setObjectName("posts_ui")
        posts_ui.resize(561, 438)
        posts_ui.setStyleSheet("background:rgb(22, 33, 62)")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(posts_ui)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_buttons_widget = QtWidgets.QWidget(posts_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_buttons_widget.sizePolicy().hasHeightForWidth())
        self.top_buttons_widget.setSizePolicy(sizePolicy)
        self.top_buttons_widget.setMinimumSize(QtCore.QSize(400, 0))
        self.top_buttons_widget.setObjectName("top_buttons_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_buttons_widget)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addPosts_btn = QtWidgets.QPushButton(self.top_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPosts_btn.sizePolicy().hasHeightForWidth())
        self.addPosts_btn.setSizePolicy(sizePolicy)
        self.addPosts_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.addPosts_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addPosts_btn.setToolTip("")
        self.addPosts_btn.setAutoFillBackground(False)
        self.addPosts_btn.setStyleSheet("QPushButton { \n"
                                        "    background: rgb(0, 179, 0); \n"
                                        "    color:white;\n"
                                        "    border: 2px solid rgb(0, 190, 0);\n"
                                        "      border-radius: 5px;\n"
                                        "    height:20px;\n"
                                        "    width:50px;\n"
                                        "    icon.name: \"add-user\";\n"
                                        "    icon.source: \"images/add-user.png\";\n"
                                        "    icon.color: black;\n"
                                        " }\n"
                                        "QPushButton:hover { \n"
                                        "    background: rgb(0, 190, 0);\n"
                                        "    border: 2px solid  rgb(0, 179, 0);\n"
                                        "      border-radius: 5px;\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/addUser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPosts_btn.setIcon(icon)
        self.addPosts_btn.setObjectName("addPosts_btn")
        self.horizontalLayout_3.addWidget(self.addPosts_btn)
        self.removePosts_btn = QtWidgets.QPushButton(self.top_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removePosts_btn.sizePolicy().hasHeightForWidth())
        self.removePosts_btn.setSizePolicy(sizePolicy)
        self.removePosts_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.removePosts_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removePosts_btn.setToolTip("")
        self.removePosts_btn.setStyleSheet("QPushButton { \n"
                                           "    background:rgb(218, 0, 0); \n"
                                           "    color:white;\n"
                                           "    border: 2px solid rgb(234, 0, 0);\n"
                                           "      border-radius: 5px;\n"
                                           "    height:20px;\n"
                                           "    width:50px;\n"
                                           " }\n"
                                           "QPushButton:hover { \n"
                                           "    background: rgb(234, 0, 0);\n"
                                           "border: 2px solid rgb(218, 0, 0);\n"
                                           "      border-radius: 5px;\n"
                                           "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/remove-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removePosts_btn.setIcon(icon1)
        self.removePosts_btn.setObjectName("removePosts_btn")
        self.horizontalLayout_3.addWidget(self.removePosts_btn)
        self.verticalLayout_2.addWidget(self.top_buttons_widget)
        self.posts_tabel_tbl = QtWidgets.QTableWidget(posts_ui)
        self.posts_tabel_tbl.setStyleSheet("QTableWidget{\n"
                                           "background:rgb(255, 255, 255);\n"
                                           "border: 2px solid rgb(160, 132, 202);\n"
                                           "border-radius:5px;\n"
                                           "}")
        self.posts_tabel_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.posts_tabel_tbl.setAlternatingRowColors(True)
        self.posts_tabel_tbl.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.posts_tabel_tbl.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.posts_tabel_tbl.setRowCount(0)
        self.posts_tabel_tbl.setColumnCount(2)
        self.posts_tabel_tbl.setObjectName("posts_tabel_tbl")
        item = QtWidgets.QTableWidgetItem()
        self.posts_tabel_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.posts_tabel_tbl.setHorizontalHeaderItem(1, item)
        self.posts_tabel_tbl.horizontalHeader().setCascadingSectionResizes(True)
        self.posts_tabel_tbl.horizontalHeader().setDefaultSectionSize(30)
        self.posts_tabel_tbl.horizontalHeader().setMinimumSectionSize(10)
        self.posts_tabel_tbl.horizontalHeader().setSortIndicatorShown(True)
        self.posts_tabel_tbl.horizontalHeader().setStretchLastSection(True)
        self.posts_tabel_tbl.verticalHeader().setVisible(False)
        self.posts_tabel_tbl.verticalHeader().setCascadingSectionResizes(True)
        self.posts_tabel_tbl.verticalHeader().setSortIndicatorShown(True)
        self.posts_tabel_tbl.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.posts_tabel_tbl)
        self.bottom_buttons_wgt = QtWidgets.QWidget(posts_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_buttons_wgt.sizePolicy().hasHeightForWidth())
        self.bottom_buttons_wgt.setSizePolicy(sizePolicy)
        self.bottom_buttons_wgt.setMinimumSize(QtCore.QSize(400, 0))
        self.bottom_buttons_wgt.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bottom_buttons_wgt.setObjectName("bottom_buttons_wgt")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom_buttons_wgt)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_all_btn = QtWidgets.QPushButton(self.bottom_buttons_wgt)
        self.select_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_all_btn.setStyleSheet("QPushButton { \n"
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
        icon2.addPixmap(QtGui.QPixmap("images/selection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_all_btn.setIcon(icon2)
        self.select_all_btn.setObjectName("select_all_btn")
        self.horizontalLayout.addWidget(self.select_all_btn)
        self.unselect_all_btn = QtWidgets.QPushButton(self.bottom_buttons_wgt)
        self.unselect_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unselect_all_btn.setStyleSheet("QPushButton { \n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/eliminate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unselect_all_btn.setIcon(icon3)
        self.unselect_all_btn.setObjectName("unselect_all_btn")
        self.horizontalLayout.addWidget(self.unselect_all_btn)
        self.save_btn = QtWidgets.QPushButton(self.bottom_buttons_wgt)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon4)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout_2.addWidget(self.bottom_buttons_wgt)

        self.retranslateUi(posts_ui)
        QtCore.QMetaObject.connectSlotsByName(posts_ui)
        self.load_data()
        self.setup_buttons()

    def setup_buttons(self):
        self.select_all_btn.clicked.connect(self.select_all)
        self.unselect_all_btn.clicked.connect(self.unselect_all)
        self.save_btn.clicked.connect(self.save)
        self.addPosts_btn.clicked.connect(self.show_add_posts_ui)
        self.removePosts_btn.clicked.connect(self.show_remove_posts_ui)

    def load_data(self):
        try:
            users = open('users.json', 'r')
            data = dict(json.load(users))
            row_index = self.posts_tabel_tbl.rowCount()
            for row in range(0, row_index):
                self.posts_tabel_tbl.removeRow(0)
            for user_status in data[self.user]:
                if 'true' in user_status:
                    for post in data[self.user][user_status]:
                        for post_status in post:
                            row_index = self.posts_tabel_tbl.rowCount()
                            selected = post[post_status]
                            self.posts_tabel_tbl.insertRow(row_index)
                            check_box = QtWidgets.QTableWidgetItem()
                            check_box.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                            check_box.setCheckState(QtCore.Qt.Checked if selected else QtCore.Qt.Unchecked)
                            self.posts_tabel_tbl.setItem(row_index, 0, check_box)
                            self.posts_tabel_tbl.setItem(row_index, 1,
                                                         QtWidgets.QTableWidgetItem(str(post_status)))
        except FileNotFoundError:
            pass

    def select_all(self):
        # self.posts_tabel_tbl.setCol
        for row in range(0, self.posts_tabel_tbl.rowCount()):
            col = self.posts_tabel_tbl.item(row, 0)
            col.setCheckState(QtCore.Qt.Checked)

    def unselect_all(self):
        # self.posts_tabel_tbl.setCol
        for row in range(0, self.posts_tabel_tbl.rowCount()):
            col = self.posts_tabel_tbl.item(row, 0)
            col.setCheckState(QtCore.Qt.Unchecked)

    def save(self):
        new_data = []
        for row in range(0, self.posts_tabel_tbl.rowCount()):
            selected = True if self.posts_tabel_tbl.item(row, 0).checkState() == 2 else False
            post = self.posts_tabel_tbl.item(row, 1).text()
            new_data.append({post: selected})
        new_data = self.merge_data(new_data)
        with open('users.json', 'w') as file:
            file.write(json.dumps(new_data, indent=4))
            file.close()
        self.accept()

    def show_add_posts_ui(self):
        dlg = Ui_add_posts(self, self.user)
        if dlg.exec():
            self.load_data()

    def show_remove_posts_ui(self):
        dlg = Ui_remove_post(self, self.user)
        if dlg.exec():
            self.load_data()

    def merge_data(self, new_data: list) -> dict:
        try:
            previous_data = open('users.json', 'r')
            data = dict(json.load(previous_data))
            data[self.user]['true'] = new_data
            previous_data.close()
            return data
        except FileNotFoundError:
            return {}

    def retranslateUi(self, posts_ui):
        _translate = QtCore.QCoreApplication.translate
        posts_ui.setWindowTitle(_translate("posts_ui", "Posts"))
        self.addPosts_btn.setText(_translate("posts_ui", "Add Post"))
        self.removePosts_btn.setText(_translate("posts_ui", "Remove Post"))
        self.posts_tabel_tbl.setSortingEnabled(True)
        item = self.posts_tabel_tbl.horizontalHeaderItem(0)
        item.setText(_translate("posts_ui", "#"))
        item = self.posts_tabel_tbl.horizontalHeaderItem(1)
        item.setText(_translate("posts_ui", "Post"))
        self.select_all_btn.setText(_translate("posts_ui", "Select All"))
        self.unselect_all_btn.setText(_translate("posts_ui", "Unselect All"))
        self.save_btn.setText(_translate("posts_ui", "Save"))
