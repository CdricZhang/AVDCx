#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import traceback
# import faulthandler
# faulthandler.enable()
import threading
import json
from PyQt5 import QtWidgets
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QApplication, QPushButton, QDialog, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt, QCoreApplication, QPoint, QRect
import sys
import time
import os.path
import requests
import shutil
import base64
import re
from PIL import Image, ImageFilter
import os
import webbrowser
from configparser import RawConfigParser
from Ui.AVDC import Ui_AVDV
from Ui.posterCutTool import Ui_Dialog_cut_poster
from Function.Function import save_config, movie_lists, get_info, getDataFromJSON, getNumber, check_pic, is_uncensored
from Function.getHtml import get_html, get_proxy_info
import socks
import urllib3,urllib
urllib3.disable_warnings()
from lxml import etree
import random
import hashlib
import zhconv
import langid
import platform
import cloudscraper
import cv2

class MyMAinWindow(QMainWindow, Ui_AVDV):
    progressBarValue = pyqtSignal(int)  # 进度条信号量
    main_logs_show = pyqtSignal(str) # 刮削日志信号
    net_logs_show = pyqtSignal(str) # 网络检测日志信号
    set_javdb_cookie = pyqtSignal(str) # 加载javdb cookie文本内容到设置页面
    set_label_file_path = pyqtSignal(str)
    set_tree_child = pyqtSignal(str, str)
    set_main_info = pyqtSignal(object)

    def __init__(self, parent=None):
        super(MyMAinWindow, self).__init__(parent)
        self.main_path = self.mainPath()
        self.Ui = Ui_AVDV()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.Init_Ui()
        self.set_style()
        self.pushButton_main_clicked()
        # 初始化需要的变量
        # self.version = '3.963'
        self.localversion = '20210928'
        self.Ui.label_show_version.setText('version ' + self.localversion)
        self.Ui.label_show_version.mousePressEvent = self.version_clicked
        self.json_data = {}
        self.img_path = ''
        self.Ui.label_number.mousePressEvent = self.label_number_clicked
        self.Ui.label_source.mousePressEvent = self.label_number_clicked
        self.Ui.label_actor.mousePressEvent = self.label_actor_clicked
        self.default_poster = self.resource_path('Img/default-poster.jpg')
        self.default_thumb = self.resource_path('Img/default-thumb.jpg')
        self.actor_xml = ''
        self.c_numuber_jsonfile = self.resource_path(self.c_numberPath())
        self.tag_file = self.resource_path(self.infoPath())
        self.actor_file = self.resource_path(self.actorPath())
        self.m_drag = False
        self.m_DragPosition = 0
        self.count_claw = 0  # 批量刮削次数
        self.item_succ = self.Ui.treeWidget_number.topLevelItem(0)
        self.item_fail = self.Ui.treeWidget_number.topLevelItem(1)
        self.set_tree_child.connect(self.addTreeChild)
        self.set_main_info.connect(self.add_label_info_Thread)
        self.single_file_path = ''
        self.json_array = {}
        self.current_proxy = ''  # 代理设置
        self.github_project_url = 'https://github.com/Hermit10/AVDCx/'  # 项目主页
        self.Init()
        self.Load_config()
        self.set_label_file_path.emit('🎈 设置-目录设置-待刮削视频目录，然后点击开始！\n')
        self.show_version() # 启动后在【日志】页面显示版本信息
        self.new_proxy = self.check_proxyChange()
        self.addNetTextMain('\n🏠 代理设置在:【设置】 - 【网络设置】 - 【代理设置】。\n') 
        self.show_netstatus(self.new_proxy) # 启动后在【检测网络】页面显示网络代理情况
        self.addNetTextMain('\n\n点击 【开始检测】以测试网络连通性。')
        self.updateCheckStart() # 检查更新


    def Init_Ui(self):
        ico_path = self.resource_path('Img/AVDC-ico.png')
        pix = QPixmap(ico_path)
        self.Ui.label_ico.setScaledContents(True)
        self.Ui.label_ico.setPixmap(pix)  # 添加图标
        self.Ui.progressBar_avdc.setValue(0)  # 进度条清0 
        self.progressBarValue.connect(self.set_processbar)
        self.Ui.progressBar_avdc.setTextVisible(False)  # 不显示进度条文字
        self.Ui.pushButton_start_cap.setCheckable(True)
        self.main_logs_show.connect(self.Ui.textBrowser_log_main.append)
        self.net_logs_show.connect(self.Ui.textBrowser_net_main.append)
        self.set_javdb_cookie.connect(self.Ui.plainTextEdit_cookie_javdb.setPlainText)
        self.set_label_file_path.connect(self.Ui.label_file_path.setText)
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowOpacity(0.98)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.Ui.treeWidget_number.expandAll()

    def set_style(self):
        # 控件美化 左侧栏样式
        self.Ui.widget_setting.setStyleSheet(
            '''
            * {
                    font-family:Courier;
            }  
            QWidget#widget_setting{
                    background:rgba(20,100,160,255);
                    border-top-left-radius:5px;
                    border-bottom-left-radius:5px;
            }
            QPushButton{
                    font-size:15px;
                    color:white;
                    border-width:9px;
                    border-color:gray;
                    border-radius:18px;
                    padding:2px 4px;
            }
            QPushButton:hover{
                    color:white;
                    background-color:#4C6EFF;
                }
            QPushButton:pressed{
                    background-color:#4C6EE0;
            }
            QLabel#label_show_version{
                    font-size:11px;
                    color: rgba(255, 255, 255, 151);
                    border:0px solid rgba(0, 0, 0, 80);
            }
            ''')
        # 主界面
        self.Ui.page_avdc.setStyleSheet(
            '''
            QLabel#label_number1,#label_actor1,#label_title1,#label_poster1,#label_number,#label_actor,#label_title,#label_poster1{
                    font-size:16px;
                    font-weight:bold;
                    background-color: rgb(246, 246, 246);
                    border:0px solid rgba(0, 0, 0, 80);
            }
            QLabel#label_file_path{
                    font-size:16px;
                    color: black;
                    background-color: rgb(246, 246, 246);
                    font-weight:bold;
                    border:0px solid rgba(0, 0, 0, 80);
            }
            ''')
        # 工具页
        self.Ui.page_tool.setStyleSheet(
            '''
            * {
                    font-family:Courier;
                    font-size:13px;
            }
            QLabel{
                    font-size:13px;
                    border:0px solid rgba(0, 0, 0, 80);
            }
            QLineEdit{
                    font-size:13px;
                    border:0px solid rgba(0, 0, 0, 80);
                    border-radius: 15px;
            }
            QComboBox{
                    font-size:13px;
            }
            QGroupBox{
                    font-size:13px;
            }
            ''')
        # 使用帮助页
        self.Ui.page_about.setStyleSheet(
            '''
            * {
                    font-family:Courier;
                    font-size:13px;
            }
            QTextBrowser{
                    font-family:Courier;
                    font-size:13px;
                    border:0px solid #BEBEBE;
                    background-color:rgba(246,246,246,0);
                    padding:2px 4px;
            }
            ''')
        # 设置页
        self.Ui.page_setting.setStyleSheet(
            '''
            * {
                    font-family:Courier;
                    font-size:13px;
            }
            QScrollArea#scrollArea{
                    background-color: rgba(246, 246, 246, 255);
                    border-color: rgba(246, 246, 246, 255);
            }
            QTabWidget#tabWidget{
                    background-color: rgba(246, 246, 246, 255);
                    border-color: rgba(246, 246, 246, 255);
            }
            QWidget#tab1,#scrollAreaWidgetContents,#tab2,#scrollAreaWidgetContents_2,#tab3,#scrollAreaWidgetContents_3,#tab4,#scrollAreaWidgetContents_4,#tab5,#scrollAreaWidgetContents_5,#tab,#tab_2,#tab_3,#tab_4,#tab_5,#scrollAreaWidgetContents_6,#scrollAreaWidgetContents_7,#tab_9{
                    background-color: rgba(246, 246, 246, 255);
                    border-color: rgba(246, 246, 246, 255);
            }
            QLabel{
                    font-size:13px;
                    border:0px solid rgba(0, 0, 0, 80);
            }
            QLineEdit{
                    font-size:13px;
                    border:0px solid rgba(0, 0, 0, 80);
                    border-radius: 15px;
            }
            QRadioButton{
                    font-size:13px;
            }
            QComboBox{
                    font-size:13px;
            }
            QCheckBox{
                    font-size:13px;
            }
            QPlainTextEdit{
                    font-size:13px;
            }
            QGroupBox{
                    background-color: rgba(246, 246, 246, 255);
            }

            ''')
        # 整个页面
        self.Ui.centralwidget.setStyleSheet(
            '''
            * {
                    font-family:Courier;
                    font-size:13px;
            }
            QTreeWidget
            {
                    background-color: rgb(246, 246, 246);
                    font-size:12px;
                    border:0px solid rgb(120,120,120);
            }
            QWidget#centralwidget{
                    background:#F6F6F6;
                    border:1px solid #BEBEBE;
                    border-radius:5px;
           }            
            QTextBrowser{
                    font-size:13px;
                    border:0px solid #BEBEBE;
                    background-color:rgba(246,246,246,0);
                    padding:2px 4px;
            }
            QLineEdit{
                    font-size:13px;
                    background:white;
                    border-radius:10px;
                    padding:2px 4px;
            }
            QPushButton#pushButton_show_pic_actor,#pushButton_add_actor_pic,#pushButton_move_mp4,#pushButton_select_file,#pushButton_select_thumb,#pushButton_start_single_file,#pushButton_init_config,#pushButton_select_file_clear_info{
                    font-size:14px;
                    background-color:rgba(220, 220,220, 255);
                    border-color:black;
                    border-width:8px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton:hover#pushButton_show_pic_actor,:hover#pushButton_add_actor_pic{
                    font-size:14px;
                    background-color:rgba(200, 200,200, 255);
                    border-color:black;
                    border-width:8px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton:pressed#pushButton_show_pic_actor,:pressed#pushButton_add_actor_pic{
                    font-size:14px;
                    background-color:rgba(200, 200,200, 120);
                    border-color:black;
                    border-width:8px;
                    border-radius:20px;
                    padding:2px 4px;
            }

            QPushButton#pushButton_save_config{
                    color:white;
                    font-size:14px;
                    background-color:#5E95CC;
                    border-radius:25px;
                    padding:2px 4px;
            }
            QPushButton:hover#pushButton_save_config,:hover#pushButton_init_config{
                    color:white;
                    background-color:#4C6EFF;
                    font-weight:bold;
                }
            QPushButton:pressed#pushButton_save_config,:pressed#pushButton_init_config{
                    background-color:#4C6EE0;
                    border-color:black;
                    border-width:14px;
                    font-weight:bold;
            }
            QPushButton#pushButton_start_cap,#pushButton_start_cap2,#pushButton_check_net{
                    color:white;
                    font-size:14px;
                    background-color:#0066CC;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton:hover#pushButton_start_cap,:hover#pushButton_start_cap2,:hover#pushButton_check_net,:hover#pushButton_move_mp4,:hover#pushButton_select_file,:hover#pushButton_select_thumb,:hover#pushButton_start_single_file,:hover#pushButton_select_file_clear_info{
                    color:white;
                    background-color:#4C6EFF;
                    font-weight:bold;
                }
            QPushButton:pressed#pushButton_start_cap,:pressed#pushButton_start_cap2,:pressed#pushButton_check_net,:pressed#pushButton_move_mp4,:pressed#pushButton_select_file,:pressed#pushButton_select_thumb,:pressed#pushButton_start_single_file,:press#pushButton_select_file_clear_info{
                    background-color:#4C6EE0;
                    border-color:black;
                    border-width:12px;
                    font-weight:bold;
            }
            QProgressBar::chunk{
                    background-color: #0066CC;
                    width: 5px; /*区块宽度*/
                    margin: 0.5px;
            }
            ''')

    # ======================================================================================按钮点击事件
    def Init(self):
        # self.Ui.treeWidget_number.clicked.connect(self.treeWidget_number_clicked)
        self.Ui.treeWidget_number.selectionModel().selectionChanged.connect(self.treeWidget_number_clicked)
        self.Ui.pushButton_close.clicked.connect(self.close_win)
        self.Ui.pushButton_min.clicked.connect(self.min_win)
        self.Ui.pushButton_main.clicked.connect(self.pushButton_main_clicked)
        self.Ui.pushButton_tool.clicked.connect(self.pushButton_tool_clicked)
        self.Ui.pushButton_setting.clicked.connect(self.pushButton_setting_clicked)
        self.Ui.pushButton_select_file.clicked.connect(self.pushButton_select_file_clicked)
        self.Ui.pushButton_about.clicked.connect(self.pushButton_about_clicked)
        self.Ui.pushButton_start_cap.clicked.connect(self.pushButton_start_cap_clicked)
        self.Ui.pushButton_start_cap2.clicked.connect(self.pushButton_start_cap_clicked)
        self.Ui.pushButton_save_config.clicked.connect(self.pushButton_save_config_clicked)
        self.Ui.pushButton_init_config.clicked.connect(self.pushButton_init_config_clicked)
        self.Ui.pushButton_move_mp4.clicked.connect(self.move_file)
        self.Ui.pushButton_check_net.clicked.connect(self.netCheck)
        self.Ui.pushButton_add_actor_pic.clicked.connect(self.pushButton_add_actor_pic_clicked)
        self.Ui.pushButton_show_pic_actor.clicked.connect(self.pushButton_show_pic_actor_clicked)
        self.Ui.pushButton_select_thumb.clicked.connect(self.pushButton_select_thumb_clicked)
        self.Ui.pushButton_log.clicked.connect(self.pushButton_show_log_clicked)
        self.Ui.pushButton_net.clicked.connect(self.pushButton_show_net_clicked)
        self.Ui.pushButton_start_single_file.clicked.connect(self.pushButton_start_single_file_clicked)
        self.Ui.pushButton_select_file_clear_info.clicked.connect(self.pushButton_select_file_clear_info_clicked)
        self.Ui.checkBox_cover.stateChanged.connect(self.cover_change)
        self.Ui.horizontalSlider_timeout.valueChanged.connect(self.lcdNumber_timeout_change)
        self.Ui.horizontalSlider_retry.valueChanged.connect(self.lcdNumber_retry_change)
        self.Ui.horizontalSlider_mark_size.valueChanged.connect(self.lcdNumber_mark_size_change)
        self.Ui.label_thumb.mousePressEvent = self.test_clicked
        self.Ui.label_poster.mousePressEvent = self.test_clicked
        self.Ui.label_download_acotr_zip.mousePressEvent = self.download_actor_zip_clicked
        self.Ui.label_get_cookie_url.mousePressEvent = self.get_cookie_url_clicked


    #  打包前（虚拟机py运行）
    #  主路径1 os.getcwd()：C:\Users\username
    #  √主路径2 sys.path[0]：\\Mac\Home\Desktop\AVDCx
    #  主路径3 os.path.split(os.path.realpath(__file__))[0]：\\Mac\Home\Desktop\AVDCx
    #  主路径4 os.path.abspath(".")：C:\Users\username 

    #  打包后（exe运行）
    #  主路径1 os.getcwd()：\\Mac\Home\Desktop\AVDCx\dist 
    #  主路径2 sys.path[0]：C:\Users\username\AppData\Local\Temp\_MEI15962\base_library.zip 
    #  主路径3 os.path.split(os.path.realpath(__file__))[0]：C:\Users\username\AppData\Local\Temp\_MEI15962 
    #  √主路径4 os.path.abspath(".")：\\Mac\Home\Desktop\AVDCx\dist     

    def mainPath(self):
        try:
            main_path = os.path.split(os.path.realpath(__file__))[0]    # 取的是__file__所在文件xx.py的所在目录
        except:
            main_path = os.path.abspath(sys.path[0]) # 或sys.argv[0],取的是被初始执行的脚本的所在目录，打包后路径会变成\base_libarary.zip
        # base_path = os.path.abspath(".")    # 取的是起始执行目录，和os.getcwd()结果一样，不太准
        if getattr(sys, 'frozen', False): #是否Bundle Resource，是否打包成exe运行
            main_path = os.path.abspath(".")    # 打包后，路径是准的
        return main_path

    # ======================================================================================生成资源文件目录访问路径
    def resource_path(self, relative_path):
        base_path = self.main_path
        # base_path = os.path.split(os.path.realpath(__file__))[0]
        if os.path.exists(os.path.join(base_path, relative_path)):
            pass
        elif getattr(sys, 'frozen', False): #是否Bundle Resource
            base_path = sys._MEIPASS
        return os.path.join(base_path, relative_path).replace('\\', '/')

    # ======================================================================================c_number.json位置
    def c_numberPath(self):
        if getattr(sys, 'frozen', False): #是否Bundle Resource，是否打包成exe运行
            c_numberPath ='c_number/c_number.json'
        else:
            c_numberPath ='Data/c_number/c_number.json'
        return c_numberPath

    def infoPath(self):
        if getattr(sys, 'frozen', False): #是否Bundle Resource，是否打包成exe运行
            infoPath ='mapping_table/mapping_info.xml'
        else:
            infoPath ='Data/mapping_table/mapping_info.xml'
        return infoPath

    def actorPath(self):
        if getattr(sys, 'frozen', False): #是否Bundle Resource，是否打包成exe运行
            actorPath ='mapping_table/mapping_actor.xml'
        else:
            actorPath ='Data/mapping_table/mapping_actor.xml'
        return actorPath


    # ======================================================================================显示版本号
    def show_version(self):
        self.addTextMain('AVDCx ' + self.localversion)
        self.addTextMain('基于项目 https://github.com/moyy996/AVDC 修改')
        self.addTextMain('报告问题 %sissues\n' % self.github_project_url)
        self.addTextMain('================================================================================')

    def version_clicked(self, test):
        webbrowser.open('%sreleases' % self.github_project_url)

    def label_number_clicked(self, test):
        try:
            if self.laberl_number_url:
                webbrowser.open(self.laberl_number_url)
        except:
            pass

    def label_actor_clicked(self, test):
        try:
            if self.laberl_actor_url:
                webbrowser.open(self.laberl_actor_url)
        except:
            pass

    def test_clicked(self, test):
        newWin2.showimage(self.img_path, self.json_data)
        newWin2.show()

    def download_actor_zip_clicked(self, test):
        webbrowser.open('https://github.com/moyy996/AVDC/releases/tag/%E5%A4%B4%E5%83%8F%E5%8C%85-2')

    def get_cookie_url_clicked(self, test):
        webbrowser.open('https://tieba.baidu.com/p/5492736764')

    # ======================================================================================鼠标拖动窗口
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 按下左键改变鼠标指针样式为手掌

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))  # 释放左键改变鼠标指针样式为箭头

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_drag:
            self.move(e.globalPos() - self.m_DragPosition)
            e.accept()

    # ======================================================================================左侧按钮点击事件响应函数
    def close_win(self):
        show_poster = self.config.get('show_poster')

        if bool(self.Ui.checkBox_cover.isChecked()) != bool(show_poster):
            if self.Ui.checkBox_cover.isChecked():
                self.config['show_poster'] = 1
            else:
                self.config['show_poster'] = 0
            try:
                save_config(self.config)
            except:
                pass
        os._exit(0)


    # ======================================================================================最小化窗口
    def min_win(self):
        self.setWindowState(Qt.WindowMinimized)
        # self.showMinimized()
        # print(self.isMinimized())


    # ====================================================================================== 根据平台转换路径
    def convert_path(self, path):
        if platform.system() == 'Windows':
            path = path.replace('/', '\\')
        else:
            path = path.replace('\\', '/')
        return path

    def pushButton_main_clicked(self):          # 点左侧的主界面按钮
        self.Ui.stackedWidget.setCurrentIndex(0)
        self.Ui.pushButton_main.setEnabled(False)
        self.Ui.pushButton_log.setEnabled(True)
        self.Ui.pushButton_net.setEnabled(True)
        self.Ui.pushButton_tool.setEnabled(True)
        self.Ui.pushButton_setting.setEnabled(True)
        self.Ui.pushButton_about.setEnabled(True)

        self.Ui.pushButton_main.setStyleSheet('QPushButton#pushButton_main{color:white;background-color:#4C6EFF;border:3px white;}')
        self.Ui.pushButton_log.setStyleSheet('QPushButton#pushButton_log{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_log{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_log{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_net.setStyleSheet('QPushButton#pushButton_net{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_net{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_net{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_tool.setStyleSheet('QPushButton#pushButton_tool{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_tool{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_tool{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_setting.setStyleSheet('QPushButton#pushButton_setting{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_setting{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_setting{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_about.setStyleSheet('QPushButton#pushButton_about{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_about{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_about{color:white;background-color:#4C6EE0;}')

    def pushButton_show_log_clicked(self):          # 点左侧的日志按钮
        self.Ui.stackedWidget.setCurrentIndex(1)
        self.Ui.pushButton_main.setEnabled(True)
        self.Ui.pushButton_log.setEnabled(False)
        self.Ui.pushButton_net.setEnabled(True)
        self.Ui.pushButton_tool.setEnabled(True)
        self.Ui.pushButton_setting.setEnabled(True)
        self.Ui.pushButton_about.setEnabled(True)

        self.Ui.pushButton_log.setStyleSheet('QPushButton#pushButton_log{color:white;background-color:#4C6EFF;border:3px white;}')
        self.Ui.pushButton_main.setStyleSheet('QPushButton#pushButton_main{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_main{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_main{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_net.setStyleSheet('QPushButton#pushButton_net{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_net{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_net{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_tool.setStyleSheet('QPushButton#pushButton_tool{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_tool{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_tool{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_setting.setStyleSheet('QPushButton#pushButton_setting{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_setting{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_setting{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_about.setStyleSheet('QPushButton#pushButton_about{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_about{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_about{color:white;background-color:#4C6EE0;}')


    def pushButton_show_net_clicked(self):  # 点击左侧【检测网络】按钮，切换到检测网络页面
        self.Ui.stackedWidget.setCurrentIndex(2)
        self.Ui.pushButton_main.setEnabled(True)
        self.Ui.pushButton_log.setEnabled(True)
        self.Ui.pushButton_net.setEnabled(False)
        self.Ui.pushButton_tool.setEnabled(True)
        self.Ui.pushButton_setting.setEnabled(True)
        self.Ui.pushButton_about.setEnabled(True)

        self.Ui.pushButton_net.setStyleSheet('QPushButton#pushButton_net{color:white;background-color:#4C6EFF;border:3px white;}')
        self.Ui.pushButton_log.setStyleSheet('QPushButton#pushButton_log{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_log{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_log{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_main.setStyleSheet('QPushButton#pushButton_main{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_main{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_main{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_tool.setStyleSheet('QPushButton#pushButton_tool{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_tool{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_tool{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_setting.setStyleSheet('QPushButton#pushButton_setting{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_setting{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_setting{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_about.setStyleSheet('QPushButton#pushButton_about{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_about{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_about{color:white;background-color:#4C6EE0;}')


    def pushButton_tool_clicked(self):          # 点左侧的工具按钮
        self.Ui.stackedWidget.setCurrentIndex(3)
        self.Ui.pushButton_main.setEnabled(True)
        self.Ui.pushButton_log.setEnabled(True)
        self.Ui.pushButton_net.setEnabled(True)
        self.Ui.pushButton_tool.setEnabled(False)
        self.Ui.pushButton_setting.setEnabled(True)
        self.Ui.pushButton_about.setEnabled(True)

        self.Ui.pushButton_tool.setStyleSheet('QPushButton#pushButton_tool{color:white;background-color:#4C6EFF;border:3px white;}')
        self.Ui.pushButton_log.setStyleSheet('QPushButton#pushButton_log{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_log{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_log{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_net.setStyleSheet('QPushButton#pushButton_net{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_net{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_net{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_main.setStyleSheet('QPushButton#pushButton_main{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_main{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_main{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_setting.setStyleSheet('QPushButton#pushButton_setting{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_setting{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_setting{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_about.setStyleSheet('QPushButton#pushButton_about{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_about{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_about{color:white;background-color:#4C6EE0;}')

    def pushButton_setting_clicked(self):          # 点左侧的设置按钮
        self.Ui.stackedWidget.setCurrentIndex(4)
        self.Ui.pushButton_main.setEnabled(True)
        self.Ui.pushButton_log.setEnabled(True)
        self.Ui.pushButton_net.setEnabled(True)
        self.Ui.pushButton_tool.setEnabled(True)
        self.Ui.pushButton_setting.setEnabled(False)
        self.Ui.pushButton_about.setEnabled(True)

        self.Ui.pushButton_setting.setStyleSheet('QPushButton#pushButton_setting{color:white;background-color:#4C6EFF;border:3px white;}')
        self.Ui.pushButton_log.setStyleSheet('QPushButton#pushButton_log{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_log{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_log{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_net.setStyleSheet('QPushButton#pushButton_net{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_net{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_net{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_tool.setStyleSheet('QPushButton#pushButton_tool{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_tool{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_tool{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_main.setStyleSheet('QPushButton#pushButton_main{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_main{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_main{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_about.setStyleSheet('QPushButton#pushButton_about{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_about{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_about{color:white;background-color:#4C6EE0;}')

    def pushButton_about_clicked(self):          # 点左侧的关于按钮
        self.Ui.stackedWidget.setCurrentIndex(5)
        self.Ui.pushButton_main.setEnabled(True)
        self.Ui.pushButton_log.setEnabled(True)
        self.Ui.pushButton_net.setEnabled(True)
        self.Ui.pushButton_tool.setEnabled(True)
        self.Ui.pushButton_setting.setEnabled(True)
        self.Ui.pushButton_about.setEnabled(False)

        self.Ui.pushButton_about.setStyleSheet('QPushButton#pushButton_about{color:white;background-color:#4C6EFF;border:3px white;}')
        self.Ui.pushButton_log.setStyleSheet('QPushButton#pushButton_log{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_log{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_log{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_net.setStyleSheet('QPushButton#pushButton_net{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_net{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_net{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_tool.setStyleSheet('QPushButton#pushButton_tool{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_tool{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_tool{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_setting.setStyleSheet('QPushButton#pushButton_setting{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_setting{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_setting{color:white;background-color:#4C6EE0;}')
        self.Ui.pushButton_main.setStyleSheet('QPushButton#pushButton_main{color:rgba(255, 255, 255, 200)}QPushButton:hover#pushButton_main{color:white;background-color:rgba(255,255,255,40);}QPushButton:pressed#pushButton_about{color:white;background-color:#4C6EE0;}')


    def lcdNumber_timeout_change(self):
        timeout = self.Ui.horizontalSlider_timeout.value()
        self.Ui.lcdNumber_timeout.display(timeout)

    def lcdNumber_retry_change(self):
        retry = self.Ui.horizontalSlider_retry.value()
        self.Ui.lcdNumber_retry.display(retry)

    def lcdNumber_mark_size_change(self):
        mark_size = self.Ui.horizontalSlider_mark_size.value()
        self.Ui.lcdNumber_mark_size.display(mark_size)

    def cover_change(self):
        if not self.Ui.checkBox_cover.isChecked():
            self.Ui.label_poster.setText("封面图")
            self.Ui.label_thumb.setText("缩略图")

    def treeWidget_number_clicked(self, qmodeLindex):
        item = self.Ui.treeWidget_number.currentItem()
        if item.text(0) != '成功' and item.text(0) != '失败':
            try:
                index_json = str(item.text(0))
                self.add_label_info(self.json_array[str(index_json)])
            except:
                print(item.text(0) + ': No info!')

    def pushButton_start_cap_clicked(self):
        self.Ui.pushButton_start_cap.setEnabled(False)
        self.Ui.pushButton_start_cap2.setEnabled(False)
        self.Ui.pushButton_start_cap.setText('正在刮削')
        self.Ui.pushButton_start_cap2.setText('正在刮削')
        self.Ui.pushButton_start_cap.setStyleSheet('QPushButton#pushButton_start_cap{color:#999999;background-color:#F0F0F0;}')
        self.Ui.pushButton_start_cap2.setStyleSheet('QPushButton#pushButton_start_cap2{color:#999999;background-color:#F0F0F0;}')
        self.progressBarValue.emit(int(0))
        try:
            t = threading.Thread(target=self.AVDC_Main, args=('default_folder',))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('Error in pushButton_start_cap_clicked: ' + str(ex))

    # ======================================================================================恢复默认config.ini
    def pushButton_init_config_clicked(self):
        self.Ui.pushButton_init_config.setEnabled(False)
        try:
            t = threading.Thread(target=self.init_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('Error in pushButton_init_config_clicked: ' + str(ex))

    def init_config_clicked(self):
        json_config = {
            'show_poster': 1,
            'no_nfo_scrape': 'off',
            'main_mode': 1,
            'main_like': 1,
            'more_website': 'javdb,jav321,javlibrary',
            'soft_link': 0,
            'switch_debug': 1,
            'success_file_move': 1,
            'failed_file_move': 1,
            'success_file_rename': 1,
            'del_empty_folder': 1,
            'series_as_set': 1,
            'update_check': 1,
            'translate_language': 'zh_cn',
            'translate_content': 'title,outline',
            'translate_by': 'youdao',
            'deepl_key': '',
            'actor_output': 'zh_cn',
            'info_output': 'zh_cn',
            'save_log': 1,
            'website': 'all',
            'failed_output_folder': 'failed',
            'success_output_folder': 'JAV_output',
            'extrafanart_folder': '',
            'type': 'no',
            'proxy': '127.0.0.1:7890',
            'timeout': 10,
            'retry': 3,
            'javdb': '',
            'folder_name': 'actor/number actor',
            'naming_media': 'number title',
            'naming_file': 'number',
            'folder_name_max': 70,
            'file_name_max': 70,
            'actor_name_max': 3,
            'actor_name_more': '等演员',
            'actor_no_name': '未知演员',
            'cnword_char': '-C.,中文,字幕',
            'cnword_style': '-C',
            'del_actor_name': 1,
            'pic_name': 1,
            'cd_name': 0,
            'folders': 'JAV_output,examples',
            'string': '1080p,720p,22-sht.me,-HD,bbs2048.org@,hhd800.com@,icao.me@,hhb_000',
            'file_size': '100.0',
            'emby_url': 'http://192.168.5.191:8096',
            'api_key': 'cb83900340b447fab785cb628a99c3da',
            'actor_photo_folder': '',
            'actor_photo_upload': 'on',
            'media_path': '',
            'media_type': '.mp4|.avi|.rmvb|.wmv|.mov|.mkv|.flv|.ts|.webm|.iso|.mpg',
            'sub_type': '.smi|.srt|.idx|.sub|.sup|.psb|.ssa|.ass|.txt|.usf|.xss|.ssf|.rt|.lrc|.sbv|.vtt|.ttml',
            'poster_mark': 1,
            'thumb_mark': 1,
            'mark_size': 5,
            'mark_type': 'SUB,LEAK,UNCENSORED',
            'mark_pos': 'top_left',
            'uncensored_prefix': 'BT|CT|EMP|CCDV|CWP|CWPBD|DSAM|DRC|DRG|GACHI|heydouga|JAV|LAF|LAFBD|HEYZO|KTG|KP|KG|LLDV|MCDV|MKD|MKBD|MMDV|NIP|PB|PT|QE|RED|RHJ|S2M|SKY|SKYHD|SMD|SSDV|SSKP|TRG|TS|xxx-av|YKB|heydouga|1pon|Carib',
            'download_nfo': 'on',
            'download_poster': 'on',
            'download_thumb': 'on',
            'download_fanart': 'on',
            'download_extrafanart': 'off',
            'download_extrafanart_copy': 'off',
            'keep_local_nfo': 'off',
            'keep_local_poster': 'off',
            'keep_local_fanart': 'off',
            'keep_local_thumb': 'off',
            'keep_local_extrafanart': 'off',
            'keep_local_extrafanart_copy': 'off',
            'poster_from': 'auto',
            'folder_cnword': 1,
            'file_cnword': 1,
        }
        save_config(json_config)
        self.check_proxyChange()
        self.Load_config()
        self.Ui.pushButton_init_config.setEnabled(True)

    # ======================================================================================加载config
    def Load_config(self):
        config_file = 'config.ini'
        if os.path.exists(config_file):
            config = RawConfigParser()
            # ======================================================================================当配置读取失败时重置
            try:
                config.read(config_file, encoding='UTF-8')
            except Exception as error_info:
                # ini损坏，重新创建
                print('ini损坏，重新创建。错误信息：\n %s' % error_info)
                self.addTextMain('config.ini 读取失败！错误信息：\n%s \nconfig.ini 将重置为初始值！\n' % error_info)
                self.init_config_clicked()
                return
            # ======================================================================================modified_time
            if not config.has_section("modified_time"):
                config.add_section("modified_time")
            try:    # 修改时间
                config.get('modified_time', 'modified_time')
            except:
                config['modified_time']['modified_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # ======================================================================================common
            if not config.has_section("common"):
                config.add_section("common")
            try:    # 刮削模式
                if int(config['common']['main_mode']) == 1:
                    self.Ui.radioButton_common.setChecked(True)
                elif int(config['common']['main_mode']) == 2:
                    self.Ui.radioButton_sort.setChecked(True)
                else:
                    self.Ui.radioButton_read.setChecked(True)
            except:
                self.Ui.radioButton_common.setChecked(True)
            try:    # 无nfo是否正常刮削
                if config['common']['no_nfo_scrape'] == 'off':
                    self.Ui.checkBox_read_no_nfo_scrape.setChecked(False)
                else:
                    self.Ui.checkBox_read_no_nfo_scrape.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if config['common']['no_nfo'] == '0':
                        self.Ui.checkBox_read_no_nfo_scrape.setChecked(False)
                    else:
                        self.Ui.checkBox_read_no_nfo_scrape.setChecked(True)
                except:
                    self.Ui.checkBox_read_no_nfo_scrape.setChecked(False)

            try:    # 刮削偏好
                if int(config['common']['main_like']) == 0:
                    self.Ui.radioButton_like_speed.setChecked(True)
                else:
                    self.Ui.radioButton_like_more.setChecked(True)
            except:
                self.Ui.radioButton_like_more.setChecked(True)
            try:    # 补全网站
                if 'javdb' in str(config['common']['more_website']):
                    self.Ui.checkBox_more_javdb.setChecked(True)
                else:
                    self.Ui.checkBox_more_javdb.setChecked(False)
                if 'jav321' in str(config['common']['more_website']):
                    self.Ui.checkBox_more_jav321.setChecked(True)
                else:
                    self.Ui.checkBox_more_jav321.setChecked(False)
                if 'javlibrary' in str(config['common']['more_website']):
                    self.Ui.checkBox_more_javlibrary.setChecked(True)
                else:
                    self.Ui.checkBox_more_javlibrary.setChecked(False)
                if 'dmm' in str(config['common']['more_website']):
                    self.Ui.checkBox_more_dmm.setChecked(True)
                else:
                    self.Ui.checkBox_more_dmm.setChecked(False)
            except:
                self.Ui.checkBox_more_javdb.setChecked(True)
                self.Ui.checkBox_more_jav321.setChecked(True)
                self.Ui.checkBox_more_javlibrary.setChecked(True)
                self.Ui.checkBox_more_dmm.setChecked(False)
            try:    # 软链接
                if int(config['common']['soft_link']) == 1:
                    self.Ui.radioButton_soft_on.setChecked(True)
                else:
                    self.Ui.radioButton_soft_off.setChecked(True)
            except:
                self.Ui.radioButton_soft_off.setChecked(True)

            try:    # 成功后移动文件
                if int(config['common']['success_file_move']) == 0:
                    self.Ui.radioButton_succ_move_off.setChecked(True)
                else:
                    self.Ui.radioButton_succ_move_on.setChecked(True)
            except:
                self.Ui.radioButton_succ_move_on.setChecked(True)

            try:    # 失败后移动文件
                if int(config['common']['failed_file_move']) == 0:
                    self.Ui.radioButton_fail_move_off.setChecked(True)
                else:
                    self.Ui.radioButton_fail_move_on.setChecked(True)
            except:
                self.Ui.radioButton_fail_move_on.setChecked(True)
            try:    # 成功后重命名文件
                if int(config['common']['success_file_rename']) == 0:
                    self.Ui.radioButton_succ_rename_off.setChecked(True)
                else:
                    self.Ui.radioButton_succ_rename_on.setChecked(True)
            except:
                self.Ui.radioButton_succ_rename_on.setChecked(True)
            try:    # 结束后删除空文件夹
                if int(config['common']['del_empty_folder']) == 0:
                    self.Ui.radioButton_del_empty_folder_off.setChecked(True)
                else:
                    self.Ui.radioButton_del_empty_folder_on.setChecked(True)
            except:
                self.Ui.radioButton_del_empty_folder_on.setChecked(True)
            try:    # 使用系列作为合集
                if int(config['common']['series_as_set']) == 0:
                    self.Ui.radioButton_series_as_set_off.setChecked(True)
                else:
                    self.Ui.radioButton_series_as_set_on.setChecked(True)
            except:
                self.Ui.radioButton_series_as_set_on.setChecked(True)

            try:    # 显示封面
                if int(config['common']['show_poster']) == 0:
                    self.Ui.checkBox_cover.setChecked(False)
                else:
                    self.Ui.checkBox_cover.setChecked(True)
            except:
                self.Ui.checkBox_cover.setChecked(True)
            
            try:    # 刮削网站
                if config['common']['website'] == 'all':
                    self.Ui.comboBox_website_all.setCurrentIndex(0)
                elif config['common']['website'] == 'iqqtv':
                    self.Ui.comboBox_website_all.setCurrentIndex(1)
                elif config['common']['website'] == 'javbus':
                    self.Ui.comboBox_website_all.setCurrentIndex(2)
                elif config['common']['website'] == 'javdb':
                    self.Ui.comboBox_website_all.setCurrentIndex(3)
                elif config['common']['website'] == 'jav321':
                    self.Ui.comboBox_website_all.setCurrentIndex(4)
                elif config['common']['website'] == 'dmm':
                    self.Ui.comboBox_website_all.setCurrentIndex(5)
                elif config['common']['website'] == 'avsox':
                    self.Ui.comboBox_website_all.setCurrentIndex(6)
                elif config['common']['website'] == 'xcity':
                    self.Ui.comboBox_website_all.setCurrentIndex(7)
                elif config['common']['website'] == 'mgstage':
                    self.Ui.comboBox_website_all.setCurrentIndex(8)
                elif config['common']['website'] == 'fc2':
                    self.Ui.comboBox_website_all.setCurrentIndex(9)
                elif config['common']['website'] == 'fc2club':
                    self.Ui.comboBox_website_all.setCurrentIndex(10)
                elif config['common']['website'] == 'fc2hub':
                    self.Ui.comboBox_website_all.setCurrentIndex(11)
                elif config['common']['website'] == 'airav':
                    self.Ui.comboBox_website_all.setCurrentIndex(12)
                elif config['common']['website'] == 'javlibrary':
                    self.Ui.comboBox_website_all.setCurrentIndex(13)
                else:
                    self.Ui.comboBox_website_all.setCurrentIndex(0)
            except:
                self.Ui.comboBox_website_all.setCurrentIndex(0)

            # ======================================================================================映射表输出
            try:    # 演员映射表输出
                if config['common']['actor_output'] == 'zh_cn':
                    self.Ui.radioButton_actor_zh_cn.setChecked(True)
                elif config['common']['actor_output'] == 'zh_tw':
                    self.Ui.radioButton_actor_zh_tw.setChecked(True)
                elif config['common']['actor_output'] == 'ja':
                    self.Ui.radioButton_actor_jp.setChecked(True)
                elif config['common']['actor_output'] == 'no':
                    self.Ui.radioButton_actor_no.setChecked(True)
                else:
                    self.Ui.radioButton_actor_zh_cn.setChecked(True)
            except:
                self.Ui.radioButton_actor_zh_cn.setChecked(True)
            try:    # 标签映射表输出
                if config['common']['info_output'] == 'zh_cn':
                    self.Ui.radioButton_tag_zh_cn.setChecked(True)
                elif config['common']['info_output'] == 'zh_tw':
                    self.Ui.radioButton_tag_zh_tw.setChecked(True)
                elif config['common']['info_output'] == 'ja':
                    self.Ui.radioButton_tag_jp.setChecked(True)
                elif config['common']['info_output'] == 'no':
                    self.Ui.radioButton_tag_no.setChecked(True)
                else:
                    self.Ui.radioButton_tag_zh_cn.setChecked(True)
            except:
                self.Ui.radioButton_tag_zh_cn.setChecked(True)

            # ======================================================================================translate_language
            try:    # 翻译语言
                if config['common']['translate_language'] == 'zh_cn':
                    self.Ui.radioButton_zh_cn.setChecked(True)
                elif config['common']['translate_language'] == 'zh_tw':
                    self.Ui.radioButton_zh_tw.setChecked(True)
                elif config['common']['translate_language'] == 'ja':
                    self.Ui.radioButton_ja.setChecked(True)
                else:
                    self.Ui.radioButton_zh_cn.setChecked(True)
            except:
                self.Ui.radioButton_zh_cn.setChecked(True)
            # ======================================================================================translate_content
            try:    # 翻译内容
                if 'title' in str(config['common']['translate_content']).lower():
                    self.Ui.checkBox_translate_title.setChecked(True)
                else:
                    self.Ui.checkBox_translate_title.setChecked(False)   
                if 'outline' in str(config['common']['translate_content']).lower():
                    self.Ui.checkBox_translate_outline.setChecked(True)
                else:
                    self.Ui.checkBox_translate_outline.setChecked(False)
            except:
                self.Ui.checkBox_translate_title.setChecked(True)
                self.Ui.checkBox_translate_outline.setChecked(True)
            # ======================================================================================translate_by
            try:    # 翻译引擎
                if config['common']['translate_by'] == 'youdao':
                    self.Ui.radioButton_youdao.setChecked(True)
                elif config['common']['translate_by'] == 'deepl':
                    self.Ui.radioButton_deepl.setChecked(True)
                else:
                    self.Ui.radioButton_youdao.setChecked(True)
            except:
                self.Ui.radioButton_youdao.setChecked(True)
            try:    # deepl_key
                self.Ui.lineEdit_deepl_key.setText(str(config['common']['deepl_key']))
            except:
                self.Ui.lineEdit_deepl_key.setText('')

            # ======================================================================================proxy
            if not config.has_section("proxy"):
                config.add_section("proxy")
            try:    # 代理类型
                if config['proxy']['type'] == 'no' or config['proxy']['type'] == '':
                    self.Ui.radioButton_proxy_nouse.setChecked(True)
                elif config['proxy']['type'] == 'http':
                    self.Ui.radioButton_proxy_http.setChecked(True)
                elif config['proxy']['type'] == 'socks5':
                    self.Ui.radioButton_proxy_socks5.setChecked(True)
                else:
                    self.Ui.radioButton_proxy_nouse.setChecked(True)
            except:
                self.Ui.radioButton_proxy_nouse.setChecked(True)
            
            try:    # 代理地址
                self.Ui.lineEdit_proxy.setText(str(config['proxy']['proxy']))
            except:
                self.Ui.lineEdit_proxy.setText('127.0.0.1:7890')
            
            try:    # 超时时间
                self.Ui.horizontalSlider_timeout.setValue(int(config['proxy']['timeout']))
            except:
                self.Ui.horizontalSlider_timeout.setValue(10)

            try:    # 重试次数
                self.Ui.horizontalSlider_retry.setValue(int(config['proxy']['retry']))
            except:
                self.Ui.horizontalSlider_retry.setValue(3)

            # ======================================================================================Cookies
            if not config.has_section("Cookies"):
                config.add_section("Cookies")
            try:    # javdb cookie
                self.set_javdb_cookie.emit(config['Cookies']['javdb'])
            except:
                self.set_javdb_cookie.emit('')
            # ======================================================================================Name_Rule
            if not config.has_section("Name_Rule"):
                config.add_section("Name_Rule")
            try:    # 视频目录命名
                self.Ui.lineEdit_dir_name.setText(str(config['Name_Rule']['folder_name']))
            except:
                self.Ui.lineEdit_dir_name.setText('actor/number actor')
            try:    # 视频文件名命名（本地文件）
                self.Ui.lineEdit_local_name.setText(str(config['Name_Rule']['naming_file']))
            except:
                self.Ui.lineEdit_local_name.setText('number')
            try:    # emby视频标题（nfo文件）
                self.Ui.lineEdit_media_name.setText(str(config['Name_Rule']['naming_media']))
            except:
                self.Ui.lineEdit_media_name.setText('number title')

            try:    # 长度命名规则-目录
                folder_name_max = config.getint('Name_Rule', 'folder_name_max')
                if folder_name_max <= 0 or folder_name_max > 255:
                    folder_name_max = 70
                self.Ui.lineEdit_folder_name_max.setText(str(folder_name_max))
            except Exception as e:
                self.Ui.lineEdit_folder_name_max.setText('70')
            try:    # 长度命名规则-文件名
                file_name_max = config.getint('Name_Rule', 'file_name_max')
                if file_name_max <= 0 or file_name_max > 255:
                    file_name_max = 70
                self.Ui.lineEdit_file_name_max.setText(str(file_name_max))
            except:
                self.Ui.lineEdit_file_name_max.setText('70')
            try:    # 长度命名规则-演员名
                self.Ui.lineEdit_actor_name_max.setText(str(config.getint('Name_Rule', 'actor_name_max')))
            except:
                self.Ui.lineEdit_actor_name_max.setText('3')
            try:    # 长度命名规则-演员名更多
                self.Ui.lineEdit_actor_name_more.setText(str(config['Name_Rule']['actor_name_more']))
            except:
                self.Ui.lineEdit_actor_name_more.setText('等演员')
            try:    # 字段命名规则-未知演员
                self.Ui.lineEdit_actor_no_name.setText(str(config['Name_Rule']['actor_no_name']))
            except:
                self.Ui.lineEdit_actor_no_name.setText('未知演员')
            try:    # 图片命名规则
                if int(config['Name_Rule']['pic_name']) == 0:
                    self.Ui.radioButton_pic_file_poster.setChecked(True)
                else:
                    self.Ui.radioButton_pic_poster.setChecked(True)
            except:
                self.Ui.radioButton_pic_file_poster.setChecked(True)
            try:    # 分集命名规则
                if int(config['Name_Rule']['cd_name']) == 0:
                    self.Ui.radioButton_cd_part_lower.setChecked(True)
                else:
                    self.Ui.radioButton_cd_part_upper.setChecked(True)
            except:
                self.Ui.radioButton_cd_part_lower.setChecked(True)
            try:    # 去除标题演员名
                if int(config['Name_Rule']['del_actor_name']) == 0:
                    self.Ui.radioButton_del_actor_off.setChecked(True)
                else:
                    self.Ui.radioButton_del_actor_on.setChecked(True)
            except:
                self.Ui.radioButton_del_actor_on.setChecked(True)

            # ======================================================================================update
            if not config.has_section("update"):
                config.add_section("update")
            try:    # 检查更新
                if int(config['update']['update_check']) == 0:
                    self.Ui.radioButton_update_off.setChecked(True)
                else:
                    self.Ui.radioButton_update_on.setChecked(True)
            except:
                self.Ui.radioButton_update_on.setChecked(True)
            # ======================================================================================log
            if not config.has_section("log"):
                config.add_section("log")            
            try:    # 保存日志
                if int(config['log']['save_log']) == 0:
                    self.Ui.radioButton_log_off.setChecked(True)
                else:
                    self.Ui.radioButton_log_on.setChecked(True)
            except:
                self.Ui.radioButton_log_on.setChecked(True)
            # ======================================================================================media
            if not config.has_section("media"):
                config.add_section("media")
            try:    # 视频目录
                self.Ui.lineEdit_movie_path.setText(str(config['media']['media_path']))
            except:
                config['media']['media_path'] = ''
                self.Ui.lineEdit_movie_path.setText('')
            try:    # 成功目录
                self.Ui.lineEdit_success.setText(str(config['media']['success_output_folder']))
            except:
                self.Ui.lineEdit_success.setText('JAV_output')
            try:    # 失败目录
                self.Ui.lineEdit_fail.setText(str(config['media']['failed_output_folder']))
            except:
                self.Ui.lineEdit_fail.setText('failed')
            try:    # 剧照目录
                self.Ui.lineEdit_extrafanart_dir.setText(str(config['media']['extrafanart_folder']))
            except:
                try:    # 剧照目录
                    self.Ui.lineEdit_extrafanart_dir.setText(str(config['extrafanart']['extrafanart_folder']))
                except:
                    self.Ui.lineEdit_extrafanart_dir.setText('')
            try:    # 视频类型
                self.Ui.lineEdit_movie_type_2.setText(str(config['media']['media_type']))
            except:
                self.Ui.lineEdit_movie_type_2.setText('.mp4|.avi|.rmvb|.wmv|.mov|.mkv|.flv|.ts|.webm|.iso|.mpg')
            try:    # 字幕类型
                self.Ui.lineEdit_sub_type_2.setText(str(config['media']['sub_type']))
            except:
                self.Ui.lineEdit_sub_type_2.setText('.smi|.srt|.idx|.sub|.sup|.psb|.ssa|.ass|.txt|.usf|.xss|.ssf|.rt|.lrc|.sbv|.vtt|.ttml')
            # ======================================================================================字幕
            try:    # 中文字幕判断字符
                self.Ui.lineEdit_cnword_char.setText(str(config['Name_Rule']['cnword_char']))
            except:
                self.Ui.lineEdit_cnword_char.setText('-C.,中文,字幕')
            try:    # 中文字幕字符样式
                self.Ui.lineEdit_cnword_style.setText(str(config['Name_Rule']['cnword_style']))
            except:
                self.Ui.lineEdit_cnword_style.setText('-C')
            try:    # 要显示中文字幕的内容
                if int(config['Name_Rule']['folder_cnword']) == 0:
                    self.Ui.checkBox_foldername.setChecked(False)
                else:
                    self.Ui.checkBox_foldername.setChecked(True)
            except:
                self.Ui.checkBox_foldername.setChecked(True)
            try:    # 要显示中文字幕的内容
                if int(config['Name_Rule']['file_cnword']) == 0:
                    self.Ui.checkBox_filename.setChecked(False)
                else:
                    self.Ui.checkBox_filename.setChecked(True)
            except:
                self.Ui.checkBox_filename.setChecked(True)
            # ======================================================================================escape
            if not config.has_section("escape"):
                config.add_section("escape")
            try:    # 排除目录
                self.Ui.lineEdit_escape_dir.setText(str(config['escape']['folders']))
            except:
                self.Ui.lineEdit_escape_dir.setText('JAV_output')
            try:    # 排除目录-工具页面
                self.Ui.lineEdit_escape_dir_move.setText(str(config['escape']['folders']))
            except:
                self.Ui.lineEdit_escape_dir_move.setText('JAV_output')
            try:    # 多余字符串
                self.Ui.lineEdit_escape_string_2.setText(str(config['escape']['string']))
            except:
                self.Ui.lineEdit_escape_string_2.setText('1080p,720p,22-sht.me,-HD,bbs2048.org@,hhd800.com@,icao.me@,hhb_000')
            try:    # 小文件
                self.Ui.lineEdit_escape_size.setText(str(float(config['escape']['file_size'])))
            except:
                self.Ui.lineEdit_escape_size.setText('100.0')

            # ======================================================================================debug_mode
            if not config.has_section("debug_mode"):
                config.add_section("debug_mode")
            try:    # 调试模式
                if int(config['debug_mode']['switch']) == 0:
                    self.Ui.radioButton_debug_off.setChecked(True)
                else:
                    self.Ui.radioButton_debug_on.setChecked(True)
            except:
                self.Ui.radioButton_debug_on.setChecked(True)
            # ======================================================================================emby
            if not config.has_section("emby"):
                config.add_section("emby")
            try:    # emby地址
                self.Ui.lineEdit_emby_url.setText(str(config['emby']['emby_url']))
            except:
                self.Ui.lineEdit_emby_url.setText('192.168.5.191:8096')
            try:    # emby密钥
                self.Ui.lineEdit_api_key.setText(str(config['emby']['api_key']))
            except:
                self.Ui.lineEdit_api_key.setText('cb83900340b447fab785cb628a99c3da')
            try:    # 头像目录
                self.Ui.lineEdit_actor_photo_folder.setText(str(config['emby']['actor_photo_folder']))
            except:
                self.Ui.lineEdit_actor_photo_folder.setText('')
            try:    # 自动上传头像
                if str(config['emby']['actor_photo_upload']) == 'on':
                    self.Ui.radioButton_actor_photo_upload_on.setChecked(True)
                else:
                    self.Ui.radioButton_actor_photo_upload_off.setChecked(True)
            except:
                self.Ui.radioButton_actor_photo_upload_on.setChecked(True)

            # ======================================================================================mark
            if not config.has_section("mark"):
                config.add_section("mark")
            try:    # 封面图加水印
                if int(config['mark']['poster_mark']) == 0:
                    self.Ui.checkBox_poster_mark.setChecked(False)
                else:
                    self.Ui.checkBox_poster_mark.setChecked(True)
            except:
                self.Ui.checkBox_poster_mark.setChecked(True)
            try:    # 缩略图加水印
                if int(config['mark']['thumb_mark']) == 0:
                    self.Ui.checkBox_thumb_mark.setChecked(False)
                else:
                    self.Ui.checkBox_thumb_mark.setChecked(True)
            except:
                self.Ui.checkBox_thumb_mark.setChecked(True)
            try:    # 水印大小
                self.Ui.horizontalSlider_mark_size.setValue(int(config['mark']['mark_size']))
            except:
                self.Ui.horizontalSlider_mark_size.setValue(5)
            try:    # 水印类型
                if 'SUB' in str(config['mark']['mark_type']).upper():
                    self.Ui.checkBox_sub.setChecked(True)
                else:
                    self.Ui.checkBox_sub.setChecked(False)
                if 'LEAK' in str(config['mark']['mark_type']).upper():
                    self.Ui.checkBox_leak.setChecked(True)
                else:
                    self.Ui.checkBox_leak.setChecked(False)
                if 'UNCENSORED' in str(config['mark']['mark_type']).upper():
                    self.Ui.checkBox_uncensored.setChecked(True)
                else:
                    self.Ui.checkBox_uncensored.setChecked(False)
            except:
                self.Ui.checkBox_sub.setChecked(True)
                self.Ui.checkBox_leak.setChecked(True)
                self.Ui.checkBox_uncensored.setChecked(True)
            try:    # 水印位置
                if 'top_left' == config['mark']['mark_pos']:
                    self.Ui.radioButton_top_left.setChecked(True)
                elif 'bottom_left' == config['mark']['mark_pos']:
                    self.Ui.radioButton_bottom_left.setChecked(True)
                elif 'top_right' == config['mark']['mark_pos']:
                    self.Ui.radioButton_top_right.setChecked(True)
                elif 'bottom_right' == config['mark']['mark_pos']:
                    self.Ui.radioButton_bottom_right.setChecked(True)
                else:
                    self.Ui.radioButton_top_left.setChecked(True)
            except:
                self.Ui.radioButton_top_left.setChecked(True)

            # ======================================================================================file_download
            if not config.has_section("file_download"):
                config.add_section("file_download")
            try:    # 下载nfo
                if config['file_download']['download_nfo'] == 'on':
                    self.Ui.checkBox_download_nfo.setChecked(True)
                else:
                    self.Ui.checkBox_download_nfo.setChecked(False)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['nfo']) == '1':
                        self.Ui.checkBox_download_nfo.setChecked(True)
                    else:
                        self.Ui.checkBox_download_nfo.setChecked(False)
                except:
                    self.Ui.checkBox_download_nfo.setChecked(True)
            try:    # 下载poster
                if config['file_download']['download_poster'] == 'on':
                    self.Ui.checkBox_download_poster.setChecked(True)
                else:
                    self.Ui.checkBox_download_poster.setChecked(False)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['poster']) == '1':
                        self.Ui.checkBox_download_poster.setChecked(True)
                    else:
                        self.Ui.checkBox_download_poster.setChecked(False)
                except:
                    self.Ui.checkBox_download_poster.setChecked(True)
            try:    # 下载thumb
                if config['file_download']['download_thumb'] == 'on':
                    self.Ui.checkBox_download_thumb.setChecked(True)
                else:
                    self.Ui.checkBox_download_thumb.setChecked(False)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['thumb']) == '1':
                        self.Ui.checkBox_download_thumb.setChecked(True)
                    else:
                        self.Ui.checkBox_download_thumb.setChecked(False)
                except:
                    self.Ui.checkBox_download_thumb.setChecked(True)
            try:    # 下载fanart
                if config['file_download']['download_fanart'] == 'on':
                    self.Ui.checkBox_download_fanart.setChecked(True)
                else:
                    self.Ui.checkBox_download_fanart.setChecked(False)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['fanart']) == '1':
                        self.Ui.checkBox_download_fanart.setChecked(True)
                    else:
                        self.Ui.checkBox_download_fanart.setChecked(False)
                except:
                    self.Ui.checkBox_download_fanart.setChecked(True)
            try:    # 下载extrafanart
                if config['file_download']['download_extrafanart'] == 'off':
                    self.Ui.checkBox_download_extrafanart.setChecked(False)
                else:
                    self.Ui.checkBox_download_extrafanart.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['extrafanart']) == '0':
                        self.Ui.checkBox_download_extrafanart.setChecked(False)
                    else:
                        self.Ui.checkBox_download_extrafanart.setChecked(True)
                except:
                    try:    # 兼容老版本
                        if str(config['extrafanart']['download_extrafanart']) == '0':
                            self.Ui.checkBox_download_extrafanart.setChecked(False)
                        else:
                            self.Ui.checkBox_download_extrafanart.setChecked(True)
                    except:
                        self.Ui.checkBox_download_extrafanart.setChecked(False)
            try:    # 下载extrafanart副本
                if config['file_download']['download_extrafanart_copy'] == 'off':
                    self.Ui.checkBox_download_extrafanart_copy.setChecked(False)
                else:
                    self.Ui.checkBox_download_extrafanart_copy.setChecked(True)
            except:
                try:
                    if str(config['file_download']['extrafanart_copy']) == '0':
                        self.Ui.checkBox_download_extrafanart_copy.setChecked(False)
                    else:
                        self.Ui.checkBox_download_extrafanart_copy.setChecked(True)
                except:
                    self.Ui.checkBox_download_extrafanart_copy.setChecked(False)

            try:    # 保留旧nfo
                if config['file_download']['keep_local_nfo'] == 'off':
                    self.Ui.checkBox_old_nfo.setChecked(False)
                else:
                    self.Ui.checkBox_old_nfo.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['old_nfo']) == '0':
                        self.Ui.checkBox_old_nfo.setChecked(False)
                    else:
                        self.Ui.checkBox_old_nfo.setChecked(True)
                except:
                    self.Ui.checkBox_old_nfo.setChecked(False)
            try:    # 保留旧poster
                if config['file_download']['keep_local_poster'] == 'off':
                    self.Ui.checkBox_old_poster.setChecked(False)
                else:
                    self.Ui.checkBox_old_poster.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['old_poster']) == '0':
                        self.Ui.checkBox_old_poster.setChecked(False)
                    else:
                        self.Ui.checkBox_old_poster.setChecked(True)                
                except:
                    self.Ui.checkBox_old_poster.setChecked(False)
            try:    # 保留旧thumb
                if config['file_download']['keep_local_thumb'] == 'off':
                    self.Ui.checkBox_old_thumb.setChecked(False)
                else:
                    self.Ui.checkBox_old_thumb.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['old_thumb']) == '0':
                        self.Ui.checkBox_old_thumb.setChecked(False)
                    else:
                        self.Ui.checkBox_old_thumb.setChecked(True)
                except:
                    self.Ui.checkBox_old_thumb.setChecked(False)

            try:    # 保留旧fanart
                if config['file_download']['keep_local_fanart'] == 'off':
                    self.Ui.checkBox_old_fanart.setChecked(False)
                else:
                    self.Ui.checkBox_old_fanart.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['old_fanart']) == '0':
                        self.Ui.checkBox_old_fanart.setChecked(False)
                    else:
                        self.Ui.checkBox_old_fanart.setChecked(True)
                except:                
                    self.Ui.checkBox_old_fanart.setChecked(False)
            try:    # 保留旧extrafanart
                if config['file_download']['keep_local_extrafanart'] == 'off':
                    self.Ui.checkBox_old_extrafanart.setChecked(False)
                else:
                    self.Ui.checkBox_old_extrafanart.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['old_extrafanart']) == '0':
                        self.Ui.checkBox_old_extrafanart.setChecked(False)
                    else:
                        self.Ui.checkBox_old_extrafanart.setChecked(True)
                except:
                    self.Ui.checkBox_old_extrafanart.setChecked(False)

            try:    # 保留旧extrafanart副本
                if config['file_download']['keep_local_extrafanart_copy'] == 'off':
                    self.Ui.checkBox_old_extrafanart_copy.setChecked(False)
                else:
                    self.Ui.checkBox_old_extrafanart_copy.setChecked(True)
            except:
                try:    # 兼容老版本0927
                    if str(config['file_download']['old_extrafanart_copy']) == '0':
                        self.Ui.checkBox_old_extrafanart_copy.setChecked(False)
                    else:
                        self.Ui.checkBox_old_extrafanart_copy.setChecked(True)
                except:
                    self.Ui.checkBox_old_extrafanart_copy.setChecked(False)

            try:    # poster图片来源:auto/download
                if config['file_download']['poster_from'] == 'download':
                    self.Ui.radioButton_poster_official.setChecked(True)
                else:
                    self.Ui.radioButton_poster_cut.setChecked(True)
            except:
                self.Ui.radioButton_poster_cut.setChecked(True)
                try:    # 兼容老版本0927
                    if config['file_download']['poster_source'] == 'download':
                        self.Ui.radioButton_poster_official.setChecked(True)
                    else:
                        self.Ui.radioButton_poster_cut.setChecked(True)
                except:
                    self.Ui.radioButton_poster_cut.setChecked(True)

            self.addTextMain('config.ini 读取完成！\n')
            print('config.ini read done!')
            self.save_config_clicked()
        else:
            # ini不存在，重新创建
            print('Create config file: config.ini\n')
            self.addTextMain('Create config file: config.ini\n')
            self.init_config_clicked()

    def check_proxyChange(self):             # 检测代理变化
        proxy_type = self.config.get('type')
        proxy = self.config.get('proxy')
        timeout = self.config.get('timeout')
        retry_count = self.config.get('retry')
        self.new_proxy = (proxy_type, proxy, timeout, retry_count)
        if self.current_proxy:
            if self.new_proxy != self.current_proxy:
                self.addNetTextMain('\n🌈 代理设置已改变：')
                self.show_netstatus(self.new_proxy)
        self.current_proxy = self.new_proxy
        return self.new_proxy

    # ======================================================================================读取设置页的设置, 保存config.ini，然后重新加载
    def pushButton_save_config_clicked(self):
        self.save_config_clicked()
        self.Load_config()

    def save_config_clicked(self):
        main_mode = 1
        no_nfo_scrape = 'off'
        main_like = 1
        more_website = ''
        success_file_move = 1
        failed_file_move = 1
        success_file_rename = 1
        del_empty_folder = 1
        series_as_set = 1
        soft_link = 0
        show_poster = 0
        switch_debug = 0
        update_check = 0
        translate_language = ''
        translate_content = ''
        translate_by = 'youdao'
        actor_output = 'zh_cn'
        info_output = 'zh_cn'
        del_actor_name = 1
        pic_name = 0
        cd_name = 0
        save_log = 0
        website = ''
        mark_type = ''
        mark_pos = ''
        poster_from = 'auto'
        download_nfo = 'on'
        download_poster = 'on'
        download_thumb = 'on'
        download_fanart = 'on'
        download_extrafanart = 'off'
        download_extrafanart_copy = 'off'
        keep_local_nfo = 'off'
        keep_local_poster = 'off'
        keep_local_fanart = 'off'
        keep_local_thumb = 'off'
        keep_local_extrafanart = 'off'
        keep_local_extrafanart_copy = 'off'
        proxy_type = ''
        folder_cnword = 1
        file_cnword = 1
        # ======================================================================================common
        if self.Ui.radioButton_common.isChecked():  # 普通模式
            main_mode = 1
        elif self.Ui.radioButton_sort.isChecked():  # 整理模式
            main_mode = 2
        elif self.Ui.radioButton_read.isChecked():  # 读取模式
            main_mode = 3
        if self.Ui.checkBox_read_no_nfo_scrape.isChecked():    # 无nfo是否刮削
            no_nfo_scrape = 'on'
        else:
            no_nfo_scrape = 'off'
        if self.Ui.radioButton_like_more.isChecked():  # 字段全
            main_like = 1
        elif self.Ui.radioButton_like_speed.isChecked():  # 快速
            main_like = 0
        if self.Ui.checkBox_more_javdb.isChecked():  # javdb
            more_website += ',javdb'
        if self.Ui.checkBox_more_jav321.isChecked():  # jav321
            more_website += ',jav321'
        if self.Ui.checkBox_more_javlibrary.isChecked():  # dmm
            more_website += ',javlibrary'
        if self.Ui.checkBox_more_dmm.isChecked():  # dmm
            more_website += ',dmm'
        if self.Ui.radioButton_soft_on.isChecked():  # 软链接开
            soft_link = 1
        elif self.Ui.radioButton_soft_off.isChecked():  # 软链接关
            soft_link = 0
        if self.Ui.radioButton_debug_on.isChecked():  # 调试模式开
            switch_debug = 1
        elif self.Ui.radioButton_debug_off.isChecked():  # 调试模式关
            switch_debug = 0
        if self.Ui.radioButton_update_on.isChecked():  # 检查更新
            update_check = 1
        elif self.Ui.radioButton_update_off.isChecked():  # 不检查更新
            update_check = 0
        if self.Ui.radioButton_actor_zh_cn.isChecked():  # 演员名输出简体
            actor_output = 'zh_cn'
        elif self.Ui.radioButton_actor_zh_tw.isChecked():  # 演员名输出繁体
            actor_output = 'zh_tw'
        elif self.Ui.radioButton_actor_jp.isChecked():  # 演员名输出日文
            actor_output = 'ja'
        elif self.Ui.radioButton_actor_no.isChecked():  # 演员名不映射
            actor_output = 'no'
        if self.Ui.radioButton_tag_zh_cn.isChecked():  # 标签名输出简体
            info_output = 'zh_cn'
        elif self.Ui.radioButton_tag_zh_tw.isChecked():  # 标签名输出繁体
            info_output = 'zh_tw'
        elif self.Ui.radioButton_tag_jp.isChecked():  # 标签名输出日文
            info_output = 'ja'
        elif self.Ui.radioButton_tag_no.isChecked():  # 标签名不映射
            info_output = 'no'
        if self.Ui.radioButton_zh_cn.isChecked():  # 翻译简体
            translate_language = 'zh_cn'
        elif self.Ui.radioButton_zh_tw.isChecked():  # 翻译繁体
            translate_language = 'zh_tw'
        elif self.Ui.radioButton_ja.isChecked():  # 翻译日文
            translate_language = 'ja'
        if self.Ui.checkBox_translate_title.isChecked():  # 翻译标题
            translate_content += ',title'
        if self.Ui.checkBox_translate_outline.isChecked():  # 翻译简介
            translate_content += ',outline'
        if self.Ui.radioButton_youdao.isChecked():  # 有道翻译
            translate_by = 'youdao'
        elif self.Ui.radioButton_deepl.isChecked():  # deepl翻译
            translate_by = 'deepl'
        if self.Ui.radioButton_pic_file_poster.isChecked():  # 图片命名规则-加文件名
            pic_name = 0
        elif self.Ui.radioButton_pic_poster.isChecked():  # 图片命名规则-不加文件名
            pic_name = 1
        if self.Ui.radioButton_cd_part_lower.isChecked():  # 分集命名规则-小写
            cd_name = 0
        elif self.Ui.radioButton_cd_part_upper.isChecked():  # 分集命名规则-大写
            cd_name = 1
        if self.Ui.radioButton_del_actor_on.isChecked():  # 去除标题歌手名开
            del_actor_name = 1
        elif self.Ui.radioButton_del_actor_off.isChecked():  # 去除标题歌手名关
            del_actor_name = 0
        if self.Ui.radioButton_log_on.isChecked():  # 开启日志
            save_log = 1
        elif self.Ui.radioButton_log_off.isChecked():  # 关闭日志
            save_log = 0
        if self.Ui.checkBox_cover.isChecked():  # 显示封面
            show_poster = 1
        else:  # 关闭封面
            show_poster = 0
        if self.Ui.radioButton_succ_move_on.isChecked():  # 成功移动开
            success_file_move = 1
        elif self.Ui.radioButton_succ_move_off.isChecked():  # 成功移动关
            success_file_move = 0
        if self.Ui.radioButton_fail_move_on.isChecked():  # 失败移动开
            failed_file_move = 1
        elif self.Ui.radioButton_fail_move_off.isChecked():  # 失败移动关
            failed_file_move = 0
        if self.Ui.radioButton_succ_rename_on.isChecked():  # 成功重命名开
            success_file_rename = 1
        elif self.Ui.radioButton_succ_rename_off.isChecked():  # 成功重命名关
            success_file_rename = 0
        if self.Ui.radioButton_del_empty_folder_on.isChecked():  # 结束后删除空文件夹开
            del_empty_folder = 1
        elif self.Ui.radioButton_del_empty_folder_off.isChecked():  # 结束后删除空文件夹关
            del_empty_folder = 0
        if self.Ui.radioButton_series_as_set_on.isChecked():  # 使用系列作为合集开
            series_as_set = 1
        elif self.Ui.radioButton_series_as_set_off.isChecked():  # 使用系列作为合集关
            series_as_set = 0
        if self.Ui.comboBox_website_all.currentText() == 'All websites':  # all
            website = 'all'
        elif self.Ui.comboBox_website_all.currentText() == 'iqqtv':  # iqqtv
            website = 'iqqtv'
        elif self.Ui.comboBox_website_all.currentText() == 'javbus':  # javbus
            website = 'javbus'
        elif self.Ui.comboBox_website_all.currentText() == 'javdb':  # javdb
            website = 'javdb'
        elif self.Ui.comboBox_website_all.currentText() == 'jav321':  # jav321
            website = 'jav321'
        elif self.Ui.comboBox_website_all.currentText() == 'dmm':  # dmm
            website = 'dmm'
        elif self.Ui.comboBox_website_all.currentText() == 'avsox':  # avsox
            website = 'avsox'
        elif self.Ui.comboBox_website_all.currentText() == 'xcity':  # xcity
            website = 'xcity'
        elif self.Ui.comboBox_website_all.currentText() == 'mgstage':  # mgstage
            website = 'mgstage'
        elif self.Ui.comboBox_website_all.currentText() == 'fc2':  # fc2
            website = 'fc2'
        elif self.Ui.comboBox_website_all.currentText() == 'fc2club':  # fc2club
            website = 'fc2club'
        elif self.Ui.comboBox_website_all.currentText() == 'fc2hub':  # fc2hub
            website = 'fc2hub'
        elif self.Ui.comboBox_website_all.currentText() == 'airav':  # airav
            website = 'airav'
        elif self.Ui.comboBox_website_all.currentText() == 'javlibrary':  # javlibrary
            website = 'javlibrary'
        # ======================================================================================proxy
        if self.Ui.radioButton_proxy_http.isChecked():  # http proxy
            proxy_type = 'http'
        elif self.Ui.radioButton_proxy_socks5.isChecked():  # socks5 proxy
            proxy_type = 'socks5'
        elif self.Ui.radioButton_proxy_nouse.isChecked():  # nouse proxy
            proxy_type = 'no'
        # ======================================================================================水印
        if self.Ui.checkBox_poster_mark.isChecked():  # 封面添加水印
            poster_mark = 1
        else:  # 关闭封面添加水印
            poster_mark = 0
        if self.Ui.checkBox_thumb_mark.isChecked():  # 缩略图添加水印
            thumb_mark = 1
        else:  # 关闭缩略图添加水印
            thumb_mark = 0
        if self.Ui.checkBox_sub.isChecked():  # 字幕
            mark_type += ',SUB'
        if self.Ui.checkBox_leak.isChecked():  # 流出
            mark_type += ',LEAK'
        if self.Ui.checkBox_uncensored.isChecked():  # 无码
            mark_type += ',UNCENSORED'
        if self.Ui.radioButton_top_left.isChecked():  # 左上
            mark_pos = 'top_left'
        elif self.Ui.radioButton_bottom_left.isChecked():  # 左下
            mark_pos = 'bottom_left'
        elif self.Ui.radioButton_top_right.isChecked():  # 右上
            mark_pos = 'top_right'
        elif self.Ui.radioButton_bottom_right.isChecked():  # 右下
            mark_pos = 'bottom_right'
        if self.Ui.radioButton_poster_official.isChecked():  # poster下载优先
            poster_from = 'download'
        elif self.Ui.radioButton_poster_cut.isChecked():  # poster自动
            poster_from = 'auto'
 
        if self.Ui.checkBox_foldername.isChecked():
            folder_cnword = 1
        else:
            folder_cnword = 0
        if self.Ui.checkBox_filename.isChecked():
            file_cnword = 1
        else:
            file_cnword = 0
        # ======================================================================================下载文件，剧照
        if self.Ui.checkBox_download_nfo.isChecked():
            download_nfo = 'on'
        else:
            download_nfo = 'off'
        if self.Ui.checkBox_download_poster.isChecked():
            download_poster = 'on'
        else:
            download_poster = 'off'
        if self.Ui.checkBox_download_fanart.isChecked():
            download_fanart = 'on'
        else:
            download_fanart = 'off'
        if self.Ui.checkBox_download_thumb.isChecked():
            download_thumb = 'on'
        else:
            download_thumb = 'off'
        if self.Ui.checkBox_download_extrafanart.isChecked():
            download_extrafanart = 'on'
        else:
            download_extrafanart = 'off'
        if self.Ui.checkBox_download_extrafanart_copy.isChecked():
            download_extrafanart_copy = 'on'
        else:
            download_extrafanart_copy = 'off'
        if self.Ui.checkBox_old_nfo.isChecked():
            keep_local_nfo = 'on'
        else:
            keep_local_nfo = 'off'
        if self.Ui.checkBox_old_poster.isChecked():
            keep_local_poster = 'on'
        else:
            keep_local_poster = 'off'
        if self.Ui.checkBox_old_fanart.isChecked():
            keep_local_fanart = 'on'
        else:
            keep_local_fanart = 'off'
        if self.Ui.checkBox_old_thumb.isChecked():
            keep_local_thumb = 'on'
        else:
            keep_local_thumb = 'off'
        if self.Ui.checkBox_old_extrafanart.isChecked():
            keep_local_extrafanart = 'on'
        else:
            keep_local_extrafanart = 'off'
        if self.Ui.checkBox_old_extrafanart_copy.isChecked():
            keep_local_extrafanart_copy = 'on'
        else:
            keep_local_extrafanart_copy = 'off'
        # 自动上传头像
        if self.Ui.radioButton_actor_photo_upload_on.isChecked():  # 自动上传头像开
            actor_photo_upload = 'on'
        elif self.Ui.radioButton_actor_photo_upload_off.isChecked():  # 自动上传头像关
            actor_photo_upload = 'off'

        # 加上错误判断
        try:    # 长度命名规则-目录
            folder_name_max = int(self.Ui.lineEdit_folder_name_max.text())
            if folder_name_max <= 0 or folder_name_max > 255:
                folder_name_max = 70
        except:
            folder_name_max = 70
        try:    # 长度命名规则-文件名
            file_name_max = int(self.Ui.lineEdit_file_name_max.text())
            if file_name_max <= 0 or file_name_max > 255:
                file_name_max = 70
        except:
            file_name_max = 70
        try:    # 长度命名规则-演员数量
            actor_name_max = int(self.Ui.lineEdit_actor_name_max.text())
        except:
            actor_name_max = 3
        try:    # 小文件大小
            file_size = float(self.Ui.lineEdit_escape_size.text())
        except:
            file_size = 100.0

        json_config = {
            'main_mode': main_mode,
            'no_nfo_scrape': no_nfo_scrape,
            'main_like': main_like,
            'more_website': more_website.strip(','),
            'soft_link': soft_link,
            'switch_debug': switch_debug,
            'show_poster': show_poster,
            'success_file_move': success_file_move,
            'failed_file_move': failed_file_move,
            'success_file_rename': success_file_rename,
            'del_empty_folder': del_empty_folder,
            'update_check': update_check,
            'translate_language': translate_language,
            'translate_content': translate_content.strip(','),
            'translate_by': translate_by,
            'actor_output': actor_output,
            'info_output': info_output,
            'deepl_key': self.Ui.lineEdit_deepl_key.text(),
            'del_actor_name': del_actor_name,
            'pic_name': pic_name,
            'cd_name': cd_name,
            'save_log': save_log,
            'website': website,
            'series_as_set': series_as_set,
            'type': proxy_type,
            'proxy': self.Ui.lineEdit_proxy.text(),
            'timeout': self.Ui.horizontalSlider_timeout.value(),
            'retry': self.Ui.horizontalSlider_retry.value(),
            'javdb': self.Ui.plainTextEdit_cookie_javdb.toPlainText(),
            'folder_name': self.Ui.lineEdit_dir_name.text(),
            'naming_media': self.Ui.lineEdit_media_name.text(),
            'naming_file': self.Ui.lineEdit_local_name.text(),
            'folder_name_max': folder_name_max,
            'file_name_max': file_name_max,
            'actor_name_max': actor_name_max,
            'actor_name_more': self.Ui.lineEdit_actor_name_more.text(),
            'actor_no_name': self.Ui.lineEdit_actor_no_name.text(),
            'folders': self.Ui.lineEdit_escape_dir.text(),
            'cnword_char': self.Ui.lineEdit_cnword_char.text(),
            'cnword_style': self.Ui.lineEdit_cnword_style.text(),
            'string': self.Ui.lineEdit_escape_string_2.text(),
            'file_size': file_size,
            'emby_url': self.Ui.lineEdit_emby_url.text(),
            'api_key': self.Ui.lineEdit_api_key.text(),
            'actor_photo_folder': self.Ui.lineEdit_actor_photo_folder.text(),
            'actor_photo_upload': actor_photo_upload,
            'media_path': self.Ui.lineEdit_movie_path.text(),
            'media_type': self.Ui.lineEdit_movie_type_2.text(),
            'sub_type': self.Ui.lineEdit_sub_type_2.text(),
            'failed_output_folder': self.Ui.lineEdit_fail.text(),
            'success_output_folder': self.Ui.lineEdit_success.text(),
            'extrafanart_folder': self.Ui.lineEdit_extrafanart_dir.text(),
            'poster_mark': poster_mark,
            'thumb_mark': thumb_mark,
            'mark_size': self.Ui.horizontalSlider_mark_size.value(),
            'mark_type': mark_type.strip(','),
            'mark_pos': mark_pos,
            'download_nfo': download_nfo,
            'download_poster': download_poster,
            'download_fanart': download_fanart,
            'download_thumb': download_thumb,
            'download_extrafanart': download_extrafanart,
            'download_extrafanart_copy': download_extrafanart_copy,
            'keep_local_nfo': keep_local_nfo,
            'keep_local_poster': keep_local_poster,
            'keep_local_fanart': keep_local_fanart,
            'keep_local_thumb': keep_local_thumb,
            'keep_local_extrafanart': keep_local_extrafanart,
            'keep_local_extrafanart_copy': keep_local_extrafanart_copy,
            'poster_from': poster_from,
            'folder_cnword': folder_cnword,
            'file_cnword': file_cnword,
        }
        self.config = json_config
        save_config(json_config)
        self.check_proxyChange()

    # ======================================================================================工具-单文件刮削
    def pushButton_select_file_clicked(self):   # 点选择文件
        media_path = self.Ui.lineEdit_movie_path.text() # 获取带刮削目录作为打开目录
        if not media_path:
            media_path = self.main_path
        file_path, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取视频文件", media_path, "Movie Files(*.mp4 "
                                                                                         "*.avi *.rmvb *.wmv "
                                                                                         "*.mov *.mkv *.flv *.ts "
                                                                                         "*.webm *.MP4 *.AVI "
                                                                                         "*.RMVB *.WMV *.MOV "
                                                                                         "*.MKV *.FLV *.TS "
                                                                                         "*.WEBM);;All Files(*)")
        select_file_path = self.convert_path(file_path)
        self.Ui.lineEdit_single_file_path.setText(select_file_path)

    def pushButton_start_single_file_clicked(self): # 点刮削
        self.single_file_path = self.Ui.lineEdit_single_file_path.text()
        if self.single_file_path != '' and os.path.isfile(self.single_file_path):
            self.pushButton_show_log_clicked() # 点击刮削按钮后跳转到日志页面
            self.Ui.pushButton_start_cap.setEnabled(False)
            self.Ui.pushButton_start_cap2.setEnabled(False)
            self.Ui.pushButton_start_cap.setText('正在刮削')
            self.Ui.pushButton_start_cap2.setText('正在刮削')
            self.Ui.pushButton_start_cap.setStyleSheet('QPushButton#pushButton_start_cap{color:#999999;background-color:#F0F0F0;}')
            self.Ui.pushButton_start_cap2.setStyleSheet('QPushButton#pushButton_start_cap2{color:#999999;background-color:#F0F0F0;}')
            self.progressBarValue.emit(int(0))
            try:
                t = threading.Thread(target=self.AVDC_Main, args=('single_file',))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as ex:
                self.addTextMain('Error in pushButton_start_single_file_clicked: ' + str(ex))

    def pushButton_select_file_clear_info_clicked(self):    # 点清空信息
        self.Ui.lineEdit_single_file_path.setText('')
        self.Ui.lineEdit_appoint_url.setText('')
        self.Ui.lineEdit_movie_number.setText('')
        self.Ui.comboBox_website.setCurrentIndex(0)


    # ======================================================================================工具-裁剪封面图
    def pushButton_select_thumb_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        if not path:
            # path = os.getcwd()
            # path = os.path.split(os.path.realpath(__file__))[0]
            path = self.main_path
        file_path, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取缩略图", path,
                                                                   "Picture Files(*.jpg *.png);;All Files(*)")
        img_name, img_ex = os.path.splitext(file_path)
        if file_path != '':
            newWin2.showimage(file_path)
            newWin2.show()

    def image_cut(self, thumb_path, poster_path, mode=1):
        try:
            if os.path.exists(poster_path):
                os.remove(poster_path)
        except Exception as ex:
            self.addTextMain(" 🔴 Failed to remove old poster!\n   >>> " + str(ex))
            return False

        """ 获取图片分辨率 """
        im = Image.open(thumb_path)  # 返回一个Image对象
        width, height = im.size

        """ 获取裁剪区域 """
        ex, ey, ew, eh = 0, 0, 0, 0
        if height / width <= 1.5:  # 长宽比大于1.5, 太宽
            ex = int((width - height / 1.5) / 2)
            ey = 0
            ew = int(height / 1.5)
            eh = int(height)
        elif height / width > 1.5:  # 长宽比小于1.5, 太窄
            ex = 0
            ey = int((height - width * 1.5) / 2)
            ew = int(width)
            eh = int(width * 1.5)

        """ 读取图片 """
        # fp = open(thumb_path, 'rb')
        # fp.read()
        img = Image.open(thumb_path)
        img = img.convert('RGB')
        img_new_png = img.crop((ex, ey, ew + ex, eh + ey))
        # fp.close()
        img_new_png.save(poster_path)
        self.addTextMain(" 🟢 Poster done!")
        if mode == 2:
            pix = QPixmap(thumb_path)
            self.Ui.label_thumb.setScaledContents(True)
            self.Ui.label_thumb.setPixmap(pix)  # 添加图标
            pix = QPixmap(poster_path)
            self.Ui.label_poster.setScaledContents(True)
            self.Ui.label_poster.setPixmap(pix)  # 添加图标
        return True

    # ======================================================================================小工具-视频移动
    def move_file(self):
        box = QMessageBox(QMessageBox.Question,'移动视频和字幕','确定要移动视频和字幕吗？')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.button(QMessageBox.Yes).setText('确定')
        box.button(QMessageBox.No).setText('取消')
        box.setDefaultButton(QMessageBox.No)
        reply = box.exec()
        if reply == QMessageBox.Yes:
            self.pushButton_show_log_clicked() # 点击开始移动按钮后跳转到日志页面
            try:
                t = threading.Thread(target=self.move_file_thread)
                t.start()  # 启动线程,即让线程开始执行
            except Exception as ex:
                self.addTextMain('Error in move_file: ' + str(ex))

    def move_file_thread(self):
        movie_path = self.Ui.lineEdit_movie_path.text().replace('\\', '/')
        escape_dir = self.Ui.lineEdit_escape_dir_move.text().replace('\\', '/')
        escape_dir = escape_dir + ',Movie_moved'
        movie_type = self.Ui.lineEdit_movie_type_2.text().lower()
        sub_type = self.Ui.lineEdit_sub_type_2.text().lower().replace('|.txt', '')
        all_type = movie_type.strip('|') + '|' + sub_type.strip('|')
        if not movie_path:  # 没有输入视频目录时，获取程序当前路径
            # movie_path = os.path.abspath(".")
            try:
                movie_path = os.path.split(os.path.realpath(__file__))[0]
            except Exception as e:
                print('move_file_thread: %s' % e)
        movie_list = movie_lists(escape_dir, all_type, movie_path)
        des_path = os.path.join(movie_path, 'Movie_moved')
        if not os.path.exists(des_path):
            self.addTextMain('Created folder: Movie_moved')
            os.makedirs(des_path)
        self.addTextMain('Start move movies...')
        skip_list = []
        for file_path in movie_list:
            file_name = os.path.split(file_path)[1]
            file_ext = os.path.splitext(file_name)[1]
            try:
                shutil.move(file_path, des_path)
                if file_ext in movie_type:
                    self.addTextMain('   Move movie: ' + file_name + ' to Movie_moved Success!')
                else:
                    self.addTextMain('   Move sub: ' + file_name + ' to Movie_moved Success!')
            except Exception as ex:
                skip_list.append([file_name, file_path, ex])
        if skip_list:
            self.addTextMain("\n%s file(s) did not move!"% len(skip_list))
            i = 0
            for info in skip_list:
                i += 1
                self.addTextMain("[%s] %s\n file path: %s\n %s\n"% (i, info[0], info[1], info[2]))
        self.addTextMain("Move movies finished!")
        self.addTextMain("================================================================================")

    # ======================================================================================设置头像
    def pushButton_add_actor_pic_clicked(self):  # 设置页面点上传头像按钮
        self.pushButton_show_log_clicked() # 点按钮后跳转到日志页面
        try:
            t = threading.Thread(target=self.uploadActorPhoto)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('Error pushButton_add_actor_pic_clicked: ' + str(ex))


    def pushButton_show_pic_actor_clicked(self):  # 设置页面点查看演员列表按钮
        self.pushButton_show_log_clicked() # 点按钮后跳转到日志页面
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.addTextMain('The emby_url is empty!')
            self.addTextMain("================================================================================")
            return
        elif api_key == '':
            self.addTextMain('The api_key is empty!')
            self.addTextMain("================================================================================")
            return
        try:
            t = threading.Thread(target=self.show_actor, args=(self.Ui.comboBox_pic_actor.currentIndex(),))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('Error in pushButton_show_pic_actor_clicked: ' + str(ex))

    def show_actor(self, mode):  # 按模式显示相应列表
        if mode == 0:  # 没有头像的演员：
            self.addTextMain('没有头像的演员：')
        elif mode == 1:  # 有头像的演员：
            self.addTextMain('有头像的演员：')
        elif mode == 2:  # 所有演员：
            self.addTextMain('所有演员：')
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.addTextMain("================================================================================")
            return
        count = 1
        actor_list_temp = ''
        for actor in actor_list['Items']:
            if mode == 2:  # 所有演员：
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            elif mode == 1 and actor['ImageTags'] != {}:  # 有头像的演员：
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            elif mode == 0 and actor['ImageTags'] == {}:  # 没有头像的演员：
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            if (count - 1) % 5 == 0 and actor_list_temp != '':
                self.addTextMain(actor_list_temp)
                actor_list_temp = ''
        self.addTextMain("================================================================================")

    def get_emby_actor_list(self):  # 获取emby的演员列表
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        emby_url = emby_url.replace('：', ':').strip('/')
        if 'http://' not in emby_url and 'https://' not in emby_url:
            url = 'http://' + emby_url + '/emby/Persons?api_key=' + api_key
        else:
            url = emby_url + '/emby/Persons?api_key=' + api_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/60.0.3100.0 Safari/537.36'}
        actor_list = {}
        try:
            getweb = requests.get(str(url), headers=headers, timeout=10)
            getweb.encoding = 'utf-8'
            actor_list = json.loads(getweb.text)
        except:
            self.addTextMain('Error! Check your emby_url or api_key!')
            actor_list['TotalRecordCount'] = 0
        return actor_list

    def uploadActorPhoto_main(self):  # 主界面上传头像
        actor_photo_upload = self.config.get('actor_photo_upload')
        if actor_photo_upload == 'on':
            try:
                t = threading.Thread(target=self.uploadActorPhoto)
                t.start()  # 启动线程,即让线程开始执行
            except Exception as ex:
                self.addTextMain('Error uploadActorPhoto_main: ' + str(ex))

    def uploadActorPhoto(self):  # 上传头像
        self.addTextMain('Start upload acotr photo...')
        result, local_actor_photo_list = self.checkEmbySetting()
        if result:
            emby_actor_list = 'emby_actor_list.json'
            if not os.path.exists(emby_actor_list):
                self.addTextMain('正在创建演员头像映射表...（第一次速度较慢，以后就快了）')
                with open(emby_actor_list, 'w', encoding='utf-8') as f:
                    f.write('{}')
            with open(emby_actor_list, 'r', encoding='utf-8') as data:
                json_data = json.load(data)
            json_data = self.found_actor_photo(json_data, local_actor_photo_list)
            with open (emby_actor_list, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )


    def checkEmbySetting(self):  # 检查emby和头像包
        emby_url = self.config.get('emby_url')
        api_key = self.config.get('api_key')
        actor_photo_folder = self.config.get('actor_photo_folder')
        if actor_photo_folder == '' or not os.path.exists(actor_photo_folder):
            self.addTextMain('Actor folder not exist!')
            self.addTextMain("================================================================================")
            return False, ''
        elif emby_url == '':
            self.addTextMain('The emby_url is empty!')
            self.addTextMain("================================================================================")
            return False, ''
        elif api_key == '':
            self.addTextMain('The api_key is empty!')
            self.addTextMain("================================================================================")
            return False, ''
        else:
            local_actor_photo_list = os.listdir(actor_photo_folder)
            if not local_actor_photo_list:
                self.addTextMain('Actor photo not exist!')
                self.addTextMain("================================================================================")
                return False, ''
            return True, local_actor_photo_list

    def found_actor_photo(self, json_data, local_actor_photo_list):  # 找到可以上传的演员，然后调用上传函数
        path = self.Ui.lineEdit_actor_photo_folder.text()
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.addTextMain("================================================================================")
            return json_data
        count = 1
        for actor in actor_list['Items']:
            flag = 0
            pic_name = ''
            if actor['ImageTags'] == {}:    # 表示emby没有头像
                actor_jp, json_data = self.getJpActorName(actor['Name'], json_data)   # 获取日文名字
                if actor_jp + '.jpg' in local_actor_photo_list:
                    flag = 1
                    pic_name = actor_jp + '.jpg'
                elif actor_jp + '.png' in local_actor_photo_list:
                    flag = 1
                    pic_name = actor_jp + '.png'
                if flag == 0:
                    byname_list = re.split('[,，()（）]', actor['Name'])
                    if len(byname_list) > 1:
                        for byname in byname_list:
                            byname_jp, json_data = self.getJpActorName(byname, json_data)  # 获取日文名字
                            if byname_jp + '.jpg' in local_actor_photo_list:
                                pic_name = byname_jp + '.jpg'
                                flag = 1
                                break
                            elif byname_jp + '.png' in local_actor_photo_list:
                                pic_name = byname_jp + '.png'
                                flag = 1
                                break
                if flag == 1:   # 表示本地头像目录有图片
                    try:
                        self.upload_actor_photo(count, actor, os.path.join(path, pic_name))
                    except Exception as ex:
                        self.addTextMain('Error in found_actor_photo! ' + str(ex))
                    count += 1
        if count == 1:
            self.addTextMain('No actor photo can be uploaded!')
        self.addTextMain("================================================================================")
        return json_data

    def upload_actor_photo(self, count, actor, pic_path):  # 上传头像
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        emby_url = emby_url.replace('：', ':').strip('/')
        if 'http://' not in emby_url and 'https://' not in emby_url:
            url = 'http://' + emby_url + '/emby/Items/' + actor['Id'] + '/Images/Primary?api_key=' + api_key
        else:
            url = emby_url + '/emby/Items/' + actor['Id'] + '/Images/Primary?api_key=' + api_key

        try:
            f = open(pic_path, 'rb')  # 二进制方式打开图文件
            b6_pic = base64.b64encode(f.read())  # 读取文件内容, 转换为base64编码
            f.close()
            if pic_path.endswith('jpg'):
                header = {"Content-Type": 'image/jpeg', }
            else:
                header = {"Content-Type": 'image/png', }
            requests.post(url=url, data=b6_pic, headers=header)
            self.addTextMain("%4s" % str(count) + '.Success upload profile picture for ' + actor['Name'] + '!')
        except Exception as ex:
            self.addTextMain('Error in upload_actor_photo! ' + str(ex))


    # ======================================================================================语句添加到日志框
    def getJpActorName(self, actor, json_data):
        try:
            actor_jp = json_data[actor]
        except:
            if not self.actor_xml:
                actor_xml_file = 'mapping_actor.xml'
                if not os.path.exists(actor_xml_file):
                    shutil.copy(self.actor_file, os.path.join(self.main_path, actor_xml_file))
                self.actor_xml = etree.parse(actor_xml_file)
            if not self.actor_xml:
                return actor, json_data
            actor_jp = actor
            actor_name = ',%s,' % actor.upper()
            actor_output_name= self.actor_xml.xpath('a[contains(@keyword, $name)]/@jp', name=actor_name)
            if actor_output_name:
                actor_jp = actor_output_name[0]
            json_data[actor] = actor_jp
        return actor_jp, json_data


    # ======================================================================================语句添加到日志框
    def addTextMain(self, text):
        if self.Ui.radioButton_log_on.isChecked():  # 保存日志
            try:
                self.log_txt.write((str(text) + '\n').encode('utf8'))
            except:
                log_folder = os.path.join(self.main_path, 'Log')
                if not os.path.exists(log_folder):
                    os.makedirs(log_folder)
                log_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.txt'
                log_name = self.convert_path(os.path.join(log_folder, log_name))

                self.log_txt = open(log_name, "wb", buffering=0)
                self.addTextMain('Create log file: ' + log_name + '\n')
                self.addTextMain(text)
                self.addTextMain(' 主程序路径：%s \n' % self.main_path)
                # aa = '主路径1 os.getcwd()：' + os.getcwd()
                # bb = '主路径2 sys.path[0]：' + sys.path[0]
                # cc = '主路径3 os.path.split(os.path.realpath(__file__))[0]：' + os.path.split(os.path.realpath(__file__))[0]
                # dd = '主路径4 os.path.abspath(".")：' + os.path.abspath(".")
                # self.addTextMain(' %s \n %s \n %s \n %s \n' % (aa, bb, cc, dd))
                print('Create log file: ' + log_name + '\n')
                print(text)
                return
        try:
            self.main_logs_show.emit(text)
        except Exception as ex:
            print('Error in addTextMain' + str(ex))
            self.Ui.textBrowser_log_main.append('Error in addTextMain' + str(ex))


    # ======================================================================================语句添加到日志框
    def addNetTextMain(self, text):
        try:
            self.net_logs_show.emit(text)
        except Exception as ex:
            print('Error in addNetTextMain' + str(ex))
            self.Ui.textBrowser_net_main.append('Error in addNetTextMain' + str(ex))


    # ======================================================================================移动到失败文件夹
    def moveFailedFolder(self, file_path, folder_old_path, failed_folder, file_ex):
        main_mode = self.config.get('main_mode')
        no_nfo_scrape = self.config.get('no_nfo_scrape')
        if main_mode == 3 and no_nfo_scrape == 'off':  # 读取模式，无nfo不刮削视频时，不移动失败文件
            return
        if self.config.get('failed_file_move') == 1:
            if self.config.get('soft_link') != 1:
                file_new_path = self.convert_path(os.path.join(failed_folder, os.path.split(file_path)[1]))
                if not os.path.exists(failed_folder):
                    self.creatFailedFolder(failed_folder)  # 创建failed文件夹
                if failed_folder not in file_path:
                    if not os.path.exists(file_new_path):
                        try:
                            shutil.move(file_path, failed_folder)
                            self.addTextMain("   >>> Move file to the failed folder! \n   >>> The new path is '%s'" % file_new_path)
                        except Exception as ex:
                            self.addTextMain("   >>> Failed to move the file to the failed folder! \n   >>> " + str(ex))
                    else:
                        self.addTextMain("   >>> The failed path '%s' already exists \n   >>> The file will not be moved to the failed folder!\n   >>> The current path is '%s'" % (file_new_path, file_path))
                else:
                    self.addTextMain("   >>> The file is already in the failed folder, no need to move it again!\n   >>> The current path is '%s'" % file_path)

    # ======================================================================================下载文件
    def downloadFileWithFilename(self, url, filename, folder_new_path):
        cookies = None
        ex1 = ''
        if url == '' or url == 'unknown':
            return False
        proxy_info = get_proxy_info()
        proxies = proxy_info.get('proxies')
        timeout = proxy_info.get('timeout')
        retry_count = proxy_info.get('retry_count')

        i = 0
        while i < retry_count:
            try:
                if not os.path.exists(folder_new_path):
                    os.makedirs(folder_new_path)
                    
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',}
                result = requests.get(str(url), headers=headers, proxies=proxies, timeout=timeout, cookies=cookies, )
                with open(str(folder_new_path) + "/" + filename, "wb") as code:
                    code.write(result.content)
                code.close()
                return True
            except Exception as ex:
                i += 1
                print(str(ex))
                ex1 = str(ex)
        self.addTextMain(" 🟠 Download failed! url ( %s )\n   >>> %s" % (url, str(ex1)))
        return False

    # ======================================================================================下载缩略图
    def thumbDownload(self, json_data, folder_new_path, thumb_new_name, thumb_new_path, fanart_new_path):
        if self.config.get('download_thumb') == 'off' and self.config.get('download_poster') == 'off' and self.config.get('download_fanart') == 'off': # 如果thumb、poster、fanart都不下载，则不需要下载thumb
            return True
        if os.path.exists(thumb_new_path):  # 本地有thumb时不下载
            return True
        if os.path.exists(fanart_new_path):  # 本地有fanart时不下载
            shutil.copy(fanart_new_path, thumb_new_path)
            return True
        # self.addTextMain(" ⏳ Start downloading the thumb... ")
        try:
            cover_url = str(json_data['cover'])
        except Exception as ex:
            self.addTextMain(" 🟠 Can't use the cover url to download thumb! beacuse the cover url is not exist! \n >>> %s" % str(ex))
        else:
            i = 1
            while i <= self.config.get('retry'):
                self.downloadFileWithFilename(cover_url, thumb_new_name, folder_new_path)
                if not check_pic(thumb_new_path):
                    i = i + 1
                else:
                    break
            if check_pic(thumb_new_path):
                self.addTextMain(" 🟢 Thumb done!")
                return True
        if os.path.exists(thumb_new_path):  # 移除已存在的thumb文件
            os.remove(thumb_new_path)
        if self.config.get('download_poster') == 'on' and self.config.get('poster_from') == 'download':
            pass    # 等待poster下载结果，如果下载成功，就使用poster作为thumb
        else:
            shutil.copy(self.default_thumb, thumb_new_path)
            self.addTextMain(" 🟠 Thumb download failed! Now use the default thumb as thumb! ")
        return True

    # ======================================================================================下载poster
    def posterDownload(self, json_data, folder_new_path, poster_new_name, thumb_new_path, poster_new_path, fanart_new_path):
        if self.config.get('download_poster') == 'off':   # 设置不下载poster时，不下载
            return True
        if os.path.exists(poster_new_path): # 本地有poster时，不下载
            return True
        if self.config.get('poster_from') == 'download' or json_data['image_download']:     # 设置中选择了下载小封面优先或者自动选择下载小封面为真时
            # self.addTextMain(" ⏳ Start downloading the poster... ")
            if self.smallCoverDownload(json_data, folder_new_path, poster_new_name, poster_new_path):
                # 如果poster下载成功，发现thumb不存在但下载开，就复制poster到thumb
                if not os.path.exists(thumb_new_path) and self.config.get('download_thumb') == 'on': 
                    shutil.copy(poster_new_path, thumb_new_path)
                    self.addTextMain(" 🟠 Thumb download failed! Now use poster as thumb! ")                    
                return True
        # 下载失败，如果存在损坏的poster，就删除掉
        if os.path.exists(poster_new_path):
            os.remove(poster_new_path)
        # 如果存在fanart，使用fanart代替thumb裁剪，因为fanart没有水印
        if os.path.exists(fanart_new_path):
            thumb_new_path = fanart_new_path
        # 如果存在thumb，使用thumb裁剪
        if os.path.exists(thumb_new_path):
            if self.cutImage(thumb_new_path, poster_new_path, json_data['image_cut']):
                return True
        # 不存在thumb，但下载thumb开
        elif self.config.get('download_thumb') == 'on':
            shutil.copy(self.default_thumb, thumb_new_path)
            self.addTextMain(" 🟠 Thumb download failed! Now use the dufault thumb as thumb! ")
        if os.path.exists(poster_new_path):
            os.remove(poster_new_path)
        shutil.copy(self.default_poster, poster_new_path)
        self.addTextMain(" 🟠 Poster failed! Now use the dufault poster as poster! ")
        return True

    # ======================================================================================下载封面图
    def smallCoverDownload(self, json_data, folder_new_path, poster_new_name, poster_new_path):
        try:
            if json_data['cover_small'] == '' or json_data['cover_small'] == 'unknown':
                return False
        except Exception as ex:
            self.addTextMain(" 🟠 Can't use the cover small url to download poster! beacuse the cover small url is not exist! \n >>> %s" % str(ex))
            return False
        if os.path.exists(poster_new_path):  # 移除已存在的poster文件，重新下载
            os.remove(poster_new_path)

        i = 1
        while i <= self.config.get('retry'):
            self.downloadFileWithFilename(json_data['cover_small'], poster_new_name, folder_new_path)
            if not check_pic(poster_new_path):
                i = i + 1
            else:
                break
        if not check_pic(poster_new_path):
            self.addTextMain(' 🟠 Poster download failed!')
            try:
                os.remove(poster_new_path)
            except:
                pass
            return False
        self.addTextMain(" 🟢 Poster done!")
        return True


    # ======================================================================================删除缩略图
    def deletethumb(self, thumb_new_name, thumb_new_path):
        if os.path.exists(thumb_new_path):
            try:
                if self.config.get('download_thumb') == 'off' and self.config.get('keep_local_thumb') == 'off':
                    os.remove(thumb_new_path)
            except Exception as ex:
                self.addTextMain(" 🔴 Failed to delete the thumb '%s'\n   >>> %s" % (thumb_new_name, str(ex)))
            return


    # ======================================================================================下载剧照
    def extrafanartDownload(self, json_data, folder_new_path):
        extrafanart_path = os.path.join(folder_new_path, 'extrafanart')
        if os.path.exists(extrafanart_path):
            return
        if self.config.get('download_extrafanart') == 'off':
            if self.config.get('download_extrafanart_copy') == 'on': # 如果要下载副本，就要下载剧照
                extrafanart_folder = self.config.get('extrafanart_folder')
                if not extrafanart_folder or extrafanart_folder == 'extrafanart':
                    return
                extrafanart_copy_path = self.convert_path(os.path.join(folder_new_path, extrafanart_folder))
                if os.path.exists(extrafanart_copy_path):
                    return
            else:
                return
        try:
            if len(json_data['extrafanart']) == 'off' or json_data['extrafanart'] == 'unknown':
                return
        except:
            return
        self.addTextMain(' ⏳ ExtraFanart downloading...')
        extrafanart_list = json_data['extrafanart']
        if not os.path.exists(extrafanart_path):
            os.makedirs(extrafanart_path)
        extrafanart_count = 0
        extrafanart_count_succ = 0
        for extrafanart_url in extrafanart_list:
            extrafanart_count += 1
            extrafanart_name = os.path.join(extrafanart_path, ('fanart' + str(extrafanart_count) + '.jpg'))
            if os.path.exists(extrafanart_name):
                os.remove(extrafanart_name)
            i = 1
            while i <= self.config.get('retry'):
                self.downloadFileWithFilename(extrafanart_url, 'fanart' + str(extrafanart_count) + '.jpg',
                                                extrafanart_path)
                if not check_pic(extrafanart_name):
                    print('Image Download Failed! Trying again. ' + str(i) + '/' + str(self.config.get('retry')))
                    i = i + 1
                else:
                    extrafanart_count_succ += 1
                    self.addTextMain(" 🟢 %s done!" % ('fanart' + str(extrafanart_count) + '.jpg'))
                    break
        self.addTextMain(" 🟢 ExtraFanart downloaded complete! Total %s , success %s " % (extrafanart_count, extrafanart_count_succ))


    # ======================================================================================拷贝剧照副本
    def extrafanartCopy(self, folder_new_path):
        if self.config.get('download_extrafanart_copy') == 'off':
            return
        extrafanart_folder = self.config.get('extrafanart_folder')
        if not extrafanart_folder or extrafanart_folder == 'extrafanart':
            return
        extrafanart_path = self.convert_path(os.path.join(folder_new_path, 'extrafanart'))
        extrafanart_copy_path = self.convert_path(os.path.join(folder_new_path, extrafanart_folder))
        if not os.path.exists(extrafanart_path) or os.path.exists(extrafanart_copy_path):
            return
        shutil.copytree(extrafanart_path, extrafanart_copy_path)
        filelist = os.listdir(extrafanart_copy_path)
        for each in filelist:
            file_new_name = each.replace('fanart', '')
            file_path = os.path.join(extrafanart_copy_path, each)
            file_new_path = os.path.join(extrafanart_copy_path, file_new_name)
            os.rename(file_path, file_new_path)
        self.addTextMain(" 🟢 ExtraFanart Copy done!")
        if self.config.get('keep_local_extrafanart') == 'off' and self.config.get('download_extrafanart') == 'off':
            shutil.rmtree(extrafanart_path)
            self.addTextMain(" 🟢 ExtraFanart del done!")


    # ======================================================================================打印NFO
    def PrintFiles(self, nfo_new_path, folder_new_path, thumb_new_name, poster_new_name, fanart_new_name, json_data):
        if os.path.exists(nfo_new_path) or self.config.get('download_nfo') == 'off':
            return True
        # 获取字段
        translate_language = self.config.get('translate_language')
        c_word = json_data['c_word']
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series, mosaic, definition = get_info(json_data)
        # 获取在媒体文件中显示的规则，不需要过滤Windows异常字符
        name_media = json_data['naming_media'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                         year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher).replace('mosaic', mosaic).replace('definition', definition).replace('cnword', c_word)
        # 字符转义，emby避免无法解析
        nfo_title = name_media.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        outline = outline.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        series = series.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        director = director.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        studio = studio.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        publisher = publisher.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        cover = cover.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        website = website.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        tag = tag.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
        tag = tag.split(',')    # str转list
        try:
            if not os.path.exists(folder_new_path):
                os.makedirs(folder_new_path)
            with open(nfo_new_path, "wt", encoding='UTF-8') as code:
                print('<?xml version="1.0" encoding="UTF-8" ?>', file=code)
                print("<movie>", file=code)
                # 输出番号
                print("  <num>" + number + "</num>", file=code)
                # 输出标题
                print("  <title>" + nfo_title + "</title>", file=code)
                # 输出简介
                if outline:
                    print("  <plot>" + outline + "</plot>", file=code)
                    print("  <outline>" + outline + "</outline>", file=code)
                # 输出合集、系列
                if series:
                    if self.config.get('series_as_set') == 1:
                        print("  <set>" + series + "</set>", file=code)
                    print("  <series>" + series + "</series>", file=code)
                # 输出发行日期
                if release:
                    if translate_language == 'zh_cn':
                        print("  <tagline>发行日期 " + release + "</tagline>", file=code)
                    else:
                        print("  <tagline>發行日期 " + release + "</tagline>", file=code)
                    print("  <premiered>" + release + "</premiered>", file=code)
                    print("  <releasedate>" + release + "</releasedate>", file=code)
                    print("  <release>" + release + "</release>", file=code)
                # 输出年代
                if str(year):
                    print("  <year>" + str(year) + "</year>", file=code)
                # 输出时长
                if str(runtime):
                    print("  <runtime>" + str(runtime).replace(" ", "") + "</runtime>", file=code)
                # 输出评分
                try:
                    if str(json_data['score']) and str(json_data['score']) != '' and float(
                            json_data['score']) != 0.0:
                        print("  <rating>" + str(json_data['score']) + "</rating>", file=code)
                except Exception as err:
                    print("Error in json_data score!" + str(err))
                # 输出导演
                if director:
                    print("  <director>" + director + "</director>", file=code)
                # 输出厂商
                if studio:
                    print("  <studio>" + studio + "</studio>", file=code)
                # 输出制作商
                    print("  <maker>" + studio + "</maker>", file=code)
                # 输出发行商
                if publisher:
                    print("  <maker>" + publisher + "</maker>", file=code)
                # 输出图片文件位置
                print("  <cover>" + cover + "</cover>", file=code)
                print("  <poster>" + poster_new_name + "</poster>", file=code)
                print("  <thumb>" + thumb_new_name + "</thumb>", file=code)
                print("  <fanart>" + fanart_new_name + "</fanart>", file=code)
                # 输出演员
                if actor_photo:
                    try:
                        for key, value in actor_photo.items():
                            if str(key):
                                key = key.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
                                print("  <actor>", file=code)
                                print("    <name>" + key + "</name>", file=code)
                                if value:
                                    value = value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
                                    print("    <thumb>" + value + "</thumb>", file=code)
                                print("  </actor>", file=code)
                    except Exception as ex:
                        self.addTextMain(' 🔴 Error when print actor to nfo\n   >>> ' + str(ex))
                else:
                    if not actor:
                        actor = self.config.get('actor_name')
                    if actor:
                        actor_list = str(actor).strip("[ ]").replace("'", '').split(',')  # 字符串转列表
                        actor_list = [actor.strip() for actor in actor_list]  # 去除空白
                        if actor_list:
                            for actor in actor_list:
                                actor = actor.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
                                print("  <actor>", file=code)
                                print("   <name>" + actor + "</name>", file=code)
                                print("  </actor>", file=code)
                print("  <label>", file=code)
                print("  </label>", file=code)
                # 输出 tag
                try:
                    for i in tag:
                        if i:
                            print("  <tag>" + i + "</tag>", file=code)
                except Exception as ex:
                    self.addTextMain('Error in tag: ' + str(ex))
                # 输出 genre
                try:
                    for i in tag:
                        if i:
                            print("  <genre>" + i + "</genre>", file=code)
                except Exception as ex:
                    self.addTextMain(' 🔴 Error when print genre to nfo\n   >>> ' + str(ex))
                print("  <website>" + website + "</website>", file=code)
                print("</movie>", file=code)
                self.addTextMain(" 🟢 Nfo done!")
        except Exception as ex:
            self.addTextMain(' 🔴 Nfo failed! \n   >>>  %s' % str(ex))

    # ======================================================================================thumb复制为fanart
    def copyRenameJpgToFanart(self, thumb_new_path, fanart_new_path):
        if self.config.get('download_fanart') == 'on':
            if os.path.exists(fanart_new_path):
                return True
            if os.path.exists(thumb_new_path):
                shutil.copy(thumb_new_path, fanart_new_path)
                self.addTextMain(" 🟢 Fanart done!")
                return True
            self.addTextMain(' 🔴 Failed to create fanart! the thumb is not exist!')
        return False

    # ======================================================================================移动视频、字幕
    def pasteFileToFolder(self, file_path, file_new_path):
        if self.config.get('soft_link') == 1:  # 如果使用软链接
            if file_path == file_new_path:  # 相同不需要创建
                self.addTextMain(" 🟢 Movie file is already in success folder! no need to movie it again!\n   >>> The current path is '%s'" % file_new_path)
            else:
                os.symlink(file_path, file_new_path)
                self.addTextMain(" 🟢 Symlink done! \n   >>> The symlink path is '%s' \n   >>> The real path is '%s'" % (file_new_path, file_path))
            return True 

        if self.config.get('success_file_move') == 0:   # 如果成功后不移动文件
            if file_path == file_new_path:          # 当路径相同，不移动
                self.addTextMain(" 🟢 Movie not moved! \n   >>> The path is '%s'" % file_new_path)
                return True
            try:    # 路径不同，就重命名
                os.rename(file_path, file_new_path)
                self.addTextMain(" 🟢 Movie renamed! \n   >>> The new name is '%s'" % file_new_path)
                return True
            except PermissionError:
                self.addTextMain(' 🔴 Failed to rename the movie! \n   >>> No permission! Please run as Administrator!')
            except Exception as ex:
                if file_path.upper() == file_new_path.upper():
                    return True
                self.addTextMain(' 🔴 Failed to rename the movie! \n   >>> %s' % str(ex))
            return False
        if file_path == file_new_path:          # 当路径相同，不移动

            self.addTextMain(" 🟢 Movie done! \n 🙉 [Movie] %s" % file_new_path)
            return True
        try:    # 路径不同，就移动文件
            shutil.move(file_path, file_new_path)
            self.addTextMain(" 🟢 Movie done! \n 🙉 [Movie] %s" % file_new_path)
            return True
        except PermissionError:
            self.addTextMain(' 🔴 Failed to move movie file to success folder! \n   >>> No permission! Please run as Administrator!')
        except Exception as ex:
            self.addTextMain(' 🔴 Failed to move movie file  to success folder! \n   >>> %s' % str(ex))
        return False

    # ======================================================================================裁剪封面
    def cutImage(self, thumb_path, poster_path, image_cut):
        if not os.path.exists(thumb_path):
            self.addTextMain(" 🟠 Poster can't cut from thumb, beacuse thumb.jpg is not exist!")
            return False
        if os.path.exists(poster_path):
            os.remove(poster_path)
        # 中间裁剪
        if image_cut == 'center':
            if self.image_cut(thumb_path, poster_path):
                return True
        # 右边裁剪
        else:
            try:
                img = Image.open(thumb_path)
                img1 = img.convert('RGB')
                w = img1.width
                h = img1.height
                if w == 800:
                    if h == 439:
                        img2 = img1.crop((420, 0, w, h))
                    elif h == 499:
                        img2 = img1.crop((437, 0, w, h))
                    else:
                        img2 = img1.crop((421, 0, w, h))
                elif w == 840:
                    if h == 472:
                        img2 = img1.crop((473, 0, 788, h))
                    else:
                        img2 = img1.crop((w / 1.9, 0, w, h))
                else:
                    img2 = img1.crop((w / 1.9, 0, w, h))
                img2.save(poster_path)
                self.addTextMain(" 🟢 Poster done!")
                return True
            except Exception as ex:
                self.addTextMain(' 🟠 Poster cut failed!\n   >>> ' + str(ex))
                return False


    def fix_size(self, path, naming_rule):
        try:
            poster_path = os.path.join(path, (naming_rule + '-poster.jpg'))
            if os.path.exists(poster_path):
                pic = Image.open(poster_path)
                (width, height) = pic.size
                if not 2 / 3 - 0.05 <= width / height <= 2 / 3 + 0.05:  # 仅处理会过度拉伸的图片
                    fixed_pic = pic.resize((int(width), int(3 / 2 * width)))  # 拉伸图片
                    fixed_pic = fixed_pic.filter(ImageFilter.GaussianBlur(radius=50))  # 高斯模糊
                    fixed_pic.paste(pic, (0, int((3 / 2 * width - height) / 2)))  # 粘贴原图
                    fixed_pic.save(poster_path)
        except Exception as ex:
            self.addTextMain('Error in fix_size: ' + str(ex))

    # ======================================================================================添加水印
    def add_mark(self, poster_new_path, thumb_new_path, json_data, poster_old=False, thumb_old=False):
        c_word = json_data['c_word']
        leak = json_data['leak']
        mosaic = json_data['mosaic']
        mark_type = self.config.get('mark_type')
        mark_type_list = mark_type.upper().split(',')
        mark_list = []
        for mark_type in mark_type_list:
            if mark_type.lower() == 'sub' and c_word:
                mark_list.append('字幕')
            elif mark_type.lower() == 'leak' and leak:
                mark_list.append('流出')
            elif mark_type.lower() == 'uncensored' and (mosaic == '無碼' or mosaic == '无码'):
                mark_list.append('无码')
        if mark_list:
            mark_show_type = str(mark_list).strip(" ['']").replace("'", "")
            if self.config.get('thumb_mark') == 1 and self.config.get('download_thumb') == 'on' and os.path.exists(thumb_new_path) and not thumb_old:
                self.add_mark_thread(thumb_new_path, mark_list)
                self.addTextMain(' 🟢 Thumb add watermark: %s!' % mark_show_type)
            if self.config.get('poster_mark') == 1 and self.config.get('download_poster') == 'on' and os.path.exists(poster_new_path) and not poster_old:
                self.add_mark_thread(poster_new_path, mark_list)
                self.addTextMain(' 🟢 Poster add watermark: %s!' % mark_show_type)

    def add_mark_thread(self, pic_path, mark_list):
        mark_pos = self.config.get('mark_pos')
        mark_size = self.config.get('mark_size')
        size = 14 - mark_size  # 获取水印自定义大小的值
        img_pic = Image.open(pic_path)
        count = 0  # 获取自定义位置, 取余配合pos达到顺时针添加的效果
        if mark_pos == 'top_left':
            count = 0
        elif mark_pos == 'top_right':
            count = 1
        elif mark_pos == 'bottom_right':
            count = 2
        elif mark_pos == 'bottom_left':
            count = 3
        for mark_type in mark_list:
            if mark_type == '字幕':
                self.add_to_pic(pic_path, img_pic, size, count, 1)  # 添加
                count = (count + 1) % 4
            elif mark_type == '流出':
                self.add_to_pic(pic_path, img_pic, size, count, 2)
                count = (count + 1) % 4
            elif mark_type == '无码':
                self.add_to_pic(pic_path, img_pic, size, count, 3)
        img_pic.close()

    def add_to_pic(self, pic_path, img_pic, size, count, mode):
        mark_pic_path = ''
        if mode == 1:
            mark_pic_path = self.resource_path('Img/SUB.png')
        elif mode == 2:
            mark_pic_path = self.resource_path('Img/LEAK.png')
        elif mode == 3:
            mark_pic_path = self.resource_path('Img/UNCENSORED.png')
        img_subt = Image.open(mark_pic_path)
        scroll_high = int(img_pic.height / size)
        scroll_wide = int(scroll_high * img_subt.width / img_subt.height)
        img_subt = img_subt.resize((scroll_wide, scroll_high), Image.ANTIALIAS)
        r, g, b, a = img_subt.split()  # 获取颜色通道, 保持png的透明性
        # 封面四个角的位置
        pos = [
            {'x': 0, 'y': 0},
            {'x': img_pic.width - scroll_wide, 'y': 0},
            {'x': img_pic.width - scroll_wide, 'y': img_pic.height - scroll_high},
            {'x': 0, 'y': img_pic.height - scroll_high},
        ]
        img_pic.paste(img_subt, (pos[count]['x'], pos[count]['y']), mask=a)
        img_pic = img_pic.convert('RGB')
        img_pic.save(pic_path, quality=95)


    # ======================================================================================更新进度条
    def set_processbar(self, value):
        self.Ui.progressBar_avdc.setProperty("value", value)

    # ======================================================================================显示jsondata结果
    def showDataResult(self, json_data):
        self.addTextMain(' 🌐 [website] %s' % json_data['req_web'].strip('-> '))
        if json_data['error_type'] or json_data['title'] == '':
            self.addTextMain(' 🟠 Data failed!')
            self.showDebugInfo(json_data)    # 调试模式打开时显示详细日志
            return False
        else:

            self.addTextMain(' 🟢 Data done!')
            return True

    # ======================================================================================输出调试信息
    def showDebugInfo(self, json_data):
        if self.config.get('switch') == 1:    # 调试模式打开时显示详细日志
            try:
                self.addTextMain('   ****** Debug Info ******')
                self.addTextMain(json_data['log_info'].strip('\n'))
            except Exception as ex:
                self.addTextMain(' 🔴 Error in showDebugInfo: ' + str(ex))

    # ======================================================================================输出 Movie 信息
    def showMovieInfo(self, json_data):
        if self.config.get('switch') == 0:    # 调试模式打开时显示详细日志
            return
        try:
            for key, value in json_data.items():
                if value == '' or key == 'image_download' or key == 'image_cut' or key == 'search_url' or key == 'log_info' or key == 'error_type' or key == 'error_info' or key == 'naming_media' or key == 'naming_file' or key == 'folder_name' or key == 'extrafanart' or key == 'actor_photo' or key == 'source' or key == 'cover' or key == 'number' or key == 'cover_small' or key == 'req_web':
                    continue

                if len(str(value)) == 0:
                    continue
                if str(value).lower() == 'unknown':
                    continue
                if key == 'outline' and len(value) > 100:
                    value = value[:98] + '......（略）'
                if key == 'destroyed':
                    value = value[1:]
                self.addTextMain('    ' + "%-10s" % key + ': ' + str(value))
        except Exception as ex:
            self.addTextMain(' 🔴 Error in showMovieInfo: ' + str(ex))

    # ======================================================================================获取输出文件夹名称
    def getFolderPath(self, file_path, success_folder, json_data):
        # 不移动文件夹开并且软连接关时，使用原来文件夹
        if self.config.get('success_file_move') == 0 and self.config.get('soft_link') == 0:
            folder_path = os.path.split(file_path)[0]
            return folder_path

        # 获取文件信息
        c_word = json_data['c_word']
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series, mosaic, definition = get_info(
            json_data)

        # 去除Windows特殊字符
        title = re.sub(r'[\\/:*?"<>|\r\n]+', '', title)
        actor = re.sub(r'[\\/:*?"<>|\r\n]+', '', actor)
        cnword = c_word

        # 是否勾选目录名添加字幕标识
        if self.config.get('folder_cnword') != 1:
            c_word = ''
        
        # 特殊情况处理
        if not series:
            series = '未知系列'
        if not actor:
            actor = self.config.get('actor_name')
        if not release:
            release = '0000-00-00'
        if not year:
            year = '0000'

        # 判断演员名长度
        actor_name_max = int(self.config.get('actor_name_max'))
        actor_name_more = self.config.get('actor_name_more')
        acotr_list = actor.split(',')
        if len(acotr_list) > actor_name_max:  # 演员多于设置值时
            cut_index = actor_name_max - len(acotr_list)
            self.addTextMain(' 🟠 当前演员数量：%s，最大显示数量：%s，目录命名时将去除后%s个演员!' % (len(acotr_list), actor_name_max, abs(cut_index)))
            actor = ''
            for i in range(actor_name_max):
                actor = actor + acotr_list[i] + ','
            actor = actor.strip(',') + actor_name_more

        # 获取文件夹名称
        folder_name = json_data['folder_name'].replace('\\', '/')
        folder_new_name = folder_name.replace('title', title).replace('studio', studio).replace('year', year).replace('runtime', runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number + c_word).replace(
            'series', series).replace('publisher', publisher).replace('mosaic', mosaic).replace('definition', definition).replace('cnword', cnword)
        folder_new_name = folder_new_name.replace('--', '-').strip('-').strip('- .')
        folder_new_name = re.sub(r'[\\:*?"<>|\r\n]+', '', folder_new_name).strip('/')

        # 判断文件夹名长度，超出长度时，截短标题名
        folder_name_max = int(self.config.get('folder_name_max'))
        if len(folder_new_name) > folder_name_max:
            cut_index = folder_name_max - len(folder_new_name)
            self.addTextMain(' 🟠 当前目录名长度：%s，最大允许长度：%s，目录命名时将去除标题后%s个字符!' % (len(folder_new_name), folder_name_max, abs(cut_index)))
            folder_new_name = folder_new_name.replace(title, title[0:cut_index])

        # 生成文件夹名
        folder_new_path = os.path.join(success_folder, folder_new_name)
        folder_new_path = self.convert_path(folder_new_path)
        return folder_new_path


    # ======================================================================================获取输出的本地文件名
    def getNamingRule(self, file_path, json_data):
        # 如果成功后不重命名，则返回原来名字
        if self.config.get('success_file_rename') == 0:
            file_name = os.path.split(file_path)[1]
            file_name = os.path.splitext(file_name)[0]
            return file_name
        
        # 获取文件信息
        c_word = json_data['c_word']
        leak = json_data['leak']
        cd_part = json_data['cd_part']
        destroyed = json_data['destroyed']
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series, mosaic, definition = get_info(json_data)

        # 去除异常字符
        title = re.sub(r'[\\/:*?"<>|\r\n]+', '', title)
        actor = re.sub(r'[\\/:*?"<>|\r\n]+', '', actor)

        # 判断是否勾选文件名添加字幕标识
        cnword = c_word
        if self.config.get('file_cnword') != 1:
            c_word = ''
        number = number + leak + cd_part + c_word

        # 处理异常情况
        if not series:
            series = '未知系列'
        if not actor:
            actor = self.config.get('actor_name')
        if not release:
            release = '0000-00-00'
        if not year:
            year = '0000'

        # 判断演员名数量
        actor_name_max = int(self.config.get('actor_name_max'))
        actor_name_more = self.config.get('actor_name_more')
        acotr_list = actor.split(',')
        if len(acotr_list) > actor_name_max:  # 演员多于设置值时
            cut_index = actor_name_max - len(acotr_list)
            self.addTextMain(' 🟠 当前演员数量：%s，最大显示数量：%s，文件命名时将去除后%s个演员!' % (len(acotr_list), actor_name_max, abs(cut_index)))
            actor = ''
            for i in range(actor_name_max):
                actor = actor + acotr_list[i] + ','
            actor = actor.strip(',') + actor_name_more

        # 获取文件名
        file_name = json_data['naming_file'].replace('title', title).replace('studio', studio).replace('year', year).replace(
            'runtime', runtime).replace('director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher).replace('mosaic', mosaic).replace('definition', definition).replace('cnword', cnword)
        file_name = file_name.replace('//', '/').replace('--', '-').strip('-') + destroyed # 加马赛克破坏版标识
        file_name = re.sub(r'[\\/:*?"<>|\r\n]+', '', file_name) # 用在保存文件时的名字，需要过滤window异常字符

        # 判断文件名长度，超出长度时，截短标题名
        file_name_max = int(self.config.get('file_name_max'))
        if len(file_name) > file_name_max:
            cut_index = file_name_max - len(file_name)
            self.addTextMain(' 🟠 当前文件名长度%s，最大允许长度：%s，文件命名时将去除标题后%s个字符!' % (len(file_name), file_name_max, abs(cut_index)))
            file_name = file_name.replace(title, title[0:cut_index])
        if not file_name:   # 文件名不能为空
            file_name = number

        return file_name

    # ======================================================================================生成各种输出文件和文件夹的名字
    def getOutPutName(self, file_path, success_folder, json_data, file_ex):
        # =====================================================================================更新输出文件夹名
        folder_new_path = self.getFolderPath(file_path, success_folder, json_data)
        # =====================================================================================更新实体文件命名规则
        naming_rule = self.getNamingRule(file_path, json_data)
        # =====================================================================================生成文件和图片新路径路径
        file_new_name = naming_rule + file_ex.lower()
        nfo_new_name = naming_rule + '.nfo'
        # 如果图片命名规则不加文件名并且视频目录不为空
        if self.config.get('pic_name') == 1 and json_data['folder_name'].replace(' ', ''):
            poster_new_name = 'poster.jpg'
            thumb_new_name = 'thumb.jpg'
            fanart_new_name = 'fanart.jpg'
        else:
            poster_new_name = naming_rule + '-poster.jpg'
            thumb_new_name = naming_rule + '-thumb.jpg'
            fanart_new_name = naming_rule + '-fanart.jpg'
        file_new_path = self.convert_path(os.path.join(folder_new_path, file_new_name))
        nfo_new_path = self.convert_path(os.path.join(folder_new_path, nfo_new_name))
        poster_new_path = self.convert_path(os.path.join(folder_new_path, poster_new_name))
        thumb_new_path = self.convert_path(os.path.join(folder_new_path, thumb_new_name))
        fanart_new_path = self.convert_path(os.path.join(folder_new_path, fanart_new_name))
        return folder_new_path, file_new_path, nfo_new_path, poster_new_path, thumb_new_path, fanart_new_path, naming_rule, file_new_name, nfo_new_name, poster_new_name, thumb_new_name, fanart_new_name

    # ======================================================================================获取刮削网站
    def getWebSite(self, file_mode):
        website_mode = 1
        if file_mode == 'default_folder':                                       # 刮削默认视频目录的文件
            website_mode = self.Ui.comboBox_website_all.currentIndex() + 1
        elif file_mode == 'single_file':                                        # 刮削单文件（工具页面）
            website_mode = self.Ui.comboBox_website.currentIndex() + 1
        return website_mode

    # ======================================================================================从指定网站获取json_data
    def getJsonData(self, file_mode, number, appoint_url, translate_language, json_data):
        website_mode = self.getWebSite(file_mode)
        if website_mode == 4:  # javdb模式，加上延时，避免被封
            ss = random.randint(1, 4)
            if ss:
                self.addTextMain(' ⏱ Please Wait %s Seconds！' % str(ss))
            time.sleep(ss)
        json_data = getDataFromJSON(number, website_mode, appoint_url, translate_language, json_data)
        return json_data

    # ======================================================================================json_data添加到主界面
    def add_label_info(self, json_data):
        self.set_main_info.emit(json_data)


    def add_label_info_Thread(self, json_data):
        try:
            if not json_data:
                json_data = {
                    'number': '',
                    'actor': '',
                    'source': '',
                    'website': '',
                    'title': '',
                    'outline': '',
                    'tag': '',
                    'release': '',
                    'year': '',
                    'runtime': '',
                    'director': '',
                    'series': '',
                    'studio': '',
                    'publisher': '',
                    'poster_path': '',
                    'thumb_path': '',
                    'fanart_path': '',
                    'img_path': '',
                    'c_word': '',
                    'leak': '',
                    'cd_part': '',
                    'mosaic': '',
                    'destroyed': '',
                    'actor_href': '',
                }
            self.Ui.label_number.setText(str(json_data['number']))
            self.laberl_number_url = json_data['website']
            self.Ui.label_actor.setText(str(json_data['actor']))
            self.laberl_actor_url = json_data['actor_href']
            if json_data.get('source'):
                self.Ui.label_source.setText('数据：' + json_data['source'].replace('.main_us','').replace('.main',''))
            else:
                self.Ui.label_source.setText('')
            self.Ui.label_title.setText(str(json_data['title']))
            self.Ui.label_outline.setText(str(json_data['outline']))
            self.Ui.label_tag.setText(str(json_data['tag']).strip(" [',']").replace('\'', ''))
            self.Ui.label_release.setText(str(json_data['release']))
            if json_data['runtime']:
                self.Ui.label_runtime.setText(str(json_data['runtime']) + ' 分钟')
            else:
                self.Ui.label_runtime.setText('')
            self.Ui.label_director.setText(str(json_data['director']))
            self.Ui.label_series.setText(str(json_data['series']))
            self.Ui.label_studio.setText(str(json_data['studio']))
            self.Ui.label_publish.setText(str(json_data['publisher']))
            # 生成img_path，用来裁剪使用
            if os.path.isfile(json_data['fanart_path']):
                json_data['img_path'] = json_data['fanart_path']
            else:
                json_data['img_path'] = json_data['thumb_path']
            # 主界面显示封面和缩略图
            if self.Ui.checkBox_cover.isChecked():
                poster_path = json_data['poster_path']
                thumb_path = json_data['thumb_path']
                fanart_path = json_data['fanart_path']
                if not os.path.exists(poster_path):
                    poster_path = self.default_poster
                if not os.path.exists(thumb_path):
                    if os.path.exists(fanart_path):
                        thumb_path = fanart_path
                    else:
                        thumb_path = self.default_thumb
                pix = QPixmap(poster_path)
                self.Ui.label_poster.setScaledContents(True)
                self.Ui.label_poster.setPixmap(pix)  # 添加封面图
                pix = QPixmap(thumb_path)
                self.Ui.label_thumb.setScaledContents(True)
                self.Ui.label_thumb.setPixmap(pix)  # 添加缩略图
        except Exception as e:
            print('add_label_info_Thread: %s'% e)

        self.json_data = json_data
        self.img_path = json_data['img_path']

    # ======================================================================================检查更新
    def updateCheck(self):
        if self.Ui.radioButton_update_on.isChecked():
            self.addTextMain('The current version is AVDCx %s' % self.localversion)                 
            try:
                result, html_content = get_html('https://api.github.com/repos/Hermit10/AVDCx/releases/latest')
                if not result:
                    self.addTextMain('UpdateCheck Failed! reason: ' + html_content)
                    self.addTextMain("================================================================================")
                    return False
                data = json.loads(html_content)
            except Exception as ex:
                self.addTextMain('UpdateCheck Failed! Error info: ' + str(ex))
                self.addTextMain("================================================================================")
                return False
            if not data.get('tag_name'):
                try:
                    result, html_content = get_html('https://api.github.com/repos/Hermit10/temp/releases/latest')
                    if not result:
                        self.addTextMain('UpdateCheck Failed! reason: ' + html_content)
                        self.addTextMain("================================================================================")
                        return False
                    data = json.loads(html_content)
                except Exception as ex:
                    self.addTextMain('UpdateCheck Failed! Error info: ' + str(ex))
                    self.addTextMain("================================================================================")
                    return False
            if data.get('tag_name'):
                if 'AVDCx' in data.get('url'):
                    self.github_project_url = 'https://github.com/Hermit10/AVDCx/'
                remote = int(data["tag_name"].replace(".",""))
                localversion = int(self.localversion.replace(".", ""))
                new_content = str(data["body"].replace(".","")).replace('====', '').replace('===', '').replace('\r\n', '\n   ')
                if localversion < remote:
                    self.Ui.label_show_version.setText('🍉 New! update ' + str(data["tag_name"]))
                    self.addTextMain('* New update AVDCx ' + str(data["tag_name"]) + ' is Available! *')
                    self.addTextMain("" + ("").center(80, '='))
                    self.addTextMain('   更新内容:' + new_content)
                    self.addTextMain('   \n   下载地址: https://github.com/Hermit10/AVDCx/releases')
                else:
                    self.addTextMain('You are using the latest version!')
                self.addTextMain("================================================================================")
            else:
                self.addTextMain('UpdateCheck Failed!')
                self.addTextMain("================================================================================")
        return True

    def updateCheckStart(self):
        try:
            t = threading.Thread(target=self.updateCheck)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('update check error : ' + str(ex))     

    def show_netstatus(self, proxy_info):
        self.addNetTextMain(time.strftime('%Y-%m-%d %H:%M:%S').center(80, '='))
        proxy_type = ''
        retry_count = 0
        proxy = ''
        timeout = 0
        try:
            proxy_type, proxy, timeout, retry_count = proxy_info
        except Exception as ex:
            print('get config failed when check net, error info: ! ' + str(ex))
        if proxy == '' or proxy_type == '' or proxy_type == 'no':
            self.addNetTextMain(' 当前网络状态：❌ 未启用代理\n   类型： ' + str(proxy_type) + '    地址：' + str(proxy) + '    超时时间：' + str(timeout) + '    重试次数：' + str(retry_count))
        else:
            self.addNetTextMain(' 当前网络状态：✅ 已启用代理\n   类型： ' + proxy_type + '    地址：' + proxy + '    超时时间：' + str(timeout) + '    重试次数：' + str(retry_count))
        self.addNetTextMain('='*80)

    def netResult(self):
        # 显示代理信息
        self.addNetTextMain('\n⛑ 开始检测网络....')
        self.show_netstatus(self.current_proxy)
        # 检测网络连通性
        self.addNetTextMain(' 检测网络连通性...')
        net_info = [['github', 'https://github.com' , ''], ['iqqtv', 'https://iqqtv.cloud' , ''], ['javbus', 'https://www.javbus.com' , ''], ['javdb', 'https://javdb.com', ''], ['jav321', 'https://www.jav321.com' , ''], ['dmm', 'https://www.dmm.co.jp' , ''], ['avsox', 'https://avsox.website' , ''], ['xcity', 'https://xcity.jp' , ''], ['mgstage', 'https://www.mgstage.com', ''], ['fc2', 'https://adult.contents.fc2.com', ''], ['fc2hub', 'https://fc2hub.com', ''], ['airav', 'https://www.airav.wiki' , ''], ['javlibrary', 'http://www.javlibrary.com' , '']]
        for each in net_info:
            proxy_info = get_proxy_info()
            proxies = proxy_info.get('proxies')
            timeout = proxy_info.get('timeout')
            if each[0] == 'javdb':
                cookies = proxy_info.get('cookie')
                scraper = cloudscraper.create_scraper(
                    browser={
                        'browser': 'firefox',
                        'platform': 'windows',
                        'mobile': False
                    }
                )  # returns a CloudScraper instance
                try:
                    html_search = scraper.get(each[1], cookies=cookies, proxies=proxies, timeout=timeout).text
                except Exception as ex:
                    each[2] = '❌ 连接失败 请检查网络或代理设置！ ' + str(ex)
                else:
                    if "The owner of this website has banned your access based on your browser's behaving" in html_search:
                        each[2] = '❌ 连接失败 基于你的异常行为，管理员禁止了你的访问！'
                    else:
                        each[2] = '✅ 连接正常'
            else:
                try:
                    result, html_content = get_html(each[1])
                    if not result:
                        each[2] = '❌ 连接失败 请检查网络或代理设置！ ' + str(html_content)
                    else:
                        if each[0] == 'dmm':
                            if re.findall('このページはお住まいの地域からご利用になれません', html_content):
                                each[2] = '❌ 连接失败 地域限制, 请使用日本节点访问！'
                            else:
                                each[2] = '✅ 连接正常'
                        elif each[0] == 'mgstage':
                            if not html_content.strip():
                                each[2] = '❌ 连接失败 请检查网络或代理设置！'
                            else:
                                each[2] = '✅ 连接正常'
                        else:
                            each[2] = '✅ 连接正常'
                except Exception as ex:
                    each[2] = '测试连接时出现异常！信息:' + str(ex)
            self.addNetTextMain('   ' + each[0].ljust(12) + each[2])
        self.addNetTextMain("================================================================================\n")
        self.Ui.pushButton_check_net.setEnabled(True)
        self.Ui.pushButton_check_net.setText('开始检测')
        self.Ui.pushButton_check_net.setStyleSheet('QPushButton#pushButton_check_net{background-color:#0066CC}QPushButton:hover#pushButton_check_net{background-color:#4C6EFF}QPushButton:pressed#pushButton_check_net{#4C6EE0}')
    # ======================================================================================网络检查
    def netCheck(self):
        self.Ui.pushButton_check_net.setEnabled(False)
        self.Ui.pushButton_check_net.setText('正在检测')
        self.Ui.pushButton_check_net.setStyleSheet('QPushButton#pushButton_check_net{color:#999999;background-color:#F0F0F0}')
        try:
            t = threading.Thread(target=self.netResult)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addNetTextMain('Error in netCheck: ' + str(ex))        


    # ======================================================================================显示正在刮削的文件路径
    def showFilePath(self, file_path):
        if len(file_path) > 55:
            show_file_path = file_path[-50:]
            show_file_path = '..' + show_file_path[show_file_path.find('/'):]
            if len(show_file_path) < 25:
                show_file_path = '..' + file_path[-40:]
        else:
            show_file_path = file_path
        return show_file_path

    # ======================================================================================新建失败输出文件夹
    def creatFailedFolder(self, failed_folder):
        if self.config.get('failed_file_move') == 1 and not os.path.exists(failed_folder):
            try:
                os.makedirs(failed_folder)
            except Exception as ex:
                self.addTextMain(' 🔴 Error: Failed to create the failed folder\n   >>> ' + str(ex))

    # ======================================================================================删除空目录
    def CEF(self, path, file_mode):
        del_empty_folder = self.config.get('del_empty_folder')
        if del_empty_folder == 0 or file_mode == 'single_file':
            return
        self.set_label_file_path.emit('🗑 正在清理空文件夹，请等待...')
        self.addTextMain(' ⌛ Cleaning empty folders...')
        if os.path.exists(path):
            all_info = os.walk(path, topdown=False)
            for root, dirs, files in all_info:
                hidden_file = os.path.join(root, '.DS_Store')
                if os.path.exists(hidden_file):
                    os.remove(hidden_file)  # 删除隐藏文件
                if not os.listdir(root):
                    try:
                        os.rmdir(root)
                        self.addTextMain(' 🗑 Delete empty folder: ' + self.convert_path(root))
                    except Exception as e:
                        self.addTextMain(' 🔴 Delete empty folder error: %s' % e)

        self.addTextMain(' 🟢 Clean done!')
        self.addTextMain('='*80)

    def addTreeChild(self, result, filename):
        if result == 'succ':
            node = QTreeWidgetItem(self.item_succ)
            node.setText(0, filename)
            self.item_succ.addChild(node)
        else:
            node = QTreeWidgetItem(self.item_fail)
            node.setText(0, filename)
            self.item_fail.addChild(node)


    def showListName(self, filename, result, json_data, real_number=''):
        # 添加树状节点
        self.set_tree_child.emit(result, filename)

        # 解析json_data，以在主界面左侧显示
        if not json_data.get('number'):
            json_data['number'] = real_number
        if not json_data.get('actor'):
            json_data['actor'] = ''
        if not json_data.get('title'):
            json_data['title'] = json_data['error_info']
        if not json_data.get('outline'):
            json_data['outline'] = ''
        if not json_data.get('tag'):
            json_data['tag'] = ''
        if not json_data.get('release'):
            json_data['release'] = ''
        if not json_data.get('runtime'):
            json_data['runtime'] = ''
        if not json_data.get('director'):
            json_data['director'] = ''
        if not json_data.get('series'):
            json_data['series'] = ''
        if not json_data.get('publisher'):
            json_data['publisher'] = ''
        if not json_data.get('studio'):
            json_data['studio'] = ''
        if not json_data.get('poster_path'):
            json_data['poster_path'] = ''
        if not json_data.get('thumb_path'):
            json_data['thumb_path'] = ''
        if not json_data.get('fanart_path'):
            json_data['fanart_path'] = ''
        if not json_data.get('website'):
            json_data['website'] = ''
        if not json_data.get('source'):
            json_data['source'] = ''
        if not json_data.get('c_word'):
            json_data['c_word'] = ''
        if not json_data.get('cd_part'):
            json_data['cd_part'] = ''
        if not json_data.get('leak'):
            json_data['leak'] = ''
        if not json_data.get('mosaic'):
            json_data['mosaic'] = ''
        if not json_data.get('actor_href'):
            json_data['actor_href'] = ''
        self.add_label_info(json_data)
        self.json_array[filename] = json_data


    # =====================================================================================获取视频文件列表（区分文件夹刮削或单文件刮削）
    def getMovieList(self, file_mode, movie_path, escape_folder):
        movie_list = []
        appoint_number = ''
        appoint_url = ''
        movie_type = self.config.get('media_type').lower()
        if file_mode == 'default_folder':                                       # 刮削默认视频目录的文件
            self.addTextMain(' 🖥 Movie path: ' + movie_path)
            self.addTextMain(' 🔎 Searching all videos...')
            self.set_label_file_path.emit('正在遍历待刮削视频目录中的所有视频，请等待...\n %s' % movie_path)
            movie_list = movie_lists(escape_folder, movie_type, movie_path)     # 获取所有需要刮削的影片列表
            count_all = len(movie_list)
            self.addTextMain(' 📺 Find ' + str(count_all) + ' movies')

        elif file_mode == 'single_file':                                        # 刮削单文件（工具页面）
            file_path = self.single_file_path
            appoint_url = self.Ui.lineEdit_appoint_url.text()
            appoint_number = self.Ui.lineEdit_movie_number.text()
            self.addTextMain(' 🖥 File path: ' + file_path)
            if appoint_url:
                self.addTextMain(' 🌐 File url: ' + appoint_url)
            if appoint_number:
                self.addTextMain(' 🚘 File number: ' + appoint_number)
            movie_list.append(file_path)                                         # 把文件路径添加到movie_list
            count_all = 1
        return movie_list, count_all, appoint_number, appoint_url

    # =====================================================================================获取视频路径设置
    def getPath(self, movie_path, path):
        if ':' not in path and not re.search('^/', path):     # 如果没有:并且首字母没有/，这样的目录视为包含在媒体目录下，需要拼接
            path = os.path.join(movie_path, path).replace('\\', '/')
        elif re.search('^/[^/]', path):                       # 首字母是/时(不是//)，需要判断Windows路径
            if ':' in movie_path or '//' in movie_path:       # windows场景时，目录视为包含在媒体目录下
                path = path.strip('/')
                path = os.path.join(movie_path, path).replace('\\', '/')
        return path

    # =====================================================================================获取视频路径设置
    def getMoviePathSetting(self):
        movie_path = self.config.get('media_path').replace('\\', '/')                       # 用户设置的扫描媒体路径
        if movie_path == '':

            movie_path = self.main_path.replace('\\', '/')
        success_folder = self.config.get('success_output_folder').replace('\\', '/')        # 用户设置的成功输出目录
        failed_folder = self.config.get('failed_output_folder').replace('\\', '/')          # 用户设置的失败输出目录
        escape_folder_list = self.config.get('folders').replace('\\', '/').replace('，', ',').split(',')     # 用户设置的排除目录
        extrafanart_folder = self.config.get('extrafanart_folder').replace('\\', '/') # 用户设置的剧照目录
        escape_folder_new_list = []

        success_folder = self.getPath(movie_path, success_folder)
        failed_folder = self.getPath(movie_path, failed_folder)
        extrafanart_folder = self.getPath(movie_path, extrafanart_folder)

        for es in escape_folder_list:   # 排除目录可以多个，以，,分割
            es = es.strip(' ')
            if es:
                es = self.getPath(movie_path, es)
                if es[-1] != '/':   # 路径尾部添加“/”，方便后面move_list查找时匹配路径
                    es += '/'
                escape_folder_new_list.append(es)
        escape_folder = str(escape_folder_new_list).strip('[]').replace("'", '').replace('"', '').replace(', ', ',')   # 重新转换为str

        return movie_path, success_folder, failed_folder, escape_folder, extrafanart_folder

    # =====================================================================================获取文件的相关信息
    def getFileInfo(self, file_path, appoint_number=''):
        try:
            file_path = file_path.replace('\\', '/')
            translate_language = self.config.get('translate_language')
            json_data = {}
            json_data['version'] = self.localversion
            c_word = ''
            cd_part = ''
            leak = ''
            destroyed = ''
            mosaic = ''
            movie_number = ''
            sub_list = []
            # 获取文件名
            folder_path, file_full_name = os.path.split(file_path)  # 获取去掉文件名的路径、完整文件名（含扩展名）
            file_name, file_ex = os.path.splitext(file_full_name)  # 获取文件名（不含扩展名）、扩展名(含有.)
            nfo_old_name = file_name + '.nfo'
            nfo_old_path = os.path.join(folder_path, nfo_old_name)
            # 获取番号
            if appoint_number:      # 如果指定了番号，则使用指定番号
                movie_number = appoint_number
            else:
                escape_string = self.config.get('string')
                movie_number = getNumber(file_path, escape_string)
            # 判断是否流出
            if '流出' in file_name:
                leak = '-流出'
            # 判断是否分集及分集序号
            file_name1 = file_name.lower().replace('_', '-').replace('.', '-') + '.'    # .作为结尾
            file_name1 = file_name1.replace('-part', '-cd').replace('-a.', '-cd1').replace('-b.', '-cd2').replace('-d.', '-cd4').replace('-e.', '-cd5').replace('-f.', '-cd6').replace('-g.', '-cd7').replace('-hd1.', '-cd1').replace('-hd2.', '-cd2').replace('-hd3.', '-cd3').replace('-hd4.', '-cd4').replace('-hd5.', '-cd5')
            if 'cd' in file_name1:
                part_list = re.search('[-_]cd\d+', file_name1)
                if part_list:
                    cd_part = part_list[0].replace('_', '-')
            else:
                part_list = re.search('[-_]\d{1}\.', file_name1)
                if part_list:
                    cd_part = '-cd' + str(re.search('\d', part_list[0])[0])
            # 判断分集命名规则是否大写
            if self.config.get('cd_name') == 1:
                cd_part = cd_part.upper()

            cnword_list = self.config.get('cnword_char').replace('，', ',').split(',')
            cnword_style = str(self.config.get('cnword_style'))
            # 查找本地字幕文件
            sub_type_list = self.config.get('sub_type').split('|')   # 本地字幕后缀
            for sub in sub_type_list:    # 查找本地字幕, 可能多个
                if os.path.exists(os.path.join(folder_path, (file_name + sub))):
                    sub_list.append(sub)
                    c_word = cnword_style   # 中文字幕影片后缀

            # 判断路径名是否有中文字幕字符
            if not c_word:
                file_temp_path = file_path.upper().replace('CD', '').replace('CARIB', '') # 去掉cd/carib，避免-c误判
                for each in cnword_list:
                    if each.upper() in file_temp_path:
                        if '無字幕' not in file_path and '无字幕' not in file_path:
                            c_word = cnword_style   # 中文字幕影片后缀
                            break

            # 判断nfo中是否有中文字幕字样
            if not c_word and os.path.exists(nfo_old_path):
                try:
                    with open(nfo_old_path, 'r', encoding='utf-8') as f:
                        nfo_content = f.read()
                    if '<genre>中文字幕</genre>' in nfo_content:
                        c_word = cnword_style   # 中文字幕影片后缀
                except:
                    pass

            # 判断文件名是否包含待命名的中文字幕样式
            if not c_word and cnword_style:
                file_temp_name = str(movie_number) + leak + cd_part + cnword_style
                if file_temp_name.upper() in file_temp_path:
                    c_word = cnword_style

            # 判断是否是马赛克破坏版
            if 'uncensored' in file_path.lower() or '无码破解' in file_path or '無碼破解' in file_path or '克破' in file_path:
                destroyed = '.马赛克破坏版'
                if translate_language != 'zh_cn':
                    destroyed = '.馬賽克破壞版'

            # 判断是否无码
            if is_uncensored(movie_number):
                mosaic == '无码'

            file_show_name = str(movie_number) + cd_part + c_word + destroyed
            file_show_path = self.showFilePath(file_path)
            json_data['c_word'] = c_word
            json_data['cd_part'] = cd_part
            json_data['leak'] = leak
            json_data['destroyed'] = destroyed
            json_data['mosaic'] = mosaic
            json_data['actor_href'] = ''
        except Exception as e:
            print(e)

        return (movie_number, folder_path, file_name, file_ex, sub_list, file_show_name, file_show_path, json_data)

    # =====================================================================================有道翻译
    def translateDeepl(self, text, s_lang='JA', t_lang='ZH'):
        deepl_key = self.config.get('deepl_key')
        url = 'https://api.deepl.com/v2/translate'
        if ':' in deepl_key:
            url = 'https://api-free.deepl.com/v2/translate'
        proxy_info = get_proxy_info()
        proxies = proxy_info.get('proxies')
        timeout = proxy_info.get('timeout')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; utf-8'
        }

        params = {
            'auth_key': deepl_key,
            'text': text,
            'target_lang': t_lang
        }

        if s_lang != '':
            params['source_lang'] = s_lang

        try:
            result = requests.post(url, data=params, headers=headers, proxies=proxies, timeout=timeout)
            result.encoding = 'utf-8'
            result = result.text
        except Exception as ex:
            self.addTextMain('   >>> 提示：deepl翻译接口请求失败，将跳过翻译！错误：' + str(ex))
        else:
            try:
                translate_results = json.loads(result)
            except Exception as ex:
                if len(result) == 0:
                    self.addTextMain(' 🟠 本次翻译将跳过！deepl API key 无效！请重新输入！')
                else:
                    self.addTextMain(' 🟠 本次翻译将跳过！deepl翻译接口返回数据异常1！返回内容：%s' % str(ex))
            else:
                if 'translations' in translate_results:
                    text = translate_results["translations"][0]["text"]
                else:
                    self.addTextMain(' 🟠 本次翻译将跳过！deepl翻译接口返回数据异常2！返回内容：%s' % str(translate_results))
        return text


    # =====================================================================================有道翻译
    def translateYoudao(self, title, outline):
        proxy_info = get_proxy_info()
        proxies = proxy_info.get('proxies')
        timeout = proxy_info.get('timeout')
        ttt = ''
        ooo = ''
        msg = '''%s
        %s
        ''' % (title, outline)
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        youdaokey = self.youdaokey
        salt = str(int(time.time() * 1000) + random.randint(0, 10))
        sign = hashlib.md5(("fanyideskweb" + msg + salt + youdaokey).encode('utf-8')).hexdigest()
        ts = str(int(time.time() * 1000))

        Form_Data = {
            'i': msg,
            'from': 'AUTO',
            'to': 'zh-CHS',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': 'c6b8c998b2cbaa29bd94afc223bc106c',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'ue' : 'UTF-8',
            'typoResult': 'true',
            'action': 'FY_BY_CLICKBUTTION'
            
        }
        Cookie = random.choice(["OUTFOX_SEARCH_USER_ID=833904829@10.169.0.84", "OUTFOX_SEARCH_USER_ID=-10218418@11.136.67.24;", "OUTFOX_SEARCH_USER_ID=1989505748@10.108.160.19;", "OUTFOX_SEARCH_USER_ID=2072418438@218.82.240.196;", "OUTFOX_SEARCH_USER_ID=1768574849@220.181.76.83;", "OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;"])

        headers = {
            # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,mt;q=0.8',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '240',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': Cookie,
            # 'Host': 'fanyi.youdao.com',
            # 'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
            # 'X-Requested-With': 'XMLHttpRequest'
        }
        try:
            req = requests.post(url=url, data=Form_Data, headers=headers, proxies=proxies, timeout=timeout)
            req.encoding = 'utf-8'
            req = req.text
        except Exception as ex:
            self.addTextMain('   >>> 提示：有道翻译接口请求失败，将跳过翻译！错误：' + str(ex))
        else:
            try:
                translate_results = json.loads(req)
            except Exception as ex:
                self.addTextMain('   >>> 提示：有道翻译接口返回数据异常1！将跳过翻译！返回内容：%s 错误：%s' % (req, str(ex)))
            else:
                # 找到翻译结果
                if 'translateResult' in translate_results:
                    translateResult = translate_results.get('translateResult')
                    msg1 = translateResult[0]
                    msg2 = translateResult[1]
                    for each in msg1:
                        ttt += each.get('tgt')
                    for each in msg2:
                        ooo += each.get('tgt')
                    title = ttt
                    outline = ooo
                else:
                    self.addTextMain('   >>> 提示：有道翻译接口返回数据异常2！将跳过翻译！返回内容：%s' % str(translate_results))
        return title, outline

    # =====================================================================================获取有道翻译key
    def getYouDaoKey(self):
        url = 'https://shared.ydstatic.com/fanyi/newweb/v1.1.7/scripts/newweb/fanyi.min.js'
        try:
            req = requests.get(url)
            req.encoding = 'utf-8'
            req = req.text
            self.youdaokey = re.search('(?<="fanyideskweb"\+e\+i\+")[^"]+', req).group(0)
            # sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")
        except Exception as ex:
            self.youdaokey = "Y2FYu%TNSbMCxc3t2u^XT"
            print('有道翻译接口key获取失败！' + str(ex))
            self.addTextMain(' 🟠 有道翻译接口key获取失败！请检查网页版有道是否正常！%s' % str(ex))
        return self.youdaokey

    # =====================================================================================创建成功输出目录
    def creatFolder(self, folder_new_path, file_path, file_new_path, thumb_new_path, poster_new_path, json_data):
        if self.config.get('success_file_move') == 0 and self.config.get('soft_link') == 0:   # 如果成功后不移动文件并且软连接关，则不创建文件夹
            return True
        if not os.path.exists(folder_new_path):   # 如果不存在目标文件夹，则创建文件夹
            try:
                os.makedirs(folder_new_path)
                self.addTextMain(" 🟢 Folder done!")
            except Exception as ex:
                self.addTextMain(' 🔴 Failed to create folder! \n   >>> ' + str(ex))
                return False
        if os.path.exists(file_new_path):   # 如果存在目标文件
            try:
                if file_new_path != os.path.realpath(file_new_path):    # 如果是软链接，删除
                    os.remove(file_new_path)
                    return True
            except:
                pass

            if self.config.get('soft_link') != 1:  # 非软链接
                if os.path.exists(thumb_new_path):
                    json_data['thumb_path'] = thumb_new_path
                if os.path.exists(poster_new_path):
                    json_data['poster_path'] = poster_new_path
                if file_new_path.lower() == file_path.lower():  # 如果路径相同，则代表已经在成功文件夹里
                    return True
                else:
                    self.addTextMain(" 🔴 The success folder already has a same name file!\n   >>> The current path is '%s'" % file_new_path)
                    json_data['title'] = "The success folder already has a same name file!"
                    json_data['error_info'] = "The success folder already has a same name file! \n   >>> The success path '%s' already exists \n   >>> The file will not be moved to the success folder!" % file_new_path
                    return False
            else:   # 软链接，有一个真实的文件，返回失败
                self.addTextMain(" 🔴 Symlink failed! \n   >>> The dest path already exists a real file! '%s'" % file_new_path)
                json_data['title'] = "The dest path already exists a real file!"
                json_data['error_info'] = "The dest path already exists a real file!"
                return False
        return True

    # =====================================================================================处理翻译
    def transLanguage(self, movie_number, jsonfile_data, json_data, translate_language, translate_content, translate_by):
        if translate_language == 'ja':
            return
        trans_title = ''
        trans_outline = ''
        deepl_key = self.config.get('deepl_key')

        # 处理title
        if 'title' in translate_content:
            movie_title = ''
            # 匹配本地高质量标题
            try:
                movie_title = jsonfile_data.get(movie_number)
            except Exception as ex:
                print('Error in transLanguage, Error info: ' + ex)
            # 匹配网络高质量标题（可在线更新）
            if not movie_title:
                result, html_search_title = get_html('http://www.yesjav.info/search.asp?q=%s&' % movie_number)
                if result:
                    html_title = etree.fromstring(html_search_title, etree.HTMLParser())
                    movie_title = str(html_title.xpath('//dl[@id="zi"]/p/font/a/b[contains(text(), $number)]/../../a[contains(text(), "中文字幕")]/text()', number=movie_number)).replace(' (中文字幕)', '').strip("['']") 
            # 使用json_data数据
            if movie_title:
                json_data['title'] = movie_title
            if langid.classify(json_data['title'])[0] == 'ja':
                trans_title = json_data['title']

        # 处理outline
        if 'outline' in translate_content:
            if langid.classify(json_data['outline'])[0] == 'ja':
                trans_outline = json_data['outline']

        # 翻译
        if trans_title or trans_outline:
            if translate_by == 'youdao':    # 使用有道翻译
                rr = random.randint(1, 5)
                self.addTextMain(' ⏱ YouDao Translation will request after %s seconds!' % str(rr))
                time.sleep(rr)  # 尝试加上延时，看被封情况
                trans_title, trans_outline = self.translateYoudao(trans_title, trans_outline)
                if trans_title:
                    json_data['title'] = trans_title
                if trans_outline:
                    json_data['outline'] = trans_outline
                self.addTextMain(' 🟢 YouDao Translation done!')
            elif translate_by == 'deepl':   # 使用deepl翻译
                if not deepl_key:
                    self.addTextMain(' 🟠 本次翻译将跳过！请在设置里填写 deepl API key 后使用！')
                    return
                if trans_title:
                    json_data['title'] = self.translateDeepl(trans_title)
                if trans_outline:
                    json_data['outline'] = self.translateDeepl(trans_outline)
                self.addTextMain(' 🟢 DeepL Translation done!')

        # 简繁转换
        if translate_language == 'zh_cn':
            json_data['title'] = zhconv.convert(json_data['title'], 'zh-cn')
            json_data['outline'] = zhconv.convert(json_data['outline'], 'zh-cn')

        elif translate_language == 'zh_tw':
            json_data['title'] = zhconv.convert(json_data['title'], 'zh-hant')
            json_data['outline'] = zhconv.convert(json_data['outline'], 'zh-hant')
            json_data['mosaic'] = zhconv.convert(json_data['mosaic'], 'zh-hant')


    # =====================================================================================清理旧的thumb、poster、fanart、nfo
    def delOldPic(self, folder_old_path, folder_new_path, file_path, file_new_path, thumb_new_path, poster_new_path, fanart_new_path, nfo_new_path, file_ex):
        poster_old = False  # 判断是不是旧文件，如何是旧文件，后面不加水印，避免二次加水印
        thumb_old = False
        nfo_old_path = file_path.replace(file_ex, '.nfo')
        folder_old_path = self.convert_path(folder_old_path)
        folder_new_path = self.convert_path(folder_new_path)
        extrafanart_old_path = self.convert_path(os.path.join(folder_old_path, 'extrafanart'))
        extrafanart_new_path = self.convert_path(os.path.join(folder_new_path, 'extrafanart'))
        # 图片加文件名时
        poster_old_path = file_path.replace(file_ex, '-poster.jpg')
        thumb_old_path = file_path.replace(file_ex, '-thumb.jpg')
        fanart_old_path = file_path.replace(file_ex, '-fanart.jpg')
        # 图片不加文件名时
        poster_old_path_no_filename = self.convert_path(os.path.join(folder_old_path, 'poster.jpg'))
        thumb_old_path_no_filename = self.convert_path(os.path.join(folder_old_path, 'thumb.jpg'))
        fanart_old_path_no_filename = self.convert_path(os.path.join(folder_old_path, 'fanart.jpg'))

        # poster
        if self.config.get('keep_local_poster') == 'on':    # 保留 poster
            if os.path.exists(poster_new_path):
                if os.path.exists(poster_old_path) and poster_old_path != poster_new_path:
                    os.remove(poster_old_path)
                if os.path.exists(poster_old_path_no_filename) and poster_old_path_no_filename != poster_new_path:
                    os.remove(poster_old_path_no_filename)
                poster_old = True
            else:
                if os.path.exists(poster_old_path):
                    shutil.move(poster_old_path, poster_new_path)
                    if os.path.exists(poster_old_path_no_filename):
                        os.remove(poster_old_path_no_filename)
                    poster_old = True
                elif os.path.exists(poster_old_path_no_filename):
                    shutil.move(poster_old_path, poster_new_path)
                    poster_old = True
        else:
            if os.path.exists(poster_new_path):
                os.remove(poster_new_path)
            if os.path.exists(poster_old_path):
                os.remove(poster_old_path)
            if os.path.exists(poster_old_path_no_filename):
                os.remove(poster_old_path_no_filename)

        # thumb
        if self.config.get('keep_local_thumb') == 'on':    # 保留 thumb
            if os.path.exists(thumb_new_path):
                if os.path.exists(thumb_old_path) and thumb_old_path != thumb_new_path:
                    os.remove(thumb_old_path)
                if os.path.exists(thumb_old_path_no_filename) and thumb_old_path_no_filename != thumb_new_path:
                    os.remove(thumb_old_path_no_filename)
                thumb_old = True
            else:
                if os.path.exists(thumb_old_path):
                    shutil.move(thumb_old_path, thumb_new_path)
                    if os.path.exists(thumb_old_path_no_filename):
                        os.remove(thumb_old_path_no_filename)
                    thumb_old = True
                elif os.path.exists(thumb_old_path_no_filename):
                    shutil.move(thumb_old_path_no_filename, thumb_new_path)
                    thumb_old = True
        else:
            if os.path.exists(thumb_new_path):
                os.remove(thumb_new_path)
            if os.path.exists(thumb_old_path):
                os.remove(thumb_old_path)
            if os.path.exists(thumb_old_path_no_filename):
                os.remove(thumb_old_path_no_filename)

        # fanart
        if self.config.get('keep_local_fanart') == 'on':    # 保留 fanart
            if os.path.exists(fanart_new_path):
                if os.path.exists(fanart_old_path) and fanart_old_path != fanart_new_path:
                    os.remove(fanart_old_path)
                if os.path.exists(fanart_old_path_no_filename) and fanart_old_path_no_filename != fanart_new_path:
                    os.remove(fanart_old_path_no_filename)
            else:
                if os.path.exists(fanart_old_path):
                    shutil.move(fanart_old_path, fanart_new_path)
                    if os.path.exists(fanart_old_path_no_filename):
                        os.remove(fanart_old_path_no_filename)
                elif os.path.exists(fanart_old_path_no_filename):
                    shutil.move(fanart_old_path_no_filename, fanart_new_path)
        else:
            if os.path.exists(fanart_new_path):
                os.remove(fanart_new_path)
            if os.path.exists(fanart_old_path):
                os.remove(fanart_old_path)
            if os.path.exists(fanart_old_path_no_filename):
                os.remove(fanart_old_path_no_filename)

        # nfo
        if self.config.get('keep_local_nfo') == 'on':    # 保留 nfo
            if os.path.exists(nfo_new_path):
                if os.path.exists(nfo_old_path) and nfo_old_path != nfo_new_path:
                    os.remove(nfo_old_path)
            elif os.path.exists(nfo_old_path):
                shutil.move(nfo_old_path, nfo_new_path)
        else:
            if os.path.exists(nfo_old_path):
                os.remove(nfo_old_path)
            if os.path.exists(nfo_new_path):
                os.remove(nfo_new_path)

        # extrafanart
        if self.config.get('keep_local_extrafanart') == 'on':    # 保留 extrafanart
            if os.path.exists(extrafanart_new_path):
                if os.path.exists(extrafanart_old_path) and extrafanart_old_path != extrafanart_new_path:
                    shutil.rmtree(extrafanart_old_path)
            elif os.path.exists(extrafanart_old_path):
                shutil.move(extrafanart_old_path, extrafanart_new_path)
        else:
            if os.path.exists(extrafanart_old_path):
                shutil.rmtree(extrafanart_old_path)
            if os.path.exists(extrafanart_new_path):
                shutil.rmtree(extrafanart_new_path)

        # extrafanart副本
        extrafanart_folder = self.config.get('extrafanart_folder')
        if self.config.get('keep_local_extrafanart_copy') == 'on' or not extrafanart_folder or extrafanart_folder == 'extrafanart':
            return poster_old, thumb_old
        extrafanart_copy_old_path = self.convert_path(os.path.join(folder_old_path, extrafanart_folder))
        extrafanart_copy_new_path = self.convert_path(os.path.join(folder_new_path, extrafanart_folder))
        if self.config.get('keep_local_extrafanart_copy') == 'on':    # 保留 extrafanart 副本
            if os.path.exists(extrafanart_copy_new_path):
                if os.path.exists(extrafanart_copy_old_path) and extrafanart_copy_old_path != extrafanart_copy_new_path:
                    shutil.rmtree(extrafanart_copy_old_path)
            elif os.path.exists(extrafanart_copy_old_path):
                shutil.move(extrafanart_copy_old_path, extrafanart_copy_new_path)
        else:
            if os.path.exists(extrafanart_copy_old_path):
                shutil.rmtree(extrafanart_copy_old_path)
            if os.path.exists(extrafanart_copy_new_path):
                shutil.rmtree(extrafanart_copy_new_path)
        return poster_old, thumb_old

    # =====================================================================================演员名映射输出处理
    def getActorData(self, json_data):
        # 如果不映射，直接返回
        actor_xml = self.actor_xml
        actor_output = self.config.get('actor_output')
        if actor_output == 'no' or not actor_xml:
            return json_data
        actor = json_data['actor']
        actor_list = actor.split(',')
        actor_href_list = []
        json_data['actor_href'] = ''
        actor_new = ''
        for each_actor in actor_list:
            if each_actor:
                actor_name = ',%s,' % each_actor.upper()
                actor_output_name = ''
                if actor_output == 'zh_cn':
                    actor_output_name= actor_xml.xpath('a[contains(@keyword, $name)]/@zh_cn', name=actor_name)
                elif actor_output == 'zh_tw':
                    actor_output_name= actor_xml.xpath('a[contains(@keyword, $name)]/@zh_tw', name=actor_name)
                elif actor_output == 'ja':
                    actor_output_name= actor_xml.xpath('a[contains(@keyword, $name)]/@jp', name=actor_name)
                if actor_output_name:
                    each_actor = actor_output_name[0]
                actor_new = actor_new + ',' + each_actor
                actor_href = actor_xml.xpath('a[contains(@keyword, $name)]/@href', name=actor_name)
                if actor_href:
                    actor_href_list.append(actor_href[0])
        actor = actor_new.strip(',')
        json_data['actor'] = actor

        # 演员主页
        if actor_href_list:
            json_data['actor_href'] = actor_href_list[0]
        if not json_data['actor_href']:
            json_data['actor_href'] = 'https://javdb.com/search?f=actor&q=' + urllib.parse.quote(json_data['actor'].split(',')[0])  # url转码，避免乱码

        return json_data

    # =====================================================================================信息（tag、series、studio、publisher、director）映射输出处理
    def getInfoData(self, json_data):
        # 如果不映射，直接返回
        info_xml = self.info_xml
        info_output = self.config.get('info_output')
        if info_output == 'no' or not info_xml:
            return json_data

        # 处理tag映射
        tag = json_data['tag']
        tag_list = tag.split(',')
        tag_new = ''
        for each_info in tag_list:
            if each_info:   # 为空时会多出来一个,
                tag_name = ',%s,' % each_info.upper()
                info_output_name = ''
                if info_output == 'zh_cn':
                    info_output_name= info_xml.xpath('a[contains(@keyword, $name)]/@zh_cn', name=tag_name)
                elif info_output == 'zh_tw':
                    info_output_name= info_xml.xpath('a[contains(@keyword, $name)]/@zh_tw', name=tag_name)
                elif info_output == 'ja':
                    info_output_name= info_xml.xpath('a[contains(@keyword, $name)]/@jp', name=tag_name)
                if info_output_name:
                    each_info = info_output_name[0]
                if each_info != '删除':
                    tag_new = tag_new + ',' + each_info
        tag = tag_new.strip(',')

        # 处理其他信息并且一部分添加到tag中
        mosaic = json_data['mosaic']
        leak = json_data['leak']
        c_word = json_data['c_word']
        destroyed = json_data['destroyed']
        series = json_data['series']
        studio = json_data['studio']
        publisher = json_data['publisher']
        director = json_data['director']
        if mosaic:
            tag += ',' + mosaic
        if leak:
            tag += ',流出'
        if c_word:
            tag += ',中文字幕'
        if destroyed:
            tag += ',' + destroyed.replace('.', '')
        # 中文简体
        if info_output == 'zh_cn':
            if series:  # 为空时会匹配所有
                series_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_cn', name=series)
                if series_output and series_output[0] !='删除':
                    series = series_output[0]
                tag += ',系列：' + series
            if studio:
                studio_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_cn', name=studio)
                if studio_output and studio_output[0] !='删除':
                    studio = studio_output[0]
                tag += ',制作：' + studio
            if not publisher:
                publisher = studio
            if publisher:
                publisher_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_cn', name=publisher)
                if publisher_output and publisher_output[0] !='删除':
                    publisher = publisher_output[0]
                tag += ',发行：' + publisher
            if director:
                director_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_cn', name=director)
                if director_output and director_output[0] !='删除':
                    director = director_output[0]
        # 中文繁体
        elif info_output == 'zh_tw':
            if series:  # 为空时会匹配所有
                series_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_tw', name=series)
                if series_output and series_output[0] !='删除':
                    series = series_output[0]
                tag += ',系列：' + series
            if studio:
                studio_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_tw', name=studio)
                if studio_output and studio_output[0] !='删除':
                    studio = studio_output[0]
                tag += ',製作：' + studio
            if not publisher:
                publisher = studio
            if publisher:
                publisher_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_tw', name=publisher)
                if publisher_output and publisher_output[0] !='删除':
                    publisher = publisher_output[0]
                tag += ',發行：' + publisher
            if director:
                director_output = info_xml.xpath('a[contains(@keyword, $name)]/@zh_tw', name=director)
                if director_output and director_output[0] !='删除':
                    director = director_output[0]
        # 日语
        elif info_output == 'ja':
            if series:  # 为空时会匹配所有
                series_output = info_xml.xpath('a[contains(@keyword, $name)]/@jp', name=series)
                if series_output and series_output[0] !='删除':
                    series = series_output[0]
                tag += ',系列：' + series
            if studio:
                studio_output = info_xml.xpath('a[contains(@keyword, $name)]/@jp', name=studio)
                if studio_output and studio_output[0] !='删除':
                    studio = studio_output[0]
                tag += ',製作：' + studio
            if not publisher:
                publisher = studio
            if publisher:
                publisher_output = info_xml.xpath('a[contains(@keyword, $name)]/@jp', name=publisher)
                if publisher_output and publisher_output[0] !='删除':
                    publisher = publisher_output[0]
                tag += ',發行：' + publisher
            if director:
                director_output = info_xml.xpath('a[contains(@keyword, $name)]/@jp', name=director)
                if director_output and director_output[0] !='删除':
                    director = director_output[0]

        json_data['tag'] = tag.strip(',')
        json_data['series'] = series
        json_data['studio'] = studio
        json_data['publisher'] = publisher
        json_data['director'] = director
        return json_data


    # =====================================================================================读取nfo
    def getNfoData(self, file_path, movie_number, json_data):
        json_data['title'] = ''
        json_data['actor'] = ''
        json_data['website'] = ''
        json_data['log_info'] = ''
        json_data['error_type'] = ''
        json_data['error_info'] = ''

        local_nfo_path = os.path.splitext(file_path)[0] + '.nfo'
        file_folder = os.path.split(file_path)[0]
        if not os.path.exists(local_nfo_path):
            json_data['error_info'] = 'nfo文件不存在'
            json_data['outline'] = os.path.split(file_path)[1]
            json_data['tag'] = file_path
            return False, json_data
        nfo_xml = etree.parse(local_nfo_path)

        title = str(nfo_xml.xpath('//title/text()')).strip("[']")
        # 获取不到标题，表示xml错误，重新刮削
        if not title:
            json_data['error_info'] = 'nfo文件损坏'
            json_data['outline'] = os.path.split(file_path)[1]
            json_data['tag'] = file_path
            return False, json_data
        number = str(nfo_xml.xpath('//num/text()')).strip("[']")
        if not number:
            number = movie_number
        actor = str(nfo_xml.xpath('//actor/name/text()')).strip("['']").replace("'", '').replace(', ', ',')
        outline = str(nfo_xml.xpath('//outline/text()')).strip("[']")
        if not outline:
            outline = str(nfo_xml.xpath('//plot/text()')).strip("[']")
        tag = str(nfo_xml.xpath('//tag/text()')).strip(" ['']").replace("'", "").replace(', ', ',')
        release = str(nfo_xml.xpath('//release/text()')).strip("[']")
        if not release:
            release = str(nfo_xml.xpath('//releasedate/text()')).strip("[']")
        year = str(nfo_xml.xpath('//year/text()')).strip("[']")
        runtime = str(nfo_xml.xpath('//runtime/text()')).strip("[']")
        score = str(nfo_xml.xpath('//rating/text()')).strip("[']")
        series = str(nfo_xml.xpath('//series/text()')).strip("[']")
        director = str(nfo_xml.xpath('//director/text()')).strip("[']")
        studio = str(nfo_xml.xpath('//studio/text()')).strip("[']")
        publisher = str(nfo_xml.xpath('//studio/text()')).strip("[']")
        website = str(nfo_xml.xpath('//website/text()')).strip("[']")
        cover = str(nfo_xml.xpath('//cover/text()')).strip("[']")
        poster = str(nfo_xml.xpath('//movie/poster/text()')).strip("[']")
        thumb = str(nfo_xml.xpath('//movie/thumb/text()')).strip("[']")
        fanart = str(nfo_xml.xpath('//movie/fanart/text()')).strip("[']")
        poster_path = os.path.join(file_folder, poster)
        thumb_path = os.path.join(file_folder, thumb)
        fanart_path = os.path.join(file_folder, fanart)

        if not os.path.isfile(poster_path):
            poster_path = ''
        if not os.path.isfile(fanart_path):
            fanart_path = ''
        if not os.path.isfile(thumb_path):
            thumb_path = fanart_path

        json_data['title'] = title
        json_data['number'] = number
        json_data['actor'] = actor
        json_data['outline'] = outline
        json_data['tag'] = tag
        json_data['year'] = year
        json_data['runtime'] = runtime
        json_data['score'] = score
        json_data['series'] = series
        json_data['director'] = director
        json_data['publisher'] = publisher
        json_data['studio'] = studio
        json_data['source'] = 'nfo'
        json_data['website'] = website
        json_data['cover'] = cover
        json_data['req_web'] = 'nfo'
        json_data['poster_path'] = poster_path
        json_data['thumb_path'] = thumb_path
        json_data['fanart_path'] = fanart_path

        return True, json_data


    # =====================================================================================检查文件
    def checkFile(self, file_path, file_escape_size, json_data):  
        if not os.path.exists(file_path):
            json_data['error_info'] = '文件不存在'
            json_data['error_type'] = json_data['error_info']
            json_data['outline'] = os.path.split(file_path)[1]
            json_data['tag'] = file_path
            return False, json_data
        file_size = os.path.getsize(file_path)/float(1024*1024)
        if file_size < file_escape_size:
            json_data['error_info'] = '文件小于 %s MB 被过滤!（实际大小 %s MB）已跳过刮削！' % (file_escape_size, round(file_size, 2))
            json_data['error_type'] = json_data['error_info']
            json_data['outline'] = os.path.split(file_path)[1]
            json_data['tag'] = file_path
            return False, json_data
        return True, json_data


    # =====================================================================================获取视频分辨率
    def getVideoSize(self, json_data, file_path):
        definition = ''
        try:
            cap = cv2.VideoCapture(file_path)
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        except:
            height = 0
        if height >= 4000:
            definition = '8K'
        elif height >= 2000:
            definition = '4K'
        elif height >= 1400:
            definition = '1440P'
        elif height >= 1000:
            definition = '1080P'
        elif height >= 900:
            definition = '960P'
        elif height >= 700:
            definition = '720P'
        elif height >= 500:
            definition = '540P'
        elif height >= 300:
            definition = '360P'
        elif height >= 100:
            definition = '144P'
        json_data['definition'] = definition
        if json_data['tag'] and definition:
            json_data['tag'] = json_data['tag'] + ',' + definition
        else:
            json_data['tag'] = json_data['tag'] + definition
        return json_data


    # =====================================================================================处理单个文件刮削
    def coreMain(self, file_path, file_info, file_mode, appoint_number='', appoint_url='', jsonfile_data={}):
        # =====================================================================================初始化所需变量
        json_data = {}
        sub_list = []
        translate_language = self.config.get('translate_language')
        translate_content = self.config.get('translate_content')
        translate_by = self.config.get('translate_by')
        main_mode = self.config.get('main_mode')
        no_nfo_scrape = self.config.get('no_nfo_scrape')
        file_escape_size = float(self.config.get('file_size'))

        # =====================================================================================获取文件信息
        movie_number, folder_old_path, file_name, file_ex, sub_list, file_show_name, file_show_path, json_data = file_info

        # =====================================================================================检查文件大小
        result, json_data = self.checkFile(file_path, file_escape_size, json_data)
        if not result:
            return False, json_data

        # =====================================================================================读取nfo模式（待添加设置项：没有nfo时文件处理方式）
        if main_mode == 3:
            result, json_data = self.getNfoData(file_path, movie_number, json_data)
            if result:
                self.showMovieInfo(json_data)
                # time.sleep(0.01)
                return True, json_data
            if no_nfo_scrape == 'off': # 无nfo时不刮削
                return False, json_data

        # =====================================================================================刮削json_data
        json_data = self.getJsonData(file_mode, movie_number, appoint_url, translate_language, json_data)

        # =====================================================================================显示json_data结果或日志
        if not self.showDataResult(json_data):
            return False, json_data                 # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================映射输出演员名/信息
        self.getActorData(json_data)
        self.getInfoData(json_data)

        # =====================================================================================翻译json_data（标题/介绍）
        self.transLanguage(movie_number, jsonfile_data, json_data, translate_language, translate_content, translate_by)

        # =====================================================================================获取视频分辨率
        json_data = self.getVideoSize(json_data, file_path)

        # =====================================================================================显示json_data内容
        self.showMovieInfo(json_data)

        # =====================================================================================获取设置的媒体目录、失败目录、成功目录
        movie_path, success_folder, failed_folder, escape_folder, extrafanart_folder = self.getMoviePathSetting()

        # =====================================================================================生成输出文件夹和输出文件的路径
        folder_new_path, file_new_path, nfo_new_path, poster_new_path, thumb_new_path, fanart_new_path, naming_rule, file_new_name, nfo_new_name, poster_new_name, thumb_new_name, fanart_new_name = self.getOutPutName(file_path, success_folder, json_data, file_ex)

        # =====================================================================================判断输出文件夹和文件是否已存在，如无则创建输出文件夹
        if  not self.creatFolder(folder_new_path, file_path, file_new_path, thumb_new_path, poster_new_path, json_data):
            return False, json_data                    # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================整理模式
        if self.config.get('main_mode') == 2: # 整理模式（仅根据刮削数据把电影命名为番号并分类到对应目录名称的文件夹下）
            if not self.pasteFileToFolder(file_path, file_new_path):   # 移动文件
                return False, json_data                   # 返回AVDC_main, 继续处理下一个文件
            else:
                self.delOldPic(folder_old_path, folder_new_path, file_path, file_new_path, thumb_new_path, poster_new_path, fanart_new_path, nfo_new_path, file_ex)   # 清理旧的thumb、poster、fanart、nfo
                return True, json_data
        # =====================================================================================刮削模式

        # =====================================================================================清理旧的thumb、poster、fanart、extrafanart、nfo
        poster_old, thumb_old = self.delOldPic(folder_old_path, folder_new_path, file_path, file_new_path, thumb_new_path, poster_new_path, fanart_new_path, nfo_new_path, file_ex)

        # =====================================================================================下载thumb
        if not self.thumbDownload(json_data, folder_new_path, thumb_new_name, thumb_new_path, fanart_new_path):
            return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================下载poster
        if not self.posterDownload(json_data, folder_new_path, poster_new_name, thumb_new_path, poster_new_path, fanart_new_path):
            return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================下载艺术图
        self.copyRenameJpgToFanart(thumb_new_path, fanart_new_path)

        # =====================================================================================删除thumb.jpg(当选择不保存时)
        self.deletethumb(thumb_new_name, thumb_new_path)

        # =====================================================================================加水印
        self.add_mark(poster_new_path, thumb_new_path, json_data, poster_old, thumb_old)

        # =====================================================================================生成nfo文件
        self.PrintFiles(nfo_new_path, folder_new_path, thumb_new_name, poster_new_name, fanart_new_name, json_data)

        # =====================================================================================下载剧照和剧照副本
        self.extrafanartDownload(json_data, folder_new_path)
        self.extrafanartCopy(folder_new_path)

        # =====================================================================================移动文件
        if not self.pasteFileToFolder(file_path, file_new_path):
            return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================移动字幕
        for sub in sub_list:
            shutil.move(os.path.join(folder_old_path, (file_name + sub)), os.path.join(folder_new_path, (naming_rule + sub)))
            self.addTextMain(" 🟢 Sub file '%s' moved successfully! " % (naming_rule + sub))

        # =====================================================================================json添加封面缩略图路径
        json_data['number'] = movie_number
        json_data['poster_path'] = poster_new_path
        json_data['thumb_path'] = thumb_new_path
        json_data['fanart_path'] = fanart_new_path
        if os.path.exists(fanart_new_path) and not os.path.exists(thumb_new_path):
            json_data['thumb_path'] = fanart_new_path

        return True, json_data


    # =====================================================================================主功能函数
    def AVDC_Main(self, file_mode):
        # os.chdir(os.getcwd())
        # =====================================================================================初始化所需变量
        count = 0
        succ_count = 0
        fail_count = 0
        movie_list = []
        appoint_number = ''
        appoint_url = ''
        json_data = {}
        self.img_path = ''
        self.add_label_info(json_data)  # 清空主界面显示信息
        self.getYouDaoKey() # 获取有道key
        # 获取设置的媒体目录、失败目录、成功目录
        movie_path, success_folder, failed_folder, escape_folder, extrafanart_folder = self.getMoviePathSetting()


        # 日志页面显示软链接信息
        if self.config.get('soft_link') == '1':
            self.addTextMain(' 🎈 Soft link mode is ENABLE!')

        # 日志页面显示开始时间
        start_time = time.time()
        if file_mode == 'single_file':
            self.addTextMain('当前是单文件刮削模式')
        self.addTextMain('\n ⏰ Start time: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        # 获取待刮削文件列表的相关信息
        movie_list, count_all, appoint_number, appoint_url = self.getMovieList(file_mode, movie_path, escape_folder)

        if count_all == 0:
            self.progressBarValue.emit(int(100))
        else:
            self.count_claw += 1

        # 载入c_numuber.json数据
        with open(self.c_numuber_jsonfile, encoding='UTF-8') as data:
            jsonfile_data = json.load(data)
        # 载入acotr.xml和info.xml数据
        actor_xml_file = 'mapping_actor.xml'
        info_xml_file = 'mapping_info.xml'
        if not os.path.exists(actor_xml_file):
            shutil.copy(self.actor_file, os.path.join(self.main_path, actor_xml_file))
        self.actor_xml = etree.parse(actor_xml_file)
        if not os.path.exists(info_xml_file):
            shutil.copy(self.tag_file, os.path.join(self.main_path, info_xml_file))
        self.info_xml = etree.parse(info_xml_file)

        # 处理视频列表
        for file_path in movie_list:
            try:    
                if os.path.exists(os.path.realpath(file_path)):
                    file_path = os.path.realpath(file_path)  # 如果文件本身是一个符号连接，这时使用它的真实地址
                else:
                    os.remove(file_path)   # 清理失效的软链接文件
            except Exception as e:
                # print(traceback.format_exc())
                print('movie_list: %s ' % e)
            count += 1
            # 获取进度
            progress_value = count / count_all * 100    
            progress_percentage = '%.2f' % progress_value + '%'                     

            # 获取文件基础信息
            file_info = self.getFileInfo(file_path, appoint_number)
            movie_number, folder_old_path, file_name, file_ex, sub_list, file_show_name, file_show_path, json_data = file_info

            # 显示刮削信息
            self.set_label_file_path.emit('正在刮削： ' + str(count) + '/' + str(count_all) + ' （' + progress_percentage + '）\n' + self.convert_path(file_show_path))
            self.Ui.label_result.setText(' 成功：%s  失败：%s' % (succ_count, fail_count))
            self.progressBarValue.emit(int(progress_value))
            self.addTextMain('\n%d/%d (%s) round(%s) %s' % (count, count_all, progress_percentage, self.count_claw, file_name+file_ex))
            self.addTextMain('='*80)
            self.addTextMain(" 🙈 [Movie] " + self.convert_path(file_path) + "\n 🚘 [Number] " + movie_number)
            succ_count += 1
            fail_count += 1
            succ_show_name = str(self.count_claw) + '-' + str(succ_count) + '.' + file_show_name
            fail_show_name = str(self.count_claw) + '-' + str(fail_count) + '.' + file_show_name
            # 处理文件
            try:
                result, json_data = self.coreMain(file_path, file_info, file_mode, appoint_number, appoint_url, jsonfile_data)
            except Exception as ex:
                # json_data = {}   # 清空数据，因为崩溃时json_data是上一个文件的数据
                # print(traceback.format_exc())
                json_data['error_info'] = 'getJsonData error: ' + str(ex)
                result = False
            if result:
                fail_count -= 1
                self.showListName(succ_show_name, 'succ', json_data, movie_number)
            else:
                succ_count -= 1
                self.showListName(fail_show_name, 'fail', json_data, movie_number)
                self.addTextMain(' 🔴 [Info] %s' % json_data['error_info'])
                self.moveFailedFolder(file_path, folder_old_path, failed_folder, file_ex)
        self.Ui.label_result.setText(' 成功：%s  失败：%s' % (succ_count, fail_count))
        self.progressBarValue.emit(100)
        self.addTextMain("================================================================================")
        self.CEF(movie_path, file_mode)
        end_time = time.time()
        used_time = str(round((end_time - start_time), 2))
        if count_all:
            average_time = str(round((end_time - start_time)/count_all, 2))
        else:
            average_time = used_time
        self.set_label_file_path.emit('🎉 恭喜！全部刮削完成！共 %s 个文件！用时 %s 秒' % (count_all, used_time))
        self.addTextMain(" 🎉🎉🎉 All finished!!! Total %s , Success %s , Failed %s " % (count_all, succ_count, fail_count))
        self.addTextMain("================================================================================")
        self.addTextMain(' 🏁 End time: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '  Used time: %s S  Per time: %s S\n\n'% (used_time, average_time))
        self.Ui.pushButton_start_cap.setEnabled(True)
        self.Ui.pushButton_start_cap2.setEnabled(True)
        self.Ui.pushButton_start_cap.setText('开始')
        self.Ui.pushButton_start_cap2.setText('开始')
        self.Ui.pushButton_start_cap.setStyleSheet('QPushButton#pushButton_start_cap{color:white;background-color:#0066CC;}QPushButton:hover#pushButton_start_cap{color:white;background-color:#4C6EFF}QPushButton:pressed#pushButton_start_cap{color:white;background-color:#4C6EE0}')
        self.Ui.pushButton_start_cap2.setStyleSheet('QPushButton#pushButton_start_cap2{color:white;background-color:#0066CC}QPushButton:hover#pushButton_start_cap2{color:white;background-color:#4C6EFF}QPushButton:pressed#pushButton_start_cap2{color:white;background-color:#4C6EE0}')
        self.uploadActorPhoto_main()


class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.iniDragCor = [0, 0]       
    def mousePressEvent(self,e):
        # print("ppp",e.pos())
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]
        # 判断水平移动或竖直移动
        if newWin2.pic_h_w_ratio <= 1.5:
            y = 0
        else:
            x = 0
            
        cor = QPoint(x, y)        
        self.move(self.mapToParent(cor))# 需要maptoparent一下才可以的,否则只是相对位置。
        # print('drag button event,',time.time(),e.pos(),e.x(),e.y())

        # 计算实际裁剪位置
        c_x, c_y, c_x2, c_y2 = newWin2.getRealPos()
        # print('拖动：%s %s %s %s' % (str(c_x), str(c_y), str(c_x2), str(c_y2))) 

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
        # 计算实际裁剪位置
        c_x, c_y, c_x2, c_y2 = newWin2.getRealPos()
        # print('松开：%s %s %s %s' % (str(c_x), str(c_y), str(c_x2), str(c_y2))) 

class CutWindow(QDialog, Ui_Dialog_cut_poster):
    def __init__(self, parent=None):
        super(CutWindow, self).__init__(parent)
        self.Ui = Ui_Dialog_cut_poster()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.m_drag = True
        self.m_DragPosition = 0
        self.show_w = self.Ui.label_backgroud_pic.width()   # 图片显示区域的宽高
        self.show_h = self.Ui.label_backgroud_pic.height()   # 图片显示区域的宽高
        self.zomm_ratio = 1
        self.pic_new_w = self.show_w
        self.pic_new_h = self.show_h
        self.pic_w = self.show_w
        self.pic_h = self.show_h
        self.Ui.pushButton_select_cutrange = DraggableButton('拖动选择裁剪范围', self.Ui.label_backgroud_pic)
        self.Ui.pushButton_select_cutrange.setObjectName(u"pushButton_select_cutrange")
        self.Ui.pushButton_select_cutrange.setGeometry(QRect(420, 0, 379, 539))
        self.Ui.pushButton_select_cutrange.setCursor(QCursor(Qt.OpenHandCursor))
        self.Ui.pushButton_select_cutrange.setAcceptDrops(True)
        self.Ui.pushButton_select_cutrange.setStyleSheet(u"background-color: rgba(200, 200, 200, 80);\n""font-size:13px;\n""font-weight:normal;""color: rgba(0, 0, 0, 255);\n"
"border:2px solid rgba(0, 55, 255, 255);\n")
        self.set_style()
        self.Ui.horizontalSlider_left.valueChanged.connect(self.change_postion_left)
        self.Ui.horizontalSlider_right.valueChanged.connect(self.change_postion_right)
        self.Ui.pushButton_open_pic.clicked.connect(self.openimage)
        self.Ui.pushButton_cut_close.clicked.connect(self.toCutClose)
        self.Ui.pushButton_cut.clicked.connect(self.toCut)
        self.Ui.pushButton_close.clicked.connect(self.close)
        self.showimage()

    def set_style(self):
        # 控件美化 裁剪弹窗
        self.Ui.widget.setStyleSheet(
            '''

            QPushButton{
                    color:black;
                    font-size:15px;
                    background-color:#CCCCCC;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton:hover{
                    color:white;
                    background-color:#4C6EFF;
                    font-weight:bold;
                }
            QPushButton:pressed{
                    background-color:#4C6EE0;
                    border-color:black;
                    border-width:12px;
                    font-weight:bold;
            }
            ''')


    def toCutClose(self):
        self.toCut()
        self.close()

    def toCut(self):
        img_path = self.show_image_path     # 被裁剪的图片
        # 路径为空时，跳过
        if not img_path:
            return
        thumb_path = self.cut_thumb_path    # 裁剪后的thumb路径
        poster_path = self.cut_poster_path  # 裁剪后的poster路径
        ui.img_path = img_path  # 裁剪后更新图片url，这样再次点击时才可以重新加载并裁剪
        # 读取配置信息
        mark_list = []
        self.config = ui.config

        download_thumb = self.config.get('download_thumb')
        poster_mark = self.config.get('poster_mark')
        thumb_mark = self.config.get('thumb_mark')
        if self.Ui.checkBox_add_sub.isChecked():
            mark_list.append('字幕')
        if self.Ui.checkBox_add_leak.isChecked():
            mark_list.append('流出')
        if self.Ui.checkBox_add_uncensored.isChecked():
            mark_list.append('无码')
        # 裁剪poster
        img = Image.open(img_path)
        img = img.convert('RGB')
        img_new_png = img.crop((self.c_x, self.c_y, self.c_x2, self.c_y2))
        try:
            if os.path.exists(poster_path):
                os.remove(poster_path)
        except Exception as ex:
            ui.addTextMain(" 🔴 Failed to remove old poster!\n   >>> " + str(ex))
            return False
        img_new_png.save(poster_path)
        ui.addTextMain(" 🟢 Poster cut successfully!")
        # poster加水印
        if poster_mark == 1:
            ui.add_mark_thread(poster_path, mark_list)

        # 裁剪thumb
        if download_thumb == 'on':
            if thumb_path != img_path:
                if os.path.exists(thumb_path):
                    os.remove(thumb_path)
                shutil.copy(img_path, thumb_path)
            # thumb加水印
            if thumb_mark == 1:
                ui.add_mark_thread(thumb_path, mark_list)
        else:
            thumb_path = img_path
        # 在主界面显示预览
        pix = QPixmap(thumb_path)
        ui.Ui.label_thumb.setScaledContents(True)
        ui.Ui.label_thumb.setPixmap(pix)  # 添加图标
        pix = QPixmap(poster_path)
        ui.Ui.label_poster.setScaledContents(True)
        ui.Ui.label_poster.setPixmap(pix)  # 添加图标
        ui.pushButton_main_clicked()
        return True

    def change_postion_left(self):
        abc = self.Ui.horizontalSlider_left.value()
        self.Ui.horizontalSlider_right.valueChanged.disconnect(self.change_postion_right)
        self.Ui.horizontalSlider_right.setValue(10000 - abc)
        self.Ui.horizontalSlider_right.valueChanged.connect(self.change_postion_right)

        self.rect_x, self.rect_y, self.rect_w, self.rect_h = self.Ui.pushButton_select_cutrange.geometry().getRect()
        self.rect_h_w_ratio = 1 + abc / 10000   # 更新高宽比
        self.Ui.label_cut_ratio.setText(str('%.2f' % self.rect_h_w_ratio))

        # 计算裁剪框大小
        if self.pic_h_w_ratio <= 1.5: # 如果高宽比小时，固定高度，右边水平移动
            self.rect_w1 = int (self.rect_h / self.rect_h_w_ratio)
            self.rect_x = self.rect_x + self.rect_w - self.rect_w1
            self.rect_w = self.rect_w1
        else:
            self.rect_h1 = int(self.rect_w * self.rect_h_w_ratio)
            self.rect_y = self.rect_y + self.rect_h - self.rect_h1
            self.rect_h = self.rect_h1
        self.Ui.pushButton_select_cutrange.setGeometry(QRect(self.rect_x, self.rect_y, self.rect_w, self.rect_h))   # 显示裁剪框
        self.getRealPos()  # 显示裁剪框实际位置

    def change_postion_right(self):
        abc = self.Ui.horizontalSlider_right.value()
        self.Ui.horizontalSlider_left.valueChanged.disconnect(self.change_postion_left)
        self.Ui.horizontalSlider_left.setValue(10000 - abc)
        self.Ui.horizontalSlider_left.valueChanged.connect(self.change_postion_left)

        self.rect_x, self.rect_y, self.rect_w, self.rect_h = self.Ui.pushButton_select_cutrange.geometry().getRect()
        self.rect_h_w_ratio = 2 - abc / 10000   # 更新高宽比
        self.Ui.label_cut_ratio.setText(str('%.2f' % self.rect_h_w_ratio))
        # 计算裁剪框大小
        if self.pic_h_w_ratio <= 1.5: # 如果高宽比小时，固定高度，右边水平移动
            self.rect_w = int (self.rect_h / self.rect_h_w_ratio)
        else:
            self.rect_h = int(self.rect_w * self.rect_h_w_ratio)
        self.Ui.pushButton_select_cutrange.setGeometry(QRect(self.rect_x, self.rect_y, self.rect_w, self.rect_h))   # 显示裁剪框
        self.getRealPos()  # 显示裁剪框实际位置

    # 打开图片选择框
    def openimage(self):
        img_path, img_type = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg *.png;;All Files(*)")
        if img_path:
            self.showimage(img_path)

    # 显示要裁剪的图片
    def showimage(self, img_path='', json_data={}):
        self.Ui.label_backgroud_pic.setText(' ')  # 清空背景
        # 初始化数据
        c_word = ''
        leak = ''
        mosaic = ''
        self.Ui.checkBox_add_sub.setChecked(False)
        self.Ui.checkBox_add_leak.setChecked(False)
        self.Ui.checkBox_add_uncensored.setChecked(False)
        self.pic_h_w_ratio = 1.5
        self.rect_h_w_ratio = 536.6 / 379
        self.show_image_path = img_path
        self.cut_thumb_path = ''    # 裁剪后的thumb路径
        self.cut_poster_path = ''  # 裁剪后的poster路径

        # 获取水印设置
        self.config = ui.config
        poster_mark = self.config.get('poster_mark')
        mark_type = self.config.get('mark_type')
        pic_name = self.config.get('pic_name')
        
        # 显示图片及水印情况
        if img_path:
            # 显示背景
            pic = QPixmap(img_path)
            self.pic_w = pic.width()
            self.pic_h = pic.height()
            self.Ui.label_origin_size.setText(str('%s, %s' % (str(self.pic_w), str(self.pic_h))))    # 显示宽高
            self.pic_h_w_ratio = self.pic_h / self.pic_w    # 图片高宽比
            abc = int((self.rect_h_w_ratio - 1) * 10000)
            self.Ui.horizontalSlider_left.setValue(abc)
            self.Ui.horizontalSlider_right.setValue(10000 - abc)
            # 背景图片等比缩放并显示
            if self.pic_h_w_ratio <= self.show_h / self.show_w: # 水平撑满
                self.pic_new_w = self.show_w
                self.pic_new_h = int(self.pic_new_w * self.pic_h / self.pic_w)
            else:   # 垂直撑满
                self.pic_new_h = self.show_h
                self.pic_new_w = int(self.pic_new_h * self.pic_w / self.pic_h)
            self.zomm_ratio = self.pic_w / self.pic_new_w
            pic = QPixmap.scaled(pic, self.pic_new_w , self.pic_new_h, aspectRatioMode=Qt.KeepAspectRatio)  # 图片缩放
            self.Ui.label_backgroud_pic.setGeometry(0, 0, self.pic_new_w , self.pic_new_h)  # 背景区域设置
            self.Ui.label_backgroud_pic.setPixmap(pic)  # 显示图片

            # 获取nfo文件名，用来设置裁剪后图片名称和裁剪时的水印状态
            img_folder, img_fullname = os.path.split(img_path)
            img_name, img_ex = os.path.splitext(img_fullname)

            # 如果没有json_data，则通过图片文件名或nfo文件名获取，目的是用来获取水印
            if not json_data:
                # 根据图片文件名获取获取水印情况
                temp_path = img_path
                # 如果图片没有番号信息，则根据nfo文件名获取水印情况
                if '-' not in img_name:
                    file_list = os.listdir(img_folder)
                    for each in file_list:
                        if '.nfo' in each:
                            temp_path = os.path.join(img_folder, each)
                            break
                movie_number, folder_old_path, file_name, file_ex, sub_list, file_show_name, file_show_path, json_data = ui.getFileInfo(temp_path)

            # 获取水印信息
            c_word = json_data['c_word']
            leak = json_data['leak']
            mosaic = json_data['mosaic']

            # 获取裁剪后的的poster和thumb路径
            poster_path = os.path.join(img_folder, 'poster.jpg')
            if pic_name == 0:    # 文件名-poster.jpg
                if '-' in img_name:
                    poster_path = img_path.replace('-fanart', '').replace('-thumb', '').replace('-poster', '').replace(img_ex, '') + '-poster.jpg'
            thumb_path = poster_path.replace('poster.', 'thumb.')
            self.cut_thumb_path = thumb_path    # 裁剪后的thumb路径
            self.cut_poster_path = poster_path  # 裁剪后的poster路径

            # poster添加水印
            if poster_mark:
                if 'SUB' in mark_type and c_word:
                    self.Ui.checkBox_add_sub.setChecked(True)
                if 'LEAK' in mark_type and leak:
                    self.Ui.checkBox_add_leak.setChecked(True)
                if 'UNCENSORED' in mark_type and (mosaic == '無碼' or mosaic == '无码'):
                    self.Ui.checkBox_add_uncensored.setChecked(True)

        # 显示裁剪框
        # 计算裁剪框大小
        if self.pic_h_w_ratio <= 1.5: # 如果高宽比小时，固定高度，水平移动
            self.rect_h = self.pic_new_h
            self.rect_w = int (self.rect_h / self.rect_h_w_ratio)
            self.rect_x = self.pic_new_w - self.rect_w
            self.rect_y = 0
        else:   # 高宽比大时，固定宽度，竖向移动
            self.rect_w = self.pic_new_w
            self.rect_h = int(self.rect_w * self.rect_h_w_ratio)
            self.rect_x = 0
            self.rect_y = int((self.pic_new_h - self.rect_h)/2)
        self.Ui.pushButton_select_cutrange.setGeometry(QRect(self.rect_x, self.rect_y, self.rect_w, self.rect_h))   # 显示裁剪框
        self.getRealPos()  # 显示裁剪框实际位置

    # 计算在原图的裁剪位置
    def getRealPos(self):
        # 边界处理
        pic_new_w = self.pic_new_w
        pic_new_h = self.pic_new_h
        px, py , pw, ph= self.Ui.pushButton_select_cutrange.geometry().getRect()
        pw1 = int(pw / 2)
        ph1 = int(ph / 2)
        if px <= - pw1: # 左边出去一半
            px = - pw1
        elif px >= pic_new_w - pw1: # x右边出去一半
            px = pic_new_w - pw1
        if py <= - ph1: # 上面出去一半
            py = - ph1
        elif py >= pic_new_h - ph1: # 下面出去一半
            py = pic_new_h - ph1

        # 更新显示裁剪框
        self.Ui.pushButton_select_cutrange.setGeometry(QRect(px, py , pw, ph))
        # 计算实际裁剪位置
        z_ratio = self.zomm_ratio    # 原图/显示图的比率
        self.c_x = int(px * z_ratio) # 左上角坐标x
        self.c_y = int(py * z_ratio) # 左上角坐标y
        self.c_w = int(pw * z_ratio)
        self.c_h = int(ph * z_ratio)
        self.c_x2 = self.c_x + self.c_w    # 右下角坐标x
        self.c_y2 = self.c_y + self.c_h    # 右下角坐标y
        # 在原图以外的区域不裁剪
        if self.c_x < 0:
            self.c_w += self.c_x
            self.c_x = 0
        if self.c_y < 0:
            self.c_h += self.c_y
            self.c_y = 0
        if self.c_x2 > self.pic_w:
            self.c_w += self.pic_w - self.c_x2
            self.c_x2 = self.pic_w
        if self.c_y2 > self.pic_h:
            self.c_h += self.pic_h - self.c_y2
            self.c_y2 = self.pic_h
        # 显示实际裁剪位置
        self.Ui.label_cut_postion.setText('%s, %s, %s, %s' % (str(self.c_x), str(self.c_y), str(self.c_x2), str(self.c_y2)))
        # print('选择位置： %s, %s, %s, %s' % (str(self.c_x), str(self.c_y), str(self.c_x2), str(self.c_y2)))
        # 显示实际裁剪尺寸
        self.Ui.label_cut_size.setText('%s, %s' % (str(self.c_w), str(self.c_h)))

        return self.c_x, self.c_y, self.c_x2, self.c_y2

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 按下左键改变鼠标指针样式为手掌

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))  # 释放左键改变鼠标指针样式为箭头

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_drag:
            self.move(e.globalPos() - self.m_DragPosition)
            e.accept()
        # print('main',e.x(),e.y())


if __name__ == '__main__':
    '''
    主函数
    '''
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ui = MyMAinWindow()
    ui.show()
    newWin2 = CutWindow()

    sys.exit(app.exec_())
