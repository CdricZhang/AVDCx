# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVDCwAedvb.ui'
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
        AVDV.resize(1018, 699)
        icon = QIcon()
        icon.addFile(u"../Img/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        AVDV.setWindowIcon(icon)
        self.centralwidget = QWidget(AVDV)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 10, 781, 681))
        self.page_avdc = QWidget()
        self.page_avdc.setObjectName(u"page_avdc")
        self.pushButton_start_cap = QPushButton(self.page_avdc)
        self.pushButton_start_cap.setObjectName(u"pushButton_start_cap")
        self.pushButton_start_cap.setGeometry(QRect(641, 10, 121, 44))
        self.treeWidget_number = QTreeWidget(self.page_avdc)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setBackground(0, QColor(236, 236, 236, 42));
        __qtreewidgetitem.setForeground(0, brush);
        self.treeWidget_number.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget_number)
        QTreeWidgetItem(self.treeWidget_number)
        self.treeWidget_number.setObjectName(u"treeWidget_number")
        self.treeWidget_number.setGeometry(QRect(0, 70, 201, 601))
        self.treeWidget_number.setStyleSheet(u"")
        self.gridLayoutWidget_2 = QWidget(self.page_avdc)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(210, 450, 161, 221))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_poster = QLabel(self.gridLayoutWidget_2)
        self.label_poster.setObjectName(u"label_poster")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_poster.sizePolicy().hasHeightForWidth())
        self.label_poster.setSizePolicy(sizePolicy)
        self.label_poster.setMinimumSize(QSize(0, 0))
        self.label_poster.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_poster.setFrameShape(QFrame.Box)
        self.label_poster.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_poster, 0, 0, 1, 1)

        self.gridLayoutWidget = QWidget(self.page_avdc)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(430, 450, 331, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_thumb = QLabel(self.gridLayoutWidget)
        self.label_thumb.setObjectName(u"label_thumb")
        self.label_thumb.setEnabled(True)
        self.label_thumb.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_thumb.setFrameShape(QFrame.Box)
        self.label_thumb.setAlignment(Qt.AlignCenter)
        self.label_thumb.setMargin(0)

        self.gridLayout.addWidget(self.label_thumb, 0, 0, 1, 1)

        self.label_11 = QLabel(self.page_avdc)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(210, 70, 51, 39))
        self.label_number = QLabel(self.page_avdc)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setGeometry(QRect(260, 70, 201, 39))
        self.label_number.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_number.setFrameShape(QFrame.Box)
        self.label_number.setLineWidth(1)
        self.label_13 = QLabel(self.page_avdc)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(480, 70, 81, 39))
        self.label_release = QLabel(self.page_avdc)
        self.label_release.setObjectName(u"label_release")
        self.label_release.setGeometry(QRect(560, 70, 201, 39))
        self.label_release.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_release.setFrameShape(QFrame.Box)
        self.label_15 = QLabel(self.page_avdc)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(210, 270, 51, 39))
        self.label_actor = QLabel(self.page_avdc)
        self.label_actor.setObjectName(u"label_actor")
        self.label_actor.setGeometry(QRect(260, 270, 501, 39))
        self.label_actor.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_actor.setFrameShape(QFrame.Box)
        self.label_actor.setLineWidth(1)
        self.label_outline = QLabel(self.page_avdc)
        self.label_outline.setObjectName(u"label_outline")
        self.label_outline.setGeometry(QRect(260, 320, 501, 39))
        self.label_outline.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_outline.setFrameShape(QFrame.Box)
        self.label_outline.setLineWidth(1)
        self.label_18 = QLabel(self.page_avdc)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(210, 320, 51, 39))
        self.label_title = QLabel(self.page_avdc)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(260, 220, 501, 39))
        self.label_title.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_title.setFrameShape(QFrame.Box)
        self.label_title.setLineWidth(1)
        self.label_20 = QLabel(self.page_avdc)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(210, 220, 51, 39))
        self.label_director = QLabel(self.page_avdc)
        self.label_director.setObjectName(u"label_director")
        self.label_director.setGeometry(QRect(260, 120, 201, 39))
        self.label_director.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_director.setFrameShape(QFrame.Box)
        self.label_director.setLineWidth(1)
        self.label_publish = QLabel(self.page_avdc)
        self.label_publish.setObjectName(u"label_publish")
        self.label_publish.setGeometry(QRect(560, 170, 201, 39))
        self.label_publish.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_publish.setFrameShape(QFrame.Box)
        self.label_23 = QLabel(self.page_avdc)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(210, 120, 51, 39))
        self.label_24 = QLabel(self.page_avdc)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(480, 170, 81, 39))
        self.label_studio = QLabel(self.page_avdc)
        self.label_studio.setObjectName(u"label_studio")
        self.label_studio.setGeometry(QRect(260, 170, 201, 39))
        self.label_studio.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_studio.setFrameShape(QFrame.Box)
        self.label_studio.setLineWidth(1)
        self.label_label = QLabel(self.page_avdc)
        self.label_label.setObjectName(u"label_label")
        self.label_label.setGeometry(QRect(560, 120, 201, 39))
        self.label_label.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_label.setFrameShape(QFrame.Box)
        self.label_30 = QLabel(self.page_avdc)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(210, 170, 51, 39))
        self.label_31 = QLabel(self.page_avdc)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(480, 120, 81, 39))
        self.label_tag = QLabel(self.page_avdc)
        self.label_tag.setObjectName(u"label_tag")
        self.label_tag.setGeometry(QRect(260, 370, 501, 39))
        self.label_tag.setStyleSheet(u"border:1px solid rgba(0, 0, 0, 80);")
        self.label_tag.setFrameShape(QFrame.Box)
        self.label_tag.setLineWidth(1)
        self.label_33 = QLabel(self.page_avdc)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(210, 370, 51, 39))
        self.checkBox_cover = QCheckBox(self.page_avdc)
        self.checkBox_cover.setObjectName(u"checkBox_cover")
        self.checkBox_cover.setGeometry(QRect(210, 420, 321, 21))
        self.progressBar_avdc = QProgressBar(self.page_avdc)
        self.progressBar_avdc.setObjectName(u"progressBar_avdc")
        self.progressBar_avdc.setGeometry(QRect(1, 20, 461, 20))
        self.progressBar_avdc.setMinimumSize(QSize(0, 5))
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
"   background-color: #FFFFFF;\n"
"}")
        self.progressBar_avdc.setValue(24)
        self.label_percent = QLabel(self.page_avdc)
        self.label_percent.setObjectName(u"label_percent")
        self.label_percent.setGeometry(QRect(470, 20, 50, 30))
        self.label_percent.setMinimumSize(QSize(50, 20))
        self.label_percent.setSizeIncrement(QSize(0, 0))
        self.label_percent.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_percent.setFont(font)
        self.label_percent.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_progress = QLabel(self.page_avdc)
        self.label_progress.setObjectName(u"label_progress")
        self.label_progress.setGeometry(QRect(540, 17, 81, 30))
        sizePolicy.setHeightForWidth(self.label_progress.sizePolicy().hasHeightForWidth())
        self.label_progress.setSizePolicy(sizePolicy)
        self.label_progress.setMinimumSize(QSize(60, 20))
        self.label_progress.setMaximumSize(QSize(16777215, 16777215))
        self.label_progress.setFont(font)
        self.label_progress.setCursor(QCursor(Qt.ArrowCursor))
        self.label_progress.setLayoutDirection(Qt.LeftToRight)
        self.label_progress.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line = QFrame(self.page_avdc)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(1, 30, 461, 30))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_avdc)
        self.pushButton_start_cap.raise_()
        self.treeWidget_number.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget.raise_()
        self.label_11.raise_()
        self.label_number.raise_()
        self.label_13.raise_()
        self.label_release.raise_()
        self.label_15.raise_()
        self.label_actor.raise_()
        self.label_outline.raise_()
        self.label_18.raise_()
        self.label_title.raise_()
        self.label_20.raise_()
        self.label_director.raise_()
        self.label_publish.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_studio.raise_()
        self.label_label.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_tag.raise_()
        self.label_33.raise_()
        self.checkBox_cover.raise_()
        self.label_percent.raise_()
        self.label_progress.raise_()
        self.line.raise_()
        self.progressBar_avdc.raise_()
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.textBrowser_log_main = QTextBrowser(self.page_log)
        self.textBrowser_log_main.setObjectName(u"textBrowser_log_main")
        self.textBrowser_log_main.setGeometry(QRect(10, 0, 771, 681))
        self.pushButton_start_cap2 = QPushButton(self.page_log)
        self.pushButton_start_cap2.setObjectName(u"pushButton_start_cap2")
        self.pushButton_start_cap2.setGeometry(QRect(641, 10, 121, 44))
        self.stackedWidget.addWidget(self.page_log)
        self.page_net = QWidget()
        self.page_net.setObjectName(u"page_net")
        self.textBrowser_net_main = QTextBrowser(self.page_net)
        self.textBrowser_net_main.setObjectName(u"textBrowser_net_main")
        self.textBrowser_net_main.setGeometry(QRect(10, 0, 771, 681))
        self.pushButton_check_net = QPushButton(self.page_net)
        self.pushButton_check_net.setObjectName(u"pushButton_check_net")
        self.pushButton_check_net.setGeometry(QRect(641, 10, 121, 44))
        self.stackedWidget.addWidget(self.page_net)
        self.page_tool = QWidget()
        self.page_tool.setObjectName(u"page_tool")
        self.groupBox_6 = QGroupBox(self.page_tool)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 10, 751, 121))
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 60, 511, 41))
        self.pushButton_move_mp4 = QPushButton(self.groupBox_6)
        self.pushButton_move_mp4.setObjectName(u"pushButton_move_mp4")
        self.pushButton_move_mp4.setGeometry(QRect(10, 30, 201, 50))
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(230, 30, 81, 24))
        self.lineEdit_escape_dir_move = QLineEdit(self.groupBox_6)
        self.lineEdit_escape_dir_move.setObjectName(u"lineEdit_escape_dir_move")
        self.lineEdit_escape_dir_move.setGeometry(QRect(310, 30, 431, 24))
        self.groupBox_7 = QGroupBox(self.page_tool)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 140, 751, 171))
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 120, 511, 41))
        self.pushButton_select_file = QPushButton(self.groupBox_7)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setGeometry(QRect(10, 30, 201, 50))
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
        self.comboBox_website.setObjectName(u"comboBox_website")
        self.comboBox_website.setGeometry(QRect(310, 90, 431, 22))
        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 90, 72, 21))
        self.lineEdit_appoint_url = QLineEdit(self.groupBox_7)
        self.lineEdit_appoint_url.setObjectName(u"lineEdit_appoint_url")
        self.lineEdit_appoint_url.setGeometry(QRect(310, 60, 431, 21))
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 60, 72, 15))
        self.lineEdit_movie_number = QLineEdit(self.groupBox_7)
        self.lineEdit_movie_number.setObjectName(u"lineEdit_movie_number")
        self.lineEdit_movie_number.setGeometry(QRect(310, 30, 431, 21))
        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(230, 30, 72, 15))
        self.pushButton_start_single_file = QPushButton(self.groupBox_7)
        self.pushButton_start_single_file.setObjectName(u"pushButton_start_single_file")
        self.pushButton_start_single_file.setGeometry(QRect(10, 120, 201, 41))
        self.groupBox_12 = QGroupBox(self.page_tool)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 340, 751, 191))
        self.pushButton_add_actor_pic = QPushButton(self.groupBox_12)
        self.pushButton_add_actor_pic.setObjectName(u"pushButton_add_actor_pic")
        self.pushButton_add_actor_pic.setGeometry(QRect(10, 30, 201, 50))
        self.lineEdit_emby_url = QLineEdit(self.groupBox_12)
        self.lineEdit_emby_url.setObjectName(u"lineEdit_emby_url")
        self.lineEdit_emby_url.setGeometry(QRect(310, 30, 431, 21))
        self.label_3 = QLabel(self.groupBox_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 30, 72, 15))
        self.label_4 = QLabel(self.groupBox_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 74, 72, 21))
        self.lineEdit_api_key = QLineEdit(self.groupBox_12)
        self.lineEdit_api_key.setObjectName(u"lineEdit_api_key")
        self.lineEdit_api_key.setGeometry(QRect(310, 70, 431, 21))
        self.label_5 = QLabel(self.groupBox_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 110, 511, 71))
        self.pushButton_show_pic_actor = QPushButton(self.groupBox_12)
        self.pushButton_show_pic_actor.setObjectName(u"pushButton_show_pic_actor")
        self.pushButton_show_pic_actor.setGeometry(QRect(10, 140, 201, 40))
        self.comboBox_pic_actor = QComboBox(self.groupBox_12)
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.setObjectName(u"comboBox_pic_actor")
        self.comboBox_pic_actor.setGeometry(QRect(10, 100, 201, 21))
        self.groupBox_13 = QGroupBox(self.page_tool)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(10, 540, 751, 111))
        self.pushButton_select_thumb = QPushButton(self.groupBox_13)
        self.pushButton_select_thumb.setObjectName(u"pushButton_select_thumb")
        self.pushButton_select_thumb.setGeometry(QRect(10, 20, 201, 50))
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 20, 511, 71))
        self.stackedWidget.addWidget(self.page_tool)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.pushButton_save_config = QPushButton(self.page_setting)
        self.pushButton_save_config.setObjectName(u"pushButton_save_config")
        self.pushButton_save_config.setGeometry(QRect(300, 630, 350, 44))
        self.tabWidget = QTabWidget(self.page_setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 771, 591))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.groupBox_10 = QGroupBox(self.tab1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 80, 741, 441))
        self.groupBox_15 = QGroupBox(self.groupBox_10)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 270, 711, 51))
        self.groupBox_15.setMinimumSize(QSize(500, 0))
        self.groupBox_15.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_12 = QWidget(self.groupBox_15)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.radioButton_fail_move_on = QRadioButton(self.horizontalLayoutWidget_12)
        self.radioButton_fail_move_on.setObjectName(u"radioButton_fail_move_on")

        self.horizontalLayout_14.addWidget(self.radioButton_fail_move_on)

        self.radioButton_fail_move_off = QRadioButton(self.horizontalLayoutWidget_12)
        self.radioButton_fail_move_off.setObjectName(u"radioButton_fail_move_off")

        self.horizontalLayout_14.addWidget(self.radioButton_fail_move_off)

        self.groupBox_3 = QGroupBox(self.groupBox_10)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 120, 711, 51))
        self.groupBox_3.setMinimumSize(QSize(500, 0))
        self.groupBox_3.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_9 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.radioButton_debug_on = QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_debug_on.setObjectName(u"radioButton_debug_on")

        self.horizontalLayout_11.addWidget(self.radioButton_debug_on)

        self.radioButton_debug_off = QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_debug_off.setObjectName(u"radioButton_debug_off")

        self.horizontalLayout_11.addWidget(self.radioButton_debug_off)

        self.groupBox_17 = QGroupBox(self.groupBox_10)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(10, 220, 711, 51))
        self.groupBox_17.setMinimumSize(QSize(500, 0))
        self.groupBox_17.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_11 = QWidget(self.groupBox_17)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.radioButton_log_on = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_on.setObjectName(u"radioButton_log_on")

        self.horizontalLayout_13.addWidget(self.radioButton_log_on)

        self.radioButton_log_off = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_off.setObjectName(u"radioButton_log_off")

        self.horizontalLayout_13.addWidget(self.radioButton_log_off)

        self.groupBox_23 = QGroupBox(self.groupBox_10)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setGeometry(QRect(10, 320, 711, 51))
        self.groupBox_23.setMinimumSize(QSize(500, 0))
        self.groupBox_23.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_13 = QWidget(self.groupBox_23)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.radioButton_extrafanart_download_on = QRadioButton(self.horizontalLayoutWidget_13)
        self.radioButton_extrafanart_download_on.setObjectName(u"radioButton_extrafanart_download_on")

        self.horizontalLayout_15.addWidget(self.radioButton_extrafanart_download_on)

        self.radioButton_extrafanart_download_off = QRadioButton(self.horizontalLayoutWidget_13)
        self.radioButton_extrafanart_download_off.setObjectName(u"radioButton_extrafanart_download_off")

        self.horizontalLayout_15.addWidget(self.radioButton_extrafanart_download_off)

        self.groupBox_2 = QGroupBox(self.groupBox_10)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 70, 711, 51))
        self.groupBox_2.setMinimumSize(QSize(500, 0))
        self.groupBox_2.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_8 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.radioButton_soft_on = QRadioButton(self.horizontalLayoutWidget_8)
        self.radioButton_soft_on.setObjectName(u"radioButton_soft_on")

        self.horizontalLayout_10.addWidget(self.radioButton_soft_on)

        self.radioButton_soft_off = QRadioButton(self.horizontalLayoutWidget_8)
        self.radioButton_soft_off.setObjectName(u"radioButton_soft_off")

        self.horizontalLayout_10.addWidget(self.radioButton_soft_off)

        self.groupBox_4 = QGroupBox(self.groupBox_10)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 170, 711, 51))
        self.groupBox_4.setMinimumSize(QSize(500, 0))
        self.groupBox_4.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_10 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.radioButton_update_on = QRadioButton(self.horizontalLayoutWidget_10)
        self.radioButton_update_on.setObjectName(u"radioButton_update_on")

        self.horizontalLayout_12.addWidget(self.radioButton_update_on)

        self.radioButton_update_off = QRadioButton(self.horizontalLayoutWidget_10)
        self.radioButton_update_off.setObjectName(u"radioButton_update_off")

        self.horizontalLayout_12.addWidget(self.radioButton_update_off)

        self.groupBox = QGroupBox(self.groupBox_10)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(11, 20, 711, 51))
        self.groupBox.setMinimumSize(QSize(500, 0))
        self.groupBox.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(120, 20, 591, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.radioButton_common = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_common.setObjectName(u"radioButton_common")

        self.horizontalLayout_9.addWidget(self.radioButton_common)

        self.radioButton_sort = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_sort.setObjectName(u"radioButton_sort")

        self.horizontalLayout_9.addWidget(self.radioButton_sort)

        self.groupBox_24 = QGroupBox(self.groupBox_10)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(10, 380, 711, 51))
        self.groupBox_24.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_14 = QWidget(self.groupBox_24)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(120, 20, 590, 31))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_download_nfo = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_nfo.setObjectName(u"checkBox_download_nfo")

        self.horizontalLayout_16.addWidget(self.checkBox_download_nfo)

        self.checkBox_download_poster = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_poster.setObjectName(u"checkBox_download_poster")

        self.horizontalLayout_16.addWidget(self.checkBox_download_poster)

        self.checkBox_download_fanart = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_fanart.setObjectName(u"checkBox_download_fanart")

        self.horizontalLayout_16.addWidget(self.checkBox_download_fanart)

        self.checkBox_download_thumb = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_thumb.setObjectName(u"checkBox_download_thumb")

        self.horizontalLayout_16.addWidget(self.checkBox_download_thumb)

        self.groupBox_11 = QGroupBox(self.tab1)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(10, 10, 741, 61))
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
        self.comboBox_website_all.setObjectName(u"comboBox_website_all")
        self.comboBox_website_all.setGeometry(QRect(130, 20, 591, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_website_all.sizePolicy().hasHeightForWidth())
        self.comboBox_website_all.setSizePolicy(sizePolicy1)
        self.comboBox_website_all.setMinimumSize(QSize(400, 30))
        self.comboBox_website_all.setMaximumSize(QSize(16000, 30))
        self.comboBox_website_all.setSizeIncrement(QSize(0, 0))
        self.comboBox_website_all.setStyleSheet(u"")
        self.comboBox_website_all.setFrame(False)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.groupBox_8 = QGroupBox(self.tab2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 10, 741, 191))
        self.formLayoutWidget_4 = QWidget(self.groupBox_8)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 30, 721, 161))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.formLayoutWidget_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(170, 30))
        self.label_43.setLayoutDirection(Qt.RightToLeft)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_43)

        self.lineEdit_dir_name = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_dir_name.setObjectName(u"lineEdit_dir_name")
        self.lineEdit_dir_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_dir_name.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.lineEdit_dir_name)

        self.label_44 = QLabel(self.formLayoutWidget_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(170, 30))
        self.label_44.setLayoutDirection(Qt.RightToLeft)
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_44)

        self.lineEdit_media_name = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_media_name.setObjectName(u"lineEdit_media_name")
        self.lineEdit_media_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_media_name.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.lineEdit_media_name)

        self.label_45 = QLabel(self.formLayoutWidget_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(170, 30))
        self.label_45.setLayoutDirection(Qt.RightToLeft)
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_local_name = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_local_name.setObjectName(u"lineEdit_local_name")
        self.lineEdit_local_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_local_name.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.lineEdit_local_name)

        self.label_51 = QLabel(self.formLayoutWidget_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(170, 30))
        self.label_51.setLayoutDirection(Qt.RightToLeft)
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_51)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton_foldername_C_on = QRadioButton(self.formLayoutWidget_4)
        self.radioButton_foldername_C_on.setObjectName(u"radioButton_foldername_C_on")
        self.radioButton_foldername_C_on.setMinimumSize(QSize(100, 30))
        self.radioButton_foldername_C_on.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_21.addWidget(self.radioButton_foldername_C_on)

        self.radioButton_foldername_C_off = QRadioButton(self.formLayoutWidget_4)
        self.radioButton_foldername_C_off.setObjectName(u"radioButton_foldername_C_off")
        self.radioButton_foldername_C_off.setMinimumSize(QSize(100, 30))
        self.radioButton_foldername_C_off.setMaximumSize(QSize(1800, 16777215))

        self.horizontalLayout_21.addWidget(self.radioButton_foldername_C_off)


        self.formLayout_6.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_21)

        self.groupBox_16 = QGroupBox(self.tab2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(10, 210, 741, 351))
        self.formLayoutWidget_5 = QWidget(self.groupBox_16)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(10, 60, 721, 271))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.formLayoutWidget_5)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(170, 30))
        self.label_49.setLayoutDirection(Qt.RightToLeft)
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_49)

        self.lineEdit_movie_path = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_movie_path.setObjectName(u"lineEdit_movie_path")
        self.lineEdit_movie_path.setMinimumSize(QSize(500, 30))
        self.lineEdit_movie_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_movie_path)

        self.label_47 = QLabel(self.formLayoutWidget_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(170, 30))
        self.label_47.setLayoutDirection(Qt.RightToLeft)
        self.label_47.setFrameShape(QFrame.NoFrame)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_47)

        self.lineEdit_success = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_success.setObjectName(u"lineEdit_success")
        self.lineEdit_success.setMinimumSize(QSize(500, 30))
        self.lineEdit_success.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_success)

        self.label_40 = QLabel(self.formLayoutWidget_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(170, 30))
        self.label_40.setLayoutDirection(Qt.RightToLeft)
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_40)

        self.lineEdit_movie_type = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_movie_type.setObjectName(u"lineEdit_movie_type")
        self.lineEdit_movie_type.setMinimumSize(QSize(500, 30))
        self.lineEdit_movie_type.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_movie_type)

        self.label_48 = QLabel(self.formLayoutWidget_5)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(170, 30))
        self.label_48.setLayoutDirection(Qt.RightToLeft)
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_48)

        self.lineEdit_escape_dir = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_escape_dir.setObjectName(u"lineEdit_escape_dir")
        self.lineEdit_escape_dir.setMinimumSize(QSize(500, 30))
        self.lineEdit_escape_dir.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_escape_dir)

        self.label_46 = QLabel(self.formLayoutWidget_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(170, 30))
        self.label_46.setLayoutDirection(Qt.RightToLeft)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_46)

        self.lineEdit_fail = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_fail.setObjectName(u"lineEdit_fail")
        self.lineEdit_fail.setMinimumSize(QSize(500, 30))
        self.lineEdit_fail.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_fail)

        self.lineEdit_sub_type = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_sub_type.setObjectName(u"lineEdit_sub_type")
        self.lineEdit_sub_type.setMinimumSize(QSize(500, 30))
        self.lineEdit_sub_type.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_sub_type)

        self.label_42 = QLabel(self.formLayoutWidget_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(170, 30))
        self.label_42.setLayoutDirection(Qt.RightToLeft)
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_42)

        self.label_50 = QLabel(self.formLayoutWidget_5)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(170, 30))
        self.label_50.setLayoutDirection(Qt.RightToLeft)
        self.label_50.setFrameShape(QFrame.NoFrame)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_50)

        self.lineEdit_extrafanart_dir = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_extrafanart_dir.setObjectName(u"lineEdit_extrafanart_dir")
        self.lineEdit_extrafanart_dir.setMinimumSize(QSize(500, 30))
        self.lineEdit_extrafanart_dir.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lineEdit_extrafanart_dir)

        self.label_7 = QLabel(self.groupBox_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 30, 501, 20))
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.groupBox_9 = QGroupBox(self.tab3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 10, 741, 211))
        self.formLayoutWidget_2 = QWidget(self.groupBox_9)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 30, 721, 171))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(170, 30))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.radioButton_proxy_http = QRadioButton(self.formLayoutWidget_2)
        self.radioButton_proxy_http.setObjectName(u"radioButton_proxy_http")
        self.radioButton_proxy_http.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_http)

        self.radioButton_proxy_socks5 = QRadioButton(self.formLayoutWidget_2)
        self.radioButton_proxy_socks5.setObjectName(u"radioButton_proxy_socks5")
        self.radioButton_proxy_socks5.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_socks5)

        self.radioButton_proxy_nouse = QRadioButton(self.formLayoutWidget_2)
        self.radioButton_proxy_nouse.setObjectName(u"radioButton_proxy_nouse")
        self.radioButton_proxy_nouse.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_nouse)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_17)

        self.label_25 = QLabel(self.formLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(170, 30))
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_25)

        self.lineEdit_proxy = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_proxy.setObjectName(u"lineEdit_proxy")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_proxy.sizePolicy().hasHeightForWidth())
        self.lineEdit_proxy.setSizePolicy(sizePolicy2)
        self.lineEdit_proxy.setMinimumSize(QSize(300, 30))
        self.lineEdit_proxy.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_proxy)

        self.label_26 = QLabel(self.formLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(170, 30))
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_26)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider_timeout = QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_timeout.setObjectName(u"horizontalSlider_timeout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalSlider_timeout.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_timeout.setSizePolicy(sizePolicy3)
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

        self.lcdNumber_timeout = QLCDNumber(self.formLayoutWidget_2)
        self.lcdNumber_timeout.setObjectName(u"lcdNumber_timeout")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcdNumber_timeout.sizePolicy().hasHeightForWidth())
        self.lcdNumber_timeout.setSizePolicy(sizePolicy4)
        self.lcdNumber_timeout.setMinimumSize(QSize(30, 30))
        self.lcdNumber_timeout.setMaximumSize(QSize(70, 30))
        self.lcdNumber_timeout.setDigitCount(5)
        self.lcdNumber_timeout.setProperty("intValue", 7)

        self.horizontalLayout_3.addWidget(self.lcdNumber_timeout)


        self.formLayout_4.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_27 = QLabel(self.formLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(170, 30))
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_27)

        self.horizontalLayout_retry = QHBoxLayout()
        self.horizontalLayout_retry.setObjectName(u"horizontalLayout_retry")
        self.horizontalSlider_retry = QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_retry.setObjectName(u"horizontalSlider_retry")
        sizePolicy3.setHeightForWidth(self.horizontalSlider_retry.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_retry.setSizePolicy(sizePolicy3)
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

        self.lcdNumber_retry = QLCDNumber(self.formLayoutWidget_2)
        self.lcdNumber_retry.setObjectName(u"lcdNumber_retry")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lcdNumber_retry.sizePolicy().hasHeightForWidth())
        self.lcdNumber_retry.setSizePolicy(sizePolicy5)
        self.lcdNumber_retry.setMinimumSize(QSize(30, 30))
        self.lcdNumber_retry.setMaximumSize(QSize(70, 30))
        self.lcdNumber_retry.setProperty("intValue", 3)

        self.horizontalLayout_retry.addWidget(self.lcdNumber_retry)


        self.formLayout_4.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_retry)

        self.groupBox_26 = QGroupBox(self.tab3)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(10, 230, 741, 321))
        self.formLayoutWidget_6 = QWidget(self.groupBox_26)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(10, 30, 721, 172))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.javdbCookiesLabel_2 = QLabel(self.formLayoutWidget_6)
        self.javdbCookiesLabel_2.setObjectName(u"javdbCookiesLabel_2")
        self.javdbCookiesLabel_2.setMinimumSize(QSize(170, 80))
        self.javdbCookiesLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.javdbCookiesLabel_2)

        self.plainTextEdit_cookie_javdb = QPlainTextEdit(self.formLayoutWidget_6)
        self.plainTextEdit_cookie_javdb.setObjectName(u"plainTextEdit_cookie_javdb")
        self.plainTextEdit_cookie_javdb.setMinimumSize(QSize(500, 80))
        self.plainTextEdit_cookie_javdb.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 1px;\n"
