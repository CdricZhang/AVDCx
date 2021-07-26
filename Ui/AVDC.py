# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVDCATAvfp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AVDV(object):
    def setupUi(self, AVDV):
        if not AVDV.objectName():
            AVDV.setObjectName(u"AVDV")
        AVDV.resize(1024, 700)
        font = QFont()
        font.setFamily(u"Courier")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        AVDV.setFont(font)
        icon = QIcon()
        icon.addFile(u"../Img/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        AVDV.setWindowIcon(icon)
        self.centralwidget = QWidget(AVDV)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(240, 9, 780, 691))
        self.stackedWidget.setFont(font)
        self.page_avdc = QWidget()
        self.page_avdc.setObjectName(u"page_avdc")
        self.pushButton_start_cap = QPushButton(self.page_avdc)
        self.pushButton_start_cap.setObjectName(u"pushButton_start_cap")
        self.pushButton_start_cap.setGeometry(QRect(650, 13, 120, 40))
        self.pushButton_start_cap.setFont(font)
        self.label_number1 = QLabel(self.page_avdc)
        self.label_number1.setObjectName(u"label_number1")
        self.label_number1.setGeometry(QRect(0, 70, 50, 40))
        self.label_number1.setFont(font)
        self.label_number = QLabel(self.page_avdc)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setGeometry(QRect(50, 70, 161, 40))
        self.label_number.setFont(font)
        self.label_number.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_number.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"color:#336699")
        self.label_number.setFrameShape(QFrame.Box)
        self.label_number.setLineWidth(1)
        self.label_13 = QLabel(self.page_avdc)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 530, 50, 40))
        self.label_13.setFont(font)
        self.label_release = QLabel(self.page_avdc)
        self.label_release.setObjectName(u"label_release")
        self.label_release.setGeometry(QRect(50, 530, 220, 40))
        self.label_release.setFont(font)
        self.label_release.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_release.setFrameShape(QFrame.Box)
        self.label_actor1 = QLabel(self.page_avdc)
        self.label_actor1.setObjectName(u"label_actor1")
        self.label_actor1.setGeometry(QRect(220, 70, 50, 40))
        self.label_actor1.setFont(font)
        self.label_actor = QLabel(self.page_avdc)
        self.label_actor.setObjectName(u"label_actor")
        self.label_actor.setGeometry(QRect(270, 70, 161, 40))
        self.label_actor.setFont(font)
        self.label_actor.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"color:#336699")
        self.label_actor.setFrameShape(QFrame.Box)
        self.label_actor.setLineWidth(1)
        self.label_outline = QLabel(self.page_avdc)
        self.label_outline.setObjectName(u"label_outline")
        self.label_outline.setGeometry(QRect(50, 430, 500, 40))
        self.label_outline.setFont(font)
        self.label_outline.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_outline.setFrameShape(QFrame.Box)
        self.label_outline.setLineWidth(1)
        self.label_18 = QLabel(self.page_avdc)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 430, 50, 40))
        self.label_18.setFont(font)
        self.label_title = QLabel(self.page_avdc)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(50, 110, 500, 40))
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_title.setFrameShape(QFrame.Box)
        self.label_title.setLineWidth(1)
        self.label_title1 = QLabel(self.page_avdc)
        self.label_title1.setObjectName(u"label_title1")
        self.label_title1.setGeometry(QRect(0, 110, 50, 40))
        self.label_title1.setFont(font)
        self.label_director = QLabel(self.page_avdc)
        self.label_director.setObjectName(u"label_director")
        self.label_director.setGeometry(QRect(50, 580, 220, 40))
        self.label_director.setFont(font)
        self.label_director.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_director.setFrameShape(QFrame.Box)
        self.label_director.setLineWidth(1)
        self.label_publish = QLabel(self.page_avdc)
        self.label_publish.setObjectName(u"label_publish")
        self.label_publish.setGeometry(QRect(330, 630, 220, 40))
        self.label_publish.setFont(font)
        self.label_publish.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_publish.setFrameShape(QFrame.Box)
        self.label_23 = QLabel(self.page_avdc)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 580, 50, 40))
        self.label_23.setFont(font)
        self.label_24 = QLabel(self.page_avdc)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(280, 630, 50, 40))
        self.label_24.setFont(font)
        self.label_studio = QLabel(self.page_avdc)
        self.label_studio.setObjectName(u"label_studio")
        self.label_studio.setGeometry(QRect(50, 630, 220, 40))
        self.label_studio.setFont(font)
        self.label_studio.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_studio.setFrameShape(QFrame.Box)
        self.label_studio.setLineWidth(1)
        self.label_series = QLabel(self.page_avdc)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setGeometry(QRect(330, 580, 220, 40))
        self.label_series.setFont(font)
        self.label_series.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_series.setFrameShape(QFrame.Box)
        self.label_30 = QLabel(self.page_avdc)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 630, 50, 40))
        self.label_30.setFont(font)
        self.label_31 = QLabel(self.page_avdc)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(280, 580, 50, 40))
        self.label_31.setFont(font)
        self.label_tag = QLabel(self.page_avdc)
        self.label_tag.setObjectName(u"label_tag")
        self.label_tag.setGeometry(QRect(50, 480, 500, 40))
        self.label_tag.setFont(font)
        self.label_tag.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_tag.setFrameShape(QFrame.Box)
        self.label_tag.setLineWidth(1)
        self.label_33 = QLabel(self.page_avdc)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(0, 480, 50, 40))
        self.label_33.setFont(font)
        self.checkBox_cover = QCheckBox(self.page_avdc)
        self.checkBox_cover.setObjectName(u"checkBox_cover")
        self.checkBox_cover.setGeometry(QRect(50, 390, 330, 30))
        self.checkBox_cover.setFont(font)
        self.label_result = QLabel(self.page_avdc)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(580, 70, 201, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        self.label_result.setMinimumSize(QSize(0, 0))
        self.label_result.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Courier")
        font1.setBold(False)
        font1.setWeight(50)
        self.label_result.setFont(font1)
        self.label_result.setCursor(QCursor(Qt.ArrowCursor))
        self.label_result.setLayoutDirection(Qt.LeftToRight)
        self.label_result.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"background-color: rgb(246, 246, 246);\n"
"font-size:14px;")
        self.label_result.setFrameShape(QFrame.Box)
        self.label_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22 = QLabel(self.page_avdc)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(280, 530, 50, 40))
        self.label_22.setFont(font)
        self.label_runtime = QLabel(self.page_avdc)
        self.label_runtime.setObjectName(u"label_runtime")
        self.label_runtime.setGeometry(QRect(330, 530, 220, 40))
        self.label_runtime.setFont(font)
        self.label_runtime.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_runtime.setFrameShape(QFrame.Box)
        self.line_6 = QFrame(self.page_avdc)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(50, 460, 500, 20))
        self.line_6.setFont(font)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.page_avdc)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(50, 510, 500, 20))
        self.line_7.setFont(font)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.page_avdc)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(50, 560, 220, 20))
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_9 = QFrame(self.page_avdc)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(330, 560, 220, 20))
        self.line_9.setFont(font)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_10 = QFrame(self.page_avdc)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(330, 610, 220, 20))
        self.line_10.setFont(font)
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_11 = QFrame(self.page_avdc)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(330, 660, 220, 20))
        self.line_11.setFont(font)
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_12 = QFrame(self.page_avdc)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(50, 610, 220, 20))
        self.line_12.setFont(font)
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_13 = QFrame(self.page_avdc)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(50, 660, 220, 20))
        self.line_13.setFont(font)
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.label_thumb = QLabel(self.page_avdc)
        self.label_thumb.setObjectName(u"label_thumb")
        self.label_thumb.setEnabled(True)
        self.label_thumb.setGeometry(QRect(222, 160, 328, 220))
        self.label_thumb.setFont(font)
        self.label_thumb.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_thumb.setFrameShape(QFrame.Box)
        self.label_thumb.setAlignment(Qt.AlignCenter)
        self.label_thumb.setMargin(0)
        self.label_poster = QLabel(self.page_avdc)
        self.label_poster.setObjectName(u"label_poster")
        self.label_poster.setGeometry(QRect(50, 160, 156, 220))
        sizePolicy.setHeightForWidth(self.label_poster.sizePolicy().hasHeightForWidth())
        self.label_poster.setSizePolicy(sizePolicy)
        self.label_poster.setMinimumSize(QSize(156, 220))
        self.label_poster.setMaximumSize(QSize(156, 220))
        self.label_poster.setFont(font)
        self.label_poster.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_poster.setFrameShape(QFrame.Box)
        self.label_poster.setAlignment(Qt.AlignCenter)
        self.label_poster1 = QLabel(self.page_avdc)
        self.label_poster1.setObjectName(u"label_poster1")
        self.label_poster1.setGeometry(QRect(0, 150, 50, 40))
        self.label_poster1.setFont(font)
        self.treeWidget_number = QTreeWidget(self.page_avdc)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font2);
        __qtreewidgetitem.setBackground(0, QColor(85, 170, 255));
        __qtreewidgetitem.setForeground(0, brush);
        self.treeWidget_number.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget_number)
        QTreeWidgetItem(self.treeWidget_number)
        self.treeWidget_number.setObjectName(u"treeWidget_number")
        self.treeWidget_number.setGeometry(QRect(570, 110, 200, 561))
        self.treeWidget_number.setFont(font)
        self.treeWidget_number.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"background-color: rgb(246, 246, 246);")
        self.treeWidget_number.setFrameShape(QFrame.NoFrame)
        self.treeWidget_number.setFrameShadow(QFrame.Plain)
        self.treeWidget_number.setLineWidth(0)
        self.treeWidget_number.setItemsExpandable(True)
        self.treeWidget_number.setHeaderHidden(True)
        self.label_file_path = QLabel(self.page_avdc)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setGeometry(QRect(0, 10, 800, 50))
        self.label_file_path.setFont(font)
        self.label_file_path.setStyleSheet(u"")
        self.label_file_path.setFrameShape(QFrame.Box)
        self.line_14 = QFrame(self.page_avdc)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(0, 60, 771, 20))
        self.line_14.setFont(font)
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.label_source = QLabel(self.page_avdc)
        self.label_source.setObjectName(u"label_source")
        self.label_source.setGeometry(QRect(430, 70, 121, 40))
        self.label_source.setFont(font)
        self.label_source.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_source.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_source.setFrameShape(QFrame.Box)
        self.label_source.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_avdc)
        self.label_number1.raise_()
        self.label_number.raise_()
        self.label_13.raise_()
        self.label_release.raise_()
        self.label_actor1.raise_()
        self.label_actor.raise_()
        self.label_outline.raise_()
        self.label_18.raise_()
        self.label_title.raise_()
        self.label_title1.raise_()
        self.label_director.raise_()
        self.label_publish.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_studio.raise_()
        self.label_series.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_tag.raise_()
        self.label_33.raise_()
        self.checkBox_cover.raise_()
        self.label_22.raise_()
        self.label_runtime.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.line_13.raise_()
        self.label_thumb.raise_()
        self.label_poster.raise_()
        self.label_poster1.raise_()
        self.treeWidget_number.raise_()
        self.label_result.raise_()
        self.label_file_path.raise_()
        self.pushButton_start_cap.raise_()
        self.line_14.raise_()
        self.label_source.raise_()
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.textBrowser_log_main = QTextBrowser(self.page_log)
        self.textBrowser_log_main.setObjectName(u"textBrowser_log_main")
        self.textBrowser_log_main.setGeometry(QRect(0, 0, 780, 680))
        self.textBrowser_log_main.setStyleSheet(u"")
        self.pushButton_start_cap2 = QPushButton(self.page_log)
        self.pushButton_start_cap2.setObjectName(u"pushButton_start_cap2")
        self.pushButton_start_cap2.setGeometry(QRect(650, 13, 120, 40))
        self.pushButton_start_cap2.setFont(font)
        self.stackedWidget.addWidget(self.page_log)
        self.page_net = QWidget()
        self.page_net.setObjectName(u"page_net")
        self.textBrowser_net_main = QTextBrowser(self.page_net)
        self.textBrowser_net_main.setObjectName(u"textBrowser_net_main")
        self.textBrowser_net_main.setGeometry(QRect(0, 0, 780, 680))
        self.textBrowser_net_main.setStyleSheet(u"")
        self.pushButton_check_net = QPushButton(self.page_net)
        self.pushButton_check_net.setObjectName(u"pushButton_check_net")
        self.pushButton_check_net.setGeometry(QRect(650, 13, 120, 40))
        self.pushButton_check_net.setFont(font)
        self.stackedWidget.addWidget(self.page_net)
        self.page_tool = QWidget()
        self.page_tool.setObjectName(u"page_tool")
        self.groupBox_6 = QGroupBox(self.page_tool)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 10, 751, 121))
        font3 = QFont()
        font3.setFamily(u"Courier")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.groupBox_6.setFont(font3)
        self.groupBox_6.setStyleSheet(u"font:\"Courier\";")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 70, 511, 41))
        self.label_8.setFont(font3)
        self.pushButton_move_mp4 = QPushButton(self.groupBox_6)
        self.pushButton_move_mp4.setObjectName(u"pushButton_move_mp4")
        self.pushButton_move_mp4.setGeometry(QRect(10, 30, 200, 50))
        self.pushButton_move_mp4.setFont(font3)
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(230, 30, 80, 30))
        self.label_41.setFont(font3)
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_escape_dir_move = QLineEdit(self.groupBox_6)
        self.lineEdit_escape_dir_move.setObjectName(u"lineEdit_escape_dir_move")
        self.lineEdit_escape_dir_move.setGeometry(QRect(310, 30, 430, 30))
        self.lineEdit_escape_dir_move.setFont(font3)
        self.lineEdit_escape_dir_move.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.groupBox_7 = QGroupBox(self.page_tool)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 140, 751, 201))
        self.groupBox_7.setFont(font3)
        self.groupBox_7.setStyleSheet(u"font:\"Courier\";")
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 150, 511, 41))
        self.label.setFont(font3)
        self.pushButton_select_file = QPushButton(self.groupBox_7)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setGeometry(QRect(10, 30, 200, 50))
        self.pushButton_select_file.setFont(font3)
        self.comboBox_website = QComboBox(self.groupBox_7)
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.setObjectName(u"comboBox_website")
        self.comboBox_website.setGeometry(QRect(310, 110, 430, 30))
        self.comboBox_website.setFont(font3)
        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 110, 80, 30))
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_appoint_url = QLineEdit(self.groupBox_7)
        self.lineEdit_appoint_url.setObjectName(u"lineEdit_appoint_url")
        self.lineEdit_appoint_url.setGeometry(QRect(310, 70, 430, 30))
        self.lineEdit_appoint_url.setFont(font3)
        self.lineEdit_appoint_url.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 70, 80, 30))
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_movie_number = QLineEdit(self.groupBox_7)
        self.lineEdit_movie_number.setObjectName(u"lineEdit_movie_number")
        self.lineEdit_movie_number.setGeometry(QRect(310, 30, 430, 30))
        self.lineEdit_movie_number.setFont(font3)
        self.lineEdit_movie_number.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(230, 30, 80, 30))
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_start_single_file = QPushButton(self.groupBox_7)
        self.pushButton_start_single_file.setObjectName(u"pushButton_start_single_file")
        self.pushButton_start_single_file.setGeometry(QRect(10, 100, 200, 50))
        self.pushButton_start_single_file.setFont(font3)
        self.groupBox_12 = QGroupBox(self.page_tool)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 350, 751, 191))
        self.groupBox_12.setFont(font3)
        self.groupBox_12.setStyleSheet(u"font:\"Courier\";")
        self.pushButton_add_actor_pic = QPushButton(self.groupBox_12)
        self.pushButton_add_actor_pic.setObjectName(u"pushButton_add_actor_pic")
        self.pushButton_add_actor_pic.setGeometry(QRect(10, 30, 200, 50))
        self.pushButton_add_actor_pic.setFont(font3)
        self.lineEdit_emby_url = QLineEdit(self.groupBox_12)
        self.lineEdit_emby_url.setObjectName(u"lineEdit_emby_url")
        self.lineEdit_emby_url.setGeometry(QRect(310, 30, 430, 30))
        self.lineEdit_emby_url.setFont(font3)
        self.lineEdit_emby_url.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_3 = QLabel(self.groupBox_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 30, 80, 30))
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.groupBox_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 74, 80, 30))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_api_key = QLineEdit(self.groupBox_12)
        self.lineEdit_api_key.setObjectName(u"lineEdit_api_key")
        self.lineEdit_api_key.setGeometry(QRect(310, 70, 430, 30))
        self.lineEdit_api_key.setFont(font3)
        self.lineEdit_api_key.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_5 = QLabel(self.groupBox_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 110, 511, 71))
        self.label_5.setFont(font3)
        self.pushButton_show_pic_actor = QPushButton(self.groupBox_12)
        self.pushButton_show_pic_actor.setObjectName(u"pushButton_show_pic_actor")
        self.pushButton_show_pic_actor.setGeometry(QRect(10, 130, 200, 50))
        self.pushButton_show_pic_actor.setFont(font3)
        self.comboBox_pic_actor = QComboBox(self.groupBox_12)
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.setObjectName(u"comboBox_pic_actor")
        self.comboBox_pic_actor.setGeometry(QRect(10, 90, 200, 30))
        self.comboBox_pic_actor.setFont(font3)
        self.groupBox_13 = QGroupBox(self.page_tool)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(10, 550, 751, 111))
        self.groupBox_13.setFont(font3)
        self.groupBox_13.setStyleSheet(u"font:\"Courier\";")
        self.pushButton_select_thumb = QPushButton(self.groupBox_13)
        self.pushButton_select_thumb.setObjectName(u"pushButton_select_thumb")
        self.pushButton_select_thumb.setGeometry(QRect(10, 30, 200, 50))
        self.pushButton_select_thumb.setFont(font3)
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 20, 511, 71))
        self.label_6.setFont(font3)
        self.stackedWidget.addWidget(self.page_tool)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.tabWidget = QTabWidget(self.page_setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 771, 671))
        self.tabWidget.setFont(font3)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setIconSize(QSize(16, 20))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, -1, 771, 553))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 771, 1600))
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 110, 701, 101))
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.groupBox.setMaximumSize(QSize(739, 16777215))
        self.groupBox.setFont(font3)
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(60, 20, 641, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_common = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_common.setObjectName(u"radioButton_common")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radioButton_common.sizePolicy().hasHeightForWidth())
        self.radioButton_common.setSizePolicy(sizePolicy2)
        self.radioButton_common.setMinimumSize(QSize(80, 0))
        self.radioButton_common.setFont(font3)
        self.radioButton_common.setAutoRepeatDelay(300)

        self.gridLayout_2.addWidget(self.radioButton_common, 0, 0, 1, 1)

        self.radioButton_sort = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_sort.setObjectName(u"radioButton_sort")
        self.radioButton_sort.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton_sort, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamily(u"Courier")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_2.addWidget(self.label_15, 1, 1, 1, 1)

        self.groupBox_25 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setGeometry(QRect(30, 830, 701, 81))
        self.groupBox_25.setMinimumSize(QSize(200, 0))
        self.groupBox_25.setMaximumSize(QSize(739, 16777215))
        self.groupBox_25.setFont(font3)
        self.horizontalLayoutWidget_15 = QWidget(self.groupBox_25)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(60, 30, 641, 31))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.radioButton_zh_cn = QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_zh_cn.setObjectName(u"radioButton_zh_cn")
        self.radioButton_zh_cn.setFont(font3)

        self.horizontalLayout_18.addWidget(self.radioButton_zh_cn)

        self.radioButton_zh_tw = QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_zh_tw.setObjectName(u"radioButton_zh_tw")
        self.radioButton_zh_tw.setFont(font3)

        self.horizontalLayout_18.addWidget(self.radioButton_zh_tw)

        self.radioButton_ja = QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_ja.setObjectName(u"radioButton_ja")
        self.radioButton_ja.setFont(font3)

        self.horizontalLayout_18.addWidget(self.radioButton_ja)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 230, 701, 101))
        self.groupBox_5.setMinimumSize(QSize(200, 0))
        self.groupBox_5.setMaximumSize(QSize(739, 16777215))
        self.groupBox_5.setFont(font3)
        self.gridLayoutWidget = QWidget(self.groupBox_5)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 20, 641, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_like_speed = QRadioButton(self.gridLayoutWidget)
        self.radioButton_like_speed.setObjectName(u"radioButton_like_speed")
        sizePolicy2.setHeightForWidth(self.radioButton_like_speed.sizePolicy().hasHeightForWidth())
        self.radioButton_like_speed.setSizePolicy(sizePolicy2)
        self.radioButton_like_speed.setMinimumSize(QSize(80, 0))
        self.radioButton_like_speed.setFont(font3)
        self.radioButton_like_speed.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.radioButton_like_speed, 0, 0, 1, 1)

        self.radioButton_like_more = QRadioButton(self.gridLayoutWidget)
        self.radioButton_like_more.setObjectName(u"radioButton_like_more")
        self.radioButton_like_more.setFont(font3)

        self.gridLayout.addWidget(self.radioButton_like_more, 1, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy3.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy3)
        self.label_28.setFont(font4)
        self.label_28.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_32, 1, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(30, 10, 701, 81))
        self.groupBox_11.setFont(font3)
        self.groupBox_11.setStyleSheet(u"")
        self.comboBox_website_all = QComboBox(self.groupBox_11)
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.setObjectName(u"comboBox_website_all")
        self.comboBox_website_all.setGeometry(QRect(60, 30, 631, 40))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_website_all.sizePolicy().hasHeightForWidth())
        self.comboBox_website_all.setSizePolicy(sizePolicy4)
        self.comboBox_website_all.setMinimumSize(QSize(400, 40))
        self.comboBox_website_all.setMaximumSize(QSize(16000, 40))
        self.comboBox_website_all.setSizeIncrement(QSize(0, 0))
        self.comboBox_website_all.setFont(font3)
        self.comboBox_website_all.setStyleSheet(u"")
        self.comboBox_website_all.setFrame(False)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 350, 701, 101))
        self.groupBox_2.setMinimumSize(QSize(200, 0))
        self.groupBox_2.setMaximumSize(QSize(739, 16777215))
        self.groupBox_2.setFont(font3)
        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(60, 20, 641, 80))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.gridLayoutWidget_4)
        self.label_36.setObjectName(u"label_36")
        sizePolicy3.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy3)
        self.label_36.setFont(font4)
        self.label_36.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_4.addWidget(self.label_36, 0, 1, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_4)
        self.label_37.setObjectName(u"label_37")
        sizePolicy3.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy3)
        self.label_37.setFont(font4)
        self.label_37.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_4.addWidget(self.label_37, 1, 1, 1, 1)

        self.radioButton_soft_on = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_soft_on.setObjectName(u"radioButton_soft_on")
        sizePolicy2.setHeightForWidth(self.radioButton_soft_on.sizePolicy().hasHeightForWidth())
        self.radioButton_soft_on.setSizePolicy(sizePolicy2)
        self.radioButton_soft_on.setMinimumSize(QSize(80, 0))
        self.radioButton_soft_on.setFont(font3)

        self.gridLayout_4.addWidget(self.radioButton_soft_on, 0, 0, 1, 1)

        self.radioButton_soft_off = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_soft_off.setObjectName(u"radioButton_soft_off")
        self.radioButton_soft_off.setFont(font3)

        self.gridLayout_4.addWidget(self.radioButton_soft_off, 1, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(30, 710, 701, 101))
        self.groupBox_18.setMinimumSize(QSize(200, 0))
        self.groupBox_18.setMaximumSize(QSize(739, 16777215))
        self.groupBox_18.setFont(font3)
        self.gridLayoutWidget_13 = QWidget(self.groupBox_18)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(60, 20, 641, 80))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.gridLayoutWidget_13)
        self.label_38.setObjectName(u"label_38")
        sizePolicy3.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy3)
        self.label_38.setFont(font4)
        self.label_38.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_13.addWidget(self.label_38, 0, 1, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_13)
        self.label_39.setObjectName(u"label_39")
        sizePolicy3.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy3)
        self.label_39.setFont(font4)
        self.label_39.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_13.addWidget(self.label_39, 1, 1, 1, 1)

        self.radioButton_succ_rename_on = QRadioButton(self.gridLayoutWidget_13)
        self.radioButton_succ_rename_on.setObjectName(u"radioButton_succ_rename_on")
        sizePolicy2.setHeightForWidth(self.radioButton_succ_rename_on.sizePolicy().hasHeightForWidth())
        self.radioButton_succ_rename_on.setSizePolicy(sizePolicy2)
        self.radioButton_succ_rename_on.setMinimumSize(QSize(80, 0))
        self.radioButton_succ_rename_on.setFont(font3)

        self.gridLayout_13.addWidget(self.radioButton_succ_rename_on, 0, 0, 1, 1)

        self.radioButton_succ_rename_off = QRadioButton(self.gridLayoutWidget_13)
        self.radioButton_succ_rename_off.setObjectName(u"radioButton_succ_rename_off")
        self.radioButton_succ_rename_off.setFont(font3)

        self.gridLayout_13.addWidget(self.radioButton_succ_rename_off, 1, 0, 1, 1)

        self.groupBox_27 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setGeometry(QRect(30, 470, 701, 101))
        self.groupBox_27.setMinimumSize(QSize(200, 0))
        self.groupBox_27.setMaximumSize(QSize(739, 16777215))
        self.groupBox_27.setFont(font3)
        self.gridLayoutWidget_6 = QWidget(self.groupBox_27)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(60, 20, 641, 80))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.gridLayoutWidget_6)
        self.label_54.setObjectName(u"label_54")
        sizePolicy3.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy3)
        self.label_54.setFont(font4)
        self.label_54.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_6.addWidget(self.label_54, 0, 1, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_6)
        self.label_55.setObjectName(u"label_55")
        sizePolicy3.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy3)
        self.label_55.setFont(font4)
        self.label_55.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_6.addWidget(self.label_55, 1, 1, 1, 1)

        self.radioButton_succ_move_on = QRadioButton(self.gridLayoutWidget_6)
        self.radioButton_succ_move_on.setObjectName(u"radioButton_succ_move_on")
        sizePolicy2.setHeightForWidth(self.radioButton_succ_move_on.sizePolicy().hasHeightForWidth())
        self.radioButton_succ_move_on.setSizePolicy(sizePolicy2)
        self.radioButton_succ_move_on.setMinimumSize(QSize(80, 0))
        self.radioButton_succ_move_on.setFont(font3)

        self.gridLayout_6.addWidget(self.radioButton_succ_move_on, 0, 0, 1, 1)

        self.radioButton_succ_move_off = QRadioButton(self.gridLayoutWidget_6)
        self.radioButton_succ_move_off.setObjectName(u"radioButton_succ_move_off")
        self.radioButton_succ_move_off.setFont(font3)

        self.gridLayout_6.addWidget(self.radioButton_succ_move_off, 1, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(30, 590, 701, 101))
        self.groupBox_15.setMinimumSize(QSize(200, 0))
        self.groupBox_15.setMaximumSize(QSize(739, 16777215))
        self.groupBox_15.setFont(font3)
        self.gridLayoutWidget_3 = QWidget(self.groupBox_15)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(60, 20, 641, 80))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")
        sizePolicy3.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy3)
        self.label_34.setFont(font4)
        self.label_34.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_3.addWidget(self.label_34, 0, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_3)
        self.label_35.setObjectName(u"label_35")
        sizePolicy3.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy3)
        self.label_35.setFont(font4)
        self.label_35.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_3.addWidget(self.label_35, 1, 1, 1, 1)

        self.radioButton_fail_move_on = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_fail_move_on.setObjectName(u"radioButton_fail_move_on")
        sizePolicy2.setHeightForWidth(self.radioButton_fail_move_on.sizePolicy().hasHeightForWidth())
        self.radioButton_fail_move_on.setSizePolicy(sizePolicy2)
        self.radioButton_fail_move_on.setMinimumSize(QSize(80, 0))
        self.radioButton_fail_move_on.setFont(font3)

        self.gridLayout_3.addWidget(self.radioButton_fail_move_on, 0, 0, 1, 1)

        self.radioButton_fail_move_off = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_fail_move_off.setObjectName(u"radioButton_fail_move_off")
        self.radioButton_fail_move_off.setFont(font3)

        self.gridLayout_3.addWidget(self.radioButton_fail_move_off, 1, 0, 1, 1)

        self.groupBox_31 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setGeometry(QRect(30, 1090, 701, 151))
        self.groupBox_31.setFont(font3)
        self.groupBox_31.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_14 = QWidget(self.groupBox_31)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(10, 30, 681, 111))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.radioButton_youdao = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_youdao.setObjectName(u"radioButton_youdao")
        self.radioButton_youdao.setMinimumSize(QSize(93, 30))
        self.radioButton_youdao.setFont(font3)

        self.horizontalLayout_20.addWidget(self.radioButton_youdao)

        self.radioButton_deepl = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_deepl.setObjectName(u"radioButton_deepl")
        self.radioButton_deepl.setMinimumSize(QSize(93, 30))
        self.radioButton_deepl.setFont(font3)

        self.horizontalLayout_20.addWidget(self.radioButton_deepl)


        self.gridLayout_14.addLayout(self.horizontalLayout_20, 0, 1, 1, 1)

        self.label_81 = QLabel(self.gridLayoutWidget_14)
        self.label_81.setObjectName(u"label_81")
        sizePolicy2.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy2)
        self.label_81.setMinimumSize(QSize(130, 30))
        self.label_81.setFont(font3)
        self.label_81.setLayoutDirection(Qt.LeftToRight)
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_81, 0, 0, 1, 1)

        self.label_80 = QLabel(self.gridLayoutWidget_14)
        self.label_80.setObjectName(u"label_80")
        sizePolicy2.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy2)
        self.label_80.setMinimumSize(QSize(130, 30))
        self.label_80.setFont(font3)
        self.label_80.setLayoutDirection(Qt.LeftToRight)
        self.label_80.setFrameShape(QFrame.NoFrame)
        self.label_80.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_80, 1, 0, 1, 1)

        self.lineEdit_deepl_key = QLineEdit(self.gridLayoutWidget_14)
        self.lineEdit_deepl_key.setObjectName(u"lineEdit_deepl_key")
        sizePolicy3.setHeightForWidth(self.lineEdit_deepl_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_deepl_key.setSizePolicy(sizePolicy3)
        self.lineEdit_deepl_key.setMinimumSize(QSize(300, 30))
        self.lineEdit_deepl_key.setFont(font3)
        self.lineEdit_deepl_key.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_14.addWidget(self.lineEdit_deepl_key, 1, 1, 1, 1)

        self.label_60 = QLabel(self.gridLayoutWidget_14)
        self.label_60.setObjectName(u"label_60")
        sizePolicy3.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy3)
        self.label_60.setFont(font4)
        self.label_60.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_14.addWidget(self.label_60, 2, 1, 1, 1)

        self.groupBox_24 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(30, 1380, 701, 81))
        self.groupBox_24.setMinimumSize(QSize(500, 0))
        self.groupBox_24.setFont(font3)
        self.horizontalLayoutWidget_14 = QWidget(self.groupBox_24)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(59, 30, 641, 31))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_download_poster = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_poster.setObjectName(u"checkBox_download_poster")
        self.checkBox_download_poster.setFont(font3)

        self.horizontalLayout_16.addWidget(self.checkBox_download_poster)

        self.checkBox_download_thumb = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_thumb.setObjectName(u"checkBox_download_thumb")
        self.checkBox_download_thumb.setFont(font3)

        self.horizontalLayout_16.addWidget(self.checkBox_download_thumb)

        self.checkBox_download_fanart = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_fanart.setObjectName(u"checkBox_download_fanart")
        self.checkBox_download_fanart.setFont(font3)

        self.horizontalLayout_16.addWidget(self.checkBox_download_fanart)

        self.checkBox_download_extrafanart = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_extrafanart.setObjectName(u"checkBox_download_extrafanart")
        self.checkBox_download_extrafanart.setFont(font3)

        self.horizontalLayout_16.addWidget(self.checkBox_download_extrafanart)

        self.checkBox_download_extrafanart_copy = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_extrafanart_copy.setObjectName(u"checkBox_download_extrafanart_copy")
        self.checkBox_download_extrafanart_copy.setFont(font3)

        self.horizontalLayout_16.addWidget(self.checkBox_download_extrafanart_copy)

        self.checkBox_download_nfo = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_nfo.setObjectName(u"checkBox_download_nfo")
        self.checkBox_download_nfo.setFont(font3)

        self.horizontalLayout_16.addWidget(self.checkBox_download_nfo)

        self.groupBox_39 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setGeometry(QRect(30, 1480, 701, 101))
        self.groupBox_39.setFont(font3)
        self.groupBox_39.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_5 = QWidget(self.groupBox_39)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(60, 20, 641, 81))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.radioButton_poster_cut = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_poster_cut.setObjectName(u"radioButton_poster_cut")
        self.radioButton_poster_cut.setMinimumSize(QSize(100, 30))
        font5 = QFont()
        font5.setFamily(u"Courier")
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.radioButton_poster_cut.setFont(font5)

        self.gridLayout_5.addWidget(self.radioButton_poster_cut, 0, 0, 1, 1)

        self.radioButton_poster_official = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_poster_official.setObjectName(u"radioButton_poster_official")
        sizePolicy2.setHeightForWidth(self.radioButton_poster_official.sizePolicy().hasHeightForWidth())
        self.radioButton_poster_official.setSizePolicy(sizePolicy2)
        self.radioButton_poster_official.setMinimumSize(QSize(100, 30))
        self.radioButton_poster_official.setFont(font3)

        self.gridLayout_5.addWidget(self.radioButton_poster_official, 1, 0, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget_5)
        self.label_52.setObjectName(u"label_52")
        sizePolicy3.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy3)
        self.label_52.setFont(font4)
        self.label_52.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_52, 1, 1, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget_5)
        self.label_53.setObjectName(u"label_53")
        sizePolicy3.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy3)
        self.label_53.setFont(font4)
        self.label_53.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_53, 0, 1, 1, 1)

        self.groupBox_26 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(30, 930, 701, 141))
        self.groupBox_26.setMinimumSize(QSize(200, 0))
        self.groupBox_26.setMaximumSize(QSize(739, 16777215))
        self.groupBox_26.setFont(font3)
        self.horizontalLayoutWidget_17 = QWidget(self.groupBox_26)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(60, 30, 641, 31))
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.checkBox_translate_title = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_translate_title.setObjectName(u"checkBox_translate_title")
        self.checkBox_translate_title.setFont(font3)

        self.horizontalLayout_22.addWidget(self.checkBox_translate_title)

        self.checkBox_translate_outline = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_translate_outline.setObjectName(u"checkBox_translate_outline")
        self.checkBox_translate_outline.setFont(font3)

        self.horizontalLayout_22.addWidget(self.checkBox_translate_outline)

        self.checkBox_translate_actor = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_translate_actor.setObjectName(u"checkBox_translate_actor")
        self.checkBox_translate_actor.setFont(font3)

        self.horizontalLayout_22.addWidget(self.checkBox_translate_actor)

        self.checkBox_translate_tag = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_translate_tag.setObjectName(u"checkBox_translate_tag")
        self.checkBox_translate_tag.setFont(font3)

        self.horizontalLayout_22.addWidget(self.checkBox_translate_tag)

        self.label_74 = QLabel(self.groupBox_26)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(60, 70, 611, 51))
        sizePolicy3.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy3)
        self.label_74.setFont(font4)
        self.label_74.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_33 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setGeometry(QRect(30, 1260, 701, 101))
        self.groupBox_33.setMinimumSize(QSize(500, 0))
        self.groupBox_33.setFont(font3)
        self.horizontalLayoutWidget_18 = QWidget(self.groupBox_33)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(59, 30, 641, 31))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.checkBox_old_poster = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_poster.setObjectName(u"checkBox_old_poster")
        self.checkBox_old_poster.setFont(font3)

        self.horizontalLayout_23.addWidget(self.checkBox_old_poster)

        self.checkBox_old_thumb = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_thumb.setObjectName(u"checkBox_old_thumb")
        self.checkBox_old_thumb.setFont(font3)

        self.horizontalLayout_23.addWidget(self.checkBox_old_thumb)

        self.checkBox_old_fanart = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_fanart.setObjectName(u"checkBox_old_fanart")
        self.checkBox_old_fanart.setFont(font3)

        self.horizontalLayout_23.addWidget(self.checkBox_old_fanart)

        self.checkBox_old_extrafanart = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_extrafanart.setObjectName(u"checkBox_old_extrafanart")
        self.checkBox_old_extrafanart.setFont(font3)

        self.horizontalLayout_23.addWidget(self.checkBox_old_extrafanart)

        self.checkBox_old_extrafanart_copy = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_extrafanart_copy.setObjectName(u"checkBox_old_extrafanart_copy")
        self.checkBox_old_extrafanart_copy.setFont(font3)

        self.horizontalLayout_23.addWidget(self.checkBox_old_extrafanart_copy)

        self.checkBox_old_nfo = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_nfo.setObjectName(u"checkBox_old_nfo")
        self.checkBox_old_nfo.setFont(font3)

        self.horizontalLayout_23.addWidget(self.checkBox_old_nfo)

        self.label_79 = QLabel(self.groupBox_33)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(60, 60, 631, 31))
        sizePolicy3.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy3)
        self.label_79.setFont(font4)
        self.label_79.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.scrollArea_2 = QScrollArea(self.tab2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, 0, 771, 553))
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 769, 1300))
        self.groupBox_16 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(30, 10, 701, 381))
        self.groupBox_16.setFont(font3)
        self.groupBox_16.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_7 = QWidget(self.groupBox_16)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 30, 681, 341))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.gridLayoutWidget_7)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setMinimumSize(QSize(160, 30))
        self.label_50.setFont(font3)
        self.label_50.setLayoutDirection(Qt.LeftToRight)
        self.label_50.setFrameShape(QFrame.NoFrame)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_50, 8, 0, 1, 1)

        self.label_58 = QLabel(self.gridLayoutWidget_7)
        self.label_58.setObjectName(u"label_58")
        sizePolicy3.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy3)
        self.label_58.setFont(font4)
        self.label_58.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_58, 7, 1, 1, 1)

        self.lineEdit_fail = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_fail.setObjectName(u"lineEdit_fail")
        sizePolicy3.setHeightForWidth(self.lineEdit_fail.sizePolicy().hasHeightForWidth())
        self.lineEdit_fail.setSizePolicy(sizePolicy3)
        self.lineEdit_fail.setMinimumSize(QSize(300, 30))
        self.lineEdit_fail.setFont(font3)
        self.lineEdit_fail.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_fail, 4, 1, 1, 1)

        self.lineEdit_extrafanart_dir = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_extrafanart_dir.setObjectName(u"lineEdit_extrafanart_dir")
        sizePolicy3.setHeightForWidth(self.lineEdit_extrafanart_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_extrafanart_dir.setSizePolicy(sizePolicy3)
        self.lineEdit_extrafanart_dir.setMinimumSize(QSize(300, 30))
        self.lineEdit_extrafanart_dir.setFont(font3)
        self.lineEdit_extrafanart_dir.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_extrafanart_dir, 8, 1, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_7)
        self.label_47.setObjectName(u"label_47")
        sizePolicy2.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy2)
        self.label_47.setMinimumSize(QSize(160, 30))
        self.label_47.setFont(font3)
        self.label_47.setLayoutDirection(Qt.LeftToRight)
        self.label_47.setFrameShape(QFrame.NoFrame)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_47, 2, 0, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_7)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setMinimumSize(QSize(160, 30))
        self.label_48.setFont(font3)
        self.label_48.setLayoutDirection(Qt.LeftToRight)
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_48, 6, 0, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_7)
        self.label_49.setObjectName(u"label_49")
        sizePolicy2.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy2)
        self.label_49.setMinimumSize(QSize(160, 30))
        self.label_49.setFont(font3)
        self.label_49.setLayoutDirection(Qt.LeftToRight)
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_59 = QLabel(self.gridLayoutWidget_7)
        self.label_59.setObjectName(u"label_59")
        sizePolicy3.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy3)
        self.label_59.setFont(font4)
        self.label_59.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_59, 9, 1, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget_7)
        self.label_56.setObjectName(u"label_56")
        sizePolicy3.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy3)
        self.label_56.setFont(font4)
        self.label_56.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_56, 1, 1, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_7)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)
        self.label_46.setMinimumSize(QSize(160, 30))
        self.label_46.setFont(font3)
        self.label_46.setLayoutDirection(Qt.LeftToRight)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_46, 4, 0, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_7)
        self.label_57.setObjectName(u"label_57")
        sizePolicy3.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy3)
        self.label_57.setFont(font4)
        self.label_57.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_57, 5, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_7)
        self.label_29.setObjectName(u"label_29")
        sizePolicy3.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy3)
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_29, 3, 1, 1, 1)

        self.lineEdit_movie_path = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_movie_path.setObjectName(u"lineEdit_movie_path")
        sizePolicy3.setHeightForWidth(self.lineEdit_movie_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_path.setSizePolicy(sizePolicy3)
        self.lineEdit_movie_path.setMinimumSize(QSize(300, 30))
        self.lineEdit_movie_path.setFont(font3)
        self.lineEdit_movie_path.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_movie_path, 0, 1, 1, 1)

        self.lineEdit_escape_dir = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_escape_dir.setObjectName(u"lineEdit_escape_dir")
        sizePolicy3.setHeightForWidth(self.lineEdit_escape_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_dir.setSizePolicy(sizePolicy3)
        self.lineEdit_escape_dir.setMinimumSize(QSize(300, 30))
        self.lineEdit_escape_dir.setFont(font3)
        self.lineEdit_escape_dir.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_escape_dir, 6, 1, 1, 1)

        self.lineEdit_success = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_success.setObjectName(u"lineEdit_success")
        sizePolicy3.setHeightForWidth(self.lineEdit_success.sizePolicy().hasHeightForWidth())
        self.lineEdit_success.setSizePolicy(sizePolicy3)
        self.lineEdit_success.setMinimumSize(QSize(300, 30))
        self.lineEdit_success.setFont(font3)
        self.lineEdit_success.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_success, 2, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(30, 410, 701, 521))
        self.groupBox_8.setFont(font3)
        self.groupBox_8.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_8 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 30, 681, 481))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_local_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_local_name.setObjectName(u"lineEdit_local_name")
        self.lineEdit_local_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_local_name.setFont(font3)
        self.lineEdit_local_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_local_name, 6, 1, 1, 1)

        self.label_62 = QLabel(self.gridLayoutWidget_8)
        self.label_62.setObjectName(u"label_62")
        sizePolicy3.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy3)
        self.label_62.setFont(font4)
        self.label_62.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_62, 9, 1, 1, 1)

        self.label_69 = QLabel(self.gridLayoutWidget_8)
        self.label_69.setObjectName(u"label_69")
        sizePolicy3.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy3)
        self.label_69.setFont(font4)
        self.label_69.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_69, 3, 1, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton_foldername_C_on = QRadioButton(self.gridLayoutWidget_8)
        self.radioButton_foldername_C_on.setObjectName(u"radioButton_foldername_C_on")
        sizePolicy3.setHeightForWidth(self.radioButton_foldername_C_on.sizePolicy().hasHeightForWidth())
        self.radioButton_foldername_C_on.setSizePolicy(sizePolicy3)
        self.radioButton_foldername_C_on.setMinimumSize(QSize(0, 30))
        self.radioButton_foldername_C_on.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_foldername_C_on.setFont(font3)
        self.radioButton_foldername_C_on.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.radioButton_foldername_C_on)

        self.radioButton_foldername_C_off = QRadioButton(self.gridLayoutWidget_8)
        self.radioButton_foldername_C_off.setObjectName(u"radioButton_foldername_C_off")
        sizePolicy3.setHeightForWidth(self.radioButton_foldername_C_off.sizePolicy().hasHeightForWidth())
        self.radioButton_foldername_C_off.setSizePolicy(sizePolicy3)
        self.radioButton_foldername_C_off.setMinimumSize(QSize(0, 30))
        self.radioButton_foldername_C_off.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_foldername_C_off.setFont(font3)

        self.horizontalLayout_21.addWidget(self.radioButton_foldername_C_off)


        self.gridLayout_8.addLayout(self.horizontalLayout_21, 2, 1, 1, 1)

        self.label_63 = QLabel(self.gridLayoutWidget_8)
        self.label_63.setObjectName(u"label_63")
        sizePolicy2.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy2)
        self.label_63.setMinimumSize(QSize(160, 30))
        self.label_63.setFont(font3)
        self.label_63.setLayoutDirection(Qt.LeftToRight)
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_63, 6, 0, 1, 1)

        self.lineEdit_dir_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_dir_name.setObjectName(u"lineEdit_dir_name")
        self.lineEdit_dir_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_dir_name.setFont(font3)
        self.lineEdit_dir_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_dir_name, 0, 1, 1, 1)

        self.label_68 = QLabel(self.gridLayoutWidget_8)
        self.label_68.setObjectName(u"label_68")
        sizePolicy3.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy3)
        self.label_68.setFont(font4)
        self.label_68.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_68, 5, 1, 1, 1)

        self.label_71 = QLabel(self.gridLayoutWidget_8)
        self.label_71.setObjectName(u"label_71")
        sizePolicy2.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy2)
        self.label_71.setMinimumSize(QSize(160, 30))
        self.label_71.setFont(font3)
        self.label_71.setLayoutDirection(Qt.LeftToRight)
        self.label_71.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_71, 8, 0, 1, 1)

        self.label_67 = QLabel(self.gridLayoutWidget_8)
        self.label_67.setObjectName(u"label_67")
        sizePolicy2.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy2)
        self.label_67.setMinimumSize(QSize(160, 30))
        self.label_67.setFont(font3)
        self.label_67.setLayoutDirection(Qt.LeftToRight)
        self.label_67.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_67, 4, 0, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget_8)
        self.label_61.setObjectName(u"label_61")
        sizePolicy3.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy3)
        self.label_61.setFont(font4)
        self.label_61.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_61, 7, 1, 1, 1)

        self.label_66 = QLabel(self.gridLayoutWidget_8)
        self.label_66.setObjectName(u"label_66")
        sizePolicy3.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy3)
        self.label_66.setFont(font4)
        self.label_66.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_66, 1, 1, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_8)
        self.label_43.setObjectName(u"label_43")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy5)
        self.label_43.setMinimumSize(QSize(160, 30))
        self.label_43.setFont(font3)
        self.label_43.setLayoutDirection(Qt.RightToLeft)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_51 = QLabel(self.gridLayoutWidget_8)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setMinimumSize(QSize(160, 30))
        self.label_51.setFont(font3)
        self.label_51.setLayoutDirection(Qt.RightToLeft)
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_51, 2, 0, 1, 1)

        self.lineEdit_media_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_media_name.setObjectName(u"lineEdit_media_name")
        self.lineEdit_media_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_media_name.setFont(font3)
        self.lineEdit_media_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_media_name, 4, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_20 = QGroupBox(self.gridLayoutWidget_8)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setStyleSheet(u"border:0px solid rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.radioButton_del_actor_on = QRadioButton(self.groupBox_20)
        self.radioButton_del_actor_on.setObjectName(u"radioButton_del_actor_on")
        self.radioButton_del_actor_on.setGeometry(QRect(0, 0, 508, 31))
        self.radioButton_del_actor_on.setAutoExclusive(True)
        self.radioButton_del_actor_off = QRadioButton(self.groupBox_20)
        self.radioButton_del_actor_off.setObjectName(u"radioButton_del_actor_off")
        self.radioButton_del_actor_off.setGeometry(QRect(250, 0, 508, 23))
        self.radioButton_del_actor_off.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.groupBox_20)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 8, 1, 1, 1)

        self.groupBox_32 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setGeometry(QRect(30, 1150, 701, 121))
        self.groupBox_32.setFont(font3)
        self.groupBox_32.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_11 = QWidget(self.groupBox_32)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(0, 30, 681, 81))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.gridLayoutWidget_11)
        self.label_72.setObjectName(u"label_72")
        sizePolicy2.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy2)
        self.label_72.setMinimumSize(QSize(160, 30))
        self.label_72.setFont(font3)
        self.label_72.setLayoutDirection(Qt.LeftToRight)
        self.label_72.setFrameShape(QFrame.NoFrame)
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_72, 1, 0, 1, 1)

        self.label_76 = QLabel(self.gridLayoutWidget_11)
        self.label_76.setObjectName(u"label_76")
        sizePolicy2.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy2)
        self.label_76.setMinimumSize(QSize(160, 30))
        self.label_76.setFont(font3)
        self.label_76.setLayoutDirection(Qt.LeftToRight)
        self.label_76.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_76, 0, 0, 1, 1)

        self.lineEdit_escape_char = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_escape_char.setObjectName(u"lineEdit_escape_char")
        sizePolicy4.setHeightForWidth(self.lineEdit_escape_char.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_char.setSizePolicy(sizePolicy4)
        self.lineEdit_escape_char.setMinimumSize(QSize(500, 30))
        self.lineEdit_escape_char.setMaximumSize(QSize(540, 16777215))
        self.lineEdit_escape_char.setFont(font3)
        self.lineEdit_escape_char.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_11.addWidget(self.lineEdit_escape_char, 0, 1, 1, 1)

        self.lineEdit_escape_string = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_escape_string.setObjectName(u"lineEdit_escape_string")
        sizePolicy4.setHeightForWidth(self.lineEdit_escape_string.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_string.setSizePolicy(sizePolicy4)
        self.lineEdit_escape_string.setMinimumSize(QSize(500, 30))
        self.lineEdit_escape_string.setMaximumSize(QSize(540, 16777215))
        self.lineEdit_escape_string.setFont(font3)
        self.lineEdit_escape_string.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_11.addWidget(self.lineEdit_escape_string, 1, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(30, 950, 701, 181))
        self.groupBox_9.setFont(font3)
        self.groupBox_9.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_12 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(0, 30, 681, 141))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.gridLayoutWidget_12)
        self.label_77.setObjectName(u"label_77")
        sizePolicy2.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy2)
        self.label_77.setMinimumSize(QSize(160, 30))
        self.label_77.setFont(font3)
        self.label_77.setLayoutDirection(Qt.LeftToRight)
        self.label_77.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_77, 1, 0, 1, 1)

        self.lineEdit_uncensored_prefix = QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_uncensored_prefix.setObjectName(u"lineEdit_uncensored_prefix")
        sizePolicy4.setHeightForWidth(self.lineEdit_uncensored_prefix.sizePolicy().hasHeightForWidth())
        self.lineEdit_uncensored_prefix.setSizePolicy(sizePolicy4)
        self.lineEdit_uncensored_prefix.setMinimumSize(QSize(500, 30))
        self.lineEdit_uncensored_prefix.setMaximumSize(QSize(540, 16777215))
        self.lineEdit_uncensored_prefix.setFont(font3)
        self.lineEdit_uncensored_prefix.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_12.addWidget(self.lineEdit_uncensored_prefix, 2, 1, 1, 1)

        self.label_78 = QLabel(self.gridLayoutWidget_12)
        self.label_78.setObjectName(u"label_78")
        sizePolicy2.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy2)
        self.label_78.setMinimumSize(QSize(160, 30))
        self.label_78.setFont(font3)
        self.label_78.setLayoutDirection(Qt.LeftToRight)
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_78, 2, 0, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget_12)
        self.label_44.setObjectName(u"label_44")
        sizePolicy5.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy5)
        self.label_44.setMinimumSize(QSize(160, 30))
        self.label_44.setFont(font3)
        self.label_44.setLayoutDirection(Qt.RightToLeft)
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_44, 0, 0, 1, 1)

        self.lineEdit_movie_type = QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_movie_type.setObjectName(u"lineEdit_movie_type")
        sizePolicy3.setHeightForWidth(self.lineEdit_movie_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_type.setSizePolicy(sizePolicy3)
        self.lineEdit_movie_type.setMinimumSize(QSize(300, 30))
        self.lineEdit_movie_type.setFont(font3)
        self.lineEdit_movie_type.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_12.addWidget(self.lineEdit_movie_type, 0, 1, 1, 1)

        self.lineEdit_sub_type = QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_sub_type.setObjectName(u"lineEdit_sub_type")
        sizePolicy3.setHeightForWidth(self.lineEdit_sub_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_sub_type.setSizePolicy(sizePolicy3)
        self.lineEdit_sub_type.setMinimumSize(QSize(300, 30))
        self.lineEdit_sub_type.setFont(font3)
        self.lineEdit_sub_type.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_12.addWidget(self.lineEdit_sub_type, 1, 1, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.scrollArea_3 = QScrollArea(self.tab3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(-1, -1, 771, 553))
        self.scrollArea_3.setFrameShape(QFrame.Box)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 771, 553))
        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(30, 270, 701, 281))
        self.groupBox_10.setFont(font3)
        self.groupBox_10.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_10 = QWidget(self.groupBox_10)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 30, 681, 131))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_cookie_javdb = QPlainTextEdit(self.gridLayoutWidget_10)
        self.plainTextEdit_cookie_javdb.setObjectName(u"plainTextEdit_cookie_javdb")
        self.plainTextEdit_cookie_javdb.setMinimumSize(QSize(300, 80))
        self.plainTextEdit_cookie_javdb.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 1px;\n"
