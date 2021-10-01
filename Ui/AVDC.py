# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVDCTOgPNa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_AVDV(object):
    def setupUi(self, AVDV):
        if not AVDV.objectName():
            AVDV.setObjectName(u"AVDV")
        AVDV.resize(1021, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AVDV.sizePolicy().hasHeightForWidth())
        AVDV.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../Users/gaogao/.designer/Img/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        AVDV.setWindowIcon(icon)
        self.centralwidget = QWidget(AVDV)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(240, 9, 780, 691))
        self.page_avdc = QWidget()
        self.page_avdc.setObjectName(u"page_avdc")
        self.pushButton_start_cap = QPushButton(self.page_avdc)
        self.pushButton_start_cap.setObjectName(u"pushButton_start_cap")
        self.pushButton_start_cap.setGeometry(QRect(650, 13, 120, 40))
        self.label_number1 = QLabel(self.page_avdc)
        self.label_number1.setObjectName(u"label_number1")
        self.label_number1.setGeometry(QRect(0, 70, 50, 40))
        self.label_number1.setLineWidth(0)
        self.label_number = QLabel(self.page_avdc)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setGeometry(QRect(50, 70, 161, 40))
        self.label_number.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_number.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"color:#336699")
        self.label_number.setFrameShape(QFrame.Box)
        self.label_number.setLineWidth(0)
        self.label_13 = QLabel(self.page_avdc)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 530, 50, 40))
        self.label_13.setLineWidth(0)
        self.label_release = QLabel(self.page_avdc)
        self.label_release.setObjectName(u"label_release")
        self.label_release.setGeometry(QRect(50, 530, 220, 40))
        self.label_release.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_release.setFrameShape(QFrame.Box)
        self.label_release.setLineWidth(0)
        self.label_actor1 = QLabel(self.page_avdc)
        self.label_actor1.setObjectName(u"label_actor1")
        self.label_actor1.setGeometry(QRect(220, 70, 50, 40))
        self.label_actor1.setLineWidth(0)
        self.label_actor = QLabel(self.page_avdc)
        self.label_actor.setObjectName(u"label_actor")
        self.label_actor.setGeometry(QRect(270, 70, 161, 40))
        self.label_actor.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_actor.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"color:#336699")
        self.label_actor.setFrameShape(QFrame.Box)
        self.label_actor.setLineWidth(0)
        self.label_outline = QLabel(self.page_avdc)
        self.label_outline.setObjectName(u"label_outline")
        self.label_outline.setGeometry(QRect(50, 430, 500, 40))
        self.label_outline.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_outline.setFrameShape(QFrame.Box)
        self.label_outline.setLineWidth(0)
        self.label_18 = QLabel(self.page_avdc)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 430, 50, 40))
        self.label_18.setLineWidth(0)
        self.label_title = QLabel(self.page_avdc)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(50, 110, 500, 40))
        self.label_title.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_title.setFrameShape(QFrame.Box)
        self.label_title.setLineWidth(0)
        self.label_title1 = QLabel(self.page_avdc)
        self.label_title1.setObjectName(u"label_title1")
        self.label_title1.setGeometry(QRect(0, 110, 50, 40))
        self.label_title1.setLineWidth(0)
        self.label_director = QLabel(self.page_avdc)
        self.label_director.setObjectName(u"label_director")
        self.label_director.setGeometry(QRect(50, 580, 220, 40))
        self.label_director.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_director.setFrameShape(QFrame.Box)
        self.label_director.setLineWidth(0)
        self.label_publish = QLabel(self.page_avdc)
        self.label_publish.setObjectName(u"label_publish")
        self.label_publish.setGeometry(QRect(330, 630, 220, 40))
        self.label_publish.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_publish.setFrameShape(QFrame.Box)
        self.label_publish.setLineWidth(0)
        self.label_23 = QLabel(self.page_avdc)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 580, 50, 40))
        self.label_23.setLineWidth(0)
        self.label_24 = QLabel(self.page_avdc)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(280, 630, 50, 40))
        self.label_24.setLineWidth(0)
        self.label_studio = QLabel(self.page_avdc)
        self.label_studio.setObjectName(u"label_studio")
        self.label_studio.setGeometry(QRect(50, 630, 220, 40))
        self.label_studio.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_studio.setFrameShape(QFrame.Box)
        self.label_studio.setLineWidth(0)
        self.label_series = QLabel(self.page_avdc)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setGeometry(QRect(330, 580, 220, 40))
        self.label_series.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_series.setFrameShape(QFrame.Box)
        self.label_series.setLineWidth(0)
        self.label_30 = QLabel(self.page_avdc)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 630, 50, 40))
        self.label_30.setLineWidth(0)
        self.label_31 = QLabel(self.page_avdc)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(280, 580, 50, 40))
        self.label_31.setLineWidth(0)
        self.label_tag = QLabel(self.page_avdc)
        self.label_tag.setObjectName(u"label_tag")
        self.label_tag.setGeometry(QRect(50, 480, 500, 40))
        self.label_tag.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_tag.setFrameShape(QFrame.Box)
        self.label_tag.setLineWidth(0)
        self.label_33 = QLabel(self.page_avdc)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(0, 480, 50, 40))
        self.label_33.setLineWidth(0)
        self.checkBox_cover = QCheckBox(self.page_avdc)
        self.checkBox_cover.setObjectName(u"checkBox_cover")
        self.checkBox_cover.setGeometry(QRect(50, 390, 291, 30))
        self.label_result = QLabel(self.page_avdc)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(570, 70, 211, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy1)
        self.label_result.setMinimumSize(QSize(0, 0))
        self.label_result.setMaximumSize(QSize(16777215, 16777215))
        self.label_result.setCursor(QCursor(Qt.ArrowCursor))
        self.label_result.setLayoutDirection(Qt.LeftToRight)
        self.label_result.setAutoFillBackground(False)
        self.label_result.setFrameShape(QFrame.Box)
        self.label_result.setLineWidth(0)
        self.label_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22 = QLabel(self.page_avdc)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(280, 530, 50, 40))
        self.label_22.setLineWidth(0)
        self.label_runtime = QLabel(self.page_avdc)
        self.label_runtime.setObjectName(u"label_runtime")
        self.label_runtime.setGeometry(QRect(330, 530, 220, 40))
        self.label_runtime.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_runtime.setFrameShape(QFrame.Box)
        self.label_runtime.setLineWidth(0)
        self.line_6 = QFrame(self.page_avdc)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(50, 460, 500, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.page_avdc)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(50, 510, 500, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.page_avdc)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(50, 560, 220, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_9 = QFrame(self.page_avdc)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(330, 560, 220, 20))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_10 = QFrame(self.page_avdc)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(330, 610, 220, 20))
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_11 = QFrame(self.page_avdc)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(330, 660, 220, 20))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_12 = QFrame(self.page_avdc)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(50, 610, 220, 20))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_13 = QFrame(self.page_avdc)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(50, 660, 220, 20))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.label_thumb = QLabel(self.page_avdc)
        self.label_thumb.setObjectName(u"label_thumb")
        self.label_thumb.setEnabled(True)
        self.label_thumb.setGeometry(QRect(222, 160, 328, 220))
        self.label_thumb.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_thumb.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_thumb.setFrameShape(QFrame.Box)
        self.label_thumb.setAlignment(Qt.AlignCenter)
        self.label_thumb.setMargin(0)
        self.label_poster = QLabel(self.page_avdc)
        self.label_poster.setObjectName(u"label_poster")
        self.label_poster.setGeometry(QRect(50, 160, 156, 220))
        sizePolicy1.setHeightForWidth(self.label_poster.sizePolicy().hasHeightForWidth())
        self.label_poster.setSizePolicy(sizePolicy1)
        self.label_poster.setMinimumSize(QSize(156, 220))
        self.label_poster.setMaximumSize(QSize(156, 220))
        self.label_poster.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_poster.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_poster.setFrameShape(QFrame.Box)
        self.label_poster.setAlignment(Qt.AlignCenter)
        self.label_poster1 = QLabel(self.page_avdc)
        self.label_poster1.setObjectName(u"label_poster1")
        self.label_poster1.setGeometry(QRect(0, 150, 50, 40))
        self.label_poster1.setLineWidth(0)
        self.treeWidget_number = QTreeWidget(self.page_avdc)
        font = QFont()
        font.setFamily(u"Courier")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget_number.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget_number)
        QTreeWidgetItem(self.treeWidget_number)
        self.treeWidget_number.setObjectName(u"treeWidget_number")
        self.treeWidget_number.setGeometry(QRect(570, 110, 202, 563))
        self.treeWidget_number.setFrameShape(QFrame.Box)
        self.treeWidget_number.setFrameShadow(QFrame.Plain)
        self.treeWidget_number.setLineWidth(0)
        self.treeWidget_number.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.treeWidget_number.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.treeWidget_number.setAutoScrollMargin(2)
        self.treeWidget_number.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.treeWidget_number.setTabKeyNavigation(False)
        self.treeWidget_number.setProperty("showDropIndicator", True)
        self.treeWidget_number.setTextElideMode(Qt.ElideRight)
        self.treeWidget_number.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeWidget_number.setIndentation(10)
        self.treeWidget_number.setRootIsDecorated(True)
        self.treeWidget_number.setUniformRowHeights(True)
        self.treeWidget_number.setItemsExpandable(True)
        self.treeWidget_number.setSortingEnabled(False)
        self.treeWidget_number.setAnimated(False)
        self.treeWidget_number.setAllColumnsShowFocus(False)
        self.treeWidget_number.setHeaderHidden(True)
        self.treeWidget_number.header().setProperty("showSortIndicator", False)
        self.label_file_path = QLabel(self.page_avdc)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setGeometry(QRect(0, 10, 800, 50))
        self.label_file_path.setStyleSheet(u"")
        self.label_file_path.setFrameShape(QFrame.Box)
        self.label_file_path.setLineWidth(0)
        self.line_14 = QFrame(self.page_avdc)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(0, 60, 771, 20))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.label_source = QLabel(self.page_avdc)
        self.label_source.setObjectName(u"label_source")
        self.label_source.setGeometry(QRect(430, 70, 121, 40))
        self.label_source.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_source.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_source.setFrameShape(QFrame.Box)
        self.label_source.setLineWidth(0)
        self.label_source.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_19 = QLabel(self.page_avdc)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(390, 390, 131, 31))
        self.label_19.setStyleSheet(u"color: rgba(0, 0, 0, 153);")
        self.label_19.setLineWidth(0)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
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
        self.label_19.raise_()
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.textBrowser_log_main = QTextBrowser(self.page_log)
        self.textBrowser_log_main.setObjectName(u"textBrowser_log_main")
        self.textBrowser_log_main.setGeometry(QRect(0, 0, 780, 680))
        self.textBrowser_log_main.setStyleSheet(u"")
        self.pushButton_start_cap2 = QPushButton(self.page_log)
        self.pushButton_start_cap2.setObjectName(u"pushButton_start_cap2")
        self.pushButton_start_cap2.setGeometry(QRect(650, 13, 120, 40))
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
        self.stackedWidget.addWidget(self.page_net)
        self.page_tool = QWidget()
        self.page_tool.setObjectName(u"page_tool")
        self.groupBox_6 = QGroupBox(self.page_tool)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(30, 10, 701, 161))
        self.groupBox_6.setStyleSheet(u"font:\"Courier\";")
        self.pushButton_move_mp4 = QPushButton(self.groupBox_6)
        self.pushButton_move_mp4.setObjectName(u"pushButton_move_mp4")
        self.pushButton_move_mp4.setGeometry(QRect(140, 70, 341, 40))
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(70, 30, 80, 30))
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_escape_dir_move = QLineEdit(self.groupBox_6)
        self.lineEdit_escape_dir_move.setObjectName(u"lineEdit_escape_dir_move")
        self.lineEdit_escape_dir_move.setGeometry(QRect(140, 30, 341, 30))
        self.lineEdit_escape_dir_move.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 120, 591, 31))
        self.label_8.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_7 = QGroupBox(self.page_tool)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(30, 190, 701, 301))
        self.groupBox_7.setStyleSheet(u"font:\"Courier\";")
        self.pushButton_select_file = QPushButton(self.groupBox_7)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setGeometry(QRect(510, 40, 151, 40))
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
        self.comboBox_website.setGeometry(QRect(140, 80, 351, 30))
        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 80, 30))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_appoint_url = QLineEdit(self.groupBox_7)
        self.lineEdit_appoint_url.setObjectName(u"lineEdit_appoint_url")
        self.lineEdit_appoint_url.setGeometry(QRect(140, 120, 351, 30))
        self.lineEdit_appoint_url.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 120, 80, 30))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_movie_number = QLineEdit(self.groupBox_7)
        self.lineEdit_movie_number.setObjectName(u"lineEdit_movie_number")
        self.lineEdit_movie_number.setGeometry(QRect(140, 160, 351, 30))
        self.lineEdit_movie_number.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 160, 80, 30))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_start_single_file = QPushButton(self.groupBox_7)
        self.pushButton_start_single_file.setObjectName(u"pushButton_start_single_file")
        self.pushButton_start_single_file.setGeometry(QRect(140, 200, 351, 40))
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 40, 80, 30))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 250, 611, 41))
        self.label.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_single_file_path = QLineEdit(self.groupBox_7)
        self.lineEdit_single_file_path.setObjectName(u"lineEdit_single_file_path")
        self.lineEdit_single_file_path.setGeometry(QRect(140, 40, 351, 30))
        self.lineEdit_single_file_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.pushButton_select_file_clear_info = QPushButton(self.groupBox_7)
        self.pushButton_select_file_clear_info.setObjectName(u"pushButton_select_file_clear_info")
        self.pushButton_select_file_clear_info.setGeometry(QRect(510, 110, 151, 40))
        self.groupBox_13 = QGroupBox(self.page_tool)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(30, 510, 701, 141))
        self.groupBox_13.setStyleSheet(u"font:\"Courier\";")
        self.pushButton_select_thumb = QPushButton(self.groupBox_13)
        self.pushButton_select_thumb.setObjectName(u"pushButton_select_thumb")
        self.pushButton_select_thumb.setGeometry(QRect(140, 80, 351, 40))
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 551, 31))
        self.label_6.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_tool)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.tabWidget = QTabWidget(self.page_setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 781, 681))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setIconSize(QSize(16, 20))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab2.sizePolicy().hasHeightForWidth())
        self.tab2.setSizePolicy(sizePolicy2)
        self.scrollArea_2 = QScrollArea(self.tab2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 771, 654))
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 771, 777))
        self.groupBox_16 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(30, 10, 701, 311))
        self.groupBox_16.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_7 = QWidget(self.groupBox_16)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(20, 30, 661, 271))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.gridLayoutWidget_7)
        self.label_46.setObjectName(u"label_46")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy3)
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setLayoutDirection(Qt.RightToLeft)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_46, 4, 0, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_7)
        self.label_47.setObjectName(u"label_47")
        sizePolicy3.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy3)
        self.label_47.setMinimumSize(QSize(0, 0))
        self.label_47.setLayoutDirection(Qt.RightToLeft)
        self.label_47.setFrameShape(QFrame.NoFrame)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_47, 2, 0, 1, 1)

        self.lineEdit_movie_path = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_movie_path.setObjectName(u"lineEdit_movie_path")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_movie_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_path.setSizePolicy(sizePolicy4)
        self.lineEdit_movie_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_movie_path.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_movie_path, 0, 1, 1, 1)

        self.lineEdit_escape_dir = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_escape_dir.setObjectName(u"lineEdit_escape_dir")
        sizePolicy4.setHeightForWidth(self.lineEdit_escape_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_dir.setSizePolicy(sizePolicy4)
        self.lineEdit_escape_dir.setMinimumSize(QSize(0, 30))
        self.lineEdit_escape_dir.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_escape_dir, 6, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_7)
        self.label_29.setObjectName(u"label_29")
        sizePolicy4.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy4)
        self.label_29.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_29, 3, 1, 1, 1)

        self.lineEdit_fail = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_fail.setObjectName(u"lineEdit_fail")
        sizePolicy4.setHeightForWidth(self.lineEdit_fail.sizePolicy().hasHeightForWidth())
        self.lineEdit_fail.setSizePolicy(sizePolicy4)
        self.lineEdit_fail.setMinimumSize(QSize(0, 30))
        self.lineEdit_fail.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_fail, 4, 1, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_7)
        self.label_48.setObjectName(u"label_48")
        sizePolicy4.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy4)
        self.label_48.setMinimumSize(QSize(130, 0))
        self.label_48.setLayoutDirection(Qt.RightToLeft)
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_48, 6, 0, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_7)
        self.label_49.setObjectName(u"label_49")
        sizePolicy3.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy3)
        self.label_49.setMinimumSize(QSize(0, 0))
        self.label_49.setLayoutDirection(Qt.RightToLeft)
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget_7)
        self.label_56.setObjectName(u"label_56")
        sizePolicy4.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy4)
        self.label_56.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_56, 1, 1, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_7)
        self.label_57.setObjectName(u"label_57")
        sizePolicy4.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy4)
        self.label_57.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_57, 5, 1, 1, 1)

        self.lineEdit_success = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_success.setObjectName(u"lineEdit_success")
        sizePolicy4.setHeightForWidth(self.lineEdit_success.sizePolicy().hasHeightForWidth())
        self.lineEdit_success.setSizePolicy(sizePolicy4)
        self.lineEdit_success.setMinimumSize(QSize(0, 30))
        self.lineEdit_success.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_success, 2, 1, 1, 1)

        self.label_58 = QLabel(self.gridLayoutWidget_7)
        self.label_58.setObjectName(u"label_58")
        sizePolicy4.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy4)
        self.label_58.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_58, 7, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(30, 540, 701, 131))
        self.groupBox_9.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_16 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(20, 30, 661, 91))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_movie_type_2 = QLineEdit(self.gridLayoutWidget_16)
        self.lineEdit_movie_type_2.setObjectName(u"lineEdit_movie_type_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_movie_type_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_type_2.setSizePolicy(sizePolicy4)
        self.lineEdit_movie_type_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_movie_type_2.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_16.addWidget(self.lineEdit_movie_type_2, 0, 1, 1, 1)

        self.label_78 = QLabel(self.gridLayoutWidget_16)
        self.label_78.setObjectName(u"label_78")
        sizePolicy3.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy3)
        self.label_78.setMinimumSize(QSize(0, 30))
        self.label_78.setLayoutDirection(Qt.RightToLeft)
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_78, 1, 0, 1, 1)

        self.lineEdit_sub_type_2 = QLineEdit(self.gridLayoutWidget_16)
        self.lineEdit_sub_type_2.setObjectName(u"lineEdit_sub_type_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_sub_type_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_sub_type_2.setSizePolicy(sizePolicy4)
        self.lineEdit_sub_type_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_sub_type_2.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_16.addWidget(self.lineEdit_sub_type_2, 1, 1, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget_16)
        self.label_50.setObjectName(u"label_50")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy5)
        self.label_50.setMinimumSize(QSize(130, 0))
        self.label_50.setLayoutDirection(Qt.RightToLeft)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_50, 0, 0, 1, 1)

        self.groupBox_32 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setGeometry(QRect(30, 340, 701, 181))
        self.groupBox_32.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_19 = QWidget(self.groupBox_32)
        self.gridLayoutWidget_19.setObjectName(u"gridLayoutWidget_19")
        self.gridLayoutWidget_19.setGeometry(QRect(20, 30, 662, 139))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_escape_string_2 = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_escape_string_2.setObjectName(u"lineEdit_escape_string_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_escape_string_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_string_2.setSizePolicy(sizePolicy6)
        self.lineEdit_escape_string_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_escape_string_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_escape_string_2.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_19.addWidget(self.lineEdit_escape_string_2, 0, 1, 1, 1)

        self.label_83 = QLabel(self.gridLayoutWidget_19)
        self.label_83.setObjectName(u"label_83")
        sizePolicy3.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy3)
        self.label_83.setMinimumSize(QSize(130, 0))
        self.label_83.setLayoutDirection(Qt.RightToLeft)
        self.label_83.setFrameShape(QFrame.NoFrame)
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_83, 0, 0, 1, 1)

        self.label_88 = QLabel(self.gridLayoutWidget_19)
        self.label_88.setObjectName(u"label_88")
        sizePolicy4.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy4)
        self.label_88.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_19.addWidget(self.label_88, 1, 1, 1, 1)

        self.lineEdit_escape_size = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_escape_size.setObjectName(u"lineEdit_escape_size")
        sizePolicy6.setHeightForWidth(self.lineEdit_escape_size.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_size.setSizePolicy(sizePolicy6)
        self.lineEdit_escape_size.setMinimumSize(QSize(0, 30))
        self.lineEdit_escape_size.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_escape_size.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_19.addWidget(self.lineEdit_escape_size, 2, 1, 1, 1)

        self.label_94 = QLabel(self.gridLayoutWidget_19)
        self.label_94.setObjectName(u"label_94")
        sizePolicy4.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy4)
        self.label_94.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_19.addWidget(self.label_94, 3, 1, 1, 1)

        self.label_93 = QLabel(self.gridLayoutWidget_19)
        self.label_93.setObjectName(u"label_93")
        sizePolicy4.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy4)
        self.label_93.setMinimumSize(QSize(0, 0))
        self.label_93.setLayoutDirection(Qt.RightToLeft)
        self.label_93.setFrameShape(QFrame.NoFrame)
        self.label_93.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_93, 2, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab2, "")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 771, 654))
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 771, 1388))
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 110, 701, 191))
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.groupBox.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(50, 30, 641, 131))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_read = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_read.setObjectName(u"radioButton_read")
        sizePolicy3.setHeightForWidth(self.radioButton_read.sizePolicy().hasHeightForWidth())
        self.radioButton_read.setSizePolicy(sizePolicy3)
        self.radioButton_read.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.radioButton_read, 2, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_2.addWidget(self.label_16, 2, 1, 1, 1)

        self.radioButton_sort = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_sort.setObjectName(u"radioButton_sort")
        sizePolicy3.setHeightForWidth(self.radioButton_sort.sizePolicy().hasHeightForWidth())
        self.radioButton_sort.setSizePolicy(sizePolicy3)
        self.radioButton_sort.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.radioButton_sort, 1, 0, 1, 1)

        self.radioButton_common = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_common.setObjectName(u"radioButton_common")
        self.radioButton_common.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.radioButton_common.sizePolicy().hasHeightForWidth())
        self.radioButton_common.setSizePolicy(sizePolicy3)
        self.radioButton_common.setMinimumSize(QSize(80, 0))
        self.radioButton_common.setAutoRepeatDelay(300)

        self.gridLayout_2.addWidget(self.radioButton_common, 0, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_2.addWidget(self.label_15, 1, 1, 1, 1)

        self.checkBox_read_no_nfo_scrape = QCheckBox(self.groupBox)
        self.checkBox_read_no_nfo_scrape.setObjectName(u"checkBox_read_no_nfo_scrape")
        self.checkBox_read_no_nfo_scrape.setGeometry(QRect(140, 160, 261, 16))
        sizePolicy3.setHeightForWidth(self.checkBox_read_no_nfo_scrape.sizePolicy().hasHeightForWidth())
        self.checkBox_read_no_nfo_scrape.setSizePolicy(sizePolicy3)
        self.checkBox_read_no_nfo_scrape.setMinimumSize(QSize(0, 0))
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 320, 701, 111))
        self.groupBox_5.setMinimumSize(QSize(200, 0))
        self.groupBox_5.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget = QWidget(self.groupBox_5)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_like_speed = QRadioButton(self.gridLayoutWidget)
        self.radioButton_like_speed.setObjectName(u"radioButton_like_speed")
        sizePolicy3.setHeightForWidth(self.radioButton_like_speed.sizePolicy().hasHeightForWidth())
        self.radioButton_like_speed.setSizePolicy(sizePolicy3)
        self.radioButton_like_speed.setMinimumSize(QSize(80, 0))
        self.radioButton_like_speed.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.radioButton_like_speed, 0, 0, 1, 1)

        self.radioButton_like_more = QRadioButton(self.gridLayoutWidget)
        self.radioButton_like_more.setObjectName(u"radioButton_like_more")

        self.gridLayout.addWidget(self.radioButton_like_more, 1, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy4.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy4)
        self.label_28.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy4.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy4)
        self.label_32.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_32, 1, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(30, 10, 701, 81))
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
        self.comboBox_website_all.setGeometry(QRect(20, 30, 661, 40))
        sizePolicy6.setHeightForWidth(self.comboBox_website_all.sizePolicy().hasHeightForWidth())
        self.comboBox_website_all.setSizePolicy(sizePolicy6)
        self.comboBox_website_all.setMinimumSize(QSize(400, 40))
        self.comboBox_website_all.setMaximumSize(QSize(16000, 40))
        self.comboBox_website_all.setSizeIncrement(QSize(0, 0))
        self.comboBox_website_all.setStyleSheet(u"")
        self.comboBox_website_all.setFrame(False)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 650, 701, 111))
        self.groupBox_2.setMinimumSize(QSize(200, 0))
        self.groupBox_2.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(50, 30, 649, 71))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.gridLayoutWidget_4)
        self.label_36.setObjectName(u"label_36")
        sizePolicy4.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy4)
        self.label_36.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_4.addWidget(self.label_36, 0, 1, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_4)
        self.label_37.setObjectName(u"label_37")
        sizePolicy4.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy4)
        self.label_37.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_4.addWidget(self.label_37, 1, 1, 1, 1)

        self.radioButton_soft_on = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_soft_on.setObjectName(u"radioButton_soft_on")
        sizePolicy3.setHeightForWidth(self.radioButton_soft_on.sizePolicy().hasHeightForWidth())
        self.radioButton_soft_on.setSizePolicy(sizePolicy3)
        self.radioButton_soft_on.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.radioButton_soft_on, 0, 0, 1, 1)

        self.radioButton_soft_off = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_soft_off.setObjectName(u"radioButton_soft_off")

        self.gridLayout_4.addWidget(self.radioButton_soft_off, 1, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(30, 1040, 701, 111))
        self.groupBox_18.setMinimumSize(QSize(200, 0))
        self.groupBox_18.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_13 = QWidget(self.groupBox_18)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.gridLayoutWidget_13)
        self.label_38.setObjectName(u"label_38")
        sizePolicy4.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy4)
        self.label_38.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_13.addWidget(self.label_38, 0, 1, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_13)
        self.label_39.setObjectName(u"label_39")
        sizePolicy4.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy4)
        self.label_39.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_13.addWidget(self.label_39, 1, 1, 1, 1)

        self.radioButton_succ_rename_on = QRadioButton(self.gridLayoutWidget_13)
        self.radioButton_succ_rename_on.setObjectName(u"radioButton_succ_rename_on")
        sizePolicy3.setHeightForWidth(self.radioButton_succ_rename_on.sizePolicy().hasHeightForWidth())
        self.radioButton_succ_rename_on.setSizePolicy(sizePolicy3)
        self.radioButton_succ_rename_on.setMinimumSize(QSize(80, 0))

        self.gridLayout_13.addWidget(self.radioButton_succ_rename_on, 0, 0, 1, 1)

        self.radioButton_succ_rename_off = QRadioButton(self.gridLayoutWidget_13)
        self.radioButton_succ_rename_off.setObjectName(u"radioButton_succ_rename_off")

        self.gridLayout_13.addWidget(self.radioButton_succ_rename_off, 1, 0, 1, 1)

        self.groupBox_27 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setGeometry(QRect(30, 780, 701, 111))
        self.groupBox_27.setMinimumSize(QSize(200, 0))
        self.groupBox_27.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_6 = QWidget(self.groupBox_27)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.gridLayoutWidget_6)
        self.label_54.setObjectName(u"label_54")
        sizePolicy4.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy4)
        self.label_54.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_6.addWidget(self.label_54, 0, 1, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_6)
        self.label_55.setObjectName(u"label_55")
        sizePolicy4.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy4)
        self.label_55.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_6.addWidget(self.label_55, 1, 1, 1, 1)

        self.radioButton_succ_move_on = QRadioButton(self.gridLayoutWidget_6)
        self.radioButton_succ_move_on.setObjectName(u"radioButton_succ_move_on")
        sizePolicy3.setHeightForWidth(self.radioButton_succ_move_on.sizePolicy().hasHeightForWidth())
        self.radioButton_succ_move_on.setSizePolicy(sizePolicy3)
        self.radioButton_succ_move_on.setMinimumSize(QSize(80, 0))

        self.gridLayout_6.addWidget(self.radioButton_succ_move_on, 0, 0, 1, 1)

        self.radioButton_succ_move_off = QRadioButton(self.gridLayoutWidget_6)
        self.radioButton_succ_move_off.setObjectName(u"radioButton_succ_move_off")

        self.gridLayout_6.addWidget(self.radioButton_succ_move_off, 1, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(30, 910, 701, 111))
        self.groupBox_15.setMinimumSize(QSize(200, 0))
        self.groupBox_15.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_3 = QWidget(self.groupBox_15)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")
        sizePolicy4.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy4)
        self.label_34.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_3.addWidget(self.label_34, 0, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_3)
        self.label_35.setObjectName(u"label_35")
        sizePolicy4.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy4)
        self.label_35.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_3.addWidget(self.label_35, 1, 1, 1, 1)

        self.radioButton_fail_move_on = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_fail_move_on.setObjectName(u"radioButton_fail_move_on")
        sizePolicy3.setHeightForWidth(self.radioButton_fail_move_on.sizePolicy().hasHeightForWidth())
        self.radioButton_fail_move_on.setSizePolicy(sizePolicy3)
        self.radioButton_fail_move_on.setMinimumSize(QSize(80, 0))

        self.gridLayout_3.addWidget(self.radioButton_fail_move_on, 0, 0, 1, 1)

        self.radioButton_fail_move_off = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_fail_move_off.setObjectName(u"radioButton_fail_move_off")

        self.gridLayout_3.addWidget(self.radioButton_fail_move_off, 1, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setGeometry(QRect(30, 450, 701, 181))
        self.gridLayoutWidget_20 = QWidget(self.groupBox_23)
        self.gridLayoutWidget_20.setObjectName(u"gridLayoutWidget_20")
        self.gridLayoutWidget_20.setGeometry(QRect(50, 30, 641, 141))
        self.gridLayout_20 = QGridLayout(self.gridLayoutWidget_20)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.checkBox_more_dmm = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_more_dmm.setObjectName(u"checkBox_more_dmm")
        sizePolicy3.setHeightForWidth(self.checkBox_more_dmm.sizePolicy().hasHeightForWidth())
        self.checkBox_more_dmm.setSizePolicy(sizePolicy3)
        self.checkBox_more_dmm.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.checkBox_more_dmm, 3, 0, 1, 1)

        self.checkBox_more_jav321 = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_more_jav321.setObjectName(u"checkBox_more_jav321")
        sizePolicy3.setHeightForWidth(self.checkBox_more_jav321.sizePolicy().hasHeightForWidth())
        self.checkBox_more_jav321.setSizePolicy(sizePolicy3)
        self.checkBox_more_jav321.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.checkBox_more_jav321, 1, 0, 1, 1)

        self.label_71 = QLabel(self.gridLayoutWidget_20)
        self.label_71.setObjectName(u"label_71")
        sizePolicy4.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy4)
        self.label_71.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_20.addWidget(self.label_71, 1, 1, 1, 1)

        self.checkBox_more_javdb = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_more_javdb.setObjectName(u"checkBox_more_javdb")
        sizePolicy3.setHeightForWidth(self.checkBox_more_javdb.sizePolicy().hasHeightForWidth())
        self.checkBox_more_javdb.setSizePolicy(sizePolicy3)
        self.checkBox_more_javdb.setMinimumSize(QSize(80, 0))

        self.gridLayout_20.addWidget(self.checkBox_more_javdb, 0, 0, 1, 1)

        self.label_62 = QLabel(self.gridLayoutWidget_20)
        self.label_62.setObjectName(u"label_62")
        sizePolicy4.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy4)
        self.label_62.setMinimumSize(QSize(0, 0))
        self.label_62.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_20.addWidget(self.label_62, 0, 1, 1, 1)

        self.label_92 = QLabel(self.gridLayoutWidget_20)
        self.label_92.setObjectName(u"label_92")
        sizePolicy4.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy4)
        self.label_92.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_20.addWidget(self.label_92, 3, 1, 1, 1)

        self.checkBox_more_javlibrary = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_more_javlibrary.setObjectName(u"checkBox_more_javlibrary")
        sizePolicy3.setHeightForWidth(self.checkBox_more_javlibrary.sizePolicy().hasHeightForWidth())
        self.checkBox_more_javlibrary.setSizePolicy(sizePolicy3)
        self.checkBox_more_javlibrary.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.checkBox_more_javlibrary, 2, 0, 1, 1)

        self.label_72 = QLabel(self.gridLayoutWidget_20)
        self.label_72.setObjectName(u"label_72")
        sizePolicy4.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy4)
        self.label_72.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_20.addWidget(self.label_72, 2, 1, 1, 1)

        self.groupBox_30 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setGeometry(QRect(30, 1170, 701, 111))
        self.groupBox_30.setMinimumSize(QSize(200, 0))
        self.groupBox_30.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_23 = QWidget(self.groupBox_30)
        self.gridLayoutWidget_23.setObjectName(u"gridLayoutWidget_23")
        self.gridLayoutWidget_23.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_23)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.gridLayoutWidget_23)
        self.label_44.setObjectName(u"label_44")
        sizePolicy4.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy4)
        self.label_44.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_23.addWidget(self.label_44, 0, 1, 1, 1)

        self.label_51 = QLabel(self.gridLayoutWidget_23)
        self.label_51.setObjectName(u"label_51")
        sizePolicy4.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy4)
        self.label_51.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_23.addWidget(self.label_51, 1, 1, 1, 1)

        self.radioButton_del_empty_folder_on = QRadioButton(self.gridLayoutWidget_23)
        self.radioButton_del_empty_folder_on.setObjectName(u"radioButton_del_empty_folder_on")
        sizePolicy3.setHeightForWidth(self.radioButton_del_empty_folder_on.sizePolicy().hasHeightForWidth())
        self.radioButton_del_empty_folder_on.setSizePolicy(sizePolicy3)
        self.radioButton_del_empty_folder_on.setMinimumSize(QSize(80, 0))

        self.gridLayout_23.addWidget(self.radioButton_del_empty_folder_on, 0, 0, 1, 1)

        self.radioButton_del_empty_folder_off = QRadioButton(self.gridLayoutWidget_23)
        self.radioButton_del_empty_folder_off.setObjectName(u"radioButton_del_empty_folder_off")

        self.gridLayout_23.addWidget(self.radioButton_del_empty_folder_off, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.scrollArea_6 = QScrollArea(self.tab_4)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setEnabled(True)
        self.scrollArea_6.setGeometry(QRect(0, 0, 771, 654))
        sizePolicy2.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy2)
        self.scrollArea_6.setFrameShape(QFrame.Box)
        self.scrollArea_6.setLineWidth(0)
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_6.setWidgetResizable(False)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 771, 846))
        self.groupBox_34 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setGeometry(QRect(30, 180, 701, 181))
        self.groupBox_34.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_19 = QWidget(self.groupBox_34)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(60, 30, 391, 37))
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.checkBox_download_extrafanart = QCheckBox(self.horizontalLayoutWidget_19)
        self.checkBox_download_extrafanart.setObjectName(u"checkBox_download_extrafanart")

        self.horizontalLayout_24.addWidget(self.checkBox_download_extrafanart)

        self.checkBox_download_extrafanart_copy = QCheckBox(self.horizontalLayoutWidget_19)
        self.checkBox_download_extrafanart_copy.setObjectName(u"checkBox_download_extrafanart_copy")

        self.horizontalLayout_24.addWidget(self.checkBox_download_extrafanart_copy)

        self.label_82 = QLabel(self.groupBox_34)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(60, 70, 641, 41))
        sizePolicy4.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy4)
        self.label_82.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_59 = QLabel(self.groupBox_34)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(60, 110, 641, 61))
        sizePolicy4.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy4)
        self.label_59.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.lineEdit_extrafanart_dir = QLineEdit(self.groupBox_34)
        self.lineEdit_extrafanart_dir.setObjectName(u"lineEdit_extrafanart_dir")
        self.lineEdit_extrafanart_dir.setGeometry(QRect(370, 30, 311, 30))
        sizePolicy4.setHeightForWidth(self.lineEdit_extrafanart_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_extrafanart_dir.setSizePolicy(sizePolicy4)
        self.lineEdit_extrafanart_dir.setMinimumSize(QSize(300, 30))
        self.lineEdit_extrafanart_dir.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.groupBox_24 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(30, 10, 701, 151))
        self.groupBox_24.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_14 = QWidget(self.groupBox_24)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_download_poster = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_poster.setObjectName(u"checkBox_download_poster")

        self.horizontalLayout_16.addWidget(self.checkBox_download_poster)

        self.checkBox_download_thumb = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_thumb.setObjectName(u"checkBox_download_thumb")

        self.horizontalLayout_16.addWidget(self.checkBox_download_thumb)

        self.checkBox_download_fanart = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_fanart.setObjectName(u"checkBox_download_fanart")

        self.horizontalLayout_16.addWidget(self.checkBox_download_fanart)

        self.checkBox_download_nfo = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_nfo.setObjectName(u"checkBox_download_nfo")

        self.horizontalLayout_16.addWidget(self.checkBox_download_nfo)

        self.label_85 = QLabel(self.groupBox_24)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(60, 60, 641, 81))
        sizePolicy4.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy4)
        self.label_85.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_22 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setGeometry(QRect(30, 630, 701, 111))
        self.groupBox_22.setMinimumSize(QSize(200, 0))
        self.groupBox_22.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_15 = QWidget(self.groupBox_22)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(60, 30, 621, 71))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.gridLayoutWidget_15)
        self.label_40.setObjectName(u"label_40")
        sizePolicy4.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy4)
        self.label_40.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_15.addWidget(self.label_40, 0, 1, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_15)
        self.label_42.setObjectName(u"label_42")
        sizePolicy4.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy4)
        self.label_42.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_15.addWidget(self.label_42, 1, 1, 1, 1)

        self.radioButton_series_as_set_on = QRadioButton(self.gridLayoutWidget_15)
        self.radioButton_series_as_set_on.setObjectName(u"radioButton_series_as_set_on")
        sizePolicy3.setHeightForWidth(self.radioButton_series_as_set_on.sizePolicy().hasHeightForWidth())
        self.radioButton_series_as_set_on.setSizePolicy(sizePolicy3)
        self.radioButton_series_as_set_on.setMinimumSize(QSize(80, 0))

        self.gridLayout_15.addWidget(self.radioButton_series_as_set_on, 0, 0, 1, 1)

        self.radioButton_series_as_set_off = QRadioButton(self.gridLayoutWidget_15)
        self.radioButton_series_as_set_off.setObjectName(u"radioButton_series_as_set_off")

        self.gridLayout_15.addWidget(self.radioButton_series_as_set_off, 1, 0, 1, 1)

        self.groupBox_39 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setGeometry(QRect(30, 500, 701, 111))
        self.groupBox_39.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_5 = QWidget(self.groupBox_39)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(60, 30, 621, 71))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.radioButton_poster_official = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_poster_official.setObjectName(u"radioButton_poster_official")
        sizePolicy3.setHeightForWidth(self.radioButton_poster_official.sizePolicy().hasHeightForWidth())
        self.radioButton_poster_official.setSizePolicy(sizePolicy3)
        self.radioButton_poster_official.setMinimumSize(QSize(80, 0))

        self.gridLayout_5.addWidget(self.radioButton_poster_official, 1, 0, 1, 1)

        self.radioButton_poster_cut = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_poster_cut.setObjectName(u"radioButton_poster_cut")
        self.radioButton_poster_cut.setMinimumSize(QSize(80, 0))

        self.gridLayout_5.addWidget(self.radioButton_poster_cut, 0, 0, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget_5)
        self.label_53.setObjectName(u"label_53")
        sizePolicy4.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy4)
        self.label_53.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_53, 0, 1, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget_5)
        self.label_52.setObjectName(u"label_52")
        sizePolicy4.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy4)
        self.label_52.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_52, 1, 1, 1, 1)

        self.groupBox_33 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setGeometry(QRect(30, 380, 701, 101))
        self.groupBox_33.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_18 = QWidget(self.groupBox_33)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.checkBox_old_poster = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_poster.setObjectName(u"checkBox_old_poster")

        self.horizontalLayout_23.addWidget(self.checkBox_old_poster)

        self.checkBox_old_thumb = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_thumb.setObjectName(u"checkBox_old_thumb")

        self.horizontalLayout_23.addWidget(self.checkBox_old_thumb)

        self.checkBox_old_fanart = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_fanart.setObjectName(u"checkBox_old_fanart")

        self.horizontalLayout_23.addWidget(self.checkBox_old_fanart)

        self.checkBox_old_nfo = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_nfo.setObjectName(u"checkBox_old_nfo")

        self.horizontalLayout_23.addWidget(self.checkBox_old_nfo)

        self.checkBox_old_extrafanart = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_extrafanart.setObjectName(u"checkBox_old_extrafanart")

        self.horizontalLayout_23.addWidget(self.checkBox_old_extrafanart)

        self.checkBox_old_extrafanart_copy = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_extrafanart_copy.setObjectName(u"checkBox_old_extrafanart_copy")

        self.horizontalLayout_23.addWidget(self.checkBox_old_extrafanart_copy)

        self.label_79 = QLabel(self.groupBox_33)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(60, 60, 641, 31))
        sizePolicy4.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy4)
        self.label_79.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.scrollArea_7 = QScrollArea(self.tab_3)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setGeometry(QRect(0, 0, 771, 654))
        self.scrollArea_7.setFrameShape(QFrame.Box)
        self.scrollArea_7.setLineWidth(0)
        self.scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setWidgetResizable(False)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 771, 1349))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy1)
        self.groupBox_35 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setGeometry(QRect(30, 1130, 701, 111))
        self.groupBox_35.setMinimumSize(QSize(200, 0))
        self.groupBox_35.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_18 = QWidget(self.groupBox_35)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(60, 30, 621, 71))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.gridLayoutWidget_18)
        self.label_86.setObjectName(u"label_86")
        sizePolicy4.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy4)
        self.label_86.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_18.addWidget(self.label_86, 0, 1, 1, 1)

        self.label_87 = QLabel(self.gridLayoutWidget_18)
        self.label_87.setObjectName(u"label_87")
        sizePolicy4.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy4)
        self.label_87.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_18.addWidget(self.label_87, 1, 1, 1, 1)

        self.radioButton_del_actor_on = QRadioButton(self.gridLayoutWidget_18)
        self.radioButton_del_actor_on.setObjectName(u"radioButton_del_actor_on")
        sizePolicy3.setHeightForWidth(self.radioButton_del_actor_on.sizePolicy().hasHeightForWidth())
        self.radioButton_del_actor_on.setSizePolicy(sizePolicy3)
        self.radioButton_del_actor_on.setMinimumSize(QSize(80, 0))
        self.radioButton_del_actor_on.setAutoExclusive(True)

        self.gridLayout_18.addWidget(self.radioButton_del_actor_on, 0, 0, 1, 1)

        self.radioButton_del_actor_off = QRadioButton(self.gridLayoutWidget_18)
        self.radioButton_del_actor_off.setObjectName(u"radioButton_del_actor_off")
        self.radioButton_del_actor_off.setMinimumSize(QSize(80, 0))
        self.radioButton_del_actor_off.setAutoExclusive(True)

        self.gridLayout_18.addWidget(self.radioButton_del_actor_off, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(30, 10, 701, 341))
        self.groupBox_8.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_8 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 30, 671, 301))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.gridLayoutWidget_8)
        self.label_67.setObjectName(u"label_67")
        sizePolicy3.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy3)
        self.label_67.setMinimumSize(QSize(0, 0))
        self.label_67.setLayoutDirection(Qt.RightToLeft)
        self.label_67.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_67, 4, 0, 1, 1)

        self.label_68 = QLabel(self.gridLayoutWidget_8)
        self.label_68.setObjectName(u"label_68")
        sizePolicy4.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy4)
        self.label_68.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_68, 5, 1, 1, 1)

        self.lineEdit_media_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_media_name.setObjectName(u"lineEdit_media_name")
        self.lineEdit_media_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_media_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_media_name, 4, 1, 1, 1)

        self.label_66 = QLabel(self.gridLayoutWidget_8)
        self.label_66.setObjectName(u"label_66")
        sizePolicy4.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy4)
        self.label_66.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_66.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_8.addWidget(self.label_66, 1, 1, 1, 1)

        self.label_63 = QLabel(self.gridLayoutWidget_8)
        self.label_63.setObjectName(u"label_63")
        sizePolicy3.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy3)
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setLayoutDirection(Qt.RightToLeft)
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_63, 2, 0, 1, 1)

        self.lineEdit_local_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_local_name.setObjectName(u"lineEdit_local_name")
        self.lineEdit_local_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_local_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_local_name, 2, 1, 1, 1)

        self.lineEdit_dir_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_dir_name.setObjectName(u"lineEdit_dir_name")
        self.lineEdit_dir_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_dir_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_dir_name, 0, 1, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_8)
        self.label_43.setObjectName(u"label_43")
        sizePolicy5.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy5)
        self.label_43.setMinimumSize(QSize(130, 0))
        self.label_43.setLayoutDirection(Qt.RightToLeft)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget_8)
        self.label_61.setObjectName(u"label_61")
        sizePolicy4.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy4)
        self.label_61.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_61, 3, 1, 1, 1)

        self.groupBox_37 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setGeometry(QRect(30, 840, 701, 111))
        self.groupBox_37.setMinimumSize(QSize(200, 0))
        self.groupBox_37.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_21 = QWidget(self.groupBox_37)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(60, 30, 621, 71))
        self.gridLayout_21 = QGridLayout(self.gridLayoutWidget_21)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.radioButton_pic_file_poster = QRadioButton(self.gridLayoutWidget_21)
        self.radioButton_pic_file_poster.setObjectName(u"radioButton_pic_file_poster")
        sizePolicy3.setHeightForWidth(self.radioButton_pic_file_poster.sizePolicy().hasHeightForWidth())
        self.radioButton_pic_file_poster.setSizePolicy(sizePolicy3)
        self.radioButton_pic_file_poster.setMinimumSize(QSize(80, 0))
        self.radioButton_pic_file_poster.setAutoExclusive(True)

        self.gridLayout_21.addWidget(self.radioButton_pic_file_poster, 0, 0, 1, 1)

        self.radioButton_pic_poster = QRadioButton(self.gridLayoutWidget_21)
        self.radioButton_pic_poster.setObjectName(u"radioButton_pic_poster")
        self.radioButton_pic_poster.setMinimumSize(QSize(80, 0))
        self.radioButton_pic_poster.setAutoExclusive(True)

        self.gridLayout_21.addWidget(self.radioButton_pic_poster, 1, 0, 1, 1)

        self.label_95 = QLabel(self.gridLayoutWidget_21)
        self.label_95.setObjectName(u"label_95")
        sizePolicy4.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy4)
        self.label_95.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_21.addWidget(self.label_95, 0, 1, 1, 1)

        self.label_96 = QLabel(self.gridLayoutWidget_21)
        self.label_96.setObjectName(u"label_96")
        sizePolicy4.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy4)
        self.label_96.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_21.addWidget(self.label_96, 1, 1, 1, 1)

        self.groupBox_38 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setGeometry(QRect(30, 970, 701, 141))
        self.groupBox_38.setMinimumSize(QSize(200, 0))
        self.groupBox_38.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_22 = QWidget(self.groupBox_38)
        self.gridLayoutWidget_22.setObjectName(u"gridLayoutWidget_22")
        self.gridLayoutWidget_22.setGeometry(QRect(60, 30, 621, 80))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_22)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.gridLayoutWidget_22)
        self.label_97.setObjectName(u"label_97")
        sizePolicy4.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy4)
        self.label_97.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_22.addWidget(self.label_97, 0, 1, 1, 1)

        self.label_98 = QLabel(self.gridLayoutWidget_22)
        self.label_98.setObjectName(u"label_98")
        sizePolicy4.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy4)
        self.label_98.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_22.addWidget(self.label_98, 1, 1, 1, 1)

        self.radioButton_cd_part_lower = QRadioButton(self.gridLayoutWidget_22)
        self.radioButton_cd_part_lower.setObjectName(u"radioButton_cd_part_lower")
        sizePolicy3.setHeightForWidth(self.radioButton_cd_part_lower.sizePolicy().hasHeightForWidth())
        self.radioButton_cd_part_lower.setSizePolicy(sizePolicy3)
        self.radioButton_cd_part_lower.setMinimumSize(QSize(80, 0))
        self.radioButton_cd_part_lower.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.radioButton_cd_part_lower, 0, 0, 1, 1)

        self.radioButton_cd_part_upper = QRadioButton(self.gridLayoutWidget_22)
        self.radioButton_cd_part_upper.setObjectName(u"radioButton_cd_part_upper")
        self.radioButton_cd_part_upper.setMinimumSize(QSize(80, 0))
        self.radioButton_cd_part_upper.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.radioButton_cd_part_upper, 1, 0, 1, 1)

        self.label_99 = QLabel(self.groupBox_38)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(60, 110, 631, 20))
        sizePolicy4.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy4)
        self.label_99.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_77 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_77.setObjectName(u"groupBox_77")
        self.groupBox_77.setGeometry(QRect(30, 370, 701, 321))
        self.groupBox_77.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_43 = QWidget(self.groupBox_77)
        self.gridLayoutWidget_43.setObjectName(u"gridLayoutWidget_43")
        self.gridLayoutWidget_43.setGeometry(QRect(10, 30, 671, 281))
        self.gridLayout_43 = QGridLayout(self.gridLayoutWidget_43)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.gridLayoutWidget_43)
        self.label_172.setObjectName(u"label_172")
        sizePolicy4.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy4)
        self.label_172.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_43.addWidget(self.label_172, 3, 1, 1, 1)

        self.label_167 = QLabel(self.gridLayoutWidget_43)
        self.label_167.setObjectName(u"label_167")
        sizePolicy3.setHeightForWidth(self.label_167.sizePolicy().hasHeightForWidth())
        self.label_167.setSizePolicy(sizePolicy3)
        self.label_167.setMinimumSize(QSize(0, 0))
        self.label_167.setLayoutDirection(Qt.RightToLeft)
        self.label_167.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_167, 4, 0, 1, 1)

        self.lineEdit_folder_name_max = QLineEdit(self.gridLayoutWidget_43)
        self.lineEdit_folder_name_max.setObjectName(u"lineEdit_folder_name_max")
        self.lineEdit_folder_name_max.setMinimumSize(QSize(450, 30))
        self.lineEdit_folder_name_max.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_43.addWidget(self.lineEdit_folder_name_max, 0, 1, 1, 1)

        self.lineEdit_actor_name_more = QLineEdit(self.gridLayoutWidget_43)
        self.lineEdit_actor_name_more.setObjectName(u"lineEdit_actor_name_more")
        self.lineEdit_actor_name_more.setMinimumSize(QSize(450, 30))
        self.lineEdit_actor_name_more.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_43.addWidget(self.lineEdit_actor_name_more, 6, 1, 1, 1)

        self.lineEdit_file_name_max = QLineEdit(self.gridLayoutWidget_43)
        self.lineEdit_file_name_max.setObjectName(u"lineEdit_file_name_max")
        self.lineEdit_file_name_max.setMinimumSize(QSize(450, 30))
        self.lineEdit_file_name_max.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_43.addWidget(self.lineEdit_file_name_max, 2, 1, 1, 1)

        self.label_168 = QLabel(self.gridLayoutWidget_43)
        self.label_168.setObjectName(u"label_168")
        sizePolicy4.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy4)
        self.label_168.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_43.addWidget(self.label_168, 5, 1, 1, 1)

        self.label_171 = QLabel(self.gridLayoutWidget_43)
        self.label_171.setObjectName(u"label_171")
        sizePolicy5.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy5)
        self.label_171.setMinimumSize(QSize(130, 0))
        self.label_171.setLayoutDirection(Qt.RightToLeft)
        self.label_171.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_171, 0, 0, 1, 1)

        self.label_170 = QLabel(self.gridLayoutWidget_43)
        self.label_170.setObjectName(u"label_170")
        sizePolicy3.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy3)
        self.label_170.setMinimumSize(QSize(0, 0))
        self.label_170.setLayoutDirection(Qt.RightToLeft)
        self.label_170.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_170, 2, 0, 1, 1)

        self.lineEdit_actor_name_max = QLineEdit(self.gridLayoutWidget_43)
        self.lineEdit_actor_name_max.setObjectName(u"lineEdit_actor_name_max")
        self.lineEdit_actor_name_max.setMinimumSize(QSize(450, 30))
        self.lineEdit_actor_name_max.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_43.addWidget(self.lineEdit_actor_name_max, 4, 1, 1, 1)

        self.label_169 = QLabel(self.gridLayoutWidget_43)
        self.label_169.setObjectName(u"label_169")
        sizePolicy4.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy4)
        self.label_169.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_43.addWidget(self.label_169, 1, 1, 1, 1)

        self.groupBox_40 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setGeometry(QRect(30, 710, 701, 111))
        self.groupBox_40.setMinimumSize(QSize(200, 0))
        self.groupBox_40.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_26 = QWidget(self.groupBox_40)
        self.gridLayoutWidget_26.setObjectName(u"gridLayoutWidget_26")
        self.gridLayoutWidget_26.setGeometry(QRect(10, 30, 671, 71))
        self.gridLayout_26 = QGridLayout(self.gridLayoutWidget_26)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.gridLayoutWidget_26)
        self.label_100.setObjectName(u"label_100")
        sizePolicy4.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy4)
        self.label_100.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_26.addWidget(self.label_100, 1, 1, 1, 1)

        self.label_173 = QLabel(self.gridLayoutWidget_26)
        self.label_173.setObjectName(u"label_173")
        sizePolicy3.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy3)
        self.label_173.setMinimumSize(QSize(130, 0))
        self.label_173.setLayoutDirection(Qt.RightToLeft)
        self.label_173.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_173, 0, 0, 1, 1)

        self.lineEdit_actor_no_name = QLineEdit(self.gridLayoutWidget_26)
        self.lineEdit_actor_no_name.setObjectName(u"lineEdit_actor_no_name")
        self.lineEdit_actor_no_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_actor_no_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_26.addWidget(self.lineEdit_actor_no_name, 0, 1, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_26 = QGroupBox(self.tab)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(30, 130, 701, 101))
        self.groupBox_26.setMinimumSize(QSize(200, 0))
        self.groupBox_26.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_17 = QWidget(self.groupBox_26)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.checkBox_translate_title = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_translate_title.setObjectName(u"checkBox_translate_title")

        self.horizontalLayout_22.addWidget(self.checkBox_translate_title)

        self.checkBox_translate_outline = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_translate_outline.setObjectName(u"checkBox_translate_outline")

        self.horizontalLayout_22.addWidget(self.checkBox_translate_outline)

        self.label_74 = QLabel(self.groupBox_26)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(60, 70, 611, 21))
        sizePolicy4.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy4)
        self.label_74.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_31 = QGroupBox(self.tab)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setGeometry(QRect(30, 250, 701, 151))
        self.groupBox_31.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_14 = QWidget(self.groupBox_31)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(10, 30, 671, 111))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.radioButton_youdao = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_youdao.setObjectName(u"radioButton_youdao")
        self.radioButton_youdao.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_20.addWidget(self.radioButton_youdao)

        self.radioButton_deepl = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_deepl.setObjectName(u"radioButton_deepl")
        self.radioButton_deepl.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_20.addWidget(self.radioButton_deepl)


        self.gridLayout_14.addLayout(self.horizontalLayout_20, 0, 1, 1, 1)

        self.label_81 = QLabel(self.gridLayoutWidget_14)
        self.label_81.setObjectName(u"label_81")
        sizePolicy3.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy3)
        self.label_81.setMinimumSize(QSize(130, 30))
        self.label_81.setLayoutDirection(Qt.LeftToRight)
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_81, 0, 0, 1, 1)

        self.label_80 = QLabel(self.gridLayoutWidget_14)
        self.label_80.setObjectName(u"label_80")
        sizePolicy3.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy3)
        self.label_80.setMinimumSize(QSize(130, 30))
        self.label_80.setLayoutDirection(Qt.LeftToRight)
        self.label_80.setFrameShape(QFrame.NoFrame)
        self.label_80.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_80, 1, 0, 1, 1)

        self.lineEdit_deepl_key = QLineEdit(self.gridLayoutWidget_14)
        self.lineEdit_deepl_key.setObjectName(u"lineEdit_deepl_key")
        sizePolicy4.setHeightForWidth(self.lineEdit_deepl_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_deepl_key.setSizePolicy(sizePolicy4)
        self.lineEdit_deepl_key.setMinimumSize(QSize(300, 30))
        self.lineEdit_deepl_key.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_14.addWidget(self.lineEdit_deepl_key, 1, 1, 1, 1)

        self.label_60 = QLabel(self.gridLayoutWidget_14)
        self.label_60.setObjectName(u"label_60")
        sizePolicy4.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy4)
        self.label_60.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_14.addWidget(self.label_60, 2, 1, 1, 1)

        self.groupBox_25 = QGroupBox(self.tab)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setGeometry(QRect(30, 10, 701, 101))
        self.groupBox_25.setMinimumSize(QSize(200, 0))
        self.groupBox_25.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_15 = QWidget(self.groupBox_25)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.radioButton_zh_cn = QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_zh_cn.setObjectName(u"radioButton_zh_cn")

        self.horizontalLayout_18.addWidget(self.radioButton_zh_cn)

        self.radioButton_zh_tw = QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_zh_tw.setObjectName(u"radioButton_zh_tw")

        self.horizontalLayout_18.addWidget(self.radioButton_zh_tw)

        self.radioButton_ja = QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_ja.setObjectName(u"radioButton_ja")

        self.horizontalLayout_18.addWidget(self.radioButton_ja)

        self.label_84 = QLabel(self.groupBox_25)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(60, 60, 611, 31))
        sizePolicy4.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy4)
        self.label_84.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.groupBox_75 = QGroupBox(self.tab_9)
        self.groupBox_75.setObjectName(u"groupBox_75")
        self.groupBox_75.setGeometry(QRect(30, 10, 701, 211))
        self.groupBox_75.setMinimumSize(QSize(200, 0))
        self.groupBox_75.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_28 = QWidget(self.groupBox_75)
        self.horizontalLayoutWidget_28.setObjectName(u"horizontalLayoutWidget_28")
        self.horizontalLayoutWidget_28.setGeometry(QRect(130, 160, 521, 31))
        self.horizontalLayout_35 = QHBoxLayout(self.horizontalLayoutWidget_28)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.radioButton_actor_zh_cn = QRadioButton(self.horizontalLayoutWidget_28)
        self.radioButton_actor_zh_cn.setObjectName(u"radioButton_actor_zh_cn")

        self.horizontalLayout_35.addWidget(self.radioButton_actor_zh_cn)

        self.radioButton_actor_zh_tw = QRadioButton(self.horizontalLayoutWidget_28)
        self.radioButton_actor_zh_tw.setObjectName(u"radioButton_actor_zh_tw")

        self.horizontalLayout_35.addWidget(self.radioButton_actor_zh_tw)

        self.radioButton_actor_jp = QRadioButton(self.horizontalLayoutWidget_28)
        self.radioButton_actor_jp.setObjectName(u"radioButton_actor_jp")

        self.horizontalLayout_35.addWidget(self.radioButton_actor_jp)

        self.radioButton_actor_no = QRadioButton(self.horizontalLayoutWidget_28)
        self.radioButton_actor_no.setObjectName(u"radioButton_actor_no")

        self.horizontalLayout_35.addWidget(self.radioButton_actor_no)

        self.radioButton_actor_zh_tw.raise_()
        self.radioButton_actor_no.raise_()
        self.radioButton_actor_jp.raise_()
        self.radioButton_actor_zh_cn.raise_()
        self.label_162 = QLabel(self.groupBox_75)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(20, 20, 671, 91))
        sizePolicy4.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy4)
        self.label_162.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_163 = QLabel(self.groupBox_75)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(20, 160, 100, 30))
        sizePolicy3.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy3)
        self.label_163.setMinimumSize(QSize(100, 30))
        self.label_163.setLayoutDirection(Qt.LeftToRight)
        self.label_163.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_164 = QLabel(self.groupBox_75)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(20, 110, 611, 41))
        sizePolicy4.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy4)
        self.label_164.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_76 = QGroupBox(self.tab_9)
        self.groupBox_76.setObjectName(u"groupBox_76")
        self.groupBox_76.setGeometry(QRect(30, 240, 701, 121))
        self.groupBox_76.setMinimumSize(QSize(200, 0))
        self.groupBox_76.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_29 = QWidget(self.groupBox_76)
        self.horizontalLayoutWidget_29.setObjectName(u"horizontalLayoutWidget_29")
        self.horizontalLayoutWidget_29.setGeometry(QRect(130, 70, 521, 31))
        self.horizontalLayout_36 = QHBoxLayout(self.horizontalLayoutWidget_29)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.radioButton_tag_zh_cn = QRadioButton(self.horizontalLayoutWidget_29)
        self.radioButton_tag_zh_cn.setObjectName(u"radioButton_tag_zh_cn")

        self.horizontalLayout_36.addWidget(self.radioButton_tag_zh_cn)

        self.radioButton_tag_zh_tw = QRadioButton(self.horizontalLayoutWidget_29)
        self.radioButton_tag_zh_tw.setObjectName(u"radioButton_tag_zh_tw")

        self.horizontalLayout_36.addWidget(self.radioButton_tag_zh_tw)

        self.radioButton_tag_jp = QRadioButton(self.horizontalLayoutWidget_29)
        self.radioButton_tag_jp.setObjectName(u"radioButton_tag_jp")

        self.horizontalLayout_36.addWidget(self.radioButton_tag_jp)

        self.radioButton_tag_no = QRadioButton(self.horizontalLayoutWidget_29)
        self.radioButton_tag_no.setObjectName(u"radioButton_tag_no")

        self.horizontalLayout_36.addWidget(self.radioButton_tag_no)

        self.label_165 = QLabel(self.groupBox_76)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(20, 30, 671, 21))
        sizePolicy4.setHeightForWidth(self.label_165.sizePolicy().hasHeightForWidth())
        self.label_165.setSizePolicy(sizePolicy4)
        self.label_165.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_166 = QLabel(self.groupBox_76)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(20, 70, 100, 30))
        sizePolicy3.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy3)
        self.label_166.setMinimumSize(QSize(100, 30))
        self.label_166.setLayoutDirection(Qt.LeftToRight)
        self.label_166.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.groupBox_42 = QGroupBox(self.tab_5)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.groupBox_42.setGeometry(QRect(30, 10, 701, 111))
        self.groupBox_42.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_24 = QWidget(self.groupBox_42)
        self.gridLayoutWidget_24.setObjectName(u"gridLayoutWidget_24")
        self.gridLayoutWidget_24.setGeometry(QRect(20, 30, 661, 71))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_24)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.gridLayoutWidget_24)
        self.label_77.setObjectName(u"label_77")
        sizePolicy4.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy4)
        self.label_77.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_24.addWidget(self.label_77, 1, 1, 1, 1)

        self.label_101 = QLabel(self.gridLayoutWidget_24)
        self.label_101.setObjectName(u"label_101")
        sizePolicy3.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy3)
        self.label_101.setMinimumSize(QSize(130, 30))
        self.label_101.setLayoutDirection(Qt.LeftToRight)
        self.label_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_101, 0, 0, 1, 1)

        self.lineEdit_actor_photo_folder = QLineEdit(self.gridLayoutWidget_24)
        self.lineEdit_actor_photo_folder.setObjectName(u"lineEdit_actor_photo_folder")
        sizePolicy4.setHeightForWidth(self.lineEdit_actor_photo_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_actor_photo_folder.setSizePolicy(sizePolicy4)
        self.lineEdit_actor_photo_folder.setMinimumSize(QSize(300, 30))
        self.lineEdit_actor_photo_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_24.addWidget(self.lineEdit_actor_photo_folder, 0, 1, 1, 1)

        self.groupBox_43 = QGroupBox(self.tab_5)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setGeometry(QRect(30, 140, 701, 161))
        self.groupBox_43.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_25 = QWidget(self.groupBox_43)
        self.gridLayoutWidget_25.setObjectName(u"gridLayoutWidget_25")
        self.gridLayoutWidget_25.setGeometry(QRect(20, 30, 661, 121))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_25)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_api_key = QLineEdit(self.gridLayoutWidget_25)
        self.lineEdit_api_key.setObjectName(u"lineEdit_api_key")
        sizePolicy4.setHeightForWidth(self.lineEdit_api_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_api_key.setSizePolicy(sizePolicy4)
        self.lineEdit_api_key.setMinimumSize(QSize(300, 30))
        self.lineEdit_api_key.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_25.addWidget(self.lineEdit_api_key, 1, 1, 1, 1)

        self.label_104 = QLabel(self.gridLayoutWidget_25)
        self.label_104.setObjectName(u"label_104")
        sizePolicy3.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy3)
        self.label_104.setMinimumSize(QSize(130, 30))
        self.label_104.setLayoutDirection(Qt.LeftToRight)
        self.label_104.setFrameShape(QFrame.NoFrame)
        self.label_104.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_104, 0, 0, 1, 1)

        self.label_105 = QLabel(self.gridLayoutWidget_25)
        self.label_105.setObjectName(u"label_105")
        sizePolicy4.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy4)
        self.label_105.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_25.addWidget(self.label_105, 2, 1, 1, 1)

        self.lineEdit_emby_url = QLineEdit(self.gridLayoutWidget_25)
        self.lineEdit_emby_url.setObjectName(u"lineEdit_emby_url")
        sizePolicy4.setHeightForWidth(self.lineEdit_emby_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_emby_url.setSizePolicy(sizePolicy4)
        self.lineEdit_emby_url.setMinimumSize(QSize(300, 30))
        self.lineEdit_emby_url.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_25.addWidget(self.lineEdit_emby_url, 0, 1, 1, 1)

        self.label_107 = QLabel(self.gridLayoutWidget_25)
        self.label_107.setObjectName(u"label_107")
        sizePolicy3.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy3)
        self.label_107.setMinimumSize(QSize(130, 30))
        self.label_107.setLayoutDirection(Qt.LeftToRight)
        self.label_107.setFrameShape(QFrame.NoFrame)
        self.label_107.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_107, 1, 0, 1, 1)

        self.groupBox_41 = QGroupBox(self.tab_5)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setGeometry(QRect(30, 320, 701, 181))
        self.groupBox_41.setMinimumSize(QSize(200, 0))
        self.groupBox_41.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_11 = QWidget(self.groupBox_41)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(20, 30, 661, 71))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.radioButton_actor_photo_upload_on = QRadioButton(self.gridLayoutWidget_11)
        self.radioButton_actor_photo_upload_on.setObjectName(u"radioButton_actor_photo_upload_on")
        self.radioButton_actor_photo_upload_on.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_19.addWidget(self.radioButton_actor_photo_upload_on)

        self.radioButton_actor_photo_upload_off = QRadioButton(self.gridLayoutWidget_11)
        self.radioButton_actor_photo_upload_off.setObjectName(u"radioButton_actor_photo_upload_off")

        self.horizontalLayout_19.addWidget(self.radioButton_actor_photo_upload_off)


        self.gridLayout_11.addLayout(self.horizontalLayout_19, 0, 1, 1, 1)

        self.label_103 = QLabel(self.gridLayoutWidget_11)
        self.label_103.setObjectName(u"label_103")
        sizePolicy3.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy3)
        self.label_103.setMinimumSize(QSize(130, 0))
        self.label_103.setLayoutDirection(Qt.RightToLeft)
        self.label_103.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_103, 0, 0, 1, 1)

        self.label_106 = QLabel(self.gridLayoutWidget_11)
        self.label_106.setObjectName(u"label_106")
        sizePolicy4.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy4)
        self.label_106.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_11.addWidget(self.label_106, 1, 1, 1, 1)

        self.pushButton_add_actor_pic = QPushButton(self.groupBox_41)
        self.pushButton_add_actor_pic.setObjectName(u"pushButton_add_actor_pic")
        self.pushButton_add_actor_pic.setGeometry(QRect(390, 120, 181, 40))
        self.pushButton_show_pic_actor = QPushButton(self.groupBox_41)
        self.pushButton_show_pic_actor.setObjectName(u"pushButton_show_pic_actor")
        self.pushButton_show_pic_actor.setGeometry(QRect(220, 120, 141, 40))
        self.pushButton_show_pic_actor.setStyleSheet(u"")
        self.comboBox_pic_actor = QComboBox(self.groupBox_41)
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.setObjectName(u"comboBox_pic_actor")
        self.comboBox_pic_actor.setGeometry(QRect(60, 120, 151, 40))
        self.label_download_acotr_zip = QLabel(self.tab_5)
        self.label_download_acotr_zip.setObjectName(u"label_download_acotr_zip")
        self.label_download_acotr_zip.setGeometry(QRect(520, 80, 93, 30))
        sizePolicy3.setHeightForWidth(self.label_download_acotr_zip.sizePolicy().hasHeightForWidth())
        self.label_download_acotr_zip.setSizePolicy(sizePolicy3)
        self.label_download_acotr_zip.setMinimumSize(QSize(0, 0))
        self.label_download_acotr_zip.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_download_acotr_zip.setLayoutDirection(Qt.RightToLeft)
        self.label_download_acotr_zip.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_download_acotr_zip.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_20 = QGroupBox(self.tab_2)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(30, 10, 701, 191))
        self.groupBox_20.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_17 = QWidget(self.groupBox_20)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(20, 30, 661, 151))
        self.gridLayout_17 = QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.gridLayoutWidget_17)
        self.label_91.setObjectName(u"label_91")
        sizePolicy4.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy4)
        self.label_91.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_17.addWidget(self.label_91, 1, 1, 1, 1)

        self.label_69 = QLabel(self.gridLayoutWidget_17)
        self.label_69.setObjectName(u"label_69")
        sizePolicy3.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy3)
        self.label_69.setMinimumSize(QSize(0, 0))
        self.label_69.setLayoutDirection(Qt.RightToLeft)
        self.label_69.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_69, 2, 0, 1, 1)

        self.label_89 = QLabel(self.gridLayoutWidget_17)
        self.label_89.setObjectName(u"label_89")
        sizePolicy3.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy3)
        self.label_89.setMinimumSize(QSize(130, 0))
        self.label_89.setLayoutDirection(Qt.RightToLeft)
        self.label_89.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_89, 0, 0, 1, 1)

        self.label_90 = QLabel(self.gridLayoutWidget_17)
        self.label_90.setObjectName(u"label_90")
        sizePolicy4.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy4)
        self.label_90.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_17.addWidget(self.label_90, 3, 1, 1, 1)

        self.lineEdit_cnword_style = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_cnword_style.setObjectName(u"lineEdit_cnword_style")
        self.lineEdit_cnword_style.setMinimumSize(QSize(450, 30))
        self.lineEdit_cnword_style.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_17.addWidget(self.lineEdit_cnword_style, 2, 1, 1, 1)

        self.lineEdit_cnword_char = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_cnword_char.setObjectName(u"lineEdit_cnword_char")
        self.lineEdit_cnword_char.setMinimumSize(QSize(450, 30))
        self.lineEdit_cnword_char.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_17.addWidget(self.lineEdit_cnword_char, 0, 1, 1, 1)

        self.groupBox_36 = QGroupBox(self.tab_2)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setGeometry(QRect(30, 220, 701, 81))
        self.groupBox_36.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_8 = QWidget(self.groupBox_36)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.checkBox_foldername = QCheckBox(self.horizontalLayoutWidget_8)
        self.checkBox_foldername.setObjectName(u"checkBox_foldername")
        sizePolicy6.setHeightForWidth(self.checkBox_foldername.sizePolicy().hasHeightForWidth())
        self.checkBox_foldername.setSizePolicy(sizePolicy6)
        self.checkBox_foldername.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_foldername)

        self.checkBox_filename = QCheckBox(self.horizontalLayoutWidget_8)
        self.checkBox_filename.setObjectName(u"checkBox_filename")
        sizePolicy6.setHeightForWidth(self.checkBox_filename.sizePolicy().hasHeightForWidth())
        self.checkBox_filename.setSizePolicy(sizePolicy6)
        self.checkBox_filename.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_filename)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.scrollArea_4 = QScrollArea(self.tab4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 0, 771, 577))
        self.scrollArea_4.setFrameShape(QFrame.Box)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(False)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 771, 577))
        self.groupBox_29 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(30, 10, 701, 81))
        self.groupBox_29.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox_29)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.checkBox_poster_mark = QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_poster_mark.setObjectName(u"checkBox_poster_mark")
        sizePolicy6.setHeightForWidth(self.checkBox_poster_mark.sizePolicy().hasHeightForWidth())
        self.checkBox_poster_mark.setSizePolicy(sizePolicy6)
        self.checkBox_poster_mark.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.checkBox_poster_mark)

        self.checkBox_thumb_mark = QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_thumb_mark.setObjectName(u"checkBox_thumb_mark")
        sizePolicy6.setHeightForWidth(self.checkBox_thumb_mark.sizePolicy().hasHeightForWidth())
        self.checkBox_thumb_mark.setSizePolicy(sizePolicy6)
        self.checkBox_thumb_mark.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.checkBox_thumb_mark)

        self.groupBox_19 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(30, 210, 701, 81))
        self.groupBox_19.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_19)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.radioButton_top_left = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_top_left.setObjectName(u"radioButton_top_left")
        sizePolicy6.setHeightForWidth(self.radioButton_top_left.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left.setSizePolicy(sizePolicy6)
        self.radioButton_top_left.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_top_left)

        self.radioButton_bottom_left = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_bottom_left.setObjectName(u"radioButton_bottom_left")
        sizePolicy6.setHeightForWidth(self.radioButton_bottom_left.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left.setSizePolicy(sizePolicy6)
        self.radioButton_bottom_left.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_bottom_left)

        self.radioButton_top_right = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_top_right.setObjectName(u"radioButton_top_right")
        sizePolicy6.setHeightForWidth(self.radioButton_top_right.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right.setSizePolicy(sizePolicy6)
        self.radioButton_top_right.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_top_right)

        self.radioButton_bottom_right = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_bottom_right.setObjectName(u"radioButton_bottom_right")
        sizePolicy6.setHeightForWidth(self.radioButton_bottom_right.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right.setSizePolicy(sizePolicy6)
        self.radioButton_bottom_right.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_bottom_right)

        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(30, 110, 701, 81))
        self.groupBox_14.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_14)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_sub = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_sub.setObjectName(u"checkBox_sub")
        sizePolicy6.setHeightForWidth(self.checkBox_sub.sizePolicy().hasHeightForWidth())
        self.checkBox_sub.setSizePolicy(sizePolicy6)
        self.checkBox_sub.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.checkBox_sub)

        self.checkBox_leak = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_leak.setObjectName(u"checkBox_leak")
        sizePolicy6.setHeightForWidth(self.checkBox_leak.sizePolicy().hasHeightForWidth())
        self.checkBox_leak.setSizePolicy(sizePolicy6)
        self.checkBox_leak.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.checkBox_leak)

        self.checkBox_uncensored = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_uncensored.setObjectName(u"checkBox_uncensored")
        sizePolicy6.setHeightForWidth(self.checkBox_uncensored.sizePolicy().hasHeightForWidth())
        self.checkBox_uncensored.setSizePolicy(sizePolicy6)
        self.checkBox_uncensored.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.checkBox_uncensored)

        self.groupBox_21 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(30, 310, 701, 71))
        self.groupBox_21.setStyleSheet(u"font:\"Courier\";")
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox_21)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(60, 20, 621, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_mark_size = QSlider(self.horizontalLayoutWidget_4)
        self.horizontalSlider_mark_size.setObjectName(u"horizontalSlider_mark_size")
        sizePolicy3.setHeightForWidth(self.horizontalSlider_mark_size.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_mark_size.setSizePolicy(sizePolicy3)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lcdNumber_mark_size.sizePolicy().hasHeightForWidth())
        self.lcdNumber_mark_size.setSizePolicy(sizePolicy7)
        self.lcdNumber_mark_size.setMinimumSize(QSize(30, 30))
        self.lcdNumber_mark_size.setMaximumSize(QSize(70, 30))
        self.lcdNumber_mark_size.setProperty("intValue", 3)

        self.horizontalLayout_6.addWidget(self.lcdNumber_mark_size)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(500, 600, 171, 101))
        self.label_9.setStyleSheet(u"font:\"Courier\";")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab4, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.scrollArea_3 = QScrollArea(self.tab3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 771, 654))
        self.scrollArea_3.setFrameShape(QFrame.Box)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -135, 756, 790))
        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(30, 270, 701, 231))
        self.groupBox_10.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_10 = QWidget(self.groupBox_10)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 30, 671, 81))
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
        self.label_45.setMinimumSize(QSize(130, 30))
        self.label_45.setLayoutDirection(Qt.RightToLeft)
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_45, 0, 0, 1, 1)

        self.label_75 = QLabel(self.groupBox_10)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(10, 120, 681, 81))
        sizePolicy4.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy4)
        self.label_75.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_75.setScaledContents(True)
        self.label_75.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.label_get_cookie_url = QLabel(self.groupBox_10)
        self.label_get_cookie_url.setObjectName(u"label_get_cookie_url")
        self.label_get_cookie_url.setGeometry(QRect(100, 200, 431, 21))
        self.label_get_cookie_url.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_get_cookie_url.setMouseTracking(False)
        self.label_get_cookie_url.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_get_cookie_url.setScaledContents(False)
        self.label_get_cookie_url.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_get_cookie_url.setOpenExternalLinks(False)
        self.label_get_cookie_url.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 200, 81, 21))
        self.label_7.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_28 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setGeometry(QRect(30, 10, 701, 241))
        self.groupBox_28.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_9 = QWidget(self.groupBox_28)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 30, 671, 201))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.gridLayoutWidget_9)
        self.label_65.setObjectName(u"label_65")
        sizePolicy3.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy3)
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setLayoutDirection(Qt.RightToLeft)
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_65, 3, 0, 1, 1)

        self.label_73 = QLabel(self.gridLayoutWidget_9)
        self.label_73.setObjectName(u"label_73")
        sizePolicy3.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy3)
        self.label_73.setMinimumSize(QSize(0, 0))
        self.label_73.setLayoutDirection(Qt.RightToLeft)
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_73, 2, 0, 1, 1)

        self.label_64 = QLabel(self.gridLayoutWidget_9)
        self.label_64.setObjectName(u"label_64")
        sizePolicy3.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy3)
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setLayoutDirection(Qt.RightToLeft)
        self.label_64.setFrameShape(QFrame.NoFrame)
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_64, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider_timeout = QSlider(self.gridLayoutWidget_9)
        self.horizontalSlider_timeout.setObjectName(u"horizontalSlider_timeout")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.horizontalSlider_timeout.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_timeout.setSizePolicy(sizePolicy8)
        self.horizontalSlider_timeout.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_timeout.setMaximumSize(QSize(66666, 30))
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
        sizePolicy7.setHeightForWidth(self.lcdNumber_timeout.sizePolicy().hasHeightForWidth())
        self.lcdNumber_timeout.setSizePolicy(sizePolicy7)
        self.lcdNumber_timeout.setMinimumSize(QSize(30, 30))
        self.lcdNumber_timeout.setMaximumSize(QSize(70, 30))
        self.lcdNumber_timeout.setDigitCount(5)
        self.lcdNumber_timeout.setProperty("intValue", 7)

        self.horizontalLayout_3.addWidget(self.lcdNumber_timeout)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalLayout_retry = QHBoxLayout()
        self.horizontalLayout_retry.setObjectName(u"horizontalLayout_retry")
        self.horizontalSlider_retry = QSlider(self.gridLayoutWidget_9)
        self.horizontalSlider_retry.setObjectName(u"horizontalSlider_retry")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_retry.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_retry.setSizePolicy(sizePolicy8)
        self.horizontalSlider_retry.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_retry.setMaximumSize(QSize(66666, 30))
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
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lcdNumber_retry.sizePolicy().hasHeightForWidth())
        self.lcdNumber_retry.setSizePolicy(sizePolicy9)
        self.lcdNumber_retry.setMinimumSize(QSize(30, 30))
        self.lcdNumber_retry.setMaximumSize(QSize(70, 30))
        self.lcdNumber_retry.setProperty("intValue", 3)

        self.horizontalLayout_retry.addWidget(self.lcdNumber_retry)


        self.gridLayout_9.addLayout(self.horizontalLayout_retry, 3, 1, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.radioButton_proxy_http = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_http.setObjectName(u"radioButton_proxy_http")
        self.radioButton_proxy_http.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_http)

        self.radioButton_proxy_socks5 = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_socks5.setObjectName(u"radioButton_proxy_socks5")
        self.radioButton_proxy_socks5.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_socks5)

        self.radioButton_proxy_nouse = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_nouse.setObjectName(u"radioButton_proxy_nouse")
        self.radioButton_proxy_nouse.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_nouse)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.label_70 = QLabel(self.gridLayoutWidget_9)
        self.label_70.setObjectName(u"label_70")
        sizePolicy3.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy3)
        self.label_70.setMinimumSize(QSize(130, 0))
        self.label_70.setLayoutDirection(Qt.RightToLeft)
        self.label_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_70, 0, 0, 1, 1)

        self.lineEdit_proxy = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_proxy.setObjectName(u"lineEdit_proxy")
        sizePolicy4.setHeightForWidth(self.lineEdit_proxy.sizePolicy().hasHeightForWidth())
        self.lineEdit_proxy.setSizePolicy(sizePolicy4)
        self.lineEdit_proxy.setMinimumSize(QSize(300, 30))
        self.lineEdit_proxy.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_9.addWidget(self.lineEdit_proxy, 1, 1, 1, 1)

        self.groupBox_44 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setGeometry(QRect(30, 520, 701, 161))
        self.groupBox_44.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_12 = QWidget(self.groupBox_44)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(10, 30, 671, 121))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_javdb_website = QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_javdb_website.setObjectName(u"lineEdit_javdb_website")
        sizePolicy4.setHeightForWidth(self.lineEdit_javdb_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_javdb_website.setSizePolicy(sizePolicy4)
        self.lineEdit_javdb_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_javdb_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_12.addWidget(self.lineEdit_javdb_website, 1, 1, 1, 1)

        self.label_109 = QLabel(self.gridLayoutWidget_12)
        self.label_109.setObjectName(u"label_109")
        sizePolicy3.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy3)
        self.label_109.setMinimumSize(QSize(130, 0))
        self.label_109.setLayoutDirection(Qt.RightToLeft)
        self.label_109.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_109, 0, 0, 1, 1)

        self.label_108 = QLabel(self.gridLayoutWidget_12)
        self.label_108.setObjectName(u"label_108")
        sizePolicy3.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy3)
        self.label_108.setMinimumSize(QSize(0, 0))
        self.label_108.setLayoutDirection(Qt.RightToLeft)
        self.label_108.setFrameShape(QFrame.NoFrame)
        self.label_108.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_108, 1, 0, 1, 1)

        self.lineEdit_javbus_website = QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_javbus_website.setObjectName(u"lineEdit_javbus_website")
        sizePolicy4.setHeightForWidth(self.lineEdit_javbus_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_javbus_website.setSizePolicy(sizePolicy4)
        self.lineEdit_javbus_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_javbus_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_12.addWidget(self.lineEdit_javbus_website, 0, 1, 1, 1)

        self.label_110 = QLabel(self.gridLayoutWidget_12)
        self.label_110.setObjectName(u"label_110")
        sizePolicy4.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy4)
        self.label_110.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_12.addWidget(self.label_110, 2, 1, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab3, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.scrollArea_5 = QScrollArea(self.tab5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(0, 0, 771, 577))
        self.scrollArea_5.setFrameShape(QFrame.Box)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setWidgetResizable(False)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 771, 577))
        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(30, 210, 701, 81))
        self.groupBox_17.setMinimumSize(QSize(200, 0))
        self.groupBox_17.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_11 = QWidget(self.groupBox_17)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.radioButton_log_on = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_on.setObjectName(u"radioButton_log_on")

        self.horizontalLayout_13.addWidget(self.radioButton_log_on)

        self.radioButton_log_off = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_off.setObjectName(u"radioButton_log_off")

        self.horizontalLayout_13.addWidget(self.radioButton_log_off)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 110, 701, 81))
        self.groupBox_3.setMinimumSize(QSize(200, 0))
        self.groupBox_3.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_9 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.radioButton_debug_on = QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_debug_on.setObjectName(u"radioButton_debug_on")

        self.horizontalLayout_11.addWidget(self.radioButton_debug_on)

        self.radioButton_debug_off = QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_debug_off.setObjectName(u"radioButton_debug_off")

        self.horizontalLayout_11.addWidget(self.radioButton_debug_off)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 10, 701, 81))
        self.groupBox_4.setMinimumSize(QSize(200, 0))
        self.groupBox_4.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.radioButton_update_on = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_update_on.setObjectName(u"radioButton_update_on")

        self.horizontalLayout_9.addWidget(self.radioButton_update_on)

        self.radioButton_update_off = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_update_off.setObjectName(u"radioButton_update_off")

        self.horizontalLayout_9.addWidget(self.radioButton_update_off)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.tabWidget.addTab(self.tab5, "")
        self.label_4 = QLabel(self.page_setting)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 620, 741, 71))
        self.label_4.setStyleSheet(u"background-color: rgba(246, 246, 246, 220);")
        self.pushButton_init_config = QPushButton(self.page_setting)
        self.pushButton_init_config.setObjectName(u"pushButton_init_config")
        self.pushButton_init_config.setGeometry(QRect(110, 630, 160, 41))
        self.pushButton_save_config = QPushButton(self.page_setting)
        self.pushButton_save_config.setObjectName(u"pushButton_save_config")
        self.pushButton_save_config.setGeometry(QRect(360, 630, 301, 50))
        self.stackedWidget.addWidget(self.page_setting)
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
        self.label_ico = QLabel(self.widget_setting)
        self.label_ico.setObjectName(u"label_ico")
        self.label_ico.setGeometry(QRect(40, 540, 141, 141))
        self.label_ico.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.widget_setting)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 221, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 0, 18, 0)
        self.pushButton_main = QPushButton(self.layoutWidget)
        self.pushButton_main.setObjectName(u"pushButton_main")
        sizePolicy.setHeightForWidth(self.pushButton_main.sizePolicy().hasHeightForWidth())
        self.pushButton_main.setSizePolicy(sizePolicy)
        self.pushButton_main.setMinimumSize(QSize(0, 40))
        self.pushButton_main.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_main)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_log = QPushButton(self.layoutWidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setMinimumSize(QSize(0, 40))
        self.pushButton_log.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_log)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_tool = QPushButton(self.layoutWidget)
        self.pushButton_tool.setObjectName(u"pushButton_tool")
        self.pushButton_tool.setMinimumSize(QSize(0, 40))
        self.pushButton_tool.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_tool)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_setting = QPushButton(self.layoutWidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setMinimumSize(QSize(0, 40))
        self.pushButton_setting.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_setting)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_net = QPushButton(self.layoutWidget)
        self.pushButton_net.setObjectName(u"pushButton_net")
        self.pushButton_net.setMinimumSize(QSize(0, 40))
        self.pushButton_net.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_net)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.pushButton_about = QPushButton(self.layoutWidget)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(0, 40))
        self.pushButton_about.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_about)

        self.layoutWidget1 = QWidget(self.widget_setting)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 91, 41))
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
        self.pushButton_close.setMouseTracking(False)
        self.pushButton_close.setStyleSheet(u"QPushButton{color:#E0E0E0;background:#F14C4C;border-radius:10px;}QPushButton:hover{color:white;font:Tahoma;background:#FF6058;}")

        self.horizontalLayout.addWidget(self.pushButton_close)

        self.pushButton_min = QPushButton(self.layoutWidget1)
        self.pushButton_min.setObjectName(u"pushButton_min")
        sizePolicy10.setHeightForWidth(self.pushButton_min.sizePolicy().hasHeightForWidth())
        self.pushButton_min.setSizePolicy(sizePolicy10)
        self.pushButton_min.setMinimumSize(QSize(20, 20))
        self.pushButton_min.setMaximumSize(QSize(20, 20))
        self.pushButton_min.setBaseSize(QSize(0, 0))
        self.pushButton_min.setMouseTracking(False)
        self.pushButton_min.setStyleSheet(u"QPushButton{color:#E0E0E0;background:rgb(246, 186, 76);border-radius:10px;}QPushButton:hover{color:white;font:Tahoma;background:rgba(246, 186, 76, 230);}\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_min)

        self.label_show_version = QLabel(self.widget_setting)
        self.label_show_version.setObjectName(u"label_show_version")
        self.label_show_version.setGeometry(QRect(0, 660, 220, 30))
        self.label_show_version.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_show_version.setStyleSheet(u"color: rgba(255, 255, 255, 151);")
        self.label_show_version.setAlignment(Qt.AlignCenter)
        self.progressBar_avdc = QProgressBar(self.centralwidget)
        self.progressBar_avdc.setObjectName(u"progressBar_avdc")
        self.progressBar_avdc.setGeometry(QRect(220, -1, 803, 10))
        self.progressBar_avdc.setMinimumSize(QSize(0, 2))
        self.progressBar_avdc.setSizeIncrement(QSize(0, 0))
        self.progressBar_avdc.setBaseSize(QSize(0, 0))
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

        self.stackedWidget.setCurrentIndex(4)
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
        self.label_33.setText(QCoreApplication.translate("AVDV", u"\u6807\u7b7e\uff1a", None))
        self.checkBox_cover.setText(QCoreApplication.translate("AVDV", u"\u663e\u793a\u5c01\u9762(\u53d6\u6d88\u52fe\u9009\u540e\uff0c\u7acb\u5373\u5173\u95ed\u5c01\u9762\u663e\u793a)", None))
        self.label_result.setText(QCoreApplication.translate("AVDV", u" \u7b49\u5f85\u5f00\u59cb ...", None))
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

        self.label_file_path.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u76ee\u5f55\u8bbe\u7f6e\uff1a\u3010\u8bbe\u7f6e\u3011-\u3010\u76ee\u5f55\u3011-\u3010\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u3011\u3002\u7a0b\u5e8f\u5c06\u522e\u524a\u8be5\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\u7684\u6240\u6709\u6587\u4ef6\u3002", None))
        self.label_source.setText("")
        self.label_19.setText(QCoreApplication.translate("AVDV", u"\u70b9\u51fb\u56fe\u7247\u53ef\u624b\u52a8\u88c1\u526a", None))
        self.pushButton_start_cap2.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb", None))
        self.pushButton_check_net.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("AVDV", u"\u79fb\u52a8\u89c6\u9891\u3001\u5b57\u5e55", None))
        self.pushButton_move_mp4.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb\u79fb\u52a8", None))
        self.label_41.setText(QCoreApplication.translate("AVDV", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("AVDV", u"\u79fb\u52a8\u300c\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u300d\u4e2d\u7684\u6240\u6709\u89c6\u9891\u548c\u5b57\u5e55\u5230\u300c\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u300d\u4e0b\u7684\u300cMovie_moved\u300d\u76ee\u5f55\u4e0b\u3002", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("AVDV", u"\u5355\u6587\u4ef6\u522e\u524a", None))
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

        self.label_2.setText(QCoreApplication.translate("AVDV", u"*\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("AVDV", u"*\u522e\u524a\u7f51\u5740\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("AVDV", u" \u5f71\u7247\u756a\u53f7\uff1a", None))
        self.pushButton_start_single_file.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a", None))
        self.label_3.setText(QCoreApplication.translate("AVDV", u"*\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.label.setText(QCoreApplication.translate("AVDV", u"\u9009\u62e9\u6587\u4ef6\u540e\uff0c\u9009\u62e9\u300c\u522e\u524a\u7f51\u7ad9\u300d\u3001\u586b\u5199\u300c\u522e\u524a\u7f51\u5740\u300d\uff08\u8be5\u756a\u53f7\u7684\u7f51\u9875\u5730\u5740\uff09\u70b9\u51fb\u522e\u524a\u5373\u53ef\uff01\n"
"\u300c\u5f71\u7247\u756a\u53f7\u300d\u53ef\u4e0d\u586b\u5199", None))
        self.pushButton_select_file_clear_info.setText(QCoreApplication.translate("AVDV", u"\u6e05\u7a7a\u4fe1\u606f", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("AVDV", u"\u88c1\u526a\u56fe\u7247", None))
        self.pushButton_select_thumb.setText(QCoreApplication.translate("AVDV", u"\u9009\u62e9\u56fe\u7247", None))
        self.label_6.setText(QCoreApplication.translate("AVDV", u"\u6b64\u5de5\u5177\u652f\u6301\u62d6\u52a8\u9009\u62e9\u88c1\u526a\u8303\u56f4\uff0c\u53ef\u5c06\u56fe\u7247\u88c1\u526a\u4e3a\u5c01\u9762\u56fe\uff08poster\uff09\u3002", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.groupBox_16.setTitle(QCoreApplication.translate("AVDV", u"\u76ee\u5f55\u8bbe\u7f6e", None))
        self.label_46.setText(QCoreApplication.translate("AVDV", u"\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.label_47.setText(QCoreApplication.translate("AVDV", u"\u6210\u529f\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.label_29.setText(QCoreApplication.translate("AVDV", u"\u6307\u522e\u524a\u6210\u529f\u65f6\uff0c\u89c6\u9891\u5c06\u79fb\u52a8\u5230\u8fd9\u4e2a\u6587\u4ef6\u5939\u3002\u8f93\u51fa\u76ee\u5f55\u53ef\u4ee5\u4e0d\u5728\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u4e0b", None))
        self.label_48.setText(QCoreApplication.translate("AVDV", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.label_49.setText(QCoreApplication.translate("AVDV", u"\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\uff1a", None))
        self.label_56.setText(QCoreApplication.translate("AVDV", u"\u6307\u672c\u5730\u542b\u6709\u89c6\u9891\u7684\u6587\u4ef6\u5939\uff0c\u5c06\u4ece\u7f51\u7edc\u4e0a\u522e\u524a\u8be5\u76ee\u5f55\uff08\u542b\u5b50\u76ee\u5f55\uff09\u6240\u6709\u89c6\u9891\u7684\u5143\u6570\u636e\u4fe1\u606f", None))
        self.label_57.setText(QCoreApplication.translate("AVDV", u"\u6307\u522e\u524a\u5931\u8d25\u65f6\uff0c\u89c6\u9891\u5c06\u79fb\u52a8\u5230\u8fd9\u4e2a\u6587\u4ef6\u5939\u3002\u8f93\u51fa\u76ee\u5f55\u53ef\u4ee5\u4e0d\u5728\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u4e0b", None))
        self.label_58.setText(QCoreApplication.translate("AVDV", u"\u6307\u4e0d\u60f3\u8981\u522e\u524a\u7684\u76ee\u5f55\uff0c\u53ef\u4ee5\u586b\u5199\u591a\u4e2a\u76ee\u5f55\uff0c\u4ee5\u9017\u53f7\u5206\u5f00\uff08\u4e2d\u82f1\u6587\u9017\u53f7\u90fd\u53ef\u4ee5\uff09", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("AVDV", u"\u6587\u4ef6\u683c\u5f0f\u8bbe\u7f6e", None))
        self.label_78.setText(QCoreApplication.translate("AVDV", u"\u5b57\u5e55\u683c\u5f0f\uff1a", None))
        self.label_50.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u683c\u5f0f\uff1a", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("AVDV", u"\u6587\u4ef6\u8fc7\u6ee4\u8bbe\u7f6e", None))
        self.label_83.setText(QCoreApplication.translate("AVDV", u"\u8fc7\u6ee4\u6587\u4ef6\u540d\u591a\u4f59\u5b57\u7b26\uff1a", None))
        self.label_88.setText(QCoreApplication.translate("AVDV", u"\u8bc6\u522b\u756a\u53f7\u65f6\uff0c\u5c06\u5148\u6392\u9664\u591a\u4f59\u5b57\u7b26\u518d\u8fdb\u884c\u8bc6\u522b\u3002\uff08\u586b\u5199\u65f6\u4ee5\u9017\u53f7\u5206\u5272\uff0c\u4e0d\u7528\u533a\u5206\u5927\u5c0f\u5199\uff09", None))
        self.label_94.setText(QCoreApplication.translate("AVDV", u"\u7528\u4e8e\u8fc7\u6ee4\u672c\u5730\u7684\u4e00\u4e9b\u5e7f\u544a\u89c6\u9891\uff0c\u6b64\u5904\u586b\u5199\u6587\u4ef6\u5927\u5c0f\uff0c\u5c0f\u4e8e\u8be5\u5927\u5c0f\u7684\u89c6\u9891\u5c06\u8df3\u8fc7\u522e\u524a", None))
        self.label_93.setText(QCoreApplication.translate("AVDV", u"\u8fc7\u6ee4\u5c0f\u6587\u4ef6(MB)\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("AVDV", u"\u76ee\u5f55", None))
        self.groupBox.setTitle(QCoreApplication.translate("AVDV", u"\u6a21\u5f0f", None))
        self.radioButton_read.setText(QCoreApplication.translate("AVDV", u"\u8bfb\u53d6\u6a21\u5f0f", None))
        self.label_11.setText(QCoreApplication.translate("AVDV", u"\u5305\u542b\u522e\u524a\u4fe1\u606f\u3001\u7ffb\u8bd1\u6807\u9898\u548c\u7b80\u4ecb\u3001\u4e0b\u8f7d\u56fe\u7247\u548cnfo\u6587\u4ef6\u3001\u91cd\u547d\u540d\u6587\u4ef6\u3001\u79fb\u52a8\u6587\u4ef6\u7b49\u5168\u90e8\u64cd\u4f5c", None))
        self.label_16.setText(QCoreApplication.translate("AVDV", u"\u672c\u5730\u6709nfo\u6587\u4ef6\u65f6\uff0c\u76f4\u63a5\u8bfb\u53d6nfo\u4fe1\u606f\uff0c\u4e0d\u8fdb\u884c\u522e\u524a", None))
        self.radioButton_sort.setText(QCoreApplication.translate("AVDV", u"\u6574\u7406\u6a21\u5f0f", None))
        self.radioButton_common.setText(QCoreApplication.translate("AVDV", u"\u6807\u51c6\u6a21\u5f0f", None))
        self.label_15.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u540e\uff0c\u4e0d\u4e0b\u8f7d\u56fe\u7247\u548cnfo\u6587\u4ef6\uff0c\u4ec5\u91cd\u547d\u540d\u6587\u4ef6", None))
        self.checkBox_read_no_nfo_scrape.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u5b58\u5728\u672c\u5730nfo\u7684\u89c6\u9891\uff0c\u6b63\u5e38\u522e\u524a", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("AVDV", u"\u504f\u597d", None))
        self.radioButton_like_speed.setText(QCoreApplication.translate("AVDV", u"\u5feb\u901f", None))
        self.radioButton_like_more.setText(QCoreApplication.translate("AVDV", u"\u5b57\u6bb5\u5168", None))
        self.label_28.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u65f6\uff0c\u4e0d\u4f1a\u5c1d\u8bd5\u8bf7\u6c42\u5176\u4ed6\u7f51\u7ad9\u8865\u5168\u7f3a\u5931\u7684\u5b57\u6bb5\uff0c\u56e0\u6b64\u901f\u5ea6\u4f1a\u5feb\u4e00\u4e9b", None))
        self.label_32.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u65f6\uff0c\u4f1a\u5c1d\u8bd5\u8bf7\u6c42\u5176\u4ed6\u7f51\u7ad9\u8865\u5168\u7f3a\u5931\u7684\u5b57\u6bb5\uff0c\u56e0\u6b64\u901f\u5ea6\u4f1a\u7565\u6162\u4e00\u4e9b", None))
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

        self.groupBox_2.setTitle(QCoreApplication.translate("AVDV", u"\u8f6f\u94fe\u63a5", None))
        self.label_36.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u5728\u6210\u529f\u8f93\u51fa\u76ee\u5f55\uff08\u9700\u4e3a\u672c\u5730\u78c1\u76d8\uff09\u521b\u5efa\u6307\u5411\u539f\u6587\u4ef6\uff08\u7f51\u7edc/\u672c\u5730\u5747\u53ef\uff09\u7684\u66ff\u8eab\u6587\u4ef6", None))
        self.label_37.setText(QCoreApplication.translate("AVDV", u"\u5f53\u9009\u62e9\u300c\u5173\u300d\u65f6\uff0c\u4e0b\u9762\u7684\u300c\u6210\u529f\u540e\u79fb\u52a8\u6587\u4ef6\u300d\u300c\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6\u300d\u624d\u4f1a\u751f\u6548", None))
        self.radioButton_soft_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_soft_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("AVDV", u"\u6210\u529f\u540e\u91cd\u547d\u540d\u6587\u4ef6", None))
        self.label_38.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u6309\u300c\u547d\u540d\u300d-\u300c\u89c6\u9891\u547d\u540d\u89c4\u5219\u300d-\u300c\u89c6\u9891\u6587\u4ef6\u540d\u300d\u91cd\u547d\u540d\u6587\u4ef6", None))
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
        self.groupBox_23.setTitle(QCoreApplication.translate("AVDV", u"\u5b57\u6bb5\u8865\u5168\u7f51\u7ad9", None))
        self.checkBox_more_dmm.setText(QCoreApplication.translate("AVDV", u"dmm", None))
        self.checkBox_more_jav321.setText(QCoreApplication.translate("AVDV", u"jav321", None))
        self.label_71.setText(QCoreApplication.translate("AVDV", u"\u8d44\u6e90\u8f83\u5168\uff0c\u5b57\u6bb5\u5168\uff0c\u6709\u7b80\u4ecb", None))
        self.checkBox_more_javdb.setText(QCoreApplication.translate("AVDV", u"javdb", None))
        self.label_62.setText(QCoreApplication.translate("AVDV", u"\u8d44\u6e90\u6700\u5168\uff0c\u5b57\u6bb5\u5168\uff0c\u4f46\u7f3a\u5c11\u7b80\u4ecb\uff0c\u4e2a\u522b\u8d44\u6e90\u9700\u8981\u586b\u5199cookie\u624d\u80fd\u67e5\u770b", None))
        self.label_92.setText(QCoreApplication.translate("AVDV", u"\u8d44\u6e90\u4e0d\u5168\uff0c\u5b57\u6bb5\u5168\uff0c\u6709\u7b80\u4ecb\uff0c\u9700\u8981\u65e5\u672c\u8282\u70b9\u8bbf\u95ee", None))
        self.checkBox_more_javlibrary.setText(QCoreApplication.translate("AVDV", u"javlibrary", None))
        self.label_72.setText(QCoreApplication.translate("AVDV", u"\u8d44\u6e90\u8f83\u5168\uff0c\u5b57\u6bb5\u5168\uff0c\u65e0\u7b80\u4ecb\uff0c\u6f14\u5458\u4fe1\u606f\u8f83\u5168", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("AVDV", u"\u7ed3\u675f\u540e\u5220\u9664\u7a7a\u6587\u4ef6\u5939", None))
        self.label_44.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u7ed3\u675f\u540e\uff0c\u5220\u9664\u522e\u524a\u76ee\u5f55\u4e2d\u7684\u6240\u6709\u7a7a\u6587\u4ef6\u5939", None))
        self.label_51.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u7ed3\u675f\u540e\uff0c\u4e0d\u5220\u9664\u7a7a\u6587\u4ef6\u5939", None))
        self.radioButton_del_empty_folder_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_del_empty_folder_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("AVDV", u"\u522e\u524a", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\u5267\u7167", None))
        self.checkBox_download_extrafanart.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167", None))
        self.checkBox_download_extrafanart_copy.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167\u526f\u672c\u76ee\u5f55", None))
        self.label_82.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167\uff1aemby\u5a92\u4f53\u5e93\u7c7b\u578b\u9009\u62e9\u300c\u5bb6\u5ead\u89c6\u9891\u4e0e\u7167\u7247\u300d\u65f6\uff0c\u5267\u7167\u53ef\u4f5c\u4e3a\u80cc\u666f\u56fe\u7247\u8f6e\u64ad\u663e\u793a\u3002\n"
"\u6ce8\u610f\uff1a\u5267\u7167\u9ed8\u8ba4\u4fdd\u5b58\u5230\u89c6\u9891\u6587\u4ef6\u76ee\u5f55\u5185\u7684\u300cextrafanart\u300d\u76ee\u5f55\u4e2d", None))
        self.label_59.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167\u526f\u672c\u76ee\u5f55\uff1aemby\u5267\u7167\u4f1a\u88ab\u9690\u85cf\uff0c\u5982\u9700\u5728emby\u4e2d\u624b\u52a8\u67e5\u770b\u5267\u7167\uff0c\u53ef\u521b\u5efa\u5267\u7167\u76ee\u5f55\u526f\u672c\u3002\n"
"\u76ee\u5f55\u540d\u5b57\u4e3a\u7a7a\u6216\u8005\u300cextrafanart\u300d\u65f6\uff0c\u5c06\u4e0d\u4f1a\u521b\u5efa\u526f\u672c\u76ee\u5f55\u3002\u8bf7\u4f7f\u7528\u300cextrafanart\u300d\u4ee5\u5916\u7684\u5176\u4ed6\u540d\u5b57\u3002\n"
"\u6ce8\u610f\uff1a\u6b64\u5904\u53ea\u9700\u586b\u5199\u76ee\u5f55\u540d\u5b57\uff0c\u8bf7\u4e0d\u8981\u586b\u5199\u5b8c\u6574\u8def\u5f84\uff01", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\u56fe\u7247\u548cnfo\u6587\u4ef6", None))
        self.checkBox_download_poster.setText(QCoreApplication.translate("AVDV", u"poster", None))
        self.checkBox_download_thumb.setText(QCoreApplication.translate("AVDV", u"thumb", None))
        self.checkBox_download_fanart.setText(QCoreApplication.translate("AVDV", u"fanart", None))
        self.checkBox_download_nfo.setText(QCoreApplication.translate("AVDV", u"nfo", None))
        self.label_85.setText(QCoreApplication.translate("AVDV", u"poster\uff1a\u6307\u5c01\u9762\u56fe\uff0cemby\u89c6\u56fe\u9009\u62e9\u5c01\u9762\u56fe\u65f6\uff0c\u4f1a\u4f7f\u7528poster\u663e\u793a\uff1b\n"
"thumb\uff1a\u6307\u7f29\u7565\u56fe\uff0cemby\u89c6\u56fe\u9009\u62e9\u7f29\u7565\u56fe\u65f6\uff0c\u4f1a\u4f7f\u7528thumb\u663e\u793a\uff1b\n"
"fanart\uff1a\u6307\u827a\u672f\u56fe\uff0cemby\u8be6\u60c5\u9875\u4f7f\u7528fanart\u4f5c\u4e3a\u80cc\u666f\u56fe\u663e\u793a\uff1b\n"
"nfo\uff1a\u6307\u4fe1\u606f\u6587\u4ef6\uff0c\u8bb0\u5f55\u5f71\u7247\u7684\u7b80\u4ecb\u3001\u6807\u7b7e\u7b49\u5404\u9879\u4fe1\u606f\uff0c\u4f1a\u5728emby\u8be6\u60c5\u9875\u5c55\u793a\u3002", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("AVDV", u"nfo\u4f7f\u7528\u7cfb\u5217\u4f5c\u4e3a\u5408\u96c6", None))
        self.label_40.setText(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58nfo\u65f6\uff0c\u5c06\u7cfb\u5217\u540d\u79f0\u4f5c\u4e3a\u5408\u96c6\u4fe1\u606f\uff0c\u4ee5\u4fbf\u5728emby\u4f7f\u7528\u5408\u96c6\u67e5\u770b\u7cfb\u5217", None))
        self.label_42.setText(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58nfo\u65f6\uff0c\u4e0d\u5199\u5165\u5408\u96c6\u4fe1\u606f", None))
        self.radioButton_series_as_set_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_series_as_set_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("AVDV", u"poster\u5904\u7406\u65b9\u5f0f", None))
        self.radioButton_poster_official.setText(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d", None))
        self.radioButton_poster_cut.setText(QCoreApplication.translate("AVDV", u"\u81ea\u52a8", None))
        self.label_53.setText(QCoreApplication.translate("AVDV", u"\u901a\u8fc7\u5185\u7f6e\u89c4\u5219\u81ea\u52a8\u5224\u65ad\uff0c\u4f18\u5148\u4f7f\u7528thumb\u88c1\u526a\uff08\u6e05\u6670\uff09\uff0c\u6709\u9700\u8981\u65f6\u518d\u4e0b\u8f7dposter", None))
        self.label_52.setText(QCoreApplication.translate("AVDV", u"\u4f18\u5148\u4ece\u7f51\u7edc\u4e0b\u8f7dposter\uff08\u4e00\u822c\u4e0d\u6e05\u6670\uff09\uff0c\u4e0b\u8f7d\u5931\u8d25\u65f6\u518d\u4f7f\u7528thumb\u88c1\u526a", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("AVDV", u"\u6709\u672c\u5730\u6587\u4ef6\u65f6\u4e0d\u4e0b\u8f7d", None))
        self.checkBox_old_poster.setText(QCoreApplication.translate("AVDV", u"poster", None))
        self.checkBox_old_thumb.setText(QCoreApplication.translate("AVDV", u"thumb", None))
        self.checkBox_old_fanart.setText(QCoreApplication.translate("AVDV", u"fanart", None))
        self.checkBox_old_nfo.setText(QCoreApplication.translate("AVDV", u"nfo", None))
        self.checkBox_old_extrafanart.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167", None))
        self.checkBox_old_extrafanart_copy.setText(QCoreApplication.translate("AVDV", u"\u5267\u7167\u526f\u672c", None))
        self.label_79.setText(QCoreApplication.translate("AVDV", u"\u6240\u52fe\u9009\u9879\u76ee\u5b58\u5728\u672c\u5730\u6587\u4ef6\u65f6\uff0c\u5c06\u4fdd\u7559\u5e76\u4f18\u5148\u4f7f\u7528\u672c\u5730\u6587\u4ef6\uff0c\u4e0d\u518d\u91cd\u65b0\u4e0b\u8f7d\uff1b\u672a\u52fe\u9009\u9879\u76ee\u7684\u672c\u5730\u6587\u4ef6\u5c06\u88ab\u6e05\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("AVDV", u"\u53bb\u9664\u6807\u9898\u672b\u5c3e\u6f14\u5458\u540d", None))
        self.label_86.setText(QCoreApplication.translate("AVDV", u"\u4e2a\u522b\u7f51\u7ad9\u6709\u65f6\u4f1a\u5728\u4e00\u4e9b\u6807\u9898\u672b\u5c3e\u52a0\u4e0a\u6f14\u5458\u540d\uff0c\u53bb\u9664\u540e\uff0ctitle = \u6807\u9898", None))
        self.label_87.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u53bb\u9664\uff0c\u8fd9\u7c7b\u7f51\u7ad9title = \u6807\u9898 \u6f14\u5458\uff0c\u5176\u4ed6\u7f51\u7ad9title = \u6807\u9898", None))
        self.radioButton_del_actor_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_del_actor_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u547d\u540d\u89c4\u5219", None))
        self.label_67.setText(QCoreApplication.translate("AVDV", u"Emby\u89c6\u9891\u540d\uff1a", None))
        self.label_68.setText(QCoreApplication.translate("AVDV", u"\u6307\u5728nfo\u6587\u4ef6\u4e2d\u7684\u6807\u9898\u683c\u5f0f\uff0c\u5728Emby\u4e2d\u4f5c\u4e3a\u89c6\u9891\u6807\u9898\u663e\u793a\uff0c\u547d\u540d\u5b57\u6bb5\u540c\u4e0a", None))
        self.label_66.setText(QCoreApplication.translate("AVDV", u"\u5f53\u522e\u524a\u6210\u529f\u65f6\uff0c\u5c06\u4e3a\u8be5\u89c6\u9891\u521b\u5efa\u4e00\u4e2a\u89c6\u9891\u76ee\u5f55\uff0c\u5e76\u79fb\u52a8\u8be5\u89c6\u9891\u76ee\u5f55\u5230\u6210\u529f\u8f93\u51fa\u76ee\u5f55\u3002\n"
"\u76ee\u5f55\u540d\u5b57\u652f\u6301\u81ea\u5b9a\u4e49\u3002\u547d\u540d\u5b57\u6bb5\u6709\uff1a\n"
"title, actor, number, studio, publisher, year, mosaic,\n"
"runtime, director, release, series, definition, cnword\n"
"\u6ce8\u610f\uff1a1\uff0c\u53ef\u4ee5\u6dfb\u52a0\u547d\u540d\u5b57\u6bb5\u4ee5\u5916\u7684\u5b57\u7b26\uff0c\u547d\u540d\u65f6\u4f1a\u539f\u6837\u4fdd\u7559\uff1b\n"
"2\uff0c\u5f53\u7559\u7a7a\u65f6\uff0c\u8868\u793a\u4e0d\u521b\u5efa\u89c6\u9891\u76ee\u5f55\uff1b\n"
"3\uff0c\u5f53\u52fe\u9009\u300c\u6210\u529f\u540e\u4e0d\u79fb\u52a8\u6587\u4ef6\u300d\u65f6\uff0c\u5c06\u4e0d\u4f1a\u521b\u5efa\u89c6\u9891\u76ee\u5f55", None))
        self.label_63.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6587\u4ef6\u540d\uff1a", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_dir_name.setAccessibleDescription(QCoreApplication.translate("AVDV", u"\u6d4b\u8bd5", None))
#endif // QT_CONFIG(accessibility)
        self.label_43.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u76ee\u5f55\u540d\uff1a", None))
        self.label_61.setText(QCoreApplication.translate("AVDV", u"\u6307\u672c\u5730\u89c6\u9891\u6587\u4ef6\u7684\u6587\u4ef6\u540d\u683c\u5f0f\uff0c\u547d\u540d\u5b57\u6bb5\u540c\u4e0a", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("AVDV", u"\u56fe\u7247\u547d\u540d\u89c4\u5219", None))
        self.radioButton_pic_file_poster.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6587\u4ef6\u540d-poster.jpg", None))
        self.radioButton_pic_poster.setText(QCoreApplication.translate("AVDV", u"poster.jpg", None))
        self.label_95.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6587\u4ef6\u540d-thumb.jpg\uff0c\u89c6\u9891\u6587\u4ef6\u540d-fanart.jpg", None))
        self.label_96.setText(QCoreApplication.translate("AVDV", u"thumb.jpg\uff0cfanart.jpg", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("AVDV", u"\u5206\u96c6\u547d\u540d\u89c4\u5219", None))
        self.label_97.setText(QCoreApplication.translate("AVDV", u"\u5c0f\u5199\uff0c-cd1\uff0c-cd2", None))
        self.label_98.setText(QCoreApplication.translate("AVDV", u"\u5927\u5199\uff0c-CD1\u3001-CD2", None))
        self.radioButton_cd_part_lower.setText(QCoreApplication.translate("AVDV", u"-cd1", None))
        self.radioButton_cd_part_upper.setText(QCoreApplication.translate("AVDV", u"-CD1", None))
        self.label_99.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6587\u4ef6\u540d\u542b\u6709-CD1/_CD1/-PART1/_PART1/.PART1/-1/_1\u5b57\u6837\u65f6\uff0c\u4f1a\u8bc6\u522b\u4e3a\u5206\u96c6\u5e76\u6309\u6240\u9009\u89c4\u5219\u91cd\u547d\u540d", None))
        self.groupBox_77.setTitle(QCoreApplication.translate("AVDV", u"\u957f\u5ea6\u547d\u540d\u89c4\u5219", None))
        self.label_172.setText(QCoreApplication.translate("AVDV", u"\u6307\u6587\u4ef6\u540d\u6700\u957f\u5b57\u7b26\u6570\uff08Windows\u5355\u6587\u4ef6\u540d\u5141\u8bb8\u6700\u5927\u957f\u5ea6255\u5b57\u7b26\uff0c\u5b8c\u6574\u8def\u5f84\u6700\u5927260\u5b57\u7b26\uff09\n"
"\u5f53\u8d85\u8fc7\u6700\u5927\u957f\u5ea6\u65f6\uff0c\u5c06\u901a\u8fc7\u622a\u77ed\u6807\u9898\u5b57\u6bb5\u5185\u5bb9\u6765\u7f29\u77ed\u957f\u5ea6", None))
        self.label_167.setText(QCoreApplication.translate("AVDV", u"\u6f14\u5458\u540d\u6700\u5927\u6570\u91cf\uff1a", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_folder_name_max.setAccessibleDescription(QCoreApplication.translate("AVDV", u"\u6d4b\u8bd5", None))
#endif // QT_CONFIG(accessibility)
        self.label_168.setText(QCoreApplication.translate("AVDV", u"\u6307\u6709\u591a\u4f4d\u6f14\u5458\u65f6\uff0c\u547d\u540d\u65f6\u6700\u591a\u663e\u793a\u7684\u6f14\u5458\u6570\u91cf\u3002\u8d85\u51fa\u7684\u6f14\u5458\u5c06\u7528\u4ee5\u4e0b\u5b57\u7b26\u66ff\u4ee3\uff1a", None))
        self.label_171.setText(QCoreApplication.translate("AVDV", u"\u76ee\u5f55\u540d\u6700\u5927\u957f\u5ea6\uff1a", None))
        self.label_170.setText(QCoreApplication.translate("AVDV", u"\u6587\u4ef6\u540d\u6700\u5927\u957f\u5ea6\uff1a", None))
        self.label_169.setText(QCoreApplication.translate("AVDV", u"\u6307\u76ee\u5f55\u540d\u6700\u957f\u5b57\u7b26\u6570\uff08Windows\u5355\u76ee\u5f55\u540d\u5141\u8bb8\u6700\u5927\u957f\u5ea6255\u5b57\u7b26\uff0c\u5b8c\u6574\u8def\u5f84\u6700\u5927260\u5b57\u7b26\uff09\n"
"\u5f53\u8d85\u8fc7\u6700\u5927\u957f\u5ea6\u65f6\uff0c\u5c06\u901a\u8fc7\u622a\u77ed\u6807\u9898\u5b57\u6bb5\u5185\u5bb9\u6765\u7f29\u77ed\u957f\u5ea6", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("AVDV", u"\u5b57\u6bb5\u547d\u540d\u89c4\u5219", None))
        self.label_100.setText(QCoreApplication.translate("AVDV", u"\u5f53\u6f14\u5458\u540d\u4e0d\u5b58\u5728\u65f6\uff0c\u5728\u4f7f\u7528\u547d\u540d\u5b57\u6bb5\u547d\u540d\u65f6\uff0c\u4f7f\u7528\u4ee5\u4e0a\u5b57\u7b26\u66ff\u4ee3", None))
        self.label_173.setText(QCoreApplication.translate("AVDV", u"\u672a\u77e5\u6f14\u5458\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("AVDV", u"\u547d\u540d", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u5185\u5bb9", None))
        self.checkBox_translate_title.setText(QCoreApplication.translate("AVDV", u"\u6807\u9898", None))
        self.checkBox_translate_outline.setText(QCoreApplication.translate("AVDV", u"\u7b80\u4ecb", None))
        self.label_74.setText(QCoreApplication.translate("AVDV", u"\u4f18\u5148\u4f7f\u7528\u522e\u524a\u7f51\u7ad9\u7684\u4e2d\u6587\u7ffb\u8bd1\uff0c\u5982\u522e\u524a\u9875\u9762\u65e0\u4e2d\u6587\u65f6\uff0c\u518d\u4f7f\u7528\u7ffb\u8bd1\u5f15\u64ce\u7ffb\u8bd1\u3002", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u5f15\u64ce", None))
        self.radioButton_youdao.setText(QCoreApplication.translate("AVDV", u"\u6709\u9053", None))
        self.radioButton_deepl.setText(QCoreApplication.translate("AVDV", u"DeepL", None))
        self.label_81.setText(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u5f15\u64ce\uff1a", None))
        self.label_80.setText(QCoreApplication.translate("AVDV", u"DeepL API key\uff1a", None))
        self.label_60.setText(QCoreApplication.translate("AVDV", u"DeepL\u662f\u4ed8\u8d39\u7ffb\u8bd1\u5f15\u64ce\uff0c\u9700\u8981\u8f93\u5165key\u624d\u80fd\u4f7f\u7528\uff08\u514d\u8d39key\u548c\u4ed8\u8d39key\u90fd\u53ef\u4ee5\uff09", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1\u8bed\u8a00", None))
        self.radioButton_zh_cn.setText(QCoreApplication.translate("AVDV", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.radioButton_zh_tw.setText(QCoreApplication.translate("AVDV", u"\u7e41\u4f53\u4e2d\u6587", None))
        self.radioButton_ja.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u7ffb\u8bd1", None))
        self.label_84.setText(QCoreApplication.translate("AVDV", u"\u4f18\u5148\u4f7f\u7528\u522e\u524a\u7f51\u7ad9\u7684\u4e2d\u6587\u7ffb\u8bd1\uff0c\u5982\u522e\u524a\u9875\u9762\u65e0\u4e2d\u6587\u65f6\uff0c\u518d\u4f7f\u7528\u7ffb\u8bd1\u5f15\u64ce\u7ffb\u8bd1\u3002", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AVDV", u"\u7ffb\u8bd1", None))
        self.groupBox_75.setTitle(QCoreApplication.translate("AVDV", u"\u6f14\u5458\u540d\u6620\u5c04", None))
        self.radioButton_actor_zh_cn.setText(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_actor_zh_tw.setText(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_actor_jp.setText(QCoreApplication.translate("AVDV", u"\u65e5\u8bed", None))
        self.radioButton_actor_no.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u4f7f\u7528\u6620\u5c04", None))
        self.label_162.setText(QCoreApplication.translate("AVDV", u"\u7531\u4e8e\u4e0d\u540c\u7f51\u7ad9\u7684\u6f14\u5458\u540d\u4e0d\u7edf\u4e00\uff0c\u5bfc\u81f4\u522e\u524a\u540e\u6f14\u5458\u547d\u540d\u6bd4\u8f83\u6df7\u4e71\u3002\u4f7f\u7528\u672c\u529f\u80fd\u53ef\u4ee5\u4f7f\u522e\u524a\u540e\u7684\u6f14\u5458\u540d\u6574\u9f50\u7edf\u4e00\u3002\n"
"\u6f14\u5458\u6620\u5c04\u8868\u6587\u4ef6\u540d\u4e3a\uff1amapping_actor.xml\u3002\u53ef\u4f7f\u7528\u6587\u4ef6\u7f16\u8f91\u5de5\u5177\u6253\u5f00\u5e76\u81ea\u5b9a\u4e49\u4fee\u6539\u3002\u6620\u5c04\u8868\u4e2d\u7684\u5b57\u6bb5\u542b\u4e49\u5982\u4e0b\uff1a\n"
"1\uff0ckeyword\uff1a\u5339\u914d\u8bcd\uff08\u6bcf\u4e2a\u540d\u5b57\u524d\u540e\u90fd\u8981\u6709\u9017\u53f7\uff09\u3002\u522e\u524a\u7f51\u7ad9\u83b7\u53d6\u6f14\u5458\u540d\u540e\uff0c\u4f1a\u5728keyword\u7684\u540d\u5b57\u4e2d\u8fdb\u884c\u5339\u914d\u3002\n"
"2\uff0czh_cn/zh_tw/jp\uff1a\u8f93\u51fa\u8bcd\u3002\u5f53keyword\u5339\u914d\u5230\u6f14\u5458\u540d\u65f6\uff0c\u53ef\u8f93\u51fa\u5bf9\u5e94\u8bed\u8a00\u7684\u540d\u5b57\u3002", None))
        self.label_163.setText(QCoreApplication.translate("AVDV", u"\u8f93\u51fa\u8bcd\uff1a", None))
        self.label_164.setText(QCoreApplication.translate("AVDV", u"\u6ce8\uff1a\u4e3a\u4e86\u4fdd\u8bc1emby\u7684\u6f14\u5458\u5934\u50cf\u6b63\u5e38\u663e\u793a\uff0cnfo\u91cc\u7684\u6f14\u5458\u4f1a\u9ed8\u8ba4\u4f7f\u7528\u65e5\u6587\u540d\u5b57\u3002", None))
        self.groupBox_76.setTitle(QCoreApplication.translate("AVDV", u"\u4fe1\u606f\u6620\u5c04\uff08\u6807\u7b7e\u3001\u5bfc\u6f14\u3001\u7cfb\u5217\u3001\u5236\u4f5c\u3001\u53d1\u884c\uff09", None))
        self.radioButton_tag_zh_cn.setText(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_tag_zh_tw.setText(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_tag_jp.setText(QCoreApplication.translate("AVDV", u"\u65e5\u8bed", None))
        self.radioButton_tag_no.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u4f7f\u7528\u6620\u5c04", None))
        self.label_165.setText(QCoreApplication.translate("AVDV", u"\u4fe1\u606f\u6620\u5c04\u8868\u6587\u4ef6\u540d\u4e3a\uff1amapping_info.xml\u3002\u4f5c\u7528\u548c\u6f14\u5458\u6620\u5c04\u8868\u7c7b\u4f3c\uff0c\u8bf4\u660e\u53ef\u53c2\u8003\u6f14\u5458\u6620\u5c04\u8868\u3002", None))
        self.label_166.setText(QCoreApplication.translate("AVDV", u"\u8f93\u51fa\u8bcd\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("AVDV", u"\u6620\u5c04", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("AVDV", u"\u5934\u50cf\u76ee\u5f55", None))
        self.label_77.setText(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\u5934\u50cf\u5305\u89e3\u538b\uff0c\u586b\u5199\u5934\u50cf\u56fe\u7247\u76ee\u5f55\u7684\u8def\u5f84", None))
        self.label_101.setText(QCoreApplication.translate("AVDV", u"\u5934\u50cf\u56fe\u7247\u76ee\u5f55\uff1a", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("AVDV", u"Emby\u4fe1\u606f", None))
        self.label_104.setText(QCoreApplication.translate("AVDV", u"Emby\u5730\u5740\uff1a", None))
        self.label_105.setText(QCoreApplication.translate("AVDV", u"API\u5bc6\u94a5\u521b\u5efa\u65b9\u6cd5\uff1aEmby\u63a7\u5236\u53f0->\u9ad8\u7ea7->API\u5bc6\u94a5->\u6dfb\u52a0(APP\u540d\u79f0\u4efb\u610f)\u3002", None))
        self.label_107.setText(QCoreApplication.translate("AVDV", u"API\u5bc6\u94a5\uff1a", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("AVDV", u"\u4e0a\u4f20\u5934\u50cf", None))
        self.radioButton_actor_photo_upload_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_actor_photo_upload_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.label_103.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u540e\u81ea\u52a8\u4e0a\u4f20\u5934\u50cf\uff1a", None))
        self.label_106.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u540e\uff0c\u4f1a\u68c0\u67e5emby\u4e2d\u7f3a\u5931\u7684\u6f14\u5458\u5934\u50cf\uff0c\u5982\u5934\u50cf\u5305\u4e2d\u6709\u5bf9\u5e94\u56fe\u7247\u5c06\u81ea\u52a8\u4e0a\u4f20\u3002", None))
        self.pushButton_add_actor_pic.setText(QCoreApplication.translate("AVDV", u"\u70b9\u51fb\u4e0a\u4f20\u5934\u50cf", None))
        self.pushButton_show_pic_actor.setText(QCoreApplication.translate("AVDV", u"\u67e5\u770b\u6f14\u5458\u5217\u8868", None))
        self.comboBox_pic_actor.setItemText(0, QCoreApplication.translate("AVDV", u"\u6ca1\u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(1, QCoreApplication.translate("AVDV", u"\u5df2\u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(2, QCoreApplication.translate("AVDV", u"\u6240\u6709\u6f14\u5458", None))

        self.label_download_acotr_zip.setText(QCoreApplication.translate("AVDV", u"\u70b9\u51fb\u4e0b\u8f7d\u5934\u50cf\u5305", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("AVDV", u"\u5934\u50cf", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u5b57\u5e55\u5b57\u7b26", None))
        self.label_91.setText(QCoreApplication.translate("AVDV", u"\u6307\u6587\u4ef6\u8def\u5f84\u4e2d\u542b\u6709\u4ee5\u4e0a\u5b57\u7b26\u65f6\uff0c\u89c6\u4e3a\u8be5\u6587\u4ef6\u6709\u4e2d\u6587\u5b57\u5e55\uff0c\u591a\u4e2a\u4ee5\u9017\u53f7\u5206\u5272", None))
        self.label_69.setText(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u5b57\u5e55\u547d\u540d\u5b57\u7b26\uff1a", None))
        self.label_89.setText(QCoreApplication.translate("AVDV", u"\u4e2d\u6587\u5b57\u5e55\u5224\u65ad\u5b57\u7b26\uff1a", None))
        self.label_90.setText(QCoreApplication.translate("AVDV", u"\u6307\u6709\u4e2d\u6587\u5b57\u5e55\u65f6\uff0c\u5728\u91cd\u547d\u540d\u6587\u4ef6\u540d\u53ca\u76ee\u5f55\u540d\u65f6\u5728\u756a\u53f7\u540e\u663e\u793a\u8be5\u5b57\u7b26\u8868\u793a\u6709\u4e2d\u6587\u5b57\u5e55", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("AVDV", u"\u8981\u663e\u793a\u4e2d\u6587\u5b57\u5e55\u547d\u540d\u5b57\u7b26\u7684\u9879", None))
        self.checkBox_foldername.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u76ee\u5f55\u540d", None))
        self.checkBox_filename.setText(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u6587\u4ef6\u540d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AVDV", u"\u5b57\u5e55", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("AVDV", u"\u8981\u6dfb\u52a0\u6c34\u5370\u7684\u56fe\u7247", None))
        self.checkBox_poster_mark.setText(QCoreApplication.translate("AVDV", u"poster", None))
        self.checkBox_thumb_mark.setText(QCoreApplication.translate("AVDV", u"thumb", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("AVDV", u"\u6c34\u5370", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("AVDV", u"Cookie\u8bbe\u7f6e", None))
        self.label_45.setText(QCoreApplication.translate("AVDV", u"javdb\uff1a\n"
"\uff08\u767b\u5f55\u72b6\u6001\uff09", None))
        self.label_75.setText(QCoreApplication.translate("AVDV", u"Cookie \u83b7\u53d6\u65b9\u6cd5\uff1a\n"
"\u4f7f\u7528 Chrome \u6253\u5f00\u76ee\u6807\u7f51\u7ad9\u540e\uff0c\u70b9\u51fb\u9f20\u6807\u53f3\u952e\uff0c\u9009\u62e9 \u201c\u68c0\u67e5\u201d \uff0c\u53f3\u4fa7\u9876\u90e8\u9009\u62e9\uff1aNetwork -> DOC\uff0c\n"
"\u7136\u540e F5 \u5237\u65b0\u9875\u9762\u3002\u70b9\u51fb name \u680f\u52a0\u8f7d\u51fa\u6765\u7684\u7b2c\u4e00\u4e2a\u5185\u5bb9 -> Headers -> Request Headers -> Cookie\u3002\n"
"\u590d\u5236 Cookie \u5bf9\u5e94\u7684\u5168\u90e8\u503c\u586b\u4eba\u4e0a\u9762\u8f93\u5165\u6846\u3002 \uff08\u6ce8\u610f\uff1aCookie \u5b58\u5728\u6709\u6548\u671f\uff0c\u8fc7\u671f\u65e0\u6548\u65f6\u8bf7\u91cd\u65b0\u83b7\u53d6\u3002\uff09", None))
        self.label_get_cookie_url.setText(QCoreApplication.translate("AVDV", u"https://tieba.baidu.com/p/5492736764", None))
        self.label_7.setText(QCoreApplication.translate("AVDV", u"\u65b9\u6cd5\u53ef\u53c2\u8003\uff1a", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("AVDV", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.label_65.setText(QCoreApplication.translate("AVDV", u"\u91cd\u8bd5\u6b21\u6570\uff1a", None))
        self.label_73.setText(QCoreApplication.translate("AVDV", u"\u8d85\u65f6\u65f6\u95f4\uff1a", None))
        self.label_64.setText(QCoreApplication.translate("AVDV", u"IP+\u7aef\u53e3\u53f7\uff1a", None))
        self.radioButton_proxy_http.setText(QCoreApplication.translate("AVDV", u"http", None))
        self.radioButton_proxy_socks5.setText(QCoreApplication.translate("AVDV", u"socks5", None))
        self.radioButton_proxy_nouse.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u4f7f\u7528", None))
        self.label_70.setText(QCoreApplication.translate("AVDV", u"\u4ee3\u7406\uff1a", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("AVDV", u"\u7f51\u5740\u8bbe\u7f6e", None))
        self.label_109.setText(QCoreApplication.translate("AVDV", u"javbus\uff1a", None))
        self.label_108.setText(QCoreApplication.translate("AVDV", u"javdb\uff1a", None))
        self.label_110.setText(QCoreApplication.translate("AVDV", u"\u5f53\u586b\u5199\u7f51\u5740\u65f6\uff0c\u4f18\u5148\u4f7f\u7528\u6b64\u5904\u586b\u5199\u7684\u7f51\u5740", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("AVDV", u"\u7f51\u7edc", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58\u65e5\u5fd7", None))
        self.radioButton_log_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_log_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AVDV", u"\u8c03\u8bd5\u6a21\u5f0f", None))
        self.radioButton_debug_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_debug_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AVDV", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.radioButton_update_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_update_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("AVDV", u"\u5176\u4ed6", None))
        self.label_4.setText("")
        self.pushButton_init_config.setText(QCoreApplication.translate("AVDV", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.pushButton_save_config.setText(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58", None))
        self.textBrowser_about.setHtml(QCoreApplication.translate("AVDV", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">AVDCx \u662f\u57fa\u4e8e AV_Data_Capture \u7684 GUI \u7248\u672c AVDC \u518d\u6b21\u4fee\u6539\u7684\u7248\u672c\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size"
                        ":13px;\">\u00b7 AV_Data_Capture \u9879\u76ee\u5730\u5740\uff1ahttps://github.com/yoshiko2/AV_Data_Capture</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u00b7 AVDC \u9879\u76ee\u5730\u5740\uff1ahttps://github.com/moyy996/AVDC</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u00b7 AVDCx \u9879\u76ee\u5730\u5740\uff1ahttps://github.com/Hermit10/AVDCx</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; fo"
                        "nt-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u4f7f\u7528\u8bf4\u660e \uff08\u5185\u5bb9\u6765\u81ea AVDC \uff1ahttps://github.com/moyy996/AVDC \uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-s"
                        "ize:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u4e00\u3001\u529f\u80fd\u7b80\u4ecb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u56db\u3001\u8bbe\u7f6e\u8bf4\u660e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">\u4e00\u3001\u529f\u80fd\u7b80\u4ecb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u65e5\u672c\u7535\u5f71\u5143\u6570\u636e\u6293\u53d6\u5de5\u5177/\u522e\u524a\u5668\uff0c\u914d\u5408\u672c\u5730\u5f71\u7247\u7ba1\u7406\u8f6f\u4ef6EMBY,KODI\uff0cPLEX\u7b49\u7ba1\u7406\u672c\u5730\u5f71\u7247\uff0c\u8be5\u8f6f\u4ef6\u8d77"
                        "\u5230\u5206\u7c7b\u4e0e\u5143\u6570\u636e\u6293\u53d6\u4f5c\u7528\uff0c\u5229\u7528\u5143\u6570\u636e\u4fe1\u606f\u6765\u5206\u7c7b\uff0c\u4f9b\u672c\u5730\u5f71\u7247\u5206\u7c7b\u6574\u7406\u4f7f\u7528\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Gui made by moyy996\uff0cCore made by yoshiko2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-family:'Courier'; font-size:13px;\">  tg\u5b98\u65b9\u7535\u62a5\u7fa4: https://t.me/joinchat/Sp_Ec-XNbUlLj4oV</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u547d\u4ee4\u884c\u7248\u9879\u76ee\u5730\u5740\uff1ahttps://github.com/yoshiko2/AV_Data_Capture</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  GUI\u7248\u9879\u76ee\u5730\u5740\uff1ahttps://github.com/moyy996/AVDC</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  GUI\u7248EXE\u4e0b\u8f7d\u5730\u5740\uff1ahttps://github.com/moyy996/AVDC/releases</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:"
                        "0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">\u4e0d\u533a\u5206\u5927\u5c0f\u5199\u3001\u522e\u524a\u524d\u5c3d\u91cf\u547d\u540d\u89c4\u8303\uff01\uff01\uff01\uff01</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.1.\u6807\u51c6\u6709\u7801</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margi"
                        "n-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Javdb\u3001Javbus:SSNI-111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Dmm\uff1assni00111</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.2.\u65e0\u7801</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Javdb\u3001Javbus\u3001Avsox:111111-11"
                        "11\u3001111111_111\u3001HEYZO-1111\u3001n1111</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.3.\u7d20\u4eba</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Mgstage:259LUXU-1111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Javdb:LUXU-1111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Fc2club:FC2-111111\u3001FC2-PPV-111111\u3001FC2PPV-111111</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.4.\u6b27\u7f8e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  Javdb\u3001Javbus:sexart.11.11.11(\u7cfb\u5217.\u5e74.\u6708.\u65e5)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.5.\u81ea\u5e26\u5b57\u5e55\u5f71\u7247</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u53ef\u4ee5\u628a\u7535\u5f71\u547d\u540d\u4e3a\u7c7b\u4f3cssni-xxx-c.mp4,ssni-xxx-C.mp4\uff0cabp-xxx-CD1-C.mp4 \u7684\u89c4\u5219\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.6.\u591a\u96c6\u5f71\u7247</span></p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u53ef\u4ee5\u628a\u591a\u96c6\u7535\u5f71\u6309\u7167\u96c6\u6570\u540e\u7f00\u547d\u540d\u4e3a\u7c7b\u4f3cssni-xxx-cd1.mp4, ssni-xxx-cd2.mp4, abp-xxx-CD1-C.mp4\u7684\u89c4\u5219\uff0c\u53ea\u8981\u542b\u6709-CDn/-cdn\u7c7b\u4f3c\u547d\u540d\u89c4\u5219\uff0c\u5373\u53ef\u4f7f\u7528\u5206\u96c6\u529f\u80fd.**\u4e0d\u652f\u6301-A -B -1 -2,\u5bb9\u6613\u8ddf\u5b57\u5e55\u7684-C\u6df7\u6dc6**.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.7.\u591a\u96c6\u3001\u5b57\u5e55\u987a\u5e8f<"
                        "/span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  abp-xxx-CD1-C.mp4\uff0c\u5206\u96c6\u5728\u524d\uff0c\u5b57\u5e55\u5728\u540e\uff0c\u5b57\u5e55\u5fc5\u987b\u4e0e\u62d3\u5c55\u540d\u9760\u8fd1\uff0c-C.mp4.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">3.8.\u5916\u6302\u5b57\u5e55\u6587\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u5b57\u5e55\u6587\u4ef6\u540d"
                        "\u5fc5\u987b\u4e0e\u5f71\u7247\u6587\u4ef6\u540d\u4e00\u81f4\uff0c\u624d\u53ef\u4ee5\u4e00\u8d77\u79fb\u52a8\u5230\u65b0\u76ee\u5f55\uff0c\u76ee\u524d\u652f\u6301srt ass sub\u7c7b\u578b\u7684\u5b57\u5e55\u6587\u4ef6\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">\u56db\u3001\u8bbe\u7f6e\u8bf4\u660e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-family:'Courier'; font-size:13px;\">\u8be6\u7ec6\u7684\u8bf4\u660e\uff1a https://github.com/moyy996/AVDC/blob/master/README.md</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.1.\u522e\u524a\u6a21\u5f0f/\u6574\u7406\u6a21\u5f0f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  1\u3001\u522e\u524a\u6a21\u5f0f\uff1a\u901a\u8fc7\u756a\u53f7\u522e\u524a\u6570\u636e\uff0c\u5305\u62ec\u5143\u6570\u636e\u3001\u5c01\u9762\u56fe\u3001\u7f29\u7565\u56fe\u3001\u80cc\u666f\u56fe\u3002</span></p>\n"
"<p style=\" marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  2\u3001\u6574\u7406\u6a21\u5f0f\uff1a\u4ec5\u6839\u636e\u5973\u4f18\u628a\u7535\u5f71\u547d\u540d\u4e3a\u756a\u53f7\u5e76\u5206\u7c7b\u5230\u5973\u4f18\u540d\u79f0\u7684\u6587\u4ef6\u5939\u4e0b\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.2.\u8f6f\u94fe\u63a5\u6a21\u5f0f\uff1a\u4f7f\u7528\u6b64\u6a21\u5f0f\uff0c\u8981\u4ee5\u7ba1\u7406\u5458\u8eab\u4efd\u8fd0\u884c\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u522e\u524a\u5b8c\u4e0d\u79fb\u52a8\u89c6\u9891\uff0c\u800c\u662f\u5728\u76f8\u5e94\u76ee\u5f55\u521b\u5efa\u8f6f\u94fe\u63a5\uff08\u7c7b\u4f3c\u4e8e\u5feb\u6377\u65b9\u5f0f\uff09\uff0c\u65b9\u4fbfPT\u4e0b\u8f7d\u5b8c\u65e2\u60f3\u522e\u524a\u53c8\u60f3\u7ee7\u7eed\u4e0a\u4f20\u7684\u4ed3\u9f20\u515a\u540c\u5fd7\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u4f46\u662f\uff0c\u53ea\u80fd\u5728\u5a92\u4f53\u5e93\u5c55\u793a\uff0c\u4e0d\u80fd\u5728\u5a92\u4f53\u5e93\u64ad\u653e\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.3.\u8c03\u8bd5\u6a21\u5f0f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u8f93\u51fa\u756a\u53f7\u7684\u5143\u6570\u636e\uff0c\u5305\u62ec\u5c01\u9762\uff0c\u5bfc\u6f14\uff0c\u6f14\u5458\uff0c\u7b80\u4ecb\u7b49\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.4.\u6392\u9664\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u5728\u591a\u5c42\u76ee\u5f55\u522e\u524a\u65f6\u6392\u9664\u6240\u586b\u76ee\u5f55\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.5.\u89c6\u9891\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u8981\u6574\u7406\u7684\u89c6\u9891\u7684\u76ee\u5f55\uff0c\u4f1a\u904d\u5386\u6b64\u76ee\u5f55\u4e0b\u7684\u6240\u6709\u89c6\u9891\uff0c\u5305\u62ec\u5b50\u76ee\u5f55\u4e2d\u3002</span></p>\n"
"<p style=\"-qt-paragraph-ty"
                        "pe:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.6.\u547d\u540d\u89c4\u5219</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  1\u3001\u76ee\u5f55\u547d\u540d\uff1a\u5b58\u653e\u89c6\u9891\u6570\u636e\u7684\u76ee\u5f55\u540d\uff0c\u652f\u6301\u591a\u5c42\u76ee\u5f55\uff0c\u652f\u6301\u81ea\u5b9a\u4e49\u7b26\u53f7\uff0c\u4f8b\uff1a[actor]/studio/number-\u3010title\u3011\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:"
                        "13px;\">  2\u3001\u89c6\u9891\u6807\u9898\uff08\u5a92\u4f53\u5e93\u4e2d\uff09\uff1anfo\u4e2d\u7684\u6807\u9898\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  3\u3001\u89c6\u9891\u6807\u9898\uff08\u672c\u5730\u6587\u4ef6\uff09\uff1a\u672c\u5730\u89c6\u9891\u3001\u56fe\u7247\u7684\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  4\u3001\u53ef\u9009\u9879\u4e3atitle\uff08\u7247\u540d\uff09\u3001actor\uff08\u6f14\u5458\uff09\u3001studio\uff08\u5236\u4f5c\u5546\uff09\u3001director\uff08\u5bfc\u6f14\uff09\u3001release\uff08\u53d1\u552e\u65e5"
                        "\uff09\u3001year\uff08\u53d1\u884c\u5e74\u4efd\uff09\u3001number\uff08\u756a\u53f7\uff09\u3001runtime\uff08\u65f6\u957f\uff09\u3001series\uff08\u7cfb\u5217\uff09\u3001publisher\uff08\u53d1\u884c\u5546\uff09</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.7.\u4ee3\u7406\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  1\u3001\u4ee3\u7406</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Co"
                        "urier'; font-size:13px;\">  proxy=127.0.0.1:1080</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  proxy\u884c\u8bbe\u7f6e\u672c\u5730\u4ee3\u7406\u5730\u5740\u548c\u7aef\u53e3\uff0c\u652f\u6301Shadowxxxx/X,V2XXX\u672c\u5730\u4ee3\u7406\u7aef\u53e3\uff0c\u4ee3\u7406\u8f6f\u4ef6\u5f00\u5168\u5c40\u6a21\u5f0f ,\u5efa\u8bae\u4f7f\u7528\u65e5\u672c\u4ee3\u7406\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u5982\u679c\u4e00\u76f4\u62a5Connect Failed! Please check your Proxy or Network!\u9519\u8bef\uff0c\u8bf7\u68c0\u67e5\u7aef\u53e3\u53f7\u662f\u5426\u6b63\u786e\uff0c\u6216\u8005\u628aproxy=\u540e\u9762\u7684\u5730\u5740\u548c\u7aef\u53e3\u5220\u9664\uff0c\u5e76\u5f00\u542f\u4ee3\u7406\u8f6f\u4ef6\u5168\u5c40\u6a21\u5f0f\uff0c"
                        "\u6216\u8005\u91cd\u542f\u7535\u8111\uff0c\u4ee3\u7406\u8f6f\u4ef6\uff0c\u7f51\u5361\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  2\u3001\u8fde\u63a5\u8d85\u65f6\u91cd\u8bd5\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  timeout=10 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  10\u4e3a\u8d85\u65f6\u91cd\u8bd5\u65f6\u95f4 \u5355\u4f4d\uff1a\u79d2\uff0c\u53ef\u9009\u8303\u56f43-10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-s"
                        "ize:13px;\">  3\u3001\u8fde\u63a5\u91cd\u8bd5\u6b21\u6570\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  retry=3 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  3\u5373\u4e3a\u91cd\u8bd5\u6b21\u6570\uff0c\u53ef\u9009\u8303\u56f42-5</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.8.\u5a92\u4f53\u5e93\u9009\u62e9</span></p>\n"
"<p style=\" margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u5982\u679c\u662fPLEX\uff0c\u8bf7\u5b89\u88c5\u63d2\u4ef6\uff1aXBMCnfoMoviesImporter</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.9.\u6392\u9664\u6307\u5b9a\u5b57\u7b26\u548c\u76ee\u5f55\uff0c\u5b57\u7b26\u4e32</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  1\u3001\u6392\u9664\u5b57\u7b26:\u6307\u5b9a\u5b57\u7b26\u5220\u9664\uff0c\u4f8b\u5982\u6392\u9664\u5b57"
                        "\u7b26\uff1a \\()\uff0c\u5220\u9664\u521b\u5efa\u6587\u4ef6\u5939\u65f6\u7684\\()\u5b57\u7b26</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  2\u3001\u6392\u9664\u76ee\u5f55:\u6307\u5b9a\u76ee\u5f55\uff0c\u4f8b\u5982\u6392\u9664\u76ee\u5f55\uff1a failed,JAV_output\uff0c\u591a\u76ee\u5f55\u522e\u524a\u65f6\u8df3\u8fc7failed,JAV_output</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  3\u3001\u6392\u9664\u5b57\u7b26\u4e32:\u63d0\u53d6\u756a\u53f7\u65f6\uff0c\u5148\u5220\u9664\u6307\u5b9a\u5b57\u7b26\u4e32\uff0c\u63d0\u9ad8\u6210\u529f\u7387\uff0c\u5b57\u7b26\u4e32\u4e4b\u95f4\u7528','\u9694\u5f00\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.10.\u7f51\u7ad9\u9009\u62e9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u53ef\u4ee5\u4f7f\u7528\u6240\u6709\u7f51\u7ad9\uff0c\u6216\u8005\u6307\u5b9a\u7f51\u7ad9\uff08avsox,javbus,dmm,javdb,fc2club\uff0cmgstage\uff09\u8fdb\u884c\u522e\u524a\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u4ec5\u4f7f\u7528javdb\u8fdb\u884c\u522e\u524a\uff0c\u5c3d\u91cf\u4e0d\u8981\u7528\uff0c\u522e\u524a30\u5de6\u53f3\u4f1a\u88abJAVDB\u5c01IP\u4e00\u6bb5"
                        "\u65f6\u95f4\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.11.\u4fdd\u5b58\u65e5\u5fd7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u5f00\u542f\u540e\u65e5\u5fd7\u4fdd\u5b58\u5728\u7a0b\u5e8f\u76ee\u5f55\u7684Log\u76ee\u5f55\u4e0b\u7684txt\u6587\u4ef6\u5185\uff0c\u6bcf\u6b21\u8fd0\u884c\u4f1a\u4ea7\u751f\u4e00\u4e2atxt\u6587\u4ef6\uff0ctxt\u6587\u4ef6\u53ef\u4ee5\u5220\u9664\uff0c\u4e0d\u5f71\u54cd\u7a0b\u5e8f\u8fd0\u884c\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px; font-weight:600;\">4.12.\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\">  \u5982\u679c\u522e\u524a\u4e0d\u5230\u5f71\u7247\u4fe1\u606f\uff0c\u53ef\u9009\u62e9\u4e0d\u79fb\u52a8\u89c6\u9891\uff0c\u6216\u8005\u81ea\u52a8\u79fb\u52a8\u5230\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\u4e2d\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:13px;\"> </span></p>\n"
"<p style=\"-qt-paragraph-t"
                        "ype:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:13px;\"><br /></p></body></html>", None))
        self.label_ico.setText(QCoreApplication.translate("AVDV", u"\u56fe\u6807", None))
        self.pushButton_main.setText(QCoreApplication.translate("AVDV", u"\u4e3b\u754c\u9762", None))
        self.pushButton_log.setText(QCoreApplication.translate("AVDV", u"\u65e5\u5fd7", None))
        self.pushButton_tool.setText(QCoreApplication.translate("AVDV", u"\u5de5\u5177", None))
        self.pushButton_setting.setText(QCoreApplication.translate("AVDV", u"\u8bbe\u7f6e", None))
        self.pushButton_net.setText(QCoreApplication.translate("AVDV", u"\u68c0\u6d4b\u7f51\u7edc", None))
        self.pushButton_about.setText(QCoreApplication.translate("AVDV", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.pushButton_close.setText(QCoreApplication.translate("AVDV", u"\u00d7", None))
        self.pushButton_min.setText(QCoreApplication.translate("AVDV", u"-", None))
        self.label_show_version.setText(QCoreApplication.translate("AVDV", u"\u7248\u672c\u53f7", None))
    # retranslateUi