"")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.plainTextEdit_cookie_javdb)

        self.plainTextEdit_cookie_dmm = QPlainTextEdit(self.formLayoutWidget_6)
        self.plainTextEdit_cookie_dmm.setObjectName(u"plainTextEdit_cookie_dmm")
        self.plainTextEdit_cookie_dmm.setMinimumSize(QSize(500, 80))
        self.plainTextEdit_cookie_dmm.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 1px;\n"
"")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit_cookie_dmm)

        self.dmmCookiesLabel_2 = QLabel(self.formLayoutWidget_6)
        self.dmmCookiesLabel_2.setObjectName(u"dmmCookiesLabel_2")
        self.dmmCookiesLabel_2.setMinimumSize(QSize(170, 80))
        self.dmmCookiesLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.dmmCookiesLabel_2)

        self.label_21 = QLabel(self.groupBox_26)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 220, 721, 91))
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Courier")
        font1.setPointSize(10)
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.groupBox_14 = QGroupBox(self.tab4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(10, 150, 741, 71))
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_14)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(150, 20, 591, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_sub = QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_sub.setObjectName(u"checkBox_sub")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
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

        self.groupBox_19 = QGroupBox(self.tab4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(10, 240, 741, 71))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_19)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(150, 20, 591, 41))
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

        self.groupBox_21 = QGroupBox(self.tab4)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(10, 330, 741, 71))
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox_21)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(150, 20, 591, 41))
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
        sizePolicy4.setHeightForWidth(self.lcdNumber_mark_size.sizePolicy().hasHeightForWidth())
        self.lcdNumber_mark_size.setSizePolicy(sizePolicy4)
        self.lcdNumber_mark_size.setMinimumSize(QSize(30, 30))
        self.lcdNumber_mark_size.setMaximumSize(QSize(70, 30))
        self.lcdNumber_mark_size.setProperty("intValue", 3)

        self.horizontalLayout_6.addWidget(self.lcdNumber_mark_size)

        self.groupBox_20 = QGroupBox(self.tab4)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(10, 10, 741, 51))
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox_20)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(150, 10, 591, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.radioButton_poster_mark_on = QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_poster_mark_on.setObjectName(u"radioButton_poster_mark_on")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.radioButton_poster_mark_on.sizePolicy().hasHeightForWidth())
        self.radioButton_poster_mark_on.setSizePolicy(sizePolicy7)
        self.radioButton_poster_mark_on.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_7.addWidget(self.radioButton_poster_mark_on)

        self.radioButton_poster_mark_off = QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_poster_mark_off.setObjectName(u"radioButton_poster_mark_off")
        sizePolicy7.setHeightForWidth(self.radioButton_poster_mark_off.sizePolicy().hasHeightForWidth())
        self.radioButton_poster_mark_off.setSizePolicy(sizePolicy7)
        self.radioButton_poster_mark_off.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_7.addWidget(self.radioButton_poster_mark_off)

        self.groupBox_22 = QGroupBox(self.tab4)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setGeometry(QRect(10, 80, 741, 51))
        self.horizontalLayoutWidget_6 = QWidget(self.groupBox_22)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(150, 10, 591, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.radioButton_thumb_mark_on = QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_thumb_mark_on.setObjectName(u"radioButton_thumb_mark_on")
        sizePolicy7.setHeightForWidth(self.radioButton_thumb_mark_on.sizePolicy().hasHeightForWidth())
        self.radioButton_thumb_mark_on.setSizePolicy(sizePolicy7)
        self.radioButton_thumb_mark_on.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_8.addWidget(self.radioButton_thumb_mark_on)

        self.radioButton_thumb_mark_off = QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_thumb_mark_off.setObjectName(u"radioButton_thumb_mark_off")
        sizePolicy7.setHeightForWidth(self.radioButton_thumb_mark_off.sizePolicy().hasHeightForWidth())
        self.radioButton_thumb_mark_off.setSizePolicy(sizePolicy7)
        self.radioButton_thumb_mark_off.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_8.addWidget(self.radioButton_thumb_mark_off)

        self.label_9 = QLabel(self.tab4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 420, 591, 61))
        self.tabWidget.addTab(self.tab4, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.groupBox_39 = QGroupBox(self.tab5)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setGeometry(QRect(10, 280, 741, 141))
        self.label_14 = QLabel(self.groupBox_39)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(150, 60, 501, 61))
        self.horizontalLayoutWidget_24 = QWidget(self.groupBox_39)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(120, 20, 541, 32))
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.radioButton_poster_official = QRadioButton(self.horizontalLayoutWidget_24)
        self.radioButton_poster_official.setObjectName(u"radioButton_poster_official")
        self.radioButton_poster_official.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_27.addWidget(self.radioButton_poster_official)

        self.radioButton_poster_cut = QRadioButton(self.horizontalLayoutWidget_24)
        self.radioButton_poster_cut.setObjectName(u"radioButton_poster_cut")
        self.radioButton_poster_cut.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_27.addWidget(self.radioButton_poster_cut)

        self.groupBox_40 = QGroupBox(self.tab5)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setGeometry(QRect(10, 140, 741, 111))
        self.formLayoutWidget = QWidget(self.groupBox_40)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 30, 711, 51))
        self.formLayout_9 = QFormLayout(self.formLayoutWidget)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy6.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy6)
        self.label_16.setMinimumSize(QSize(170, 30))
        self.label_16.setMaximumSize(QSize(1700000, 1700000))
        self.label_16.setLayoutDirection(Qt.RightToLeft)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_uncensored_prefix = QLineEdit(self.formLayoutWidget)
        self.lineEdit_uncensored_prefix.setObjectName(u"lineEdit_uncensored_prefix")
        sizePolicy6.setHeightForWidth(self.lineEdit_uncensored_prefix.sizePolicy().hasHeightForWidth())
        self.lineEdit_uncensored_prefix.setSizePolicy(sizePolicy6)
        self.lineEdit_uncensored_prefix.setMinimumSize(QSize(500, 30))
        self.lineEdit_uncensored_prefix.setMaximumSize(QSize(540, 16777215))
        self.lineEdit_uncensored_prefix.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.lineEdit_uncensored_prefix)

        self.label_17 = QLabel(self.groupBox_40)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(150, 70, 571, 31))
        self.groupBox_18 = QGroupBox(self.tab5)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(10, 10, 741, 121))
        self.formLayoutWidget_3 = QWidget(self.groupBox_18)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 30, 711, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_escape_char = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_escape_char.setObjectName(u"lineEdit_escape_char")
        sizePolicy6.setHeightForWidth(self.lineEdit_escape_char.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_char.setSizePolicy(sizePolicy6)
        self.lineEdit_escape_char.setMinimumSize(QSize(500, 30))
        self.lineEdit_escape_char.setMaximumSize(QSize(540, 16777215))
        self.lineEdit_escape_char.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_escape_char)

        self.label_39 = QLabel(self.formLayoutWidget_3)
        self.label_39.setObjectName(u"label_39")
        sizePolicy6.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy6)
        self.label_39.setMinimumSize(QSize(170, 30))
        self.label_39.setMaximumSize(QSize(1700000, 1700000))
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_39)

        self.lineEdit_escape_string = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_escape_string.setObjectName(u"lineEdit_escape_string")
        sizePolicy6.setHeightForWidth(self.lineEdit_escape_string.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_string.setSizePolicy(sizePolicy6)
        self.lineEdit_escape_string.setMinimumSize(QSize(500, 30))
        self.lineEdit_escape_string.setMaximumSize(QSize(540, 16777215))
        self.lineEdit_escape_string.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_escape_string)

        self.label_38 = QLabel(self.formLayoutWidget_3)
        self.label_38.setObjectName(u"label_38")
        sizePolicy6.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy6)
        self.label_38.setMinimumSize(QSize(170, 30))
        self.label_38.setMaximumSize(QSize(1700000, 1700000))
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_38)

        self.tabWidget.addTab(self.tab5, "")
        self.pushButton_init_config = QPushButton(self.page_setting)
        self.pushButton_init_config.setObjectName(u"pushButton_init_config")
        self.pushButton_init_config.setGeometry(QRect(70, 630, 120, 40))
        self.stackedWidget.addWidget(self.page_setting)
        self.tabWidget.raise_()
        self.pushButton_init_config.raise_()
        self.pushButton_save_config.raise_()
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.textBrowser_about = QTextBrowser(self.page_about)
        self.textBrowser_about.setObjectName(u"textBrowser_about")
        self.textBrowser_about.setGeometry(QRect(0, 0, 781, 681))
        self.stackedWidget.addWidget(self.page_about)
        self.widget_setting = QWidget(self.centralwidget)
        self.widget_setting.setObjectName(u"widget_setting")
        self.widget_setting.setGeometry(QRect(0, 0, 221, 701))
        self.label_ico = QLabel(self.widget_setting)
        self.label_ico.setObjectName(u"label_ico")
        self.label_ico.setGeometry(QRect(40, 470, 141, 221))
        self.layoutWidget = QWidget(self.widget_setting)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 201, 360))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_close = QPushButton(self.layoutWidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(20)
        sizePolicy8.setVerticalStretch(20)
        sizePolicy8.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy8)
        self.pushButton_close.setMinimumSize(QSize(20, 20))
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        self.pushButton_close.setBaseSize(QSize(0, 0))
        self.pushButton_close.setMouseTracking(False)
        self.pushButton_close.setStyleSheet(u"QPushButton{color:#515151;background:#F14C4C;border-radius:10px;}QPushButton:hover{color:white;font:Tahoma;background:#FF6058;}")

        self.horizontalLayout.addWidget(self.pushButton_close)

        self.mini = QLabel(self.layoutWidget)
        self.mini.setObjectName(u"mini")
        self.mini.setStyleSheet(u"border: 1px #336699;")

        self.horizontalLayout.addWidget(self.mini)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_main = QPushButton(self.layoutWidget)
        self.pushButton_main.setObjectName(u"pushButton_main")
        self.pushButton_main.setMinimumSize(QSize(0, 40))
        self.pushButton_main.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.pushButton_main)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_log = QPushButton(self.layoutWidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setMinimumSize(QSize(0, 40))
        self.pushButton_log.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.pushButton_log)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_net = QPushButton(self.layoutWidget)
        self.pushButton_net.setObjectName(u"pushButton_net")
        self.pushButton_net.setMinimumSize(QSize(0, 40))
        self.pushButton_net.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.pushButton_net)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_tool = QPushButton(self.layoutWidget)
        self.pushButton_tool.setObjectName(u"pushButton_tool")
        self.pushButton_tool.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.pushButton_tool)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButton_setting = QPushButton(self.layoutWidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.pushButton_setting)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.pushButton_about = QPushButton(self.layoutWidget)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.pushButton_about)

        AVDV.setCentralWidget(self.centralwidget)

        self.retranslateUi(AVDV)

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AVDV)
    # setupUi

    def retranslateUi(self, AVDV):
        AVDV.setWindowTitle(QCoreApplication.translate("AVDV", u"AVDC", None))
        self.pushButton_start_cap.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb", None))
        ___qtreewidgetitem = self.treeWidget_number.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AVDV", u"\u7ed3\u679c", None));

        __sortingEnabled = self.treeWidget_number.isSortingEnabled()
        self.treeWidget_number.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_number.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("AVDV", u"\u6210\u529f", None));
        ___qtreewidgetitem2 = self.treeWidget_number.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("AVDV", u"\u5931\u8d25", None));
        self.treeWidget_number.setSortingEnabled(__sortingEnabled)

        self.label_poster.setText(QCoreApplication.translate("AVDV", u"\u5c01\u9762\u56fe", None))
        self.label_thumb.setText(QCoreApplication.translate("AVDV", u"\u7f29\u7565\u56fe", None))
        self.label_11.setText(QCoreApplication.translate("AVDV", u"\u756a\u53f7\uff1a", None))
        self.label_number.setText("")
        self.label_13.setText(QCoreApplication.translate("AVDV", u"\u53d1\u884c\u65e5\u671f\uff1a", None))
        self.label_release.setText("")
        self.label_15.setText(QCoreApplication.translate("AVDV", u"\u6f14\u5458\uff1a", None))
        self.label_actor.setText("")
        self.label_outline.setText("")
        self.label_18.setText(QCoreApplication.translate("AVDV", u"\u7b80\u4ecb\uff1a", None))
        self.label_title.setText("")
        self.label_20.setText(QCoreApplication.translate("AVDV", u"\u6807\u9898\uff1a", None))
        self.label_director.setText("")
        self.label_publish.setText("")
        self.label_23.setText(QCoreApplication.translate("AVDV", u"\u5bfc\u6f14\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("AVDV", u"\u53d1\u884c\uff1a", None))
        self.label_studio.setText("")
        self.label_label.setText("")
        self.label_30.setText(QCoreApplication.translate("AVDV", u"\u5236\u4f5c\uff1a", None))
        self.label_31.setText(QCoreApplication.translate("AVDV", u"\u7cfb\u5217\uff1a", None))
        self.label_tag.setText("")
        self.label_33.setText(QCoreApplication.translate("AVDV", u"\u7c7b\u522b\uff1a", None))
        self.checkBox_cover.setText(QCoreApplication.translate("AVDV", u"\u663e\u793a\u5c01\u9762(\u53d6\u6d88\u52fe\u9009\u540e\uff0c\u7acb\u5373\u5173\u95ed\u5c01\u9762\u663e\u793a)", None))
        self.label_percent.setText(QCoreApplication.translate("AVDV", u"0%", None))
        self.label_progress.setText(QCoreApplication.translate("AVDV", u"0/0", None))
        self.pushButton_start_cap2.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb", None))
        self.pushButton_check_net.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("AVDV", u"\u89c6\u9891\u3001\u5b57\u5e55\u79fb\u52a8", None))
        self.label_8.setText(QCoreApplication.translate("AVDV", u"\u2018\u89c6\u9891\u76ee\u5f55\u2019\u7684\u6240\u6709\u5b50\u76ee\u5f55(\u4e0d\u5305\u62ec\u6392\u9664\u76ee\u5f55)\u4e0b\u7684\u89c6\u9891\u53ca\u540c\u540d\u5b57\u5e55\uff0c\n"
"\u79fb\u52a8\u5230\u2018\u89c6\u9891\u76ee\u5f55\u2019\u4e0b\u7684\u2018Movie_moved\u2019\u76ee\u5f55\u4e0b\u3002", None))
        self.pushButton_move_mp4.setText(QCoreApplication.translate("AVDV", u"\u5f00\u59cb\u79fb\u52a8", None))
        self.label_41.setText(QCoreApplication.translate("AVDV", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("AVDV", u"\u5355\u6587\u4ef6\u522e\u524a", None))
        self.label.setText(QCoreApplication.translate("AVDV", u"\u9009\u62e9\u5355\u4e2a\u6587\u4ef6(\u2018\u89c6\u9891\u76ee\u5f55\u2019\u4e0b\u6216\u8005\u5b50\u76ee\u5f55\u4e0b)\u3002\n"
"\u4e0d\u6307\u5b9a\u756a\u53f7\uff0c\u5219\u9ed8\u8ba4\u4f7f\u7528\u6587\u4ef6\u540d\u505a\u4e3a\u756a\u53f7\u8fdb\u884c\u522e\u524a\u3002", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("AVDV", u"\u9009\u62e9\u6587\u4ef6", None))
        self.comboBox_website.setItemText(0, QCoreApplication.translate("AVDV", u"All websites", None))
        self.comboBox_website.setItemText(1, QCoreApplication.translate("AVDV", u"javbus", None))
        self.comboBox_website.setItemText(2, QCoreApplication.translate("AVDV", u"javdb", None))
        self.comboBox_website.setItemText(3, QCoreApplication.translate("AVDV", u"jav321", None))
        self.comboBox_website.setItemText(4, QCoreApplication.translate("AVDV", u"dmm", None))
        self.comboBox_website.setItemText(5, QCoreApplication.translate("AVDV", u"avsox", None))
        self.comboBox_website.setItemText(6, QCoreApplication.translate("AVDV", u"xcity", None))
        self.comboBox_website.setItemText(7, QCoreApplication.translate("AVDV", u"mgstage", None))
        self.comboBox_website.setItemText(8, QCoreApplication.translate("AVDV", u"fc2club", None))

        self.label_2.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u7f51\u7ad9:", None))
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
"  1\u3001\u5bf9\u6709\u4e9b\u5c01\u9762\u56fe(poster)\u4e0d\u6ee1\u610f,\u6bd4\u4f8b\u4e0d\u5bf9\u6216\u8005\u5206\u8fa8\u7387\u592a\u4f4e,\u53ef\u4f7f\u7528\u6b64\u5de5\u5177\u3002\n"
"  2\u3001\u6b64\u5de5\u5177\u901a\u8fc7\u5224\u65ad\u4eba\u8138\u4f4d\u7f6e\uff0c\u53ef\u4ee5\u5c06\u7f29\u7565\u56fe(thumb)\u88c1\u526a\u4e3a\u5c01\u9762\u56fe\u3002", None))
        self.pushButton_save_config.setText(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.groupBox_10.setTitle(QCoreApplication.translate("AVDV", u"\u57fa\u672c\u8bbe\u7f6e", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("AVDV", u"\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6\uff1a", None))
        self.radioButton_fail_move_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_fail_move_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AVDV", u"\u8c03\u8bd5\u6a21\u5f0f\uff1a", None))
        self.radioButton_debug_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_debug_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("AVDV", u"\u4fdd\u5b58\u65e5\u5fd7\uff1a", None))
        self.radioButton_log_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_log_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\u5267\u7167\uff1a", None))
        self.radioButton_extrafanart_download_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_extrafanart_download_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AVDV", u"\u8f6f\u94fe\u63a5\u6a21\u5f0f\uff1a", None))
        self.radioButton_soft_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_soft_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AVDV", u"\u68c0\u6d4b\u66f4\u65b0\uff1a", None))
        self.radioButton_update_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_update_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox.setTitle(QCoreApplication.translate("AVDV", u"\u6a21\u5f0f\uff1a", None))
        self.radioButton_common.setText(QCoreApplication.translate("AVDV", u"\u522e\u524a\u6a21\u5f0f", None))
        self.radioButton_sort.setText(QCoreApplication.translate("AVDV", u"\u6574\u7406\u6a21\u5f0f", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("AVDV", u"\u4e0b\u8f7d\u6587\u4ef6", None))
        self.checkBox_download_nfo.setText(QCoreApplication.translate("AVDV", u"nfo", None))
        self.checkBox_download_poster.setText(QCoreApplication.translate("AVDV", u"poster", None))
        self.checkBox_download_fanart.setText(QCoreApplication.translate("AVDV", u"fanart", None))
        self.checkBox_download_thumb.setText(QCoreApplication.translate("AVDV", u"thumb", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("AVDV", u"\u7f51\u7ad9\u9009\u62e9", None))
        self.comboBox_website_all.setItemText(0, QCoreApplication.translate("AVDV", u"All websites", None))
        self.comboBox_website_all.setItemText(1, QCoreApplication.translate("AVDV", u"javbus", None))
        self.comboBox_website_all.setItemText(2, QCoreApplication.translate("AVDV", u"javdb", None))
        self.comboBox_website_all.setItemText(3, QCoreApplication.translate("AVDV", u"jav321", None))
        self.comboBox_website_all.setItemText(4, QCoreApplication.translate("AVDV", u"dmm", None))
        self.comboBox_website_all.setItemText(5, QCoreApplication.translate("AVDV", u"avsox", None))
        self.comboBox_website_all.setItemText(6, QCoreApplication.translate("AVDV", u"xcity", None))
        self.comboBox_website_all.setItemText(7, QCoreApplication.translate("AVDV", u"mgstage", None))
        self.comboBox_website_all.setItemText(8, QCoreApplication.translate("AVDV", u"fc2club", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("AVDV", u"\u57fa\u672c\u8bbe\u7f6e", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("AVDV", u"\u547d\u540d\u89c4\u5219", None))
        self.label_43.setText(QCoreApplication.translate("AVDV", u"  \u76ee\u5f55\u547d\u540d\uff1a", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_dir_name.setAccessibleDescription(QCoreApplication.translate("AVDV", u"\u6d4b\u8bd5", None))
#endif // QT_CONFIG(accessibility)
        self.label_44.setText(QCoreApplication.translate("AVDV", u"   \u89c6\u9891\u6807\u9898(\u5a92\u4f53\u5e93\u4e2d)\uff1a", None))
        self.label_45.setText(QCoreApplication.translate("AVDV", u"   \u89c6\u9891\u6807\u9898(\u672c\u5730\u6587\u4ef6)\uff1a", None))
        self.label_51.setText(QCoreApplication.translate("AVDV", u"\u6709\u5b57\u5e55\u65f6\u76ee\u5f55\u540d\u79f0\u540e\u6dfb\u52a0-C\uff1a", None))
        self.radioButton_foldername_C_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_foldername_C_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("AVDV", u"\u76ee\u5f55\u8bbe\u7f6e", None))
        self.label_49.setText(QCoreApplication.translate("AVDV", u"   \u89c6\u9891\u76ee\u5f55\uff1a", None))
        self.label_47.setText(QCoreApplication.translate("AVDV", u"   \u6210\u529f\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.label_40.setText(QCoreApplication.translate("AVDV", u"   \u89c6\u9891\u7c7b\u578b\uff1a", None))
        self.label_48.setText(QCoreApplication.translate("AVDV", u"   \u6392\u9664\u76ee\u5f55\uff1a", None))
        self.label_46.setText(QCoreApplication.translate("AVDV", u"   \u5931\u8d25\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.label_42.setText(QCoreApplication.translate("AVDV", u"   \u5b57\u5e55\u7c7b\u578b\uff1a", None))
        self.label_50.setText(QCoreApplication.translate("AVDV", u"   \u5267\u7167\u76ee\u5f55\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("AVDV", u"\u6ce8\u610f\uff1a\u2018\u6210\u529f\u8f93\u51fa\u76ee\u5f55\u2019\u3001\u2018\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\u2019\u3001\u2018\u6392\u9664\u76ee\u5f55\u2019\u5e94\u4e3a\u2018\u89c6\u9891\u76ee\u5f55\u2019\u4e0b\u7684\u76ee\u5f55\u3002", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("AVDV", u"\u76ee\u5f55\u8bbe\u7f6e", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("AVDV", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.label_19.setText(QCoreApplication.translate("AVDV", u"   \u4ee3\u7406\uff1a", None))
        self.radioButton_proxy_http.setText(QCoreApplication.translate("AVDV", u"http", None))
        self.radioButton_proxy_socks5.setText(QCoreApplication.translate("AVDV", u"socks5", None))
        self.radioButton_proxy_nouse.setText(QCoreApplication.translate("AVDV", u"\u4e0d\u4f7f\u7528", None))
        self.label_25.setText(QCoreApplication.translate("AVDV", u"   IP+\u7aef\u53e3\u53f7\uff1a", None))
        self.label_26.setText(QCoreApplication.translate("AVDV", u"   \u8d85\u65f6\u91cd\u8bd5\u65f6\u95f4\uff1a", None))
        self.label_27.setText(QCoreApplication.translate("AVDV", u"   \u91cd\u8bd5\u6b21\u6570\uff1a", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("AVDV", u"Cookie\u8bbe\u7f6e", None))
        self.javdbCookiesLabel_2.setText(QCoreApplication.translate("AVDV", u"javdb\uff1a\n"
"\uff08\u767b\u5f55\u72b6\u6001\uff09", None))
        self.dmmCookiesLabel_2.setText(QCoreApplication.translate("AVDV", u"dmm\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("AVDV", u"Cookie \u83b7\u53d6\u65b9\u6cd5\uff1a\n"
"\u4f7f\u7528 Chrome \u6253\u5f00\u76ee\u6807\u7f51\u7ad9\u540e\uff0c\u70b9\u51fb\u9f20\u6807\u53f3\u952e\uff0c\u9009\u62e9 \u201c\u68c0\u67e5\u201d \uff0c\u53f3\u4fa7\u9876\u90e8\u9009\u62e9\uff1aNetwork -> DOC\uff0c\n"
"\u7136\u540e F5 \u5237\u65b0\u9875\u9762\u3002\u70b9\u51fb name \u680f\u52a0\u8f7d\u51fa\u6765\u7684\u7b2c\u4e00\u4e2a\u5185\u5bb9 -> Headers -> Request Headers -> Cookie\u3002\n"
"\u590d\u5236 Cookie \u5bf9\u5e94\u7684\u5168\u90e8\u503c\u586b\u4eba\u4e0a\u9762\u8f93\u5165\u6846\u3002 \uff08\u6ce8\u610f\uff1aCookie \u5b58\u5728\u6709\u6548\u671f\uff0c\u8fc7\u671f\u65e0\u6548\u65f6\u8bf7\u91cd\u65b0\u83b7\u53d6\u3002\uff09", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("AVDV", u"\u7f51\u7edc\u8bbe\u7f6e", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("AVDV", u"\u8981\u6dfb\u52a0\u7684\u6c34\u5370\u7c7b\u578b", None))
        self.checkBox_sub.setText(QCoreApplication.translate("AVDV", u"\u5b57\u5e55", None))
        self.checkBox_leak.setText(QCoreApplication.translate("AVDV", u"\u6d41\u51fa", None))
        self.checkBox_uncensored.setText(QCoreApplication.translate("AVDV", u"\u65e0\u7801", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("AVDV", u"\u9996\u4e2a\u6c34\u5370\u4f4d\u7f6e", None))
        self.radioButton_top_left.setText(QCoreApplication.translate("AVDV", u"\u5de6\u4e0a", None))
        self.radioButton_bottom_left.setText(QCoreApplication.translate("AVDV", u"\u5de6\u4e0b", None))
        self.radioButton_top_right.setText(QCoreApplication.translate("AVDV", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right.setText(QCoreApplication.translate("AVDV", u"\u53f3\u4e0b", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("AVDV", u"\u6c34\u5370\u5927\u5c0f", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("AVDV", u"\u5c01\u9762\u56fe\u6dfb\u52a0\u6c34\u5370", None))
        self.radioButton_poster_mark_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_poster_mark_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("AVDV", u"\u7f29\u7565\u56fe\u6dfb\u52a0\u6c34\u5370", None))
        self.radioButton_thumb_mark_on.setText(QCoreApplication.translate("AVDV", u"\u5f00", None))
        self.radioButton_thumb_mark_off.setText(QCoreApplication.translate("AVDV", u"\u5173", None))
        self.label_9.setText(QCoreApplication.translate("AVDV", u"\u8bf4\u660e\uff1a\n"
"    1\u3001\u591a\u4e2a\u6c34\u5370\u65f6,\u4ece\u9996\u4e2a\u6c34\u5370,\u987a\u65f6\u9488\u6dfb\u52a0.\n"
"    2\u3001\u6c34\u5370\u6587\u4ef6\u53ef\u81ea\u5df1\u66ff\u6362,\u5206\u8fa8\u7387\u8981\u6c42\u957f\u5bbd 500x300,\u80cc\u666f\u900f\u660e\uff0cpng\u683c\u5f0f.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("AVDV", u"\u6c34\u5370\u8bbe\u7f6e", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("AVDV", u"\u65e0\u7801\u5c01\u9762", None))
        self.label_14.setText(QCoreApplication.translate("AVDV", u"\u8bf4\u660e\uff1a\n"
"    1\u3001\u5b98\u65b9\u5c01\u9762--\u5b8c\u6574\u3001\u4e0d\u6e05\u6670\uff1b\u88c1\u526a\u5c01\u9762--\u6e05\u6670\u3001\u4e0d\u5b8c\u6574\u3002\n"
"    2\u3001\u5b98\u65b9\u65e0\u56fe\uff0c\u81ea\u52a8\u88c1\u526a\u7f29\u7565\u56fe\u3002", None))
        self.radioButton_poster_official.setText(QCoreApplication.translate("AVDV", u"\u5b98\u65b9", None))
        self.radioButton_poster_cut.setText(QCoreApplication.translate("AVDV", u"\u88c1\u526a", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("AVDV", u"\u65e0\u7801\u756a\u53f7", None))
        self.label_16.setText(QCoreApplication.translate("AVDV", u"   \u65e0\u7801\u756a\u53f7\u524d\u7f00\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("AVDV", u"\u8bf4\u660e\uff1a\u53ea\u6dfb\u52a0 HEYZO\u3001n1111\u3001111111-111\u4e4b\u5916\u7684\u524d\u7f00\u3002", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("AVDV", u"\u6392\u9664\u8bbe\u7f6e", None))
        self.label_39.setText(QCoreApplication.translate("AVDV", u"   \u591a\u4f59\u5b57\u7b26\u4e32\uff1a", None))
        self.label_38.setText(QCoreApplication.translate("AVDV", u"   \u5f02\u5e38\u5b57\u7b26\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("AVDV", u"\u5176\u5b83\u8bbe\u7f6e", None))
        self.pushButton_init_config.setText(QCoreApplication.translate("AVDV", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.textBrowser_about.setHtml(QCoreApplication.translate("AVDV", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:20pt; font-weight:600;\">AVDC</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:14pt; font-weight:600;\">\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u4e00\u3001\u529f\u80fd\u7b80\u4ecb\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:6"
                        "00; text-decoration: underline; color:#0000ff;\">\u4e00\u3001\u529f\u80fd\u7b80\u4ecb</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_\u8bbe\u7f6e\u8bf4\u660e\"><span style=\" font-fami"
                        "ly:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">\u56db\u3001\u8bbe\u7f6e\u8bf4\u660e</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u4e00\u3001\u529f\u80fd\u7b80\u4ecb\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u4e00</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u529f\u80fd\u7b80\u4ecb</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  \u65e5\u672c\u7535\u5f71</span><span style=\" font-family:'Co"
                        "urier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5143\u6570\u636e\u6293\u53d6\u5de5\u5177</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">/\u522e\u524a\u5668\uff0c\u914d\u5408\u672c\u5730\u5f71\u7247\u7ba1\u7406\u8f6f\u4ef6</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">EMBY,KODI\uff0cPLEX</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">\u7b49\u7ba1\u7406\u672c\u5730\u5f71\u7247\uff0c\u8be5\u8f6f\u4ef6\u8d77\u5230\u5206\u7c7b\u4e0e\u5143\u6570\u636e\u6293\u53d6\u4f5c\u7528\uff0c\u5229\u7528\u5143\u6570\u636e\u4fe1\u606f\u6765\u5206\u7c7b\uff0c\u4f9b\u672c\u5730\u5f71\u7247</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5206\u7c7b\u6574\u7406</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e;"
                        " background-color:#ffffff;\">\u4f7f\u7528\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u4e8c</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u9879\u76ee\u7b80\u4ecb</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">Gui made by </span><span style=\" font-family:'Courier'; fon"
                        "t-size:12pt; font-weight:600; color:#ff0000;\">moyy996</span><span style=\" font-family:'Courier'; font-size:12pt;\">\uff0cCore made by </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">yoshiko2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">tg\u5b98\u65b9\u7535\u62a5\u7fa4:</span><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:'Courier'; font-size:12pt; text-decoration: underline; color:#0000ff;\"> </span></a><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">\u547d\u4ee4\u884c\u7248\u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/yoshiko2/AV_Data_Capture\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/yoshiko2/AV_Data_Capture</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">GUI\u7248\u9879\u76ee\u5730\u5740\uff1a</span><a href=\"https://github.com/moyy996/AVDC\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff"
                        ";\">https://github.com/moyy996/AVDC</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt;\">GUI\u7248EXE\u4e0b\u8f7d\u5730\u5740\uff1a</span><a href=\"https://github.com/moyy996/AVDC/releases\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC/releases</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003\"></a><span style=\""
                        " font-family:'Courier'; font-size:22pt; font-weight:600;\">\u4e09</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u4e0d\u533a\u5206\u5927\u5c0f\u5199\u3001\u522e\u524a\u524d\u5c3d\u91cf\u547d\u540d\u89c4\u8303\uff01\uff01\uff01\uff01</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">1\u3001\u6807\u51c6\u6709\u7801</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; backgr"
                        "ound-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb\u3001Javbus:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">SSNI-111</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Dmm\uff1a</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">ssni00111</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">2\u3001\u65e0\u7801</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb\u3001Javbus\u3001Avsox:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">111111-1111\u3001111111_111\u3001HEYZO-1111\u3001n1111</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">3\u3001\u7d20\u4eba</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt"
                        "; font-weight:600;\">Mgstage:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">259LUXU-1111</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">LUXU-1111</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Fc2club:</span><span style=\" font-family:'Courier'; "
                        "font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">FC2-111111\u3001FC2-PPV-111111\u3001FC2PPV-111111</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4\u3001\u6b27\u7f8e</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">Javdb\u3001Javbus:</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">sexart.11.11.11(\u7cfb\u5217.\u5e74.\u6708.\u65e5)</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\"> </span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">5\u3001\u81ea\u5e26\u5b57\u5e55\u5f71\u7247</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u53ef\u4ee5\u628a\u7535\u5f71\u547d\u540d\u4e3a\u7c7b\u4f3c</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-c.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">,</span><span style=\" font-family:'Courier'; font-size:12pt; font-w"
                        "eight:600; color:#ff0000;\">ssni-xxx-C.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\uff0c</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">abp-xxx-CD1-C.mp4 </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7684\u89c4\u5219\u3002</span></h4>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">6\u3001\u591a\u96c6\u5f71\u7247</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u53ef\u4ee5\u628a\u591a\u96c6\u7535\u5f71\u6309\u7167\u96c6\u6570\u540e\u7f00\u547d\u540d\u4e3a\u7c7b"
                        "\u4f3c</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-cd1.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">, </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">ssni-xxx-cd2.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">, </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">abp-xxx-CD1-C.mp4</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7684\u89c4\u5219\uff0c\u53ea\u8981\u542b\u6709</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">-CDn/-cdn</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7c7b\u4f3c\u547d\u540d\u89c4\u5219\uff0c\u5373\u53ef\u4f7f\u7528\u5206\u96c6\u529f\u80fd.**\u4e0d\u652f\u6301-A -B -1 -2,\u5bb9\u6613\u8ddf\u5b57\u5e55\u7684-C\u6df7\u6dc6**.</span></h4>\n"
"<h4 style=\" mar"
                        "gin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">7\u3001\u591a\u96c6\u3001\u5b57\u5e55\u987a\u5e8f</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">abp-xxx-CD1-C.mp4</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">\uff0c</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5206\u96c6\u5728\u524d\uff0c\u5b57\u5e55\u5728\u540e</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-"
                        "color:#ffffff;\">\uff0c</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">\u5b57\u5e55\u5fc5\u987b\u4e0e\u62d3\u5c55\u540d\u9760\u8fd1</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">\uff0c-</span><span style=\" font-family:'Courier'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">C.mp4</span><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">.</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">8\u3001\u5916\u6302\u5b57\u5e55\u6587\u4ef6</span></h4>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; font-wei"
                        "ght:600; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">\u5b57\u5e55\u6587\u4ef6\u540d</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u5fc5\u987b\u4e0e</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">\u5f71\u7247\u6587\u4ef6\u540d</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u4e00\u81f4\uff0c\u624d\u53ef\u4ee5\u4e00\u8d77\u79fb\u52a8\u5230\u65b0\u76ee\u5f55\uff0c\u76ee\u524d\u652f\u6301</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600; color:#ff0000;\">srt ass sub</span><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">\u7c7b\u578b\u7684\u5b57\u5e55\u6587\u4ef6\u3002</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;"
                        "\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_\u8bbe\u7f6e\u8bf4\u660e\"></a><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u56db</span><span style=\" font-family:'Courier'; font-size:22pt; font-weight:600;\">\u3001\u8bbe\u7f6e\u8bf4\u660e</span></h1>\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:22pt; font-weight:600;\"><br /></h1>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">\u8be6\u7ec6\u7684\u8bf4\u660e\uff1a </span><a href=\"https://github.com/moyy996/AVDC/blob/master/README.md\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:60"
                        "0; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC/blob/master/README.md</span></a></h1>\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"><br /></h1>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.1.\u522e\u524a\u6a21\u5f0f/\u6574\u7406\u6a21\u5f0f</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">1\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600;"
                        " color:#ff0000;\">\u522e\u524a\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff1a\u901a\u8fc7\u756a\u53f7\u522e\u524a\u6570\u636e\uff0c\u5305\u62ec\u5143\u6570\u636e\u3001\u5c01\u9762\u56fe\u3001\u7f29\u7565\u56fe\u3001\u80cc\u666f\u56fe\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">2\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6574\u7406\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff1a\u4ec5\u6839\u636e\u5973\u4f18\u628a\u7535\u5f71\u547d\u540d\u4e3a\u756a\u53f7\u5e76\u5206\u7c7b\u5230\u5973\u4f18\u540d\u79f0\u7684\u6587\u4ef6\u5939\u4e0b\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.2.\u8f6f\u94fe\u63a5\u6a21\u5f0f\uff1a\u4f7f\u7528\u6b64\u6a21\u5f0f\uff0c\u8981\u4ee5\u7ba1\u7406\u5458\u8eab\u4efd\u8fd0\u884c\u3002</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u522e\u524a\u5b8c\u4e0d\u79fb\u52a8\u89c6\u9891\uff0c\u800c\u662f\u5728\u76f8\u5e94\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt; color:#ff0000;\">\u521b\u5efa\u8f6f\u94fe\u63a5</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u7c7b\u4f3c\u4e8e\u5feb\u6377\u65b9\u5f0f\uff09\uff0c\u65b9\u4fbfPT\u4e0b\u8f7d\u5b8c\u65e2\u60f3\u522e\u524a\u53c8\u60f3\u7ee7\u7eed\u4e0a\u4f20\u7684\u4ed3\u9f20\u515a\u540c\u5fd7"
                        "\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4f46\u662f\uff0c\u53ea\u80fd\u5728\u5a92\u4f53\u5e93\u5c55\u793a\uff0c\u4e0d</span><span style=\" font-family:'Courier'; font-size:10.5pt; color:#ff0000;\">\u80fd\u5728\u5a92\u4f53\u5e93\u64ad\u653e</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.3.\u8c03\u8bd5\u6a21\u5f0f</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#2"
                        "4292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u8f93\u51fa\u756a\u53f7\u7684\u5143\u6570\u636e\uff0c\u5305\u62ec\u5c01\u9762\uff0c\u5bfc\u6f14\uff0c\u6f14\u5458\uff0c\u7b80\u4ecb\u7b49\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.4.\u6392\u9664\u76ee\u5f55</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5728\u591a\u5c42\u76ee\u5f55\u522e\u524a\u65f6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u6240\u586b\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-si"
                        "ze:10.5pt;\">\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.5.\u89c6\u9891\u76ee\u5f55</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u8981\u6574\u7406\u7684\u89c6\u9891\u7684\u76ee\u5f55\uff0c\u4f1a\u904d\u5386\u6b64\u76ee\u5f55\u4e0b\u7684\u6240\u6709\u89c6\u9891\uff0c</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5305\u62ec\u5b50\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e2d\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.6.\u547d\u540d\u89c4\u5219</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">1\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u76ee\u5f55\u547d\u540d</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff1a\u5b58\u653e\u89c6\u9891\u6570\u636e\u7684\u76ee\u5f55\u540d\uff0c\u652f\u6301</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u591a\u5c42\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u652f\u6301</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u81ea\u5b9a\u4e49\u7b26"
                        "\u53f7</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u4f8b\uff1a[actor]/studio/number-\u3010title\u3011\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">2\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u89c6\u9891\u6807\u9898</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u5a92\u4f53\u5e93\u4e2d\uff09\uff1a</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">nfo</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e2d\u7684\u6807\u9898\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">3\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u89c6\u9891\u6807\u9898</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u672c\u5730\u6587\u4ef6\uff09\uff1a\u672c\u5730\u89c6\u9891\u3001\u56fe\u7247\u7684\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">4\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;"
                        "\">\u53ef\u9009\u9879</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e3a</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">title</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u7247\u540d\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">actor</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u6f14\u5458\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">studio</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u5236\u4f5c\u5546\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">director</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u5bfc\u6f14\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">release</span><span style=\" font-fami"
                        "ly:'Courier'; font-size:10.5pt;\">\uff08\u53d1\u552e\u65e5\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">year</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u53d1\u884c\u5e74\u4efd\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">number</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u756a\u53f7\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">runtime</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u65f6\u957f\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">series</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08\u7cfb\u5217\uff09\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">publisher</span><span style=\" font-family:'Courier'; f"
                        "ont-size:10.5pt;\">\uff08\u53d1\u884c\u5546\uff09</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.7.\u4ee3\u7406\u8bbe\u7f6e</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\">(1).\u4ee3\u7406</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">proxy=127.0.0.1:1080</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; col"
                        "or:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">proxy\u884c\u8bbe\u7f6e</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u672c\u5730\u4ee3\u7406\u5730\u5740\u548c\u7aef\u53e3</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u652f\u6301Shadowxxxx/X,V2XXX\u672c\u5730\u4ee3\u7406\u7aef\u53e3\uff0c\u4ee3\u7406\u8f6f\u4ef6\u5f00</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5168\u5c40\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\"> ,\u5efa\u8bae\u4f7f\u7528</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u65e5\u672c\u4ee3\u7406</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5982\u679c\u4e00\u76f4\u62a5Connect Failed! Please check your Proxy or Network!\u9519\u8bef\uff0c\u8bf7</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u68c0\u67e5\u7aef\u53e3\u53f7</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u662f\u5426\u6b63\u786e\uff0c\u6216\u8005\u628aproxy=\u540e\u9762\u7684\u5730\u5740\u548c\u7aef\u53e3</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5220\u9664</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u5e76\u5f00\u542f\u4ee3\u7406\u8f6f\u4ef6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5168\u5c40\u6a21\u5f0f</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u6216\u8005\u91cd\u542f\u7535\u8111\uff0c\u4ee3\u7406\u8f6f\u4ef6\uff0c\u7f51"
                        "\u5361\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\">(2).\u8fde\u63a5\u8d85\u65f6\u91cd\u8bd5\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">timeout=10 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">10\u4e3a\u8d85\u65f6\u91cd\u8bd5\u65f6\u95f4 \u5355\u4f4d\uff1a\u79d2\uff0c\u53ef\u9009\u8303\u56f43-10</span></p>\n"
"<p style=\" margin-top:12p"
                        "x; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\">(3).\u8fde\u63a5\u91cd\u8bd5\u6b21\u6570\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">retry=3 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">3\u5373\u4e3a\u91cd\u8bd5\u6b21\u6570\uff0c\u53ef\u9009\u8303\u56f42-5</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.8.\u5a92\u4f53\u5e93\u9009\u62e9</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5982\u679c\u662fPLEX\uff0c\u8bf7\u5b89\u88c5\u63d2\u4ef6\uff1a</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">XBMCnfoMoviesImporter</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.9.\u6392\u9664\u6307\u5b9a\u5b57\u7b26\u548c\u76ee\u5f55\uff0c\u5b57\u7b26\u4e32</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">1\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u5b57\u7b26</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">:\u6307\u5b9a\u5b57\u7b26\u5220\u9664\uff0c\u4f8b\u5982\u6392\u9664\u5b57\u7b26\uff1a \\()\uff0c\u5220\u9664</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u521b\u5efa\u6587\u4ef6\u5939\u65f6</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u7684\\()\u5b57\u7b26</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">2\u3001</span><span sty"
                        "le=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u76ee\u5f55</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">:\u6307\u5b9a\u76ee\u5f55\uff0c\u4f8b\u5982\u6392\u9664\u76ee\u5f55\uff1a failed,JAV_output\uff0c\u591a\u76ee\u5f55\u522e\u524a\u65f6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u8df3\u8fc7</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">failed,JAV_output</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">3\u3001</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6392\u9664\u5b57\u7b26\u4e32</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">:\u63d0\u53d6\u756a\u53f7\u65f6"
                        "\uff0c\u5148\u5220\u9664\u6307\u5b9a\u5b57\u7b26\u4e32\uff0c\u63d0\u9ad8\u6210\u529f\u7387\uff0c\u5b57\u7b26\u4e32\u4e4b\u95f4\u7528','\u9694\u5f00\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.10.\u7f51\u7ad9\u9009\u62e9</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u53ef\u4ee5\u4f7f\u7528</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u6240\u6709\u7f51\u7ad9</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u6216\u8005</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">"
                        "\u6307\u5b9a\u7f51\u7ad9</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff08</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">avsox,javbus,dmm,javdb,fc2club\uff0cmgstage</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff09\u8fdb\u884c\u522e\u524a\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4ec5\u4f7f\u7528javdb\u8fdb\u884c\u522e\u524a\uff0c</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u5c3d\u91cf\u4e0d\u8981\u7528</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u522e\u524a30\u5de6\u53f3\u4f1a\u88abJAVDB</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff00"
                        "00;\">\u5c01IP</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u4e00\u6bb5\u65f6\u95f4\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.11.\u4fdd\u5b58\u65e5\u5fd7</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5f00\u542f\u540e\u65e5\u5fd7\u4fdd\u5b58\u5728</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u7a0b\u5e8f\u76ee\u5f55\u7684Log\u76ee\u5f55\u4e0b</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u7684txt\u6587\u4ef6\u5185\uff0c\u6bcf\u6b21\u8fd0\u884c\u4f1a\u4ea7\u751f\u4e00\u4e2atxt\u6587\u4ef6\uff0c"
                        "txt\u6587\u4ef6</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u53ef\u4ee5\u5220\u9664</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u4e0d\u5f71\u54cd\u7a0b\u5e8f\u8fd0\u884c\u3002</span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:12pt; font-weight:600;\">4.12.\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6</span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">  </span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\u5982\u679c\u522e\u524a\u4e0d\u5230\u5f71\u7247\u4fe1\u606f\uff0c</span><span style=\" font-family:'Courier'; font-size:10.5pt; font-weight:600; color:#ff0000;\">\u53ef\u9009\u62e9\u4e0d\u79fb\u52a8\u89c6"
                        "\u9891</span><span style=\" font-family:'Courier'; font-size:10.5pt;\">\uff0c\u6216\u8005\u81ea\u52a8\u79fb\u52a8\u5230\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\u4e2d\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier'; font-size:10.5pt;\"> </span></p></body></html>", None))
        self.label_ico.setText(QCoreApplication.translate("AVDV", u"\u56fe\u6807", None))
        self.pushButton_close.setText(QCoreApplication.translate("AVDV", u"\u00d7", None))
        self.mini.setText("")
        self.pushButton_main.setText(QCoreApplication.translate("AVDV", u"\u4e3b\u754c\u9762", None))
        self.pushButton_log.setText(QCoreApplication.translate("AVDV", u"\u65e5\u5fd7", None))
        self.pushButton_net.setText(QCoreApplication.translate("AVDV", u"\u68c0\u6d4b\u7f51\u7edc", None))
        self.pushButton_tool.setText(QCoreApplication.translate("AVDV", u"\u5de5\u5177", None))
        self.pushButton_setting.setText(QCoreApplication.translate("AVDV", u"\u8bbe\u7f6e", None))
        self.pushButton_about.setText(QCoreApplication.translate("AVDV", u"\u5173\u4e8e", None))
    # retranslateUi