"font: \"Courier\";")

        self.gridLayout_10.addWidget(self.plainTextEdit_cookie_javdb, 0, 1, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget_10)
        self.label_45.setObjectName(u"label_45")
        sizePolicy5.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy5)
        self.label_45.setMinimumSize(QSize(160, 30))
        self.label_45.setFont(font3)
        self.label_45.setLayoutDirection(Qt.RightToLeft)
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_45, 0, 0, 1, 1)

        self.label_75 = QLabel(self.groupBox_10)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(10, 170, 691, 91))
        sizePolicy3.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy3)
        self.label_75.setFont(font4)
        self.label_75.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_75.setScaledContents(True)
        self.groupBox_28 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setGeometry(QRect(30, 10, 701, 241))
        self.groupBox_28.setFont(font3)
        self.groupBox_28.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_9 = QWidget(self.groupBox_28)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(0, 30, 681, 201))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.gridLayoutWidget_9)
        self.label_65.setObjectName(u"label_65")
        sizePolicy2.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy2)
        self.label_65.setMinimumSize(QSize(160, 30))
        self.label_65.setFont(font3)
        self.label_65.setLayoutDirection(Qt.LeftToRight)
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_65, 3, 0, 1, 1)

        self.label_73 = QLabel(self.gridLayoutWidget_9)
        self.label_73.setObjectName(u"label_73")
        sizePolicy2.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy2)
        self.label_73.setMinimumSize(QSize(160, 30))
        self.label_73.setFont(font3)
        self.label_73.setLayoutDirection(Qt.LeftToRight)
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_73, 2, 0, 1, 1)

        self.label_64 = QLabel(self.gridLayoutWidget_9)
        self.label_64.setObjectName(u"label_64")
        sizePolicy2.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy2)
        self.label_64.setMinimumSize(QSize(160, 30))
        self.label_64.setFont(font3)
        self.label_64.setLayoutDirection(Qt.LeftToRight)
        self.label_64.setFrameShape(QFrame.NoFrame)
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_64, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider_timeout = QSlider(self.gridLayoutWidget_9)
        self.horizontalSlider_timeout.setObjectName(u"horizontalSlider_timeout")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.horizontalSlider_timeout.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_timeout.setSizePolicy(sizePolicy6)
        self.horizontalSlider_timeout.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_timeout.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_timeout.setFont(font5)
        self.horizontalSlider_timeout.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_timeout.setAutoFillBackground(False)
        self.horizontalSlider_timeout.setMinimum(3)
        self.horizontalSlider_timeout.setMaximum(30)
        self.horizontalSlider_timeout.setPageStep(1)
        self.horizontalSlider_timeout.setValue(7)
        self.horizontalSlider_timeout.setTracking(True)
        self.horizontalSlider_timeout.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider_timeout)

        self.lcdNumber_timeout = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_timeout.setObjectName(u"lcdNumber_timeout")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lcdNumber_timeout.sizePolicy().hasHeightForWidth())
        self.lcdNumber_timeout.setSizePolicy(sizePolicy7)
        self.lcdNumber_timeout.setMinimumSize(QSize(30, 30))
        self.lcdNumber_timeout.setMaximumSize(QSize(70, 30))
        self.lcdNumber_timeout.setFont(font5)
        self.lcdNumber_timeout.setDigitCount(5)
        self.lcdNumber_timeout.setProperty("intValue", 7)

        self.horizontalLayout_3.addWidget(self.lcdNumber_timeout)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalLayout_retry = QHBoxLayout()
        self.horizontalLayout_retry.setObjectName(u"horizontalLayout_retry")
        self.horizontalSlider_retry = QSlider(self.gridLayoutWidget_9)
        self.horizontalSlider_retry.setObjectName(u"horizontalSlider_retry")
        sizePolicy6.setHeightForWidth(self.horizontalSlider_retry.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_retry.setSizePolicy(sizePolicy6)
        self.horizontalSlider_retry.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_retry.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_retry.setFont(font5)
        self.horizontalSlider_retry.setMouseTracking(False)
        self.horizontalSlider_retry.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_retry.setMinimum(2)
        self.horizontalSlider_retry.setMaximum(5)
        self.horizontalSlider_retry.setPageStep(1)
        self.horizontalSlider_retry.setValue(3)
        self.horizontalSlider_retry.setOrientation(Qt.Horizontal)

        self.horizontalLayout_retry.addWidget(self.horizontalSlider_retry)

        self.lcdNumber_retry = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_retry.setObjectName(u"lcdNumber_retry")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lcdNumber_retry.sizePolicy().hasHeightForWidth())
        self.lcdNumber_retry.setSizePolicy(sizePolicy8)
        self.lcdNumber_retry.setMinimumSize(QSize(30, 30))
        self.lcdNumber_retry.setMaximumSize(QSize(70, 30))
        self.lcdNumber_retry.setFont(font5)
        self.lcdNumber_retry.setProperty("intValue", 3)

        self.horizontalLayout_retry.addWidget(self.lcdNumber_retry)


        self.gridLayout_9.addLayout(self.horizontalLayout_retry, 3, 1, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.radioButton_proxy_http = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_http.setObjectName(u"radioButton_proxy_http")
        self.radioButton_proxy_http.setMinimumSize(QSize(93, 30))
        self.radioButton_proxy_http.setFont(font3)

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_http)

        self.radioButton_proxy_socks5 = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_socks5.setObjectName(u"radioButton_proxy_socks5")
        self.radioButton_proxy_socks5.setMinimumSize(QSize(93, 30))
        self.radioButton_proxy_socks5.setFont(font3)

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_socks5)

        self.radioButton_proxy_nouse = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_nouse.setObjectName(u"radioButton_proxy_nouse")
        self.radioButton_proxy_nouse.setMinimumSize(QSize(93, 30))
        self.radioButton_proxy_nouse.setFont(font3)

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_nouse)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.label_70 = QLabel(self.gridLayoutWidget_9)
        self.label_70.setObjectName(u"label_70")
        sizePolicy2.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy2)
        self.label_70.setMinimumSize(QSize(160, 30))
        self.label_70.setFont(font3)
        self.label_70.setLayoutDirection(Qt.LeftToRight)
        self.label_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_70, 0, 0, 1, 1)

        self.lineEdit_proxy = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_proxy.setObjectName(u"lineEdit_proxy")
        sizePolicy3.setHeightForWidth(self.lineEdit_proxy.sizePolicy().hasHeightForWidth())
        self.lineEdit_proxy.setSizePolicy(sizePolicy3)
        self.lineEdit_proxy.setMinimumSize(QSize(300, 30))
        self.lineEdit_proxy.setFont(font3)
        self.lineEdit_proxy.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_9.addWidget(self.lineEdit_proxy, 1, 1, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.scrollArea_4 = QScrollArea(self.tab4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(-1, -1, 771, 553))
        self.scrollArea_4.setFrameShape(QFrame.Box)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(False)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 769, 800))
        self.groupBox_29 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(30, 10, 701, 81))
        self.groupBox_29.setMinimumSize(QSize(500, 0))
        self.groupBox_29.setFont(font3)
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox_29)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.radioButton_poster_mark_on = QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_poster_mark_on.setObjectName(u"radioButton_poster_mark_on")
        sizePolicy3.setHeightForWidth(self.radioButton_poster_mark_on.sizePolicy().hasHeightForWidth())
        self.radioButton_poster_mark_on.setSizePolicy(sizePolicy3)
        self.radioButton_poster_mark_on.setMinimumSize(QSize(0, 0))
        self.radioButton_poster_mark_on.setFont(font3)

        self.horizontalLayout_7.addWidget(self.radioButton_poster_mark_on)

        self.radioButton_poster_mark_off = QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_poster_mark_off.setObjectName(u"radioButton_poster_mark_off")
        sizePolicy3.setHeightForWidth(self.radioButton_poster_mark_off.sizePolicy().hasHeightForWidth())
        self.radioButton_poster_mark_off.setSizePolicy(sizePolicy3)
        self.radioButton_poster_mark_off.setMinimumSize(QSize(0, 0))
        self.radioButton_poster_mark_off.setFont(font3)

        self.horizontalLayout_7.addWidget(self.radioButton_poster_mark_off)

        self.groupBox_30 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setGeometry(QRect(30, 110, 701, 81))
        self.groupBox_30.setMinimumSize(QSize(200, 0))
        self.groupBox_30.setMaximumSize(QSize(739, 16777215))
        self.groupBox_30.setFont(font3)
        self.horizontalLayoutWidget_6 = QWidget(self.groupBox_30)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.radioButton_thumb_mark_on = QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_thumb_mark_on.setObjectName(u"radioButton_thumb_mark_on")
        sizePolicy3.setHeightForWidth(self.radioButton_thumb_mark_on.sizePolicy().hasHeightForWidth())
        self.radioButton_thumb_mark_on.setSizePolicy(sizePolicy3)
        self.radioButton_thumb_mark_on.setMinimumSize(QSize(0, 0))
        self.radioButton_thumb_mark_on.setFont(font3)

        self.horizontalLayout_8.addWidget(self.radioButton_thumb_mark_on)

        self.radioButton_thumb_mark_off = QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_thumb_mark_off.setObjectName(u"radioButton_thumb_mark_off")
        sizePolicy3.setHeightForWidth(self.radioButton_thumb_mark_off.sizePolicy().hasHeightForWidth())
        self.radioButton_thumb_mark_off.setSizePolicy(sizePolicy3)
        self.radioButton_thumb_mark_off.setMinimumSize(QSize(0, 0))
        self.radioButton_thumb_mark_off.setFont(font3)

        self.horizontalLayout_8.addWidget(self.radioButton_thumb_mark_off)

        self.groupBox_23 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setGeometry(QRect(30, 510, 701, 81))
        self.groupBox_23.setFont(font3)
        self.groupBox_23.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_16 = QWidget(self.groupBox_23)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.radioButton_top_left_3 = QRadioButton(self.horizontalLayoutWidget_16)
        self.radioButton_top_left_3.setObjectName(u"radioButton_top_left_3")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left_3.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left_3.setSizePolicy(sizePolicy4)
        self.radioButton_top_left_3.setMinimumSize(QSize(0, 30))
        self.radioButton_top_left_3.setFont(font3)

        self.horizontalLayout_19.addWidget(self.radioButton_top_left_3)

        self.radioButton_bottom_left_3 = QRadioButton(self.horizontalLayoutWidget_16)
        self.radioButton_bottom_left_3.setObjectName(u"radioButton_bottom_left_3")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left_3.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left_3.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left_3.setMinimumSize(QSize(0, 30))
        self.radioButton_bottom_left_3.setFont(font3)

        self.horizontalLayout_19.addWidget(self.radioButton_bottom_left_3)

        self.radioButton_top_right_3 = QRadioButton(self.horizontalLayoutWidget_16)
        self.radioButton_top_right_3.setObjectName(u"radioButton_top_right_3")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right_3.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right_3.setSizePolicy(sizePolicy4)
        self.radioButton_top_right_3.setMinimumSize(QSize(0, 30))
        self.radioButton_top_right_3.setFont(font3)

        self.horizontalLayout_19.addWidget(self.radioButton_top_right_3)

        self.groupBox_19 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(30, 310, 701, 81))
        self.groupBox_19.setFont(font3)
        self.groupBox_19.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_19)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.radioButton_top_left = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_top_left.setObjectName(u"radioButton_top_left")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left.setSizePolicy(sizePolicy4)
        self.radioButton_top_left.setMinimumSize(QSize(0, 30))
        self.radioButton_top_left.setFont(font3)

        self.horizontalLayout_4.addWidget(self.radioButton_top_left)

        self.radioButton_bottom_left = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_bottom_left.setObjectName(u"radioButton_bottom_left")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left.setMinimumSize(QSize(0, 30))
        self.radioButton_bottom_left.setFont(font3)

        self.horizontalLayout_4.addWidget(self.radioButton_bottom_left)

        self.radioButton_top_right = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_top_right.setObjectName(u"radioButton_top_right")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right.setSizePolicy(sizePolicy4)
        self.radioButton_top_right.setMinimumSize(QSize(0, 30))
        self.radioButton_top_right.setFont(font3)

        self.horizontalLayout_4.addWidget(self.radioButton_top_right)

        self.radioButton_bottom_right = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_bottom_right.setObjectName(u"radioButton_bottom_right")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_right.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_right.setMinimumSize(QSize(0, 30))
        self.radioButton_bottom_right.setFont(font3)

        self.horizontalLayout_4.addWidget(self.radioButton_bottom_right)

        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(30, 210, 701, 81))
        self.groupBox_14.setFont(font3)
        self.groupBox_14.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_14)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_sub = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_sub.setObjectName(u"checkBox_sub")
        sizePolicy4.setHeightForWidth(self.checkBox_sub.sizePolicy().hasHeightForWidth())
        self.checkBox_sub.setSizePolicy(sizePolicy4)
        self.checkBox_sub.setMinimumSize(QSize(100, 30))
        self.checkBox_sub.setFont(font3)

        self.horizontalLayout_5.addWidget(self.checkBox_sub)

        self.checkBox_leak = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_leak.setObjectName(u"checkBox_leak")
        sizePolicy4.setHeightForWidth(self.checkBox_leak.sizePolicy().hasHeightForWidth())
        self.checkBox_leak.setSizePolicy(sizePolicy4)
        self.checkBox_leak.setMinimumSize(QSize(100, 30))
        self.checkBox_leak.setFont(font3)

        self.horizontalLayout_5.addWidget(self.checkBox_leak)

        self.checkBox_uncensored = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_uncensored.setObjectName(u"checkBox_uncensored")
        sizePolicy4.setHeightForWidth(self.checkBox_uncensored.sizePolicy().hasHeightForWidth())
        self.checkBox_uncensored.setSizePolicy(sizePolicy4)
        self.checkBox_uncensored.setMinimumSize(QSize(100, 30))
        self.checkBox_uncensored.setFont(font3)

        self.horizontalLayout_5.addWidget(self.checkBox_uncensored)

        self.groupBox_21 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(30, 410, 701, 81))
        self.groupBox_21.setFont(font3)
        self.groupBox_21.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox_21)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_mark_size = QSlider(self.horizontalLayoutWidget_4)
        self.horizontalSlider_mark_size.setObjectName(u"horizontalSlider_mark_size")
        sizePolicy2.setHeightForWidth(self.horizontalSlider_mark_size.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_mark_size.setSizePolicy(sizePolicy2)
        self.horizontalSlider_mark_size.setMinimumSize(QSize(400, 30))
        self.horizontalSlider_mark_size.setMaximumSize(QSize(500, 30))
        self.horizontalSlider_mark_size.setMinimum(1)
        self.horizontalSlider_mark_size.setMaximum(5)
        self.horizontalSlider_mark_size.setPageStep(1)
        self.horizontalSlider_mark_size.setValue(3)
        self.horizontalSlider_mark_size.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider_mark_size)

        self.lcdNumber_mark_size = QLCDNumber(self.horizontalLayoutWidget_4)
        self.lcdNumber_mark_size.setObjectName(u"lcdNumber_mark_size")
        sizePolicy7.setHeightForWidth(self.lcdNumber_mark_size.sizePolicy().hasHeightForWidth())
        self.lcdNumber_mark_size.setSizePolicy(sizePolicy7)
        self.lcdNumber_mark_size.setMinimumSize(QSize(30, 30))
        self.lcdNumber_mark_size.setMaximumSize(QSize(70, 30))
        self.lcdNumber_mark_size.setProperty("intValue", 3)

        self.horizontalLayout_6.addWidget(self.lcdNumber_mark_size)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(500, 600, 171, 101))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"font:\"Courier\";")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab4, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.scrollArea_5 = QScrollArea(self.tab5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(-1, -1, 771, 553))
        self.scrollArea_5.setFrameShape(QFrame.Box)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setWidgetResizable(False)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 769, 550))
        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(30, 210, 701, 91))
        self.groupBox_17.setMinimumSize(QSize(200, 0))
        self.groupBox_17.setMaximumSize(QSize(739, 16777215))
        self.groupBox_17.setFont(font3)
        self.horizontalLayoutWidget_11 = QWidget(self.groupBox_17)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.radioButton_log_on = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_on.setObjectName(u"radioButton_log_on")
        self.radioButton_log_on.setFont(font3)

        self.horizontalLayout_13.addWidget(self.radioButton_log_on)

        self.radioButton_log_off = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_off.setObjectName(u"radioButton_log_off")
        self.radioButton_log_off.setFont(font3)

        self.horizontalLayout_13.addWidget(self.radioButton_log_off)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 110, 701, 81))
        self.groupBox_3.setMinimumSize(QSize(200, 0))
        self.groupBox_3.setMaximumSize(QSize(739, 16777215))
        self.groupBox_3.setFont(font3)
        self.horizontalLayoutWidget_9 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.radioButton_debug_on = QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_debug_on.setObjectName(u"radioButton_debug_on")
        self.radioButton_debug_on.setFont(font3)

        self.horizontalLayout_11.addWidget(self.radioButton_debug_on)

        self.radioButton_debug_off = QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_debug_off.setObjectName(u"radioButton_debug_off")
        self.radioButton_debug_off.setFont(font3)

        self.horizontalLayout_11.addWidget(self.radioButton_debug_off)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 10, 701, 81))
        self.groupBox_4.setMinimumSize(QSize(200, 0))
        self.groupBox_4.setMaximumSize(QSize(739, 16777215))
        self.groupBox_4.setFont(font3)
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(60, 30, 641, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.radioButton_update_on = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_update_on.setObjectName(u"radioButton_update_on")
        self.radioButton_update_on.setFont(font3)

        self.horizontalLayout_9.addWidget(self.radioButton_update_on)

        self.radioButton_update_off = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_update_off.setObjectName(u"radioButton_update_off")
        self.radioButton_update_off.setFont(font3)

        self.horizontalLayout_9.addWidget(self.radioButton_update_off)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.tabWidget.addTab(self.tab5, "")
        self.pushButton_save_config = QPushButton(self.page_setting)
        self.pushButton_save_config.setObjectName(u"pushButton_save_config")
        self.pushButton_save_config.setGeometry(QRect(320, 620, 350, 50))
        font6 = QFont()
        font6.setFamily(u"Courier")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.pushButton_save_config.setFont(font6)
        self.pushButton_init_config = QPushButton(self.page_setting)
        self.pushButton_init_config.setObjectName(u"pushButton_init_config")
        self.pushButton_init_config.setGeometry(QRect(90, 620, 160, 50))
        self.pushButton_init_config.setFont(font6)
        self.stackedWidget.addWidget(self.page_setting)
        self.tabWidget.raise_()
        self.pushButton_init_config.raise_()
        self.pushButton_save_config.raise_()
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.textBrowser_about = QTextBrowser(self.page_about)
        self.textBrowser_about.setObjectName(u"textBrowser_about")
        self.textBrowser_about.setGeometry(QRect(0, 0, 780, 680))
        self.textBrowser_about.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_about)
        self.widget_setting = QWidget(self.centralwidget)
        self.widget_setting.setObjectName(u"widget_setting")
        self.widget_setting.setGeometry(QRect(0, 0, 220, 700))
        self.widget_setting.setFont(font)
        self.label_ico = QLabel(self.widget_setting)
        self.label_ico.setObjectName(u"label_ico")
        self.label_ico.setGeometry(QRect(40, 540, 141, 141))
        self.label_ico.setFont(font)
        self.label_ico.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.widget_setting)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 40, 221, 331))
        self.layoutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 0, 18, 0)
        self.pushButton_main = QPushButton(self.layoutWidget)
        self.pushButton_main.setObjectName(u"pushButton_main")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_main.sizePolicy().hasHeightForWidth())
        self.pushButton_main.setSizePolicy(sizePolicy9)
        self.pushButton_main.setMinimumSize(QSize(0, 40))
        self.pushButton_main.setMaximumSize(QSize(16777215, 40))
        self.pushButton_main.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_main)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_log = QPushButton(self.layoutWidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setMinimumSize(QSize(0, 40))
        self.pushButton_log.setMaximumSize(QSize(16777215, 40))
        self.pushButton_log.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_log)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_net = QPushButton(self.layoutWidget)
        self.pushButton_net.setObjectName(u"pushButton_net")
        self.pushButton_net.setMinimumSize(QSize(0, 40))
        self.pushButton_net.setMaximumSize(QSize(16777215, 40))
        self.pushButton_net.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_net)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_tool = QPushButton(self.layoutWidget)
        self.pushButton_tool.setObjectName(u"pushButton_tool")
        self.pushButton_tool.setMinimumSize(QSize(0, 40))
        self.pushButton_tool.setMaximumSize(QSize(16777215, 40))
        self.pushButton_tool.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_tool)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_setting = QPushButton(self.layoutWidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setMinimumSize(QSize(0, 40))
        self.pushButton_setting.setMaximumSize(QSize(16777215, 40))
        self.pushButton_setting.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_setting)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.pushButton_about = QPushButton(self.layoutWidget)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(0, 40))
        self.pushButton_about.setMaximumSize(QSize(16777215, 40))
        self.pushButton_about.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_about)

        self.layoutWidget1 = QWidget(self.widget_setting)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 41, 41))
        self.layoutWidget1.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_close = QPushButton(self.layoutWidget1)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(20)
        sizePolicy10.setVerticalStretch(20)
        sizePolicy10.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy10)
        self.pushButton_close.setMinimumSize(QSize(20, 20))
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        self.pushButton_close.setBaseSize(QSize(0, 0))
        self.pushButton_close.setFont(font)
        self.pushButton_close.setMouseTracking(False)
        self.pushButton_close.setStyleSheet(u"QPushButton{color:#E0E0E0;background:#F14C4C;border-radius:10px;}QPushButton:hover{color:white;font:Tahoma;background:#FF6058;}")

        self.horizontalLayout.addWidget(self.pushButton_close)

        self.label_show_version = QLabel(self.widget_setting)
        self.label_show_version.setObjectName(u"label_show_version")
        self.label_show_version.setGeometry(QRect(0, 660, 220, 30))
        self.label_show_version.setFont(font)
        self.label_show_version.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_show_version.setStyleSheet(u"color: rgba(255, 255, 255, 151);")
        self.label_show_version.setAlignment(Qt.AlignCenter)
        self.progressBar_avdc = QProgressBar(self.centralwidget)
        self.progressBar_avdc.setObjectName(u"progressBar_avdc")
        self.progressBar_avdc.setGeometry(QRect(220, -1, 803, 10))
        self.progressBar_avdc.setMinimumSize(QSize(0, 2))
        self.progressBar_avdc.setSizeIncrement(QSize(0, 0))
        self.progressBar_avdc.setBaseSize(QSize(0, 0))
        self.progressBar_avdc.setFont(font)
        self.progressBar_avdc.setStyleSheet(u"QProgressBar::chunk {\n"
"   background-color: #336699;\n"
"   width: 3px;\n"
"}\n"
"QProgressBar {\n"
"   border: 0px solid rgba(51,102,153, 80);\n"
"   border-radius: 0px;\n"
"   text-align: center;\n"
"	background-color: rgba(246, 246, 246, 0);\n"
"}")
        self.progressBar_avdc.setValue(24)
        AVDV.setCentralWidget(self.centralwidget)
        self.progressBar_avdc.raise_()
        self.stackedWidget.raise_()
        self.widget_setting.raise_()

        self.retranslateUi(AVDV)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AVDV)
    # setupUi

    def retranslateUi(self, AVDV):
        AVDV.setWindowTitle(QCoreApplication.translate("AVDV", u"AVDCx", None))
        self.pushButton_start_cap.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb", None))
        self.label_number1.setText(QCoreApplication.translate("AVDV", u"\u756a\u53f7\uff1a", None))
        self.label_number.setText("")
        self.label_13.setText(QCoreApplication.translate("AVDV", u"\u65e5\u671f\uff1a", None))
        self.label_release.setText("")
        self.label_actor1.setText(QCoreApplication.translate("AVDV", u"\u6f14\u5458\uff1a", None))
        self.label_actor.setText("")
        self.label_outline.setText("")
        self.label_18.setText(QCoreApplication.translate("AVDV", u"\u7b80\u4ecb\uff1a", None))
        self.label_title.setText("")
        self.label_title1.setText(QCoreApplication.translate("AVDV", u"\u6807\u9898\uff1a", None))
        self.label_director.setText("")
        self.label_publish.setText("")
        self.label_23.setText(QCoreApplication.translate("AVDV", u"\u5bfc\u6f14\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("AVDV", u"\u53d1\u884c\uff1a", None))
        self.label_studio.setText("")
        self.label_series.setText("")
        self.label_30.setText(QCoreApplication.translate("AVDV", u"\u5236\u4f5c\uff1a", None))
        self.label_31.setText(QCoreApplication.translate("AVDV", u"\u7cfb\u5217\uff1a", None))
        self.label_tag.setText("")
        self.label_33.setText(QCoreApplication.translate("AVDV", u"\u7c7b\u522b\uff1a", None))
        self.checkBox_cover.setText(QCoreApplication.translate("AVDV", u"\u663e\u793a\u5c01\u9762(\u53d6\u6d88\u52fe\u9009\u540e\uff0c\u7acb\u5373\u5173\u95ed\u5c01\u9762\u663e\u793a)", None))
        self.label_result.setText(QCoreApplication.translate("AVDV", u"\u7b49\u5f85\u5f00\u59cb ...", None))
        self.label_22.setText(QCoreApplication.translate("AVDV", u"\u65f6\u957f\uff1a", None))
        self.label_runtime.setText("")
        self.label_thumb.setText(QCoreApplication.translate("AVDV", u"\u7f29\u7565\u56fe", None))
        self.label_poster.setText(QCoreApplication.translate("AVDV", u"\u5c01\u9762\u56fe", None))
        self.label_poster1.setText(QCoreApplication.translate("AVDV", u"\u5c01\u9762\uff1a", None))
        ___qtreewidgetitem = self.treeWidget_number.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AVDV", u"111", None));

        __sortingEnabled = self.treeWidget_number.isSortingEnabled()
        self.treeWidget_number.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_number.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("AVDV", u"\u6210\u529f", None));
        ___qtreewidgetitem2 = self.treeWidget_number.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("AVDV", u"\u5931\u8d25", None));
        self.treeWidget_number.setSortingEnabled(__sortingEnabled)

        self.label_file_path.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u76ee\u5f55\u8bbe\u7f6e\uff1a\u3010\u8bbe\u7f6e\u3011-\u3010\u76ee\u5f55\u8bbe\u7f6e\u3011-\u3010\u89c6\u9891\u76ee\u5f55\u3011\u3002\u7a0b\u5e8f\u5c06\u522e\u524a\u8be5\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\u7684\u6240\u6709\u6587\u4ef6\u3002", None))
        self.label_source.setText("")
        self.pushButton_start_cap2.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb", None))
        self.pushButton_check_net.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u3001\u5b57\u5e55\u79fb\u52a8", None))
        self.label_8.setText(QCoreApplication.translate("AVDV", u"\u79fb\u52a8\u300c\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u300d\u4e2d\u7684\u6240\u6709\u89c6\u9891\u5230\u300c\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u300d\u7684\n"
"\u300cMovie_moved\u300d\u76ee\u5f55\u4e0b\u3002\u4e0d\u5305\u62ec\u300c\u6392\u9664\u76ee\u5f55\u300d\u4e0b\u7684\u89c6\u9891\u53ca\u540c\u540d\u5b57\u5e55", None))
        self.pushButton_move_mp4.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb\u79fb\u52a8", None))
        self.label_41.setText(QCoreApplication.translate("AVDV", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("AVDV", u"\u5355\u6587\u4ef6\u522e\u524a", None))
        self.label.setText(QCoreApplication.translate("AVDV", u"\u5982\u4e0d\u6307\u5b9a\u756a\u53f7\uff0c\u5219\u9ed8\u8ba4\u4f7f\u7528\u6587\u4ef6\u540d\u8bc6\u522b\u756a\u53f7\u8fdb\u884c\u522e\u524a\u3002\n"
"\u5982\u6307\u5b9a\u4e86\u522e\u524a\u7f51\u5740\uff0c\u5219\u300c\u522e\u524a\u7f51\u7ad9\u300d\u8bf7\u9009\u62e9\u5bf9\u5e94\u7f51\u7ad9\uff01", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("AVDV", u"\u9009\u62e9\u6587\u4ef6", None))
        self.comboBox_website.setItemText(0, QCoreApplication.translate("AVDV", u"All websites", None))
        self.comboBox_website.setItemText(1, QCoreApplication.translate("AVDV", u"iqqtv", None))
        self.comboBox_website.setItemText(2, QCoreApplication.translate("AVDV", u"javbus", None))
        self.comboBox_website.setItemText(3, QCoreApplication.translate("AVDV", u"javdb", None))
        self.comboBox_website.setItemText(4, QCoreApplication.translate("AVDV", u"jav321", None))
        self.comboBox_website.setItemText(5, QCoreApplication.translate("AVDV", u"dmm", None))
        self.comboBox_website.setItemText(6, QCoreApplication.translate("AVDV", u"avsox", None))
        self.comboBox_website.setItemText(7, QCoreApplication.translate("AVDV", u"xcity", None))
        self.comboBox_website.setItemText(8, QCoreApplication.translate("AVDV", u"mgstage", None))
        self.comboBox_website.setItemText(9, QCoreApplication.translate("AVDV", u"fc2", None))
        self.comboBox_website.setItemText(10, QCoreApplication.translate("AVDV", u"fc2club", None))
        self.comboBox_website.setItemText(11, QCoreApplication.translate("AVDV", u"fc2hub", None))
        self.comboBox_website.setItemText(12, QCoreApplication.translate("AVDV", u"airav", None))
        self.comboBox_website.setItemText(13, QCoreApplication.translate("AVDV", u"javlibrary", None))

        self.label_2.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u7f51\u5740\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("AVDV", u"\u5f71\u7247\u756a\u53f7\uff1a", None))
        self.pushButton_start_single_file.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("AVDV", u"Emby-\u6f14\u5458\u5934\u50cf", None))
        self.pushButton_add_actor_pic.setText(QCoreApplication.translate("AVDV", u"\u6dfb\u52a0\u5934\u50cf", None))
        self.label_3.setText(QCoreApplication.translate("AVDV", u"Emby\u5730\u5740\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("AVDV", u"API\u5bc6\u94a5\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("AVDV", u"\u8bf4\u660e:\n"
"   1\u3001\u5934\u50cf\u8bf7\u653e\u5728\u7a0b\u5e8f\u76ee\u5f55(AVDC\u76ee\u5f55)\u4e0b\u7684Actor\u76ee\u5f55\u4e2d\u3002\n"
"   2\u3001\u5bc6\u94a5\u521b\u5efa\u65b9\u6cd5\uff1aEmby\u63a7\u5236\u53f0->\u9ad8\u7ea7->API\u5bc6\u94a5->\u6dfb\u52a0(APP\u540d\u79f0\u4efb\u610f)\u3002", None))
        self.pushButton_show_pic_actor.setText(QCoreApplication.translate("AVDV", u"\u67e5\u770b", None))
        self.comboBox_pic_actor.setItemText(0, QCoreApplication.translate("AVDV", u"\u53ef\u6dfb\u52a0\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(1, QCoreApplication.translate("AVDV", u"\u6ca1\u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(2, QCoreApplication.translate("AVDV", u"\u5df2\u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(3, QCoreApplication.translate("AVDV", u"\u6240\u6709\u6f14\u5458", None))

        self.groupBox_13.setTitle(QCoreApplication.translate("AVDV", u"\u88c1\u526a\u5c01\u9762\u56fe", None))
        self.pushButton_select_thumb.setText(QCoreApplication.translate("AVDV", u"\u9009\u62e9\u7f29\u7565\u56fe", None))
        self.label_6.setText(QCoreApplication.translate("AVDV", u"\u8bf4\u660e:\n"
"  1\u3001\u5bf9\u6709\u4e9b\u5c01\u9762\u56fe(poster)\u4e0d\u6ee1\u610f\uff0c\u6bd4\u4f8b\u4e0d\u5bf9\u6216\u8005\u5206\u8fa8\u7387\u592a\u4f4e\uff0c\u53ef\u4f7f\u7528\u6b64\u5de5\u5177\u3002\n"
"  2\u3001\u6b64\u5de5\u5177\u652f\u6301\u624b\u52a8\u9009\u62e9\u88c1\u526a\u8303\u56f4\uff0c\u53ef\u4ee5\u5c06\u7f29\u7565\u56fe(thumb)\u88c1\u526a\u4e3a\u5c01\u9762\u56fe\u3002", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle(QCoreApplication.translate("AVDV", u"\u5de5\u4f5c\u6a21\u5f0f", None))
        self.radioButton_common.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6a21\u5f0f", None))
        self.radioButton_sort.setText(QCoreApplication.translate("AVDV", u"\u6574\u7406\u6a21\u5f0f", None))
        self.label_11.setText(QCoreApplication.translate("AVDV", u"\u5305\u542b\u522e\u524a\u4fe1\u606f\u3001\u7ffb\u8bd1\u6807\u9898\u548c\u7b80\u4ecb\u3001\u4e0b\u8f7d\u56fe\u7247\u548cnfo\u6587\u4ef6\u3001\u91cd\u547d\u540d\u6587\u4ef6\u3001\u79fb\u52a8\u6587\u4ef6\u7b49\u5168\u90e8\u64cd\u4f5c", None))
        self.label_15.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u4e0b\u8f7d\u56fe\u7247\u548cnfo\u6587\u4ef6\uff0c\u5176\u4ed6\u540c\u4e0a", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u8bed\u8a00", None))
        self.radioButton_zh_cn.setText(QCoreApplication.translate("AVDV", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.radioButton_zh_tw.setText(QCoreApplication.translate("AVDV", u"\u7e41\u4f53\u4e2d\u6587", None))
        self.radioButton_ja.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u7ffb\u8bd1", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("AVDV", u"\u522e\u524a\u504f\u597d", None))
        self.radioButton_like_speed.setText(QCoreApplication.translate("AVDV", u"\u5feb\u901f", None))
        self.radioButton_like_more.setText(QCoreApplication.translate("AVDV", u"\u5b57\u6bb5\u5168", None))
        self.label_28.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u4e0d\u4f1a\u5c1d\u8bd5\u8bf7\u6c42\u5176\u4ed6\u7f51\u7ad9\u8865\u5168\u7f3a\u5931\u7684\u5b57\u6bb5\uff0c\u56e0\u6b64\u901f\u5ea6\u4f1a\u5feb\u4e00\u4e9b", None))
        self.label_32.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u4f1a\u5c1d\u8bd5\u8bf7\u6c42\u5176\u4ed6\u7f51\u7ad9\u8865\u5168\u7f3a\u5931\u7684\u5b57\u6bb5\uff0c\u56e0\u6b64\u901f\u5ea6\u4f1a\u7565\u6162\u4e00\u4e9b", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("AVDV", u"\u522e\u524a\u7f51\u7ad9", None))
        self.comboBox_website_all.setItemText(0, QCoreApplication.translate("AVDV", u"All websites", None))
        self.comboBox_website_all.setItemText(1, QCoreApplication.translate("AVDV", u"iqqtv", None))
        self.comboBox_website_all.setItemText(2, QCoreApplication.translate("AVDV", u"javbus", None))
        self.comboBox_website_all.setItemText(3, QCoreApplication.translate("AVDV", u"javdb", None))
        self.comboBox_website_all.setItemText(4, QCoreApplication.translate("AVDV", u"jav321", None))
        self.comboBox_website_all.setItemText(5, QCoreApplication.translate("AVDV", u"dmm", None))
        self.comboBox_website_all.setItemText(6, QCoreApplication.translate("AVDV", u"avsox", None))
        self.comboBox_website_all.setItemText(7, QCoreApplication.translate("AVDV", u"xcity", None))
        self.comboBox_website_all.setItemText(8, QCoreApplication.translate("AVDV", u"mgstage", None))
        self.comboBox_website_all.setItemText(9, QCoreApplication.translate("AVDV", u"fc2", None))
        self.comboBox_website_all.setItemText(10, QCoreApplication.translate("AVDV", u"fc2club", None))
        self.comboBox_website_all.setItemText(11, QCoreApplication.translate("AVDV", u"fc2hub", None))
        self.comboBox_website_all.setItemText(12, QCoreApplication.translate("AVDV", u"airav", None))
        self.comboBox_website_all.setItemText(13, QCoreApplication.translate("AVDV", u"javlibrary", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("AVDV", u"\u8f6f\u94fe\u63a5\u6a21\u5f0f", None))
        self.label_36.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u5728\u6210\u529f\u8f93\u51fa\u76ee\u5f55\uff08\u9700\u4e3a\u672c\u5730\u78c1\u76d8\uff09\u521b\u5efa\u6307\u5411\u539f\u6587\u4ef6\uff08\u7f51\u7edc/\u672c\u5730\u5747\u53ef\uff09\u7684\u66ff\u8eab\u6587\u4ef6", None))
        self.label_37.setText(QCoreApplication.translate("AVDV", u"\u5f53\u9009\u62e9\u300c\u5173\u300d\u65f6\uff0c\u4e0b\u9762\u7684\u300c\u6210\u529f\u540e\u79fb\u52a8\u6587\u4ef6\u300d\u300c\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6\u300d\u624d\u4f1a\u751f\u6548", None))
        self.radioButton_soft_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_soft_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("AVDV", u"\u6210\u529f\u540e\u91cd\u547d\u540d\u6587\u4ef6", None))
        self.label_38.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u6309\u300c\u76ee\u5f55\u548c\u6587\u4ef6\u8bbe\u7f6e\u300d-\u300c\u547d\u540d\u89c4\u5219\u300d-\u300c\u89c6\u9891\u6807\u9898(\u672c\u5730\u6587\u4ef6)\u300d\u91cd\u547d\u540d\u6587\u4ef6", None))
        self.label_39.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u7ee7\u7eed\u4f7f\u7528\u539f\u6765\u6587\u4ef6\u540d", None))
        self.radioButton_succ_rename_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_succ_rename_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("AVDV", u"\u6210\u529f\u540e\u79fb\u52a8\u6587\u4ef6", None))
        self.gridLayoutWidget_6.setStyleSheet(QCoreApplication.translate("AVDV", u"color: rgb(80, 80, 80);", None))
        self.label_54.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u79fb\u52a8\u6587\u4ef6\u5230\u6210\u529f\u8f93\u51fa\u76ee\u5f55", None))
        self.label_55.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u4e0d\u79fb\u52a8\u6587\u4ef6\u4f4d\u7f6e\uff0c\u4ecd\u5728\u539f\u76ee\u5f55\uff08\u9002\u5408\u5df2\u6574\u7406\u597d\u6587\u4ef6\u5939\u6216\u4e8c\u6b21\u522e\u524a\u573a\u666f\uff09", None))
        self.radioButton_succ_move_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_succ_move_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("AVDV", u"\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6", None))
        self.label_34.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u5931\u8d25\u540e\uff0c\u79fb\u52a8\u6587\u4ef6\u5230\u5931\u8d25\u8f93\u51fa\u76ee\u5f55", None))
        self.label_35.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u5931\u8d25\u540e\uff0c\u4e0d\u79fb\u52a8\u6587\u4ef6\u4f4d\u7f6e\uff0c\u4ecd\u5728\u539f\u76ee\u5f55", None))
        self.radioButton_fail_move_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_fail_move_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u5f15\u64ce", None))
        self.radioButton_youdao.setText(QCoreApplication.translate("AVDV", u"\u6709\u9053", None))
        self.radioButton_deepl.setText(QCoreApplication.translate("AVDV", u"DeepL", None))
        self.label_81.setText(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u5f15\u64ce\uff1a", None))
        self.label_80.setText(QCoreApplication.translate("AVDV", u"DeepL API key\uff1a", None))
        self.label_60.setText(QCoreApplication.translate("AVDV", u"DeepL\u662f\u4ed8\u8d39\u7ffb\u8bd1\u5f15\u64ce\uff0c\u9700\u8981\u8f93\u5165key\u624d\u80fd\u4f7f\u7528", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\u56fe\u7247\u548cnfo\u6587\u4ef6", None))
        self.checkBox_download_poster.setText(QCoreApplication.translate("AVDV", u"poster", None))
        self.checkBox_download_thumb.setText(QCoreApplication.translate("AVDV", u"thumb", None))
        self.checkBox_download_fanart.setText(QCoreApplication.translate("AVDV", u"fanart", None))
        self.checkBox_download_extrafanart.setText(QCoreApplication.translate("AVDV", u"extrafanart", None))
        self.checkBox_download_extrafanart_copy.setText(QCoreApplication.translate("AVDV", u"extrafanart\u526f\u672c", None))
        self.checkBox_download_nfo.setText(QCoreApplication.translate("AVDV", u"nfo", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("AVDV", u"poster\u5904\u7406\u65b9\u5f0f", None))
        self.radioButton_poster_cut.setText(QCoreApplication.translate("AVDV", u"thumb\u88c1\u526a\uff08\u6e05\u6670\uff09", None))
        self.radioButton_poster_official.setText(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\uff08\u6a21\u7cca\uff09", None))
        self.label_52.setText(QCoreApplication.translate("AVDV", u"\u4ece\u7f51\u7edc\u4e0b\u8f7d\u56fe\u7247\uff0c\u4e00\u822c\u5f88\u4e0d\u6e05\u6670\u3002\u5f53\u6ca1\u6709\u4e0b\u8f7d\u94fe\u63a5\u65f6\uff0c\u5c06\u81ea\u52a8\u4f7f\u7528thumb\u88c1\u526a", None))
        self.label_53.setText(QCoreApplication.translate("AVDV", u"\u63a8\u8350\uff0c\u5c06\u4f7f\u7528thumb\u88c1\u526a\uff0c\u56fe\u7247\u6e05\u6670", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u5185\u5bb9", None))
        self.checkBox_translate_title.setText(QCoreApplication.translate("AVDV", u"\u6807\u9898", None))
        self.checkBox_translate_outline.setText(QCoreApplication.translate("AVDV", u"\u7b80\u4ecb", None))
        self.checkBox_translate_actor.setText(QCoreApplication.translate("AVDV", u"\u6f14\u5458", None))
        self.checkBox_translate_tag.setText(QCoreApplication.translate("AVDV", u"\u6807\u7b7e", None))
        self.label_74.setText(QCoreApplication.translate("AVDV", u"\u4e3a\u907f\u514d\u7ffb\u8bd1\u9519\u8bef\uff0c\u6f14\u5458\u3001\u6807\u7b7e\u4f7f\u7528\u7684\u662f\u522e\u524a\u7f51\u7ad9\u7ffb\u8bd1\u7684\u5185\u5bb9\uff0c\u5e76\u4e0d\u4f7f\u7528\u6709\u9053\u7ffb\u8bd1\u3002\n"
"\u56e0\u6b64\uff0c\u5f53\u522e\u524a\u7f51\u7ad9\u6ca1\u6709\u7ffb\u8bd1\u65f6\uff0c\u6f14\u5458\u548c\u6807\u7b7e\u4e5f\u4e0d\u4f1a\u7ffb\u8bd1\uff0c\u663e\u793a\u4ecd\u65e7\u4e3a\u65e5\u8bed\u3002\n"
"\u53e6\u5916\uff0c\u4e3a\u4e86\u4fdd\u8bc1\u6f14\u5458\u5934\u50cf\u6b63\u5e38\u663e\u793a\uff0cnfo\u91cc\u7684\u6f14\u5458\u4f1a\u9ed8\u8ba4\u4f7f\u7528\u65e5\u6587\u540d\u5b57\u3002", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("AVDV", u"\u4f18\u5148\u4f7f\u7528\u672c\u5730\u6587\u4ef6", None))
        self.checkBox_old_poster.setText(QCoreApplication.translate("AVDV", u"poster", None))
        self.checkBox_old_thumb.setText(QCoreApplication.translate("AVDV", u"thumb", None))
        self.checkBox_old_fanart.setText(QCoreApplication.translate("AVDV", u"fanart", None))
        self.checkBox_old_extrafanart.setText(QCoreApplication.translate("AVDV", u"extrafanart", None))
        self.checkBox_old_extrafanart_copy.setText(QCoreApplication.translate("AVDV", u"extrafanart\u526f\u672c", None))
        self.checkBox_old_nfo.setText(QCoreApplication.translate("AVDV", u"nfo", None))
        self.label_79.setText(QCoreApplication.translate("AVDV", u"\u6240\u52fe\u9009\u9879\u76ee\u5b58\u5728\u672c\u5730\u6587\u4ef6\u65f6\uff0c\u5c06\u4fdd\u7559\u5e76\u4f18\u5148\u4f7f\u7528\u672c\u5730\u6587\u4ef6\uff0c\u4e0d\u518d\u91cd\u65b0\u4e0b\u8f7d\uff1b\u672a\u52fe\u9009\u9879\u76ee\u7684\u672c\u5730\u6587\u4ef6\u5c06\u88ab\u6e05\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("AVDV", u"\u522e\u524a\u8bbe\u7f6e", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("AVDV", u"\u76ee\u5f55\u8bbe\u7f6e", None))
        self.label_50.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167\u526f\u672c\u76ee\u5f55\uff1a", None))
        self.label_58.setText(QCoreApplication.translate("AVDV", u"\u6307\u4e0d\u60f3\u8981\u522e\u524a\u7684\u76ee\u5f55\uff0c\u53ef\u4ee5\u586b\u5199\u591a\u4e2a\u76ee\u5f55\uff0c\u4ee5\u9017\u53f7\u5206\u5f00\uff08\u4e2d\u82f1\u6587\u9017\u53f7\u90fd\u53ef\u4ee5\uff09", None))
        self.label_47.setText(QCoreApplication.translate("AVDV", u"\u6210\u529f\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.label_48.setText(QCoreApplication.translate("AVDV", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.label_49.setText(QCoreApplication.translate("AVDV", u"\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\uff1a", None))
        self.label_59.setText(QCoreApplication.translate("AVDV", u"\u6307\u628a\u5267\u7167\u76ee\u5f55exfanart\u5185\u5bb9\u518d\u590d\u5236\u5230\u53e6\u4e00\u4e2a\u76ee\u5f55\uff0c\u4ee5\u4fbf\u5267\u7167\u53ef\u4ee5\u5728emby\u6d4f\u89c8\u67e5\u770b", None))
        self.label_56.setText(QCoreApplication.translate("AVDV", u"\u6307\u672c\u5730\u542b\u6709\u89c6\u9891\u7684\u6587\u4ef6\u5939\uff0c\u5c06\u4ece\u7f51\u7edc\u4e0a\u522e\u524a\u8be5\u76ee\u5f55\uff08\u542b\u5b50\u76ee\u5f55\uff09\u6240\u6709\u89c6\u9891\u7684\u5143\u6570\u636e\u4fe1\u606f", None))
        self.label_46.setText(QCoreApplication.translate("AVDV", u"\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.label_57.setText(QCoreApplication.translate("AVDV", u"\u6307\u522e\u524a\u5931\u8d25\u65f6\uff0c\u89c6\u9891\u5c06\u79fb\u52a8\u5230\u8fd9\u4e2a\u6587\u4ef6\u5939\u3002\u8f93\u51fa\u76ee\u5f55\u53ef\u4ee5\u4e0d\u5728\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u4e0b", None))
        self.label_29.setText(QCoreApplication.translate("AVDV", u"\u6307\u522e\u524a\u6210\u529f\u65f6\uff0c\u89c6\u9891\u5c06\u79fb\u52a8\u5230\u8fd9\u4e2a\u6587\u4ef6\u5939\u3002\u8f93\u51fa\u76ee\u5f55\u53ef\u4ee5\u4e0d\u5728\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u4e0b", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("AVDV", u"\u547d\u540d\u89c4\u5219", None))
        self.label_62.setText(QCoreApplication.translate("AVDV", u"\u4e2a\u522b\u7f51\u7ad9\u6709\u65f6\u4f1a\u5728\u4e00\u4e9b\u6807\u9898\u672b\u5c3e\u52a0\u4e0a\u6f14\u5458\u540d\uff0c\u6b64\u65f6\u7684\u6807\u9898\u5176\u5b9e = \u6807\u9898 \u6f14\u5458", None))
        self.label_69.setText(QCoreApplication.translate("AVDV", u"\u5f53\u6709\u5b57\u5e55\u65f6\uff0c\u6587\u4ef6\u5939\u540d\u5b57\u540e\u9762\u6dfb\u52a0-C\u3002\u6ee1\u8db3\u4ee5\u4e0b\u4efb\u4e00\u6761\u4ef6\uff0c\u89c6\u4e3a\u6709\u4e2d\u6587\u5b57\u5e55\uff1a\n"
"1\uff0c\u6587\u4ef6\u540d\u4e2d\u542b\u6709-C\uff1b2\uff0c\u8def\u5f84\u4e2d\u542b\u6709\u300c\u4e2d\u6587\u300d\u3001\u300c\u5b57\u5e55\u300d\u5b57\u7b26", None))
        self.radioButton_foldername_C_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_foldername_C_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.label_63.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6807\u9898(\u672c\u5730\u6587\u4ef6)\uff1a", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_dir_name.setAccessibleDescription(QCoreApplication.translate("AVDV", u"\u6d4b\u8bd5", None))
#endif // QT_CONFIG(accessibility)
        self.label_68.setText(QCoreApplication.translate("AVDV", u"\u6307\u5728nfo\u6587\u4ef6\u4e2d\u7684\u6807\u9898\u683c\u5f0f\uff0c\u547d\u540d\u5b57\u6bb5\u540c\u4e0a", None))
        self.label_71.setText(QCoreApplication.translate("AVDV", u"\u53bb\u9664\u6807\u9898\u672b\u5c3e\u6f14\u5458\u540d\uff1a", None))
        self.label_67.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6807\u9898(\u5a92\u4f53\u5e93\u4e2d)\uff1a", None))
        self.label_61.setText(QCoreApplication.translate("AVDV", u"\u6307\u672c\u5730\u89c6\u9891\u6587\u4ef6\u7684\u6807\u9898\u683c\u5f0f\uff0c\u547d\u540d\u5b57\u6bb5\u540c\u4e0a", None))
        self.label_66.setText(QCoreApplication.translate("AVDV", u"\u5f53\u522e\u524a\u6210\u529f\u65f6\uff0c\u4e3a\u8be5\u89c6\u9891\u521b\u5efa\u4e00\u4e2a\u89c6\u9891\u76ee\u5f55\uff0c\u5e76\u79fb\u52a8\u8be5\u89c6\u9891\u76ee\u5f55\u5230\u6210\u529f\u8f93\u51fa\u76ee\u5f55\u3002\n"
"\u76ee\u5f55\u540d\u5b57\u652f\u6301\u81ea\u5b9a\u4e49\u3002\u547d\u540d\u5b57\u6bb5\u6709\uff1a\n"
"title, actor, number, studio, publisher, year, mosaic,\n"
"runtime, director, release, series\n"
"\u6ce8\u610f\uff1a1\uff0c\u53ef\u4ee5\u6dfb\u52a0\u547d\u540d\u5b57\u6bb5\u4ee5\u5916\u7684\u5b57\u7b26\uff0c\u547d\u540d\u65f6\u4f1a\u539f\u6837\u4fdd\u7559\uff1b\n"
"2\uff0c\u5f53\u7559\u7a7a\u65f6\uff0c\u8868\u793a\u4e0d\u521b\u5efa\u89c6\u9891\u76ee\u5f55\uff1b\n"
"3\uff0c\u5f53\u52fe\u9009\u300c\u6210\u529f\u540e\u4e0d\u79fb\u52a8\u6587\u4ef6\u300d\u65f6\uff0c\u5c06\u4e0d\u4f1a\u521b\u5efa\u89c6\u9891\u76ee\u5f55", None))
        self.label_43.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u76ee\u5f55\u547d\u540d\uff1a", None))
        self.label_51.setText(QCoreApplication.translate("AVDV", u"\u6709\u5b57\u5e55\u65f6\u76ee\u5f55\u6dfb\u52a0-C\uff1a", None))
        self.groupBox_20.setTitle("")
        self.radioButton_del_actor_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_del_actor_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("AVDV", u"\u6587\u4ef6\u540d\u6392\u9664\u8bbe\u7f6e", None))
        self.label_72.setText(QCoreApplication.translate("AVDV", u"\u591a\u4f59\u5b57\u7b26\u4e32\uff1a", None))
        self.label_76.setText(QCoreApplication.translate("AVDV", u"\u5f02\u5e38\u5b57\u7b26\uff1a", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("AVDV", u"\u6587\u4ef6\u540e\u7f00\u548c\u756a\u53f7\u524d\u7f00", None))
        self.label_77.setText(QCoreApplication.translate("AVDV", u"\u5b57\u5e55\u7c7b\u578b\u540e\u7f00\uff1a", None))
        self.label_78.setText(QCoreApplication.translate("AVDV", u"\u65e0\u7801\u756a\u53f7\u524d\u7f00\uff1a", None))
        self.label_44.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u7c7b\u578b\u540e\u7f00\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("AVDV", u"\u76ee\u5f55\u548c\u6587\u4ef6\u8bbe\u7f6e", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("AVDV", u"Cookie\u8bbe\u7f6e", None))
        self.label_45.setText(QCoreApplication.translate("AVDV", u"javdb\uff1a\n"
"\uff08\u767b\u5f55\u72b6\u6001\uff09", None))
        self.label_75.setText(QCoreApplication.translate("AVDV", u"Cookie \u83b7\u53d6\u65b9\u6cd5\uff1a\n"
"\u4f7f\u7528 Chrome \u6253\u5f00\u76ee\u6807\u7f51\u7ad9\u540e\uff0c\u70b9\u51fb\u9f20\u6807\u53f3\u952e\uff0c\u9009\u62e9 \u201c\u68c0\u67e5\u201d \uff0c\u53f3\u4fa7\u9876\u90e8\u9009\u62e9\uff1aNetwork -> DOC\uff0c\n"
"\u7136\u540e F5 \u5237\u65b0\u9875\u9762\u3002\u70b9\u51fb name \u680f\u52a0\u8f7d\u51fa\u6765\u7684\u7b2c\u4e00\u4e2a\u5185\u5bb9 -> Headers -> Request Headers -> Cookie\u3002\n"
"\u590d\u5236 Cookie \u5bf9\u5e94\u7684\u5168\u90e8\u503c\u586b\u4eba\u4e0a\u9762\u8f93\u5165\u6846\u3002 \uff08\u6ce8\u610f\uff1aCookie \u5b58\u5728\u6709\u6548\u671f\uff0c\u8fc7\u671f\u65e0\u6548\u65f6\u8bf7\u91cd\u65b0\u83b7\u53d6\u3002\uff09", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("AVDV", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.label_65.setText(QCoreApplication.translate("AVDV", u"\u91cd\u8bd5\u6b21\u6570\uff1a", None))
        self.label_73.setText(QCoreApplication.translate("AVDV", u"\u8d85\u65f6\u65f6\u95f4\uff1a", None))
        self.label_64.setText(QCoreApplication.translate("AVDV", u"IP+\u7aef\u53e3\u53f7\uff1a", None))
        self.radioButton_proxy_http.setText(QCoreApplication.translate("AVDV", u"http", None))
        self.radioButton_proxy_socks5.setText(QCoreApplication.translate("AVDV", u"socks5", None))
        self.radioButton_proxy_nouse.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u4f7f\u7528", None))
        self.label_70.setText(QCoreApplication.translate("AVDV", u"\u4ee3\u7406\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("AVDV", u"\u7f51\u7edc\u8bbe\u7f6e", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("AVDV", u"\u5c01\u9762\u56fe\u6dfb\u52a0\u6c34\u5370", None))
        self.radioButton_poster_mark_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_poster_mark_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("AVDV", u"\u7f29\u7565\u56fe\u6dfb\u52a0\u6c34\u5370", None))
        self.radioButton_thumb_mark_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_thumb_mark_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("AVDV", u"\u6c34\u5370\u6837\u5f0f\uff08\u5f85\u5f00\u53d1\uff09", None))
        self.radioButton_top_left_3.setText(QCoreApplication.translate("AVDV", u"\u9ed8\u8ba4\u6837\u5f0f", None))
        self.radioButton_bottom_left_3.setText(QCoreApplication.translate("AVDV", u"\u6837\u5f0f2", None))
        self.radioButton_top_right_3.setText(QCoreApplication.translate("AVDV", u"\u81ea\u5b9a\u4e49", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("AVDV", u"\u9996\u4e2a\u6c34\u5370\u4f4d\u7f6e\uff08\u6709\u591a\u4e2a\u6c34\u5370\u65f6\uff0c\u5c06\u4ece\u9996\u4e2a\u6c34\u5370\uff0c\u987a\u65f6\u9488\u6dfb\u52a0\uff09", None))
        self.radioButton_top_left.setText(QCoreApplication.translate("AVDV", u"\u5de6\u4e0a", None))
        self.radioButton_bottom_left.setText(QCoreApplication.translate("AVDV", u"\u5de6\u4e0b", None))
        self.radioButton_top_right.setText(QCoreApplication.translate("AVDV", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right.setText(QCoreApplication.translate("AVDV", u"\u53f3\u4e0b", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("AVDV", u"\u8981\u6dfb\u52a0\u7684\u6c34\u5370\u7c7b\u578b", None))
        self.checkBox_sub.setText(QCoreApplication.translate("AVDV", u"\u5b57\u5e55", None))
        self.checkBox_leak.setText(QCoreApplication.translate("AVDV", u"\u6d41\u51fa", None))
        self.checkBox_uncensored.setText(QCoreApplication.translate("AVDV", u"\u65e0\u7801", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("AVDV", u"\u6c34\u5370\u5927\u5c0f", None))
        self.label_9.setText(QCoreApplication.translate("AVDV", u"\u6c34\u5370\u6587\u4ef6\u53ef\u81ea\u5df1\u66ff\u6362\n"
"\u5206\u8fa8\u7387\u8981\u6c42\u957f\u5bbd 500x300,\n"
"\u80cc\u666f\u900f\u660e\uff0cpng\u683c\u5f0f.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("AVDV", u"\u6c34\u5370\u8bbe\u7f6e", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58\u65e5\u5fd7", None))
        self.radioButton_log_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_log_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AVDV", u"\u8c03\u8bd5\u6a21\u5f0f", None))
        self.radioButton_debug_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_debug_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AVDV", u"\u68c0\u6d4b\u66f4\u65b0", None))
        self.radioButton_update_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_update_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("AVDV", u"\u66f4\u591a\u8bbe\u7f6e", None))
        self.pushButton_save_config.setText(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58", None))
        self.pushButton_init_config.setText(QCoreApplication.translate("AVDV", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.textBrowser_about.setHtml(QCoreApplication.translate("AVDV", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Courier','Courier'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:20pt; font-weight:600;\">AVDCx</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:16pt; font-weight:600;\">AVDCx \u662f\u57fa\u4e8e AV_Data_Capture \u7684 GUI \u7248\u672c AVDC "
                        "\u518d\u6b21\u4fee\u6539\u7684\u7248\u672c\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt;\">\u00b7 AV_Data_Capture \u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/yoshiko2/AV_Data_Capture\"><span style=\" font-family:'Courier'; font-size:12pt; text-decoration: underline; color:#0068da;\">https://github.com/yoshiko2/AV_Data_Capture</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt;\">\u00b7 AVDC \u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/moyy996/AVDC\"><span style=\" font"
                        "-family:'Courier'; font-size:12pt; text-decoration: underline; color:#0068da;\">https://github.com/moyy996/AVDC</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt;\">\u00b7 AVDCx \u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/Hermit10/temp\"><span style=\" font-family:'Courier'; font-size:12pt; text-decoration: underline; color:#0068da;\">https://github.com/Hermit10/temp</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:24pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:24pt; font-weight:600;\">\u4f7f\u7528\u8bf4\u660e</span><span style=\" font-family:'Courier';\"> \uff08\u5185\u5bb9\u6765\u81ea AVDC \uff1a</span><a href=\"https://github.com/Hermit10/temp\"><span style=\" font-family:'Courier'; text-decoration: underline; color:#0068da;\">https://github.com/moyy996/AVDC</span></a><span style=\" font-family:'Courier';\"> \uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:14pt;\">\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014</span></p>\n"
"<p style"
                        "=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:14pt; font-weight:600;\">\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u4e00\u3001\u529f\u80fd\u7b80\u4ecb\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">\u4e00\u3001\u529f\u80fd\u7b80\u4ecb</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000f"
                        "f;\">\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u8bbe\u7f6e\u8bf4\u660e\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">\u56db\u3001\u8bbe\u7f6e\u8bf4\u660e</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600;\"> </span></p>\n"
"<h1 style=\" margin-top:0px"
                        "; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u4e00\u3001\u529f\u80fd\u7b80\u4ecb\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u4e00</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u529f\u80fd\u7b80\u4ecb</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  \u65e5\u672c\u7535\u5f71</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5143\u6570\u636e\u6293\u53d6\u5de5\u5177</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">/\u522e\u524a\u5668\uff0c\u914d\u5408\u672c\u5730\u5f71\u7247\u7ba1\u7406\u8f6f\u4ef6</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weig"
                        "ht:600; color:#ff0000; background-color:#ffffff;\">EMBY,KODI\uff0cPLEX</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">\u7b49\u7ba1\u7406\u672c\u5730\u5f71\u7247\uff0c\u8be5\u8f6f\u4ef6\u8d77\u5230\u5206\u7c7b\u4e0e\u5143\u6570\u636e\u6293\u53d6\u4f5c\u7528\uff0c\u5229\u7528\u5143\u6570\u636e\u4fe1\u606f\u6765\u5206\u7c7b\uff0c\u4f9b\u672c\u5730\u5f71\u7247</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5206\u7c7b\u6574\u7406</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">\u4f7f\u7528\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><a name=\"_\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u4e8c</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u9879\u76ee\u7b80\u4ecb</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">Gui made by </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">moyy996</span><span style=\" font-family:'Courier'; font-size:12pt;\">\uff0cCore made by </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">yoshiko2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">tg\u5b98\u65b9\u7535\u62a5\u7fa4:</span><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:'Courier'; font-size:12pt; text-decoration: underline; color:#0000ff;\"> </span></a><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">\u547d\u4ee4\u884c\u7248\u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/yoshiko2/AV_Data_Capture\"><span style=\" font-family:'"
                        "Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/yoshiko2/AV_Data_Capture</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">GUI\u7248\u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/moyy996/AVDC\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">GUI\u7248EXE\u4e0b\u8f7d\u5730\u5740\uff1a</span>"
                        "<a href=\"https://github.com/moyy996/AVDC/releases\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC/releases</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u4e09</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:1"
                        "0.5pt; font-weight:600; color:#ff0000;\">\u4e0d\u533a\u5206\u5927\u5c0f\u5199\u3001\u522e\u524a\u524d\u5c3d\u91cf\u547d\u540d\u89c4\u8303\uff01\uff01\uff01\uff01</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">1\u3001\u6807\u51c6\u6709\u7801</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb\u3001Javbus:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">SSNI-111</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Dmm\uff1a</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">ssni00111</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">2\u3001\u65e0\u7801</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb\u3001Javbus\u3001Avsox:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#f"
                        "f0000; background-color:#ffffff;\">111111-1111\u3001111111_111\u3001HEYZO-1111\u3001n1111</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">3\u3001\u7d20\u4eba</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Mgstage:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">259LUXU-1111</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e;"
                        " background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">LUXU-1111</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Fc2club:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">FC2-111111\u3001FC2-PPV-111111\u3001FC2PPV-111111</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4\u3001\u6b27\u7f8e</span></h4>\n"
"<h4 style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb\u3001Javbus:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">sexart.11.11.11(\u7cfb\u5217.\u5e74.\u6708.\u65e5)</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\"> </span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">5\u3001\u81ea\u5e26\u5b57\u5e55\u5f71\u7247</span></h4>\n"
""
                        "<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u53ef\u4ee5\u628a\u7535\u5f71\u547d\u540d\u4e3a\u7c7b\u4f3c</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-c.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">,</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-C.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\uff0c</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">abp-xxx-CD1-C.mp4 </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7684\u89c4\u5219\u3002</span></h4>\n"
"<h4 style=\" margin-top:12p"
                        "x; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">6\u3001\u591a\u96c6\u5f71\u7247</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u53ef\u4ee5\u628a\u591a\u96c6\u7535\u5f71\u6309\u7167\u96c6\u6570\u540e\u7f00\u547d\u540d\u4e3a\u7c7b\u4f3c</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-cd1.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">, </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-cd2.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600"
                        ";\">, </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">abp-xxx-CD1-C.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7684\u89c4\u5219\uff0c\u53ea\u8981\u542b\u6709</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">-CDn/-cdn</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7c7b\u4f3c\u547d\u540d\u89c4\u5219\uff0c\u5373\u53ef\u4f7f\u7528\u5206\u96c6\u529f\u80fd.**\u4e0d\u652f\u6301-A -B -1 -2,\u5bb9\u6613\u8ddf\u5b57\u5e55\u7684-C\u6df7\u6dc6**.</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">7\u3001\u591a\u96c6\u3001\u5b57\u5e55\u987a\u5e8f</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ff"
                        "ffff;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">abp-xxx-CD1-C.mp4</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">\uff0c</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5206\u96c6\u5728\u524d\uff0c\u5b57\u5e55\u5728\u540e</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">\uff0c</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5b57\u5e55\u5fc5\u987b\u4e0e\u62d3\u5c55\u540d\u9760\u8fd1</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">\uff0c-</span><span style=\" font-family:'Courier'; font-si"
                        "ze:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">C.mp4</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">.</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">8\u3001\u5916\u6302\u5b57\u5e55\u6587\u4ef6</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">\u5b57\u5e55\u6587\u4ef6\u540d</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u5fc5\u987b\u4e0e</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">\u5f71\u7247\u6587"
                        "\u4ef6\u540d</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u4e00\u81f4\uff0c\u624d\u53ef\u4ee5\u4e00\u8d77\u79fb\u52a8\u5230\u65b0\u76ee\u5f55\uff0c\u76ee\u524d\u652f\u6301</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">srt ass sub</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7c7b\u578b\u7684\u5b57\u5e55\u6587\u4ef6\u3002</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u8bbe\u7f6e\u8bf4\u660e\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u56db</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u8bbe\u7f6e\u8bf4\u660e</span></h1>\n"
""
                        "<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:22pt; font-weight:600;\"><br /></h1>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">\u8be6\u7ec6\u7684\u8bf4\u660e\uff1a </span><a href=\"https://github.com/moyy996/AVDC/blob/master/README.md\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC/blob/master/README.md</span></a></h1>\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"><br /></h1>\n"
"<h4 st"
                        "yle=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.1.\u522e\u524a\u6a21\u5f0f/\u6574\u7406\u6a21\u5f0f</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">1\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u522e\u524a\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff1a\u901a\u8fc7\u756a\u53f7\u522e\u524a\u6570\u636e\uff0c\u5305\u62ec\u5143\u6570\u636e\u3001\u5c01\u9762\u56fe\u3001\u7f29\u7565\u56fe\u3001\u80cc\u666f\u56fe\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">2\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6574\u7406\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff1a\u4ec5\u6839\u636e\u5973\u4f18\u628a\u7535\u5f71\u547d\u540d\u4e3a\u756a\u53f7\u5e76\u5206\u7c7b\u5230\u5973\u4f18\u540d\u79f0\u7684\u6587\u4ef6\u5939\u4e0b\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.2.\u8f6f\u94fe\u63a5\u6a21\u5f0f\uff1a\u4f7f\u7528\u6b64\u6a21\u5f0f\uff0c\u8981\u4ee5\u7ba1\u7406\u5458\u8eab\u4efd\u8fd0\u884c\u3002</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u522e\u524a\u5b8c\u4e0d\u79fb\u52a8\u89c6\u9891\uff0c\u800c\u662f\u5728\u76f8\u5e94\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt; color:#ff0000;\">\u521b\u5efa\u8f6f\u94fe\u63a5</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u7c7b\u4f3c\u4e8e\u5feb\u6377\u65b9\u5f0f\uff09\uff0c\u65b9\u4fbfPT\u4e0b\u8f7d\u5b8c\u65e2\u60f3\u522e\u524a\u53c8\u60f3\u7ee7\u7eed\u4e0a\u4f20\u7684\u4ed3\u9f20\u515a\u540c\u5fd7\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4f46\u662f\uff0c\u53ea\u80fd\u5728\u5a92\u4f53\u5e93\u5c55\u793a\uff0c\u4e0d"
                        "</span><span style=\" font-family:'Courier'; font-size:10.5pt; color:#ff0000;\">\u80fd\u5728\u5a92\u4f53\u5e93\u64ad\u653e</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.3.\u8c03\u8bd5\u6a21\u5f0f</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u8f93\u51fa\u756a\u53f7\u7684\u5143\u6570\u636e\uff0c\u5305\u62ec\u5c01\u9762\uff0c\u5bfc\u6f14\uff0c\u6f14\u5458\uff0c\u7b80\u4ecb\u7b49\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><s"
                        "pan style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.4.\u6392\u9664\u76ee\u5f55</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5728\u591a\u5c42\u76ee\u5f55\u522e\u524a\u65f6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u6240\u586b\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.5.\u89c6\u9891\u76ee\u5f55</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u8981\u6574\u7406\u7684\u89c6\u9891\u7684\u76ee\u5f55\uff0c\u4f1a\u904d\u5386\u6b64\u76ee\u5f55\u4e0b\u7684\u6240\u6709\u89c6\u9891\uff0c</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5305\u62ec\u5b50\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e2d\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.6.\u547d\u540d\u89c4\u5219</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" fon"
                        "t-family:'Courier'; font-size:10.5pt;\">1\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u76ee\u5f55\u547d\u540d</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff1a\u5b58\u653e\u89c6\u9891\u6570\u636e\u7684\u76ee\u5f55\u540d\uff0c\u652f\u6301</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u591a\u5c42\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u652f\u6301</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u81ea\u5b9a\u4e49\u7b26\u53f7</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u4f8b\uff1a[actor]/studio/number-\u3010title\u3011\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><sp"
                        "an style=\" font-family:'Courier'; font-size:10.5pt;\">2\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u89c6\u9891\u6807\u9898</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u5a92\u4f53\u5e93\u4e2d\uff09\uff1a</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">nfo</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e2d\u7684\u6807\u9898\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">3\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u89c6\u9891\u6807\u9898</span><span sty"
                        "le=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u672c\u5730\u6587\u4ef6\uff09\uff1a\u672c\u5730\u89c6\u9891\u3001\u56fe\u7247\u7684\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">4\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u53ef\u9009\u9879</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e3a</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">title</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u7247\u540d\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;"
                        "\">actor</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u6f14\u5458\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">studio</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u5236\u4f5c\u5546\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">director</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u5bfc\u6f14\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">release</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u53d1\u552e\u65e5\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">year</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u53d1\u884c\u5e74\u4efd\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">number</"
                        "span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u756a\u53f7\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">runtime</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u65f6\u957f\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">series</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u7cfb\u5217\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">publisher</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u53d1\u884c\u5546\uff09</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.7.\u4ee3\u7406\u8bbe\u7f6e</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\">(1).\u4ee3\u7406</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">proxy=127.0.0.1:1080</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">proxy\u884c\u8bbe\u7f6e</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u672c\u5730\u4ee3\u7406\u5730\u5740\u548c\u7aef\u53e3</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u652f\u6301Shadowxxxx/X,V2XXX\u672c"
                        "\u5730\u4ee3\u7406\u7aef\u53e3\uff0c\u4ee3\u7406\u8f6f\u4ef6\u5f00</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5168\u5c40\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\"> ,\u5efa\u8bae\u4f7f\u7528</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u65e5\u672c\u4ee3\u7406</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5982\u679c\u4e00\u76f4\u62a5Connect Failed! Please check your Proxy or Network!\u9519\u8bef\uff0c\u8bf7</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u68c0\u67e5\u7aef\u53e3\u53f7</span><span style="
                        "\" font-family:'Courier'; font-size:10.5pt;\">\u662f\u5426\u6b63\u786e\uff0c\u6216\u8005\u628aproxy=\u540e\u9762\u7684\u5730\u5740\u548c\u7aef\u53e3</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5220\u9664</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u5e76\u5f00\u542f\u4ee3\u7406\u8f6f\u4ef6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5168\u5c40\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u6216\u8005\u91cd\u542f\u7535\u8111\uff0c\u4ee3\u7406\u8f6f\u4ef6\uff0c\u7f51\u5361\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\">(2).\u8fde\u63a5\u8d85\u65f6\u91cd\u8bd5\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">timeout=10 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">10\u4e3a\u8d85\u65f6\u91cd\u8bd5\u65f6\u95f4 \u5355\u4f4d\uff1a\u79d2\uff0c\u53ef\u9009\u8303\u56f43-10</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\">(3).\u8fde\u63a5\u91cd\u8bd5\u6b21\u6570\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; f"
                        "ont-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">retry=3 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">3\u5373\u4e3a\u91cd\u8bd5\u6b21\u6570\uff0c\u53ef\u9009\u8303\u56f42-5</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.8.\u5a92\u4f53\u5e93\u9009\u62e9</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-fam"
                        "ily:'Courier'; font-size:10.5pt;\">\u5982\u679c\u662fPLEX\uff0c\u8bf7\u5b89\u88c5\u63d2\u4ef6\uff1a</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">XBMCnfoMoviesImporter</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.9.\u6392\u9664\u6307\u5b9a\u5b57\u7b26\u548c\u76ee\u5f55\uff0c\u5b57\u7b26\u4e32</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">1\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u5b57\u7b26</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">:\u6307\u5b9a\u5b57"
                        "\u7b26\u5220\u9664\uff0c\u4f8b\u5982\u6392\u9664\u5b57\u7b26\uff1a \\()\uff0c\u5220\u9664</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u521b\u5efa\u6587\u4ef6\u5939\u65f6</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u7684\\()\u5b57\u7b26</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">2\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">:\u6307\u5b9a\u76ee\u5f55\uff0c\u4f8b\u5982\u6392\u9664\u76ee\u5f55\uff1a failed,JAV_output\uff0c\u591a\u76ee\u5f55\u522e\u524a\u65f6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:"
                        "#ff0000;\">\u8df3\u8fc7</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">failed,JAV_output</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">3\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u5b57\u7b26\u4e32</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">:\u63d0\u53d6\u756a\u53f7\u65f6\uff0c\u5148\u5220\u9664\u6307\u5b9a\u5b57\u7b26\u4e32\uff0c\u63d0\u9ad8\u6210\u529f\u7387\uff0c\u5b57\u7b26\u4e32\u4e4b\u95f4\u7528','\u9694\u5f00\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.10.\u7f51\u7ad9\u9009"
                        "\u62e9</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u53ef\u4ee5\u4f7f\u7528</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6240\u6709\u7f51\u7ad9</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u6216\u8005</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6307\u5b9a\u7f51\u7ad9</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">avsox,javbus,dmm,javdb,fc2club\uff0cmgstage</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff09\u8fdb\u884c\u522e\u524a\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-b"
                        "ottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4ec5\u4f7f\u7528javdb\u8fdb\u884c\u522e\u524a\uff0c</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5c3d\u91cf\u4e0d\u8981\u7528</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u522e\u524a30\u5de6\u53f3\u4f1a\u88abJAVDB</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5c01IP</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e00\u6bb5\u65f6\u95f4\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.11.\u4fdd\u5b58\u65e5\u5fd7</span></h4>\n"
"<p style=\" margin-to"
                        "p:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5f00\u542f\u540e\u65e5\u5fd7\u4fdd\u5b58\u5728</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u7a0b\u5e8f\u76ee\u5f55\u7684Log\u76ee\u5f55\u4e0b</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u7684txt\u6587\u4ef6\u5185\uff0c\u6bcf\u6b21\u8fd0\u884c\u4f1a\u4ea7\u751f\u4e00\u4e2atxt\u6587\u4ef6\uff0ctxt\u6587\u4ef6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u53ef\u4ee5\u5220\u9664</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u4e0d\u5f71\u54cd\u7a0b\u5e8f\u8fd0\u884c\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.12.\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5982\u679c\u522e\u524a\u4e0d\u5230\u5f71\u7247\u4fe1\u606f\uff0c</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u53ef\u9009\u62e9\u4e0d\u79fb\u52a8\u89c6\u9891</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u6216\u8005\u81ea\u52a8\u79fb\u52a8\u5230\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\u4e2d\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\"> </span></p>\n"
"<p style"
                        "=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\"> </span></p></body></html>", None))
        self.label_ico.setText(QCoreApplication.translate("AVDV", u"\u56fe\u6807", None))
        self.pushButton_main.setText(QCoreApplication.translate("AVDV", u"\u4e3b\u754c\u9762", None))
        self.pushButton_log.setText(QCoreApplication.translate("AVDV", u"\u65e5\u5fd7", None))
        self.pushButton_net.setText(QCoreApplication.translate("AVDV", u"\u68c0\u6d4b\u7f51\u7edc", None))
        self.pushButton_tool.setText(QCoreApplication.translate("AVDV", u"\u5de5\u5177", None))
        self.pushButton_setting.setText(QCoreApplication.translate("AVDV", u"\u8bbe\u7f6e", None))
        self.pushButton_about.setText(QCoreApplication.translate("AVDV", u"\u5173\u4e8e", None))
        self.pushButton_close.setText(QCoreApplication.translate("AVDV", u"\u00d7", None))
        self.label_show_version.setText(QCoreApplication.translate("AVDV", u"\u7248\u672c\u53f7", None))
    # retranslateUi

