#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logging import error, exception
import threading
import json
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QTextCursor, QCursor
from PySide2.QtWidgets import QMainWindow, QTreeWidgetItem, QApplication
from PySide2.QtCore import Signal, Qt, QCoreApplication
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
from Function.Function import save_config, movie_lists, get_info, getDataFromJSON, escapePath, getNumber, check_pic
from Function.getHtml import get_html, get_proxies, get_proxy
import socks
import urllib3
urllib3.disable_warnings()

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MyMAinWindow(QMainWindow, Ui_AVDV):
    progressBarValue = Signal(int)  # 进度条信号量
    main_logs_show = Signal(str) # 刮削日志信号
    net_logs_show = Signal(str) # 网络检测日志信号
    set_javdb_cookie = Signal(str) # 加载javdb cookie文本内容到设置页面
    set_dmm_cookie = Signal(str) # 加载javdb cookie文本内容到设置页面


    def __init__(self, parent=None):
        super(MyMAinWindow, self).__init__(parent)
        self.Ui = Ui_AVDV()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.Init_Ui()
        self.set_style()
        self.pushButton_main_clicked()
        # 初始化需要的变量
        # self.version = '3.963'
        self.localversion = '20210619'
        self.Ui.label_show_version.setText('version ' + self.localversion)
        self.Ui.label_show_version.mousePressEvent = self.version_clicked
        self.laberl_number_url = ''
        self.Ui.label_number.mousePressEvent = self.label_number_clicked
        self.Ui.label_source.mousePressEvent = self.label_number_clicked
        self.soft_path = os.getcwd()
        self.default_poster = self.soft_path + resource_path('/Img/default-poster.jpg')
        self.default_thumb = self.soft_path + resource_path('/Img/default-thumb.jpg')
        self.m_drag = False
        self.m_DragPosition = 0
        self.count_claw = 0  # 批量刮削次数
        self.item_succ = self.Ui.treeWidget_number.topLevelItem(0)
        self.item_fail = self.Ui.treeWidget_number.topLevelItem(1)
        self.select_file_path = ''
        self.json_array = {}
        self.current_proxy = ''  # 代理设置
        self.Init()
        self.Load_Config()
        self.Ui.label_filepath.setText('🎈 设置视频目录（设置-目录设置-视频目录），然后点击开始！\n')
        self.show_version() # 启动后在【日志】页面显示版本信息
        self.new_proxy = self.check_proxyChange()
        self.add_net_text_main('\n🏠 代理设置在:【设置】 - 【网络设置】 - 【代理设置】。\n') 
        self.show_netstatus(self.new_proxy) # 启动后在【检测网络】页面显示网络代理情况
        self.add_net_text_main('\n\n点击 【开始检测】以测试网络连通性。')
        self.UpdateCheck_start() # 检查更新


    def Init_Ui(self):
        ico_path = resource_path('Img/AVDC-ico.png')
        # if os.path.exists('AVDC-ico.png'):
        #     ico_path = 'AVDC-ico.png'
        # elif os.path.exists('Img/AVDC-ico.png'):
        #     ico_path = 'Img/AVDC-ico.png'
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
        self.set_dmm_cookie.connect(self.Ui.plainTextEdit_cookie_dmm.setPlainText)
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
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
                    background:#336699;
                    border-right:1px solid gray;
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
                    border:0px solid rgba(0, 0, 0, 80);
            }
            QLabel#label_filepath{
                    font-size:16px;
                    color: black;
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
        # 设置页
        self.Ui.page_setting.setStyleSheet(
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
                    font-size:13px;
            }
            ''')
        # 整个页面
        self.Ui.centralwidget.setStyleSheet(
            '''
            * {
                    font-family:Courier;
                    font-size:13px;
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
            QPushButton#pushButton_start_cap,#pushButton_init_config,#pushButton_start_cap2,#pushButton_check_net,#pushButton_move_mp4,#pushButton_select_file,#pushButton_add_actor_pic,#pushButton_select_thumb,#pushButton_save_config,#pushButton_start_single_file,#pushButton_show_pic_actor{
                    color:white;
                    font-size:14px;
                    background-color:#0066CC;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton:hover#pushButton_start_cap,:hover#pushButton_start_cap2,:hover#pushButton_check_net,:hover#pushButton_move_mp4,:hover#pushButton_select_file,:hover#pushButton_add_actor_pic,:hover#pushButton_select_thumb,:hover#pushButton_save_config,:hover#pushButton_init_config,:hover#pushButton_start_single_file,:hover#pushButton_show_pic_actor{
                    color:white;
                    background-color:#4C6EFF;
                    font-weight:bold;
                }
            QPushButton:pressed#pushButton_start_cap,:pressed#pushButton_start_cap2,:pressed#pushButton_check_net,:pressed#pushButton_move_mp4,:pressed#pushButton_select_file,:pressed#pushButton_add_actor_pic,:pressed#pushButton_select_thumb,:pressed#pushButton_save_config,:pressed#pushButton_init_config,:pressed#pushButton_start_single_file,:pressed#pushButton_show_pic_actor{
                    background-color:#4C6EE0;
                    border-color:black;
                    border-width:12px;
                    font-weight:bold;
            }
            QProgressBar::chunk{
                    background-color: #336699;
                    width: 5px; /*区块宽度*/
                    margin: 0.5px;
            }
            ''')

    # ========================================================================按钮点击事件
    def Init(self):
        # self.Ui.stackedWidget.setCurrentIndex(0)
        self.Ui.treeWidget_number.clicked.connect(self.treeWidget_number_clicked)
        self.Ui.pushButton_close.clicked.connect(self.close_win)
        # self.Ui.pushButton_min.clicked.connect(self.min_win)
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
        self.Ui.pushButton_check_net.clicked.connect(self.NetCheck)
        self.Ui.pushButton_add_actor_pic.clicked.connect(self.pushButton_add_actor_pic_clicked)
        self.Ui.pushButton_show_pic_actor.clicked.connect(self.pushButton_show_pic_actor_clicked)
        self.Ui.pushButton_select_thumb.clicked.connect(self.pushButton_select_thumb_clicked)
        self.Ui.pushButton_log.clicked.connect(self.pushButton_show_log_clicked)
        self.Ui.pushButton_net.clicked.connect(self.pushButton_show_net_clicked)
        self.Ui.pushButton_start_single_file.clicked.connect(self.pushButton_start_single_file_clicked)
        self.Ui.checkBox_cover.stateChanged.connect(self.cover_change)
        self.Ui.horizontalSlider_timeout.valueChanged.connect(self.lcdNumber_timeout_change)
        self.Ui.horizontalSlider_retry.valueChanged.connect(self.lcdNumber_retry_change)
        self.Ui.horizontalSlider_mark_size.valueChanged.connect(self.lcdNumber_mark_size_change)

    # ========================================================================显示版本号
    def show_version(self):
        self.add_text_main('[*]' + 'AVDCx'.center(80, '='))
        self.add_text_main('[*]' + ('Current Version: ' + self.localversion).center(80))
        self.add_text_main('[*]' + '基于项目 https://github.com/moyy996/AVDC 修改'.center(80))
        self.add_text_main('[*]' + '报告问题 https://github.com/Hermit10/temp/issues'.center(80))
        self.add_text_main('[*]================================================================================')

    def version_clicked(self, test):
        webbrowser.open('https://github.com/Hermit10/temp/releases')

    def label_number_clicked(self, test):
        if self.laberl_number_url:
            webbrowser.open(self.laberl_number_url)


    # ========================================================================鼠标拖动窗口
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

    # ========================================================================左侧按钮点击事件响应函数
    def close_win(self):
        config_file = 'config.ini'
        config = RawConfigParser()
        config.read(config_file, encoding='UTF-8')
        show_poster = int(config.get('common', 'show_poster'))

        if bool(self.Ui.checkBox_cover.isChecked()) != bool(show_poster):
            if self.Ui.checkBox_cover.isChecked():
                config.set('common', 'show_poster', 1)
            else:
                config.set('common', 'show_poster', 0)
            code = open(config_file, 'w')
            config.write(code)    
            code.close()
        os._exit(0)


    def min_win(self):
        self.setWindowState(Qt.WindowMinimized)

    def pushButton_main_clicked(self):
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

    def pushButton_show_log_clicked(self):
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


    def pushButton_tool_clicked(self):
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

    def pushButton_setting_clicked(self):
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

    def pushButton_about_clicked(self):
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
            t = threading.Thread(target=self.AVDC_Main)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_start_cap_clicked: ' + str(error_info))

    # ========================================================================恢复默认config.ini
    def pushButton_init_config_clicked(self):
        self.Ui.pushButton_init_config.setEnabled(False)
        try:
            t = threading.Thread(target=self.init_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_init_config_clicked: ' + str(error_info))

    def init_config_clicked(self):
        json_config = {
            'show_poster': 1,
            'main_mode': 1,
            'soft_link': 0,
            'switch_debug': 1,
            'failed_file_move': 1,
            'update_check': 1,
            'save_log': 1,
            'website': 'all',
            'failed_output_folder': 'failed',
            'success_output_folder': 'JAV_output',
            'type': 'no',
            'proxy': '127.0.0.1:7890',
            'timeout': 10,
            'retry': 3,
            'javdb': '',
            'dmm': '',
            'folder_name': 'actor/number actor',
            'naming_media': 'number title',
            'naming_file': 'number',
            'folder_name_C': 1,
            'literals': '\()',
            'folders': 'JAV_output',
            'string': '1080p,720p,22-sht.me,-HD',
            'emby_url': '192.168.5.191:8096',
            'api_key': 'cb83900340b447fab785cb628a99c3da',
            'media_path': '',
            'media_type': '.mp4|.avi|.rmvb|.wmv|.mov|.mkv|.flv|.ts|.webm|.MP4|.AVI|.RMVB|.WMV|.MOV|.MKV|.FLV|.TS|.WEBM',
            'sub_type': '.smi|.srt|.idx|.sub|.sup|.psb|.ssa|.ass|.txt|.usf|.xss|.ssf|.rt|.lrc|.sbv|.vtt|.ttml',
            'poster_mark': 1,
            'thumb_mark': 1,
            'mark_size': 5,
            'mark_type': 'SUB,LEAK,UNCENSORED',
            'mark_pos': 'top_left',
            'uncensored_poster': 0,
            'uncensored_prefix': 'S2M|BT|LAF|SMD',
            'nfo_download': 1,
            'poster_download': 1,
            'fanart_download': 1,
            'thumb_download': 1,
            'extrafanart_download': 0,
            'extrafanart_folder': 'extrafanart',
        }
        save_config(json_config)
        self.check_proxyChange()
        self.Load_Config()
        self.Ui.pushButton_init_config.setEnabled(True)

    # ========================================================================加载config
    def Load_Config(self):
        config_file = 'config.ini'
        if os.path.exists(config_file):
            config = RawConfigParser()
            try:
                config.read(config_file, encoding='UTF-8')
                # ========================================================================common
                if int(config['common']['main_mode']) == 1:
                    self.Ui.radioButton_common.setChecked(True)
                elif int(config['common']['main_mode']) == 2:
                    self.Ui.radioButton_sort.setChecked(True)
                if int(config['common']['soft_link']) == 1:
                    self.Ui.radioButton_soft_on.setChecked(True)
                elif int(config['common']['soft_link']) == 0:
                    self.Ui.radioButton_soft_off.setChecked(True)
                if int(config['common']['failed_file_move']) == 1:
                    self.Ui.radioButton_fail_move_on.setChecked(True)
                elif int(config['common']['failed_file_move']) == 0:
                    self.Ui.radioButton_fail_move_off.setChecked(True)
                if int(config['common']['show_poster']) == 1:
                    self.Ui.checkBox_cover.setChecked(True)
                    self.cover_flag = True
                elif int(config['common']['show_poster']) == 0:
                    self.Ui.checkBox_cover.setChecked(False)
                    self.cover_flag = False
                if config['common']['website'] == 'all':
                    self.Ui.comboBox_website_all.setCurrentIndex(0)
                elif config['common']['website'] == 'javbus':
                    self.Ui.comboBox_website_all.setCurrentIndex(1)
                elif config['common']['website'] == 'javdb':
                    self.Ui.comboBox_website_all.setCurrentIndex(2)
                elif config['common']['website'] == 'jav321':
                    self.Ui.comboBox_website_all.setCurrentIndex(3)
                elif config['common']['website'] == 'dmm':
                    self.Ui.comboBox_website_all.setCurrentIndex(4)
                elif config['common']['website'] == 'avsox':
                    self.Ui.comboBox_website_all.setCurrentIndex(5)
                elif config['common']['website'] == 'xcity':
                    self.Ui.comboBox_website_all.setCurrentIndex(6)
                elif config['common']['website'] == 'mgstage':
                    self.Ui.comboBox_website_all.setCurrentIndex(7)
                elif config['common']['website'] == 'fc2hub':
                    self.Ui.comboBox_website_all.setCurrentIndex(8)

                # ========================================================================proxy
                if config['proxy']['type'] == 'no' or config['proxy']['type'] == '':
                    self.Ui.radioButton_proxy_nouse.setChecked(True)
                elif config['proxy']['type'] == 'http':
                    self.Ui.radioButton_proxy_http.setChecked(True)
                elif config['proxy']['type'] == 'socks5':
                    self.Ui.radioButton_proxy_socks5.setChecked(True)
                self.Ui.lineEdit_proxy.setText(config['proxy']['proxy'])
                self.Ui.horizontalSlider_timeout.setValue(int(config['proxy']['timeout']))
                self.Ui.horizontalSlider_retry.setValue(int(config['proxy']['retry']))
                # ========================================================================Cookies
                self.set_javdb_cookie.emit(config['Cookies']['javdb'])
                self.set_dmm_cookie.emit(config['Cookies']['dmm'])
                # ========================================================================Name_Rule
                self.Ui.lineEdit_dir_name.setText(config['Name_Rule']['folder_name'])
                self.Ui.lineEdit_media_name.setText(config['Name_Rule']['naming_media'])
                self.Ui.lineEdit_local_name.setText(config['Name_Rule']['naming_file'])
                # ========================================================================update
                if int(config['update']['update_check']) == 1:
                    self.Ui.radioButton_update_on.setChecked(True)
                elif int(config['update']['update_check']) == 0:
                    self.Ui.radioButton_update_off.setChecked(True)
                # ========================================================================folder_name_C
                if int(config['Name_Rule']['folder_name_C']) == 1:
                    self.Ui.radioButton_foldername_C_on.setChecked(True)
                elif int(config['Name_Rule']['folder_name_C']) == 0:
                    self.Ui.radioButton_foldername_C_off.setChecked(True)
                # ========================================================================log
                if int(config['log']['save_log']) == 1:
                    self.Ui.radioButton_log_on.setChecked(True)
                elif int(config['log']['save_log']) == 0:
                    self.Ui.radioButton_log_off.setChecked(True)
                # ========================================================================media
                self.Ui.lineEdit_movie_path.setText(str(config['media']['media_path']).replace('\\', '/'))
                self.Ui.lineEdit_movie_type.setText(config['media']['media_type'])
                self.Ui.lineEdit_sub_type.setText(config['media']['sub_type'])
                self.Ui.lineEdit_success.setText(config['media']['success_output_folder'])
                self.Ui.lineEdit_fail.setText(config['media']['failed_output_folder'])
                # ========================================================================escape
                self.Ui.lineEdit_escape_dir.setText(config['escape']['folders'])
                self.Ui.lineEdit_escape_char.setText(config['escape']['literals'])
                self.Ui.lineEdit_escape_dir_move.setText(config['escape']['folders'])
                self.Ui.lineEdit_escape_string.setText(config['escape']['string'])
                # ========================================================================debug_mode
                if int(config['debug_mode']['switch']) == 1:
                    self.Ui.radioButton_debug_on.setChecked(True)
                elif int(config['debug_mode']['switch']) == 0:
                    self.Ui.radioButton_debug_off.setChecked(True)
                # ========================================================================emby
                self.Ui.lineEdit_emby_url.setText(config['emby']['emby_url'])
                self.Ui.lineEdit_api_key.setText(config['emby']['api_key'])
                # ========================================================================mark
                if int(config['mark']['poster_mark']) == 1:
                    self.Ui.radioButton_poster_mark_on.setChecked(True)
                elif int(config['mark']['poster_mark']) == 0:
                    self.Ui.radioButton_poster_mark_off.setChecked(True)
                if int(config['mark']['thumb_mark']) == 1:
                    self.Ui.radioButton_thumb_mark_on.setChecked(True)
                elif int(config['mark']['thumb_mark']) == 0:
                    self.Ui.radioButton_thumb_mark_off.setChecked(True)
                self.Ui.horizontalSlider_mark_size.setValue(int(config['mark']['mark_size']))
                if 'SUB' in str(config['mark']['mark_type']).upper():
                    self.Ui.checkBox_sub.setChecked(True)
                if 'LEAK' in str(config['mark']['mark_type']).upper():
                    self.Ui.checkBox_leak.setChecked(True)
                if 'UNCENSORED' in str(config['mark']['mark_type']).upper():
                    self.Ui.checkBox_uncensored.setChecked(True)
                if 'top_left' == config['mark']['mark_pos']:
                    self.Ui.radioButton_top_left.setChecked(True)
                elif 'bottom_left' == config['mark']['mark_pos']:
                    self.Ui.radioButton_bottom_left.setChecked(True)
                elif 'top_right' == config['mark']['mark_pos']:
                    self.Ui.radioButton_top_right.setChecked(True)
                elif 'bottom_right' == config['mark']['mark_pos']:
                    self.Ui.radioButton_bottom_right.setChecked(True)
                # ========================================================================uncensored
                if int(config['uncensored']['uncensored_poster']) == 1:
                    self.Ui.radioButton_poster_cut.setChecked(True)
                elif int(config['uncensored']['uncensored_poster']) == 0:
                    self.Ui.radioButton_poster_official.setChecked(True)
                self.Ui.lineEdit_uncensored_prefix.setText(config['uncensored']['uncensored_prefix'])
                # ========================================================================file_download
                if int(config['file_download']['nfo']) == 1:
                    self.Ui.checkBox_download_nfo.setChecked(True)
                elif int(config['file_download']['nfo']) == 0:
                    self.Ui.checkBox_download_nfo.setChecked(False)
                if int(config['file_download']['poster']) == 1:
                    self.Ui.checkBox_download_poster.setChecked(True)
                elif int(config['file_download']['poster']) == 0:
                    self.Ui.checkBox_download_poster.setChecked(False)
                if int(config['file_download']['fanart']) == 1:
                    self.Ui.checkBox_download_fanart.setChecked(True)
                elif int(config['file_download']['fanart']) == 0:
                    self.Ui.checkBox_download_fanart.setChecked(False)
                if int(config['file_download']['thumb']) == 1:
                    self.Ui.checkBox_download_thumb.setChecked(True)
                elif int(config['file_download']['thumb']) == 0:
                    self.Ui.checkBox_download_thumb.setChecked(False)
                # ========================================================================extrafanart
                if int(config['extrafanart']['extrafanart_download']) == 1:
                    self.Ui.radioButton_extrafanart_download_on.setChecked(True)
                elif int(config['extrafanart']['extrafanart_download']) == 0:
                    self.Ui.radioButton_extrafanart_download_off.setChecked(True)
                self.Ui.lineEdit_extrafanart_dir.setText(config['extrafanart']['extrafanart_folder'])
            except:
                self.add_text_main('config.ini is corrupt, and has been reset now.\n')
                return self.init_config_clicked()
        else:
            # ini不存在，重新创建
            self.add_text_main('Create config file: config.ini\n')
            self.init_config_clicked()

    def check_proxyChange(self):             # 检测代理变化
        config_file = 'config.ini'
        config = RawConfigParser()
        config.read(config_file, encoding='UTF-8')
        proxy_type = config.get('proxy', 'type')
        proxy = config.get('proxy', 'proxy')
        timeout = config.getint('proxy', 'timeout')
        retry_count = config.getint('proxy', 'retry')
        self.new_proxy = (proxy_type, proxy, timeout, retry_count)
        if self.current_proxy:        
            if self.new_proxy != self.current_proxy:
                self.add_net_text_main('\n🌈 代理设置已改变：')
                self.show_netstatus(self.new_proxy)
        self.current_proxy = self.new_proxy
        return self.new_proxy

    # ========================================================================读取设置页设置, 保存在config.ini
    def pushButton_save_config_clicked(self):
        try:
            t = threading.Thread(target=self.save_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_save_config_clicked: ' + str(error_info))

    def save_config_clicked(self):
        main_mode = 1
        failed_file_move = 1
        soft_link = 0
        show_poster = 0
        switch_debug = 0
        update_check = 0
        folder_name_C = 0
        save_log = 0
        website = ''
        add_mark = 1
        mark_size = 3
        mark_type = ''
        mark_pos = ''
        uncensored_poster = 0
        nfo_download = 0
        poster_download = 0
        fanart_download = 0
        thumb_download = 0
        extrafanart_download = 0
        extrafanart_folder = ''
        proxy_type = ''
        # ========================================================================common
        if self.Ui.radioButton_common.isChecked():  # 普通模式
            main_mode = 1
        elif self.Ui.radioButton_sort.isChecked():  # 整理模式
            main_mode = 2
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
        if self.Ui.radioButton_foldername_C_on.isChecked():  # 文件夹加-C
            folder_name_C = 1
        elif self.Ui.radioButton_foldername_C_off.isChecked():  # 文件夹不加-C
            folder_name_C = 0
        if self.Ui.radioButton_log_on.isChecked():  # 开启日志
            save_log = 1
        elif self.Ui.radioButton_log_off.isChecked():  # 关闭日志
            save_log = 0
        if self.Ui.checkBox_cover.isChecked():  # 显示封面
            show_poster = 1
        else:  # 关闭封面
            show_poster = 0
        if self.Ui.radioButton_fail_move_on.isChecked():  # 失败移动开
            failed_file_move = 1
        elif self.Ui.radioButton_fail_move_off.isChecked():  # 失败移动关
            failed_file_move = 0
        if self.Ui.comboBox_website_all.currentText() == 'All websites':  # all
            website = 'all'
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
        elif self.Ui.comboBox_website_all.currentText() == 'fc2hub':  # fc2hub
            website = 'fc2hub'
        # ========================================================================proxy
        if self.Ui.radioButton_proxy_http.isChecked():  # http proxy
            proxy_type = 'http'
        elif self.Ui.radioButton_proxy_socks5.isChecked():  # socks5 proxy
            proxy_type = 'socks5'
        elif self.Ui.radioButton_proxy_nouse.isChecked():  # nouse proxy
            proxy_type = 'no'
        # ========================================================================水印
        if self.Ui.radioButton_poster_mark_on.isChecked():  # 封面添加水印
            poster_mark = 1
        else:  # 关闭封面添加水印
            poster_mark = 0
        if self.Ui.radioButton_thumb_mark_on.isChecked():  # 缩略图添加水印
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
        if self.Ui.radioButton_poster_official.isChecked():  # 官方
            uncensored_poster = 0
        elif self.Ui.radioButton_poster_cut.isChecked():  # 裁剪
            uncensored_poster = 1
        # ========================================================================下载文件，剧照
        if self.Ui.checkBox_download_nfo.isChecked():
            nfo_download = 1
        else:
            nfo_download = 0
        if self.Ui.checkBox_download_poster.isChecked():
            poster_download = 1
        else:
            poster_download = 0
        if self.Ui.checkBox_download_fanart.isChecked():
            fanart_download = 1
        else:
            fanart_download = 0
        if self.Ui.checkBox_download_thumb.isChecked():
            thumb_download = 1
        else:
            thumb_download = 0
        if self.Ui.radioButton_extrafanart_download_on.isChecked():  # 下载剧照
            extrafanart_download = 1
        else:  # 关闭封面
            extrafanart_download = 0
        json_config = {
            'main_mode': main_mode,
            'soft_link': soft_link,
            'switch_debug': switch_debug,
            'show_poster': show_poster,
            'failed_file_move': failed_file_move,
            'update_check': update_check,
            'folder_name_C': folder_name_C,
            'save_log': save_log,
            'website': website,
            'type': proxy_type,
            'proxy': self.Ui.lineEdit_proxy.text(),
            'timeout': self.Ui.horizontalSlider_timeout.value(),
            'retry': self.Ui.horizontalSlider_retry.value(),
            'javdb': self.Ui.plainTextEdit_cookie_javdb.toPlainText(),
            'dmm': self.Ui.plainTextEdit_cookie_dmm.toPlainText(),
            'folder_name': self.Ui.lineEdit_dir_name.text(),
            'naming_media': self.Ui.lineEdit_media_name.text(),
            'naming_file': self.Ui.lineEdit_local_name.text(),
            'literals': self.Ui.lineEdit_escape_char.text(),
            'folders': self.Ui.lineEdit_escape_dir.text(),
            'string': self.Ui.lineEdit_escape_string.text(),
            'emby_url': self.Ui.lineEdit_emby_url.text(),
            'api_key': self.Ui.lineEdit_api_key.text(),
            'media_path': self.Ui.lineEdit_movie_path.text(),
            'media_type': self.Ui.lineEdit_movie_type.text(),
            'sub_type': self.Ui.lineEdit_sub_type.text(),
            'failed_output_folder': self.Ui.lineEdit_fail.text(),
            'success_output_folder': self.Ui.lineEdit_success.text(),
            'poster_mark': poster_mark,
            'thumb_mark': thumb_mark,
            'mark_size': self.Ui.horizontalSlider_mark_size.value(),
            'mark_type': mark_type.strip(','),
            'mark_pos': mark_pos,
            'uncensored_poster': uncensored_poster,
            'uncensored_prefix': self.Ui.lineEdit_uncensored_prefix.text(),
            'nfo_download': nfo_download,
            'poster_download': poster_download,
            'fanart_download': fanart_download,
            'thumb_download': thumb_download,
            'extrafanart_download': extrafanart_download,
            'extrafanart_folder': self.Ui.lineEdit_extrafanart_dir.text(),
        }
        save_config(json_config)
        self.check_proxyChange()

    # ========================================================================小工具-单视频刮削
    def pushButton_select_file_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        filepath, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取视频文件", path, "Movie Files(*.mp4 "
                                                                                         "*.avi *.rmvb *.wmv "
                                                                                         "*.mov *.mkv *.flv *.ts "
                                                                                         "*.webm *.MP4 *.AVI "
                                                                                         "*.RMVB *.WMV *.MOV "
                                                                                         "*.MKV *.FLV *.TS "
                                                                                         "*.WEBM);;All Files(*)")
        self.select_file_path = filepath

    def pushButton_start_single_file_clicked(self):
        if self.select_file_path != '':
            # self.Ui.stackedWidget.setCurrentIndex(1) # 点击刮削按钮后跳转到日志页面, 日志页面是1, 主界面是0
            self.pushButton_main_clicked() # 点击刮削按钮后跳转到主页面
            try:
                t = threading.Thread(target=self.select_file_thread)
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_start_single_file_clicked: ' + str(error_info))

    def select_file_thread(self):
        file_name = self.select_file_path
        if len(file_name) > 55:     # 截断路径长度，以方便在主界面显示路径时能看到后面的文件名
            show_filepath = file_name[-55:]
            show_filepath = '...' + show_filepath[show_filepath.find('/'):]
            if len(show_filepath) < 25:
                show_filepath = '...' + file_name[-45:]
        else:
            show_filepath = file_name
        file_root = os.getcwd().replace("\\\\", "/").replace("\\", "/")
        file_path = file_name.replace(file_root, '.').replace("\\\\", "/").replace("\\", "/")
        # 获取去掉拓展名的文件名做为番号
        file_name = os.path.splitext(file_name.split('/')[-1])[0]
        mode = self.Ui.comboBox_website.currentIndex() + 1
        # 指定的网址
        appoint_url = self.Ui.lineEdit_appoint_url.text()
        appoint_number = self.Ui.lineEdit_movie_number.text()
        self.count_claw += 1
        count = 0
        succ_count = 0
        fail_count = 0
        count += 1
        json_data= ''
        self.Ui.label_result.setText('成功：%s  失败：%s' % (succ_count, fail_count))
        percentage = str(count / int(count) * 100)[:4] + '%'
        value = int(count / int(count) * 100)
        self.progressBarValue.emit(int(value))
        self.add_text_main('[*]' + '='*80)
        self.add_text_main('[!]Round (' + str(self.count_claw) + ') - [' + str(count) + '/' + str(count) + '] - ' + percentage)
        self.add_text_main('[*]' + '='*80)
        self.Ui.label_filepath.setText( '当前：' + str(count) + '/' + str(1) + ' ' + str(value) + '% 正在刮削：\n' + show_filepath)
        try:
            if appoint_number:
                file_name = appoint_number
            else:
                if '-CD' in file_name or '-cd' in file_name:
                    part = ''
                    if re.search('-CD\d+', file_name):
                        part = re.findall('-CD\d+', file_name)[0]
                    elif re.search('-cd\d+', file_name):
                        part = re.findall('-cd\d+', file_name)[0]
                    file_name = file_name.replace(part, '')
                if '-c.' in file_path or '-C.' in file_path:
                    file_name = file_name[0:-2]
                if '-uncensored' in file_path or '-UNCENSORED' in file_path:
                    file_name = file_name.upper().replace('-UNCENSORED', '')
            self.add_text_main("[!]Making Data for   [" + file_path + "], the number is [" + file_name + "]")

            result, json_data, succ_count, fail_count = self.Core_Main(file_path, file_name, mode, count, succ_count, fail_count, appoint_url)

            # self.Core_Main(file_path, file_name, mode, 0, appoint_url)
        except Exception as error_info:
            fail_count += 1
            fail_showName = str(self.count_claw) + '-' + str(fail_count) + '.' + os.path.splitext(file_path.split('/')[-1])[0]
            self.ShowListName(fail_showName, 'fail', json_data, file_name)
            self.add_text_main('[-]Error in select_file_thread: ' + str(error_info))
        self.add_text_main("[*]================================================================================")
        self.Ui.label_result.setText('成功：%s  失败：%s' % (succ_count, fail_count))
        self.progressBarValue.emit(100)
        self.Ui.label_filepath.setText('🎉 恭喜！全部刮削完成！')

    # ========================================================================小工具-裁剪封面图
    def pushButton_select_thumb_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取缩略图", path,
                                                                   "Picture Files(*.jpg);;All Files(*)")
        if filePath != '':
            self.Ui.stackedWidget.setCurrentIndex(1)
            try:
                t = threading.Thread(target=self.select_thumb_thread, args=(filePath,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_select_thumb_clicked: ' + str(error_info))

    def select_thumb_thread(self, file_path):
        file_name = file_path.split('/')[-1]
        file_path = file_path.replace('/' + file_name, '')
        self.image_cut(file_path, file_name, 2)
        self.add_text_main("[*]================================================================================")

    def image_cut(self, path, file_name, mode=1):
        png_name = file_name.replace('-thumb.jpg', '-poster.jpg')
        file_path = os.path.join(path, file_name)
        png_path = os.path.join(path, png_name)
        try:
            if os.path.exists(png_path):
                os.remove(png_path)
        except Exception as error_info:
            self.add_text_main('[-]Error in image_cut: ' + str(error_info))
            return

        """ 获取图片分辨率 """
        im = Image.open(file_path)  # 返回一个Image对象
        width, height = im.size
        """ 读取图片 """
        with open(file_path, 'rb') as fp:
            image = fp.read()
        ex, ey, ew, eh = 0, 0, 0, 0
        """ 获取裁剪区域 """
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
        fp = open(file_path, 'rb')
        img = Image.open(fp)
        img = img.convert('RGB')
        img_new_png = img.crop((ex, ey, ew + ex, eh + ey))
        fp.close()
        img_new_png.save(png_path)
        self.add_text_main('[+]Poster Cut         ' + png_name + ' from ' + file_name + '!')
        if mode == 2:
            pix = QPixmap(file_path)
            self.Ui.label_thumb.setScaledContents(True)
            self.Ui.label_thumb.setPixmap(pix)  # 添加图标
            pix = QPixmap(png_path)
            self.Ui.label_poster.setScaledContents(True)
            self.Ui.label_poster.setPixmap(pix)  # 添加图标

    # ========================================================================小工具-视频移动
    def move_file(self):
        # self.Ui.stackedWidget.setCurrentIndex(1)
        self.pushButton_show_log_clicked() # 点击开始移动按钮后跳转到日志页面
        try:
            t = threading.Thread(target=self.move_file_thread)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in move_file: ' + str(error_info))

    def move_file_thread(self):
        movie_path = self.Ui.lineEdit_movie_path.text()
        escape_dir = self.Ui.lineEdit_escape_dir_move.text()
        movie_type = self.Ui.lineEdit_movie_type.text()
        sub_type = self.Ui.lineEdit_sub_type.text().split('|')
        if not movie_path:  # 没有输入视频目录时，获取程序当前路径
            movie_path = os.path.abspath(".")
        movie_list = movie_lists(escape_dir, movie_type, movie_path)
        des_path = movie_path + '/Movie_moved'
        print(des_path)
        if not os.path.exists(des_path):
            self.add_text_main('[+]Created folder Movie_moved!')
            os.makedirs(des_path)
        self.add_text_main('[+]Move Movies Start!')
        for movie in movie_list:
            if des_path in movie:
                continue
            sour = movie
            des = des_path + '/' + sour.split('/')[-1]
            try:
                shutil.move(sour, des)
                self.add_text_main('   [+]Move ' + sour.split('/')[-1] + ' to Movie_moved Success!')
                path_old = sour.replace(sour.split('/')[-1], '')
                filename = sour.split('/')[-1].split('.')[0]
                for sub in sub_type:
                    if os.path.exists(path_old + '/' + filename + sub):  # 字幕移动
                        shutil.move(path_old + '/' + filename + sub, des_path + '/' + filename + sub)
                        self.add_text_main('   [+]Sub moved! ' + filename + sub)
            except Exception as error_info:
                self.add_text_main('[-]Error in move_file_thread: ' + str(error_info))
        self.add_text_main("[+]Move Movies All Finished!!!")
        self.add_text_main("[*]================================================================================")

    # ========================================================================小工具-emby女优头像
    def pushButton_add_actor_pic_clicked(self):  # 添加头像按钮响应
        self.Ui.stackedWidget.setCurrentIndex(1)
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.add_text_main('[-]The emby_url is empty!')
            self.add_text_main("[*]================================================================================")
            return
        elif api_key == '':
            self.add_text_main('[-]The api_key is empty!')
            self.add_text_main("[*]================================================================================")
            return
        try:
            t = threading.Thread(target=self.found_profile_picture, args=(1,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_add_actor_pic_clicked: ' + str(error_info))

    def pushButton_show_pic_actor_clicked(self):  # 查看按钮响应
        # self.Ui.stackedWidget.setCurrentIndex(1)
        self.pushButton_show_log_clicked() # 点击查看按钮后跳转到日志页面
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.add_text_main('[-]The emby_url is empty!')
            self.add_text_main("[*]================================================================================")
            return
        elif api_key == '':
            self.add_text_main('[-]The api_key is empty!')
            self.add_text_main("[*]================================================================================")
            return
        if self.Ui.comboBox_pic_actor.currentIndex() == 0:  # 可添加头像的女优
            try:
                t = threading.Thread(target=self.found_profile_picture, args=(2,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_show_pic_actor_clicked: ' + str(error_info))
        else:
            try:
                t = threading.Thread(target=self.show_actor, args=(self.Ui.comboBox_pic_actor.currentIndex(),))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_show_pic_actor_clicked: ' + str(error_info))

    def show_actor(self, mode):  # 按模式显示相应列表
        if mode == 1:  # 没有头像的女优
            self.add_text_main('[+]没有头像的女优!')
        elif mode == 2:  # 有头像的女优
            self.add_text_main('[+]有头像的女优!')
        elif mode == 3:  # 所有女优
            self.add_text_main('[+]所有女优!')
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.add_text_main("[*]================================================================================")
            return
        count = 1
        actor_list_temp = ''
        for actor in actor_list['Items']:
            if mode == 3:  # 所有女优
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            elif mode == 2 and actor['ImageTags'] != {}:  # 有头像的女优
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            elif mode == 1 and actor['ImageTags'] == {}:  # 没有头像的女优
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            if (count - 1) % 5 == 0 and actor_list_temp != '':
                self.add_text_main('[+]' + actor_list_temp)
                actor_list_temp = ''
        self.add_text_main("[*]================================================================================")

    def get_emby_actor_list(self):  # 获取emby的演员列表
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        emby_url = emby_url.replace('：', ':')
        url = 'http://' + emby_url + '/emby/Persons?api_key=' + api_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/60.0.3100.0 Safari/537.36'}
        actor_list = {}
        try:
            getweb = requests.get(str(url), headers=headers, timeout=10)
            getweb.encoding = 'utf-8'
            actor_list = json.loads(getweb.text)
        except:
            self.add_text_main('[-]Error! Check your emby_url or api_key!')
            actor_list['TotalRecordCount'] = 0
        return actor_list

    def found_profile_picture(self, mode):  # mode=1, 上传头像, mode=2, 显示可添加头像的女优
        if mode == 1:
            self.add_text_main('[+]Start upload profile pictures!')
        elif mode == 2:
            self.add_text_main('[+]可添加头像的女优!')
        path = 'Actor'
        if not os.path.exists(path):
            self.add_text_main('[+]Actor folder not exist!')
            self.add_text_main("[*]================================================================================")
            return
        path_success = 'Actor/Success'
        if not os.path.exists(path_success):
            os.makedirs(path_success)
        profile_pictures = os.listdir(path)
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.add_text_main("[*]================================================================================")
            return
        count = 1
        for actor in actor_list['Items']:
            flag = 0
            pic_name = ''
            if actor['Name'] + '.jpg' in profile_pictures:
                flag = 1
                pic_name = actor['Name'] + '.jpg'
            elif actor['Name'] + '.png' in profile_pictures:
                flag = 1
                pic_name = actor['Name'] + '.png'
            if flag == 0:
                byname_list = re.split('[,，()（）]', actor['Name'])
                for byname in byname_list:
                    if byname + '.jpg' in profile_pictures:
                        pic_name = byname + '.jpg'
                        flag = 1
                        break
                    elif byname + '.png' in profile_pictures:
                        pic_name = byname + '.png'
                        flag = 1
                        break
            if flag == 1 and (actor['ImageTags'] == {} or not os.path.exists(path_success + '/' + pic_name)):
                if mode == 1:
                    try:
                        self.upload_profile_picture(count, actor, path + '/' + pic_name)
                        shutil.copy(path + '/' + pic_name, path_success + '/' + pic_name)
                    except Exception as error_info:
                        self.add_text_main('[-]Error in found_profile_picture! ' + str(error_info))
                else:
                    self.add_text_main('[+]' + "%4s" % str(count) + '.Actor name: ' + actor['Name'] + '  Pic name: '
                                       + pic_name)
                count += 1
        if count == 1:
            self.add_text_main('[-]NO profile picture can be uploaded!')
        self.add_text_main("[*]================================================================================")

    def upload_profile_picture(self, count, actor, pic_path):  # 上传头像
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        emby_url = emby_url.replace('：', ':')
        try:
            f = open(pic_path, 'rb')  # 二进制方式打开图文件
            b6_pic = base64.b64encode(f.read())  # 读取文件内容, 转换为base64编码
            f.close()
            url = 'http://' + emby_url + '/emby/Items/' + actor['Id'] + '/Images/Primary?api_key=' + api_key
            if pic_path.endswith('jpg'):
                header = {"Content-Type": 'image/png', }
            else:
                header = {"Content-Type": 'image/jpeg', }
            requests.post(url=url, data=b6_pic, headers=header)
            self.add_text_main(
                '[+]' + "%4s" % str(count) + '.Success upload profile picture for ' + actor['Name'] + '!')
        except Exception as error_info:
            self.add_text_main('[-]Error in upload_profile_picture! ' + str(error_info))

    # ========================================================================自定义文件名
    def get_naming_rule(self, json_data):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        if len(actor.split(',')) >= 10:  # 演员过多取前五个
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        name_file = json_data['naming_file'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                       year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        name_file = name_file.replace('//', '/').replace('--', '-').strip('-')
        if len(name_file) > 100:  # 文件名过长 取标题前70个字符
            self.add_text_main('[-]提示：标题名过长，取前70个字作为标题!')
            name_file = name_file.replace(title, title[0:70])
        return name_file

    # ========================================================================语句添加到日志框
    def add_text_main(self, text):
        if self.Ui.radioButton_log_on.isChecked():
            try:
                self.log_txt.write((str(text) + '\n').encode('utf8'))
            except:
                if not os.path.exists('Log'):
                    os.makedirs('Log')  
                log_name = 'Log/' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.txt'
                self.log_txt = open(log_name, "wb", buffering=0)

                self.add_text_main('Create log file: ' + log_name + '\n')
                self.add_text_main(text)
                return
        try:
            self.main_logs_show.emit(text)
            # time.sleep(0.1)
            # self.Ui.textBrowser_log_main.append(str(text))
            # self.Ui.textBrowser_log_main.moveCursor(QTextCursor.End)
            # self.Ui.textBrowser_log_main.verticalScrollBar().setValue(self.Ui.textBrowser_log_main.verticalScrollBar().maximum())
        except Exception as error_info:
            self.Ui.textBrowser_log_main.append('[-]Error in add_text_main' + str(error_info))
    # ========================================================================语句添加到日志框
    def add_net_text_main(self, text):
        try:
            self.net_logs_show.emit(text)
            # time.sleep(0.1)
            # self.Ui.textBrowser_net_main.append(text)
            # self.Ui.textBrowser_net_main.moveCursor(QTextCursor.End)
            # self.Ui.textBrowser_net_main.verticalScrollBar().setValue(self.Ui.textBrowser_net_main.verticalScrollBar().maximum())
        except Exception as error_info:
            self.Ui.textBrowser_net_main.append('[-]Error in add_net_text_main' + str(error_info))


    # ========================================================================移动到失败文件夹
    def moveFailedFolder(self, filepath, failed_folder):
        if self.Ui.radioButton_fail_move_on.isChecked():
            if self.Ui.radioButton_soft_off.isChecked():
                # self.add_text_main('   >>> 准备移动当前文件到失败文件夹:\n       ' + failed_folder)
                if os.path.split(filepath)[0] != failed_folder:
                    try:
                        shutil.move(filepath, failed_folder + '/')
                        self.add_text_main('   >>> 移动文件到失败文件夹, 路径:\n       ' + failed_folder + '/' + os.path.split(filepath)[1])
                    except Exception as error_info:
                        self.add_text_main('   >>> 移动文件到失败文件夹时失败！错误信息:' + str(error_info))
                else:
                    self.add_text_main('   >>> 当前文件已在失败文件夹, 路径:\n       ' + filepath)

    # ========================================================================下载文件
    def DownloadFileWithFilename(self, url, filename, path, Config, filepath, failed_folder):
        proxy_type = ''
        retry_count = 0
        proxy = ''
        timeout = 0
        try:
            proxy_type, proxy, timeout, retry_count = get_proxy()
        except Exception as error_info:
            print('[-]Error in DownloadFileWithFilename1! ' + str(error_info))
            self.add_text_main('[-]Error in DownloadFileWithFilename! Proxy config error! Please check the config.')
        proxies = get_proxies(proxy_type, proxy)
        i = 0
        while i < retry_count:
            try:
                if not os.path.exists(path):
                    os.makedirs(path)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36'}
                result = requests.get(str(url), headers=headers, timeout=timeout, proxies=proxies)
                with open(str(path) + "/" + filename, "wb") as code:
                    code.write(result.content)
                code.close()
                return
            except Exception as error_info:
                error_info1 = error_info
                i += 1
                print('[-]Error in DownloadFileWithFilename2! ' + str(error_info1))
                print('[-]Image Download :   Connect retry ' + str(i) + '/' + str(retry_count))
        self.add_text_main('[-]Timeout when download file! Please check your Proxy or Network!' + str(error_info1))
        self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================下载缩略图
    def thumbDownload(self, json_data, path, naming_rule, Config, filepath, thumb_path, poster_path, failed_folder):
        thumb_name = naming_rule + '-thumb.jpg'
        if os.path.exists(poster_path):
            self.add_text_main('[+]Thumb Existed!     ' + thumb_name)
            return
        i = 1
        while i <= int(Config['proxy']['retry']):
            self.DownloadFileWithFilename(json_data['cover'], thumb_name, path, Config, filepath,
                                          failed_folder)
            if not check_pic(path + '/' + thumb_name):
                print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                i = i + 1
            else:
                break
        if check_pic(path + '/' + thumb_name):
            self.add_text_main('[+]Thumb Downloaded!  ' + thumb_name)
        elif json_data['cover_small']:
            self.DownloadFileWithFilename(json_data['cover_small'], thumb_name, path, Config, filepath, failed_folder)
            if os.path.exists(path + '/' + thumb_name):
                if not check_pic(path + '/' + thumb_name):
                    os.remove(path + '/' + thumb_name)
                    raise Exception("The Size of Thumb is Error! Deleted " + thumb_name + '!')

    def deletethumb(self, path, naming_rule):
        try:
            thumb_path = path + '/' + naming_rule + '-thumb.jpg'
            if (not self.Ui.checkBox_download_thumb.isChecked()) and os.path.exists(thumb_path):
                os.remove(thumb_path)
                self.add_text_main('[+]Thumb Delete!      ' + naming_rule + '-thumb.jpg')
        except Exception as error_info:
            self.add_text_main('[-]Error in deletethumb: ' + str(error_info))

    # ========================================================================无码片下载封面图
    def smallCoverDownload(self, path, naming_rule, json_data, Config, filepath, failed_folder):
        if json_data['imagecut'] == 3:
            if json_data['cover_small'] == '':
                return 'small_cover_error'
            is_pic_open = 0
            poster_name = naming_rule + '-poster.jpg'
            if os.path.exists(path + '/' + poster_name):
                self.add_text_main('[+]Poster Existed!    ' + poster_name)
                return
            self.DownloadFileWithFilename(json_data['cover_small'], 'cover_small.jpg', path, Config, filepath,
                                          failed_folder)
            try:
                if not check_pic(path + '/cover_small.jpg'):
                    raise Exception("The Size of smallcover is Error! Deleted cover_small.jpg!")
                fp = open(path + '/cover_small.jpg', 'rb')
                is_pic_open = 1
                img = Image.open(fp)
                w = img.width
                h = img.height
                if not (1.4 <= h / w <= 1.6):
                    self.add_text_main('[-]The size of cover_small.jpg is unfit, Try to cut thumb!')
                    # fp.close()
                    # os.remove(path + '/cover_small.jpg')
                    # return 'small_cover_error'
                img.save(path + '/' + poster_name)
                self.add_text_main('[+]Poster Downloaded! ' + poster_name)
                fp.close()
                os.remove(path + '/cover_small.jpg')
            except Exception as error_info:
                self.add_text_main('[-]Error in smallCoverDownload: ' + str(error_info))
                if is_pic_open:
                    fp.close()
                os.remove(path + '/cover_small.jpg')
                self.add_text_main('[+]Try to cut cover!')
                return 'small_cover_error'

    # ========================================================================下载剧照
    def extrafanartDownload(self, json_data, path, Config, filepath, failed_folder):
        if len(json_data['extrafanart']) == 0:
            json_data['extrafanart'] = ''
        if self.Ui.radioButton_extrafanart_download_on.isChecked() and str(json_data['extrafanart']) != '':
            self.add_text_main('[+]ExtraFanart Downloading!')
            extrafanart_folder = self.Ui.lineEdit_extrafanart_dir.text()
            if extrafanart_folder == '':
                extrafanart_folder = 'extrafanart'
            extrafanart_path = path + '/' + extrafanart_folder
            extrafanart_list = json_data['extrafanart']
            if not os.path.exists(extrafanart_path):
                os.makedirs(extrafanart_path)
            extrafanart_count = 0
            for extrafanart_url in extrafanart_list:
                extrafanart_count += 1
                if not os.path.exists(extrafanart_path + '/fanart' + str(extrafanart_count) + '.jpg'):
                    i = 1
                    while i <= int(Config['proxy']['retry']):
                        self.DownloadFileWithFilename(extrafanart_url, 'fanart' + str(extrafanart_count) + '.jpg',
                                                      extrafanart_path, Config, filepath, failed_folder)
                        if not check_pic(extrafanart_path + '/fanart' + str(extrafanart_count) + '.jpg'):
                            print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                            i = i + 1
                        else:
                            break

    # ========================================================================打印NFO
    def PrintFiles(self, path, name_file, cn_sub, leak, json_data, filepath, failed_folder):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        name_media = json_data['naming_media'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                         year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            if os.path.exists(path + "/" + name_file + ".nfo"):
                self.add_text_main('[+]Nfo Existed!       ' + name_file + ".nfo")
                return
            with open(path + "/" + name_file + ".nfo", "wt", encoding='UTF-8') as code:
                print('<?xml version="1.0" encoding="UTF-8" ?>', file=code)
                print("<movie>", file=code)
                print("  <title>" + name_media + "</title>", file=code)
                print("  <set>", file=code)
                print("  </set>", file=code)
                try:
                    if str(json_data['score']) != 'unknown' and str(json_data['score']) != '' and float(
                            json_data['score']) != 0.0:
                        print("  <rating>" + str(json_data['score']) + "</rating>", file=code)
                except Exception as err:
                    print("Error in json_data score!" + str(err))
                if studio != 'unknown':
                    print("  <studio>" + studio + "</studio>", file=code)
                if str(year) != 'unknown':
                    print("  <year>" + year + "</year>", file=code)
                if outline != 'unknown':
                    print("  <outline>" + outline + "</outline>", file=code)
                    print("  <plot>" + outline + "</plot>", file=code)
                if str(runtime) != 'unknown':
                    print("  <runtime>" + str(runtime).replace(" ", "") + "</runtime>", file=code)
                if director != 'unknown':
                    print("  <director>" + director + "</director>", file=code)
                print("  <poster>" + name_file + "-poster.jpg</poster>", file=code)
                print("  <thumb>" + name_file + "-thumb.jpg</thumb>", file=code)
                print("  <fanart>" + name_file + "-fanart.jpg</fanart>", file=code)
                if actor_photo and actor_photo != 'unknown':
                    try:
                        for key, value in actor_photo.items():
                            if str(key) != 'unknown' and str(key) != '':
                                print("  <actor>", file=code)
                                print("   <name>" + key + "</name>", file=code)
                                if not value == '':  # or actor_photo == []:
                                    print("   <thumb>" + value + "</thumb>", file=code)
                                print("  </actor>", file=code)
                    except Exception as error_info:
                        self.add_text_main('[-]Error in actor_photo: ' + str(error_info))
                if studio != 'unknown':
                    print("  <maker>" + studio + "</maker>", file=code)
                if publisher != 'unknown':
                    print("  <maker>" + publisher + "</maker>", file=code)
                print("  <label>", file=code)
                print("  </label>", file=code)
                try:
                    for i in tag:
                        if i != 'unknown':
                            print("  <tag>" + i + "</tag>", file=code)
                except Exception as error_info:
                    self.add_text_main('[-]Error in tag: ' + str(error_info))
                if json_data['imagecut'] == 3:
                    print("  <tag>無碼</tag>", file=code)
                if leak == 1:
                    print("  <tag>流出</tag>", file=code)
                if cn_sub == 1:
                    print("  <tag>中文字幕</tag>", file=code)
                if series != 'unknown':
                    print("  <tag>" + '系列:' + series + "</tag>", file=code)
                if studio != 'unknown':
                    print("  <tag>" + '製作:' + studio + "</tag>", file=code)
                if publisher != 'unknown':
                    print("  <tag>" + '發行:' + publisher + "</tag>", file=code)
                try:
                    for i in tag:
                        if i != 'unknown':
                            print("  <genre>" + i + "</genre>", file=code)
                except Exception as error_info:
                    self.add_text_main('[-]Error in genre: ' + str(error_info))
                if json_data['imagecut'] == 3:
                    print("  <genre>無碼</genre>", file=code)
                if leak == 1:
                    print("  <genre>流出</genre>", file=code)
                if cn_sub == 1:
                    print("  <genre>中文字幕</genre>", file=code)
                if series != 'unknown':
                    print("  <genre>" + '系列:' + series + "</genre>", file=code)
                if studio != 'unknown':
                    print("  <genre>" + '製作:' + studio + "</genre>", file=code)
                if publisher != 'unknown':
                    print("  <genre>" + '發行:' + publisher + "</genre>", file=code)
                print("  <num>" + number + "</num>", file=code)
                if release != 'unknown':
                    print("  <premiered>" + release + "</premiered>", file=code)
                    print("  <release>" + release + "</release>", file=code)
                print("  <cover>" + cover + "</cover>", file=code)
                print("  <website>" + website + "</website>", file=code)
                print("</movie>", file=code)
                self.add_text_main("[+]Nfo Wrote!         " + name_file + ".nfo")
        except Exception as error_info:
            self.add_text_main("[-]Write Failed!")
            self.add_text_main('[-]Error in PrintFiles: ' + str(error_info))
            self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================thumb复制为fanart
    def copyRenameJpgToFanart(self, path, naming_rule):
        if os.path.exists(path + '/' + naming_rule + '-thumb.jpg'):
            if not os.path.exists(path + '/' + naming_rule + '-fanart.jpg'):
                shutil.copy(path + '/' + naming_rule + '-thumb.jpg', path + '/' + naming_rule + '-fanart.jpg')

    # ========================================================================移动视频、字幕
    def pasteFileToFolder(self, filepath, path, naming_rule, failed_folder):
        type = str(os.path.splitext(filepath)[1])
        try:
            if os.path.exists(path + '/' + naming_rule + type):
                raise FileExistsError
            if self.Ui.radioButton_soft_on.isChecked():  # 如果使用软链接
                os.symlink(filepath, path + '/' + naming_rule + type)
                self.add_text_main('[+]Movie Linked!     ' + naming_rule + type)
            else:
                shutil.move(filepath, path + '/' + naming_rule + type)
                self.add_text_main('[+]Movie Moved!       ' + naming_rule + type)

        except FileExistsError:
            self.add_text_main('[+]Movie Existed!     ' + naming_rule + type)
            self.add_text_main('   >>> 目标文件夹存在相同文件！')
            if os.path.split(filepath)[0] != path and os.path.split(filepath)[0] != failed_folder:
                self.moveFailedFolder(filepath, failed_folder)
                self.add_text_main('   >>> 移动当前文件到失败文件夹:\n       ' + failed_folder + os.path.split(filepath)[1])
            else:
                self.add_text_main('   >>> 当前文件已在失败文件夹, 无需移动, 当前路径:' + filepath)
        except PermissionError:
            self.add_text_main('[-]PermissionError! Please run as Administrator!')
        except Exception as error_info:
            self.add_text_main('[-]Error in pasteFileToFolder: ' + str(error_info))
        return False

    # ========================================================================有码片裁剪封面
    def cutImage(self, imagecut, path, naming_rule):
        if imagecut != 3:
            thumb_name = naming_rule + '-thumb.jpg'
            poster_name = naming_rule + '-poster.jpg'
            if os.path.exists(path + '/' + poster_name):
                self.add_text_main('[+]Poster Existed!    ' + poster_name)
                return
            if imagecut == 0:
                self.image_cut(path, thumb_name)
            else:
                try:
                    img = Image.open(path + '/' + thumb_name)
                    img1 = img.convert('RGB')
                    w = img1.width
                    h = img1.height
                    img2 = img1.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/' + poster_name)
                    self.add_text_main('[+]Poster Cut!        ' + poster_name)
                except:
                    self.add_text_main('[-]Thumb cut failed!')

    def fix_size(self, path, naming_rule):
        try:
            poster_path = path + '/' + naming_rule + '-poster.jpg'
            if os.path.exists(poster_path):
                pic = Image.open(poster_path)
                (width, height) = pic.size
                if not 2 / 3 - 0.05 <= width / height <= 2 / 3 + 0.05:  # 仅处理会过度拉伸的图片
                    fixed_pic = pic.resize((int(width), int(3 / 2 * width)))  # 拉伸图片
                    fixed_pic = fixed_pic.filter(ImageFilter.GaussianBlur(radius=50))  # 高斯模糊
                    fixed_pic.paste(pic, (0, int((3 / 2 * width - height) / 2)))  # 粘贴原图
                    fixed_pic.save(poster_path)
        except Exception as error_info:
            self.add_text_main('[-]Error in fix_size: ' + str(error_info))

    # ========================================================================加水印
    def add_mark(self, poster_path, thumb_path, cn_sub, leak, uncensored, config):
        mark_type = ''
        if self.Ui.checkBox_sub.isChecked() and cn_sub:
            mark_type += ',字幕'
        if self.Ui.checkBox_leak.isChecked() and leak:
            mark_type += ',流出'
        if self.Ui.checkBox_uncensored.isChecked() and uncensored:
            mark_type += ',无码'
        if self.Ui.radioButton_thumb_mark_on.isChecked() and mark_type != '' and self.Ui.checkBox_download_thumb.isChecked() and os.path.exists(thumb_path):
            self.add_mark_thread(thumb_path, cn_sub, leak, uncensored)
            self.add_text_main('[+]Thumb Add Mark:    ' + mark_type.strip(','))
        if self.Ui.radioButton_poster_mark_on.isChecked() and mark_type != '' and self.Ui.checkBox_download_poster.isChecked() and os.path.exists(poster_path):
            self.add_mark_thread(poster_path, cn_sub, leak, uncensored)
            self.add_text_main('[+]Poster Add Mark:   ' + mark_type.strip(','))

    def add_mark_thread(self, pic_path, cn_sub, leak, uncensored):
        size = 14 - int(self.Ui.horizontalSlider_mark_size.value())  # 获取自定义大小的值
        img_pic = Image.open(pic_path)
        count = 0  # 获取自定义位置, 取余配合pos达到顺时针添加的效果
        if self.Ui.radioButton_top_left.isChecked():
            count = 0
        elif self.Ui.radioButton_top_right.isChecked():
            count = 1
        elif self.Ui.radioButton_bottom_right.isChecked():
            count = 2
        elif self.Ui.radioButton_bottom_left.isChecked():
            count = 3
        if self.Ui.checkBox_sub.isChecked() and cn_sub == 1:
            self.add_to_pic(pic_path, img_pic, size, count, 1)  # 添加
            count = (count + 1) % 4
        if self.Ui.checkBox_leak.isChecked() and leak == 1:
            self.add_to_pic(pic_path, img_pic, size, count, 2)
            count = (count + 1) % 4
        if self.Ui.checkBox_uncensored.isChecked() and uncensored == 1:
            self.add_to_pic(pic_path, img_pic, size, count, 3)
        img_pic.close()

    def add_to_pic(self, pic_path, img_pic, size, count, mode):
        mark_pic_path = ''
        if mode == 1:
            mark_pic_path = resource_path('Img/SUB.png')
        elif mode == 2:
            mark_pic_path = resource_path('Img/LEAK.png')
        elif mode == 3:
            mark_pic_path = resource_path('Img/UNCENSORED.png')
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
        img_pic.save(pic_path, quality=95)

    # ========================================================================获取分集序号
    def get_part(self, filepath, failed_folder):
        try:
            if re.search('-CD\d+', filepath):
                return re.findall('-CD\d+', filepath)[0].lower()
            if re.search('-cd\d+', filepath):
                return re.findall('-cd\d+', filepath)[0]
        except Exception as error_info:
            self.add_text_main('[-]Error in get_part: ' + str(error_info))
            self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================更新进度条
    def set_processbar(self, value):
        self.Ui.progressBar_avdc.setProperty("value", value)

    def show_dataResult(self, json_data):
        if json_data['error_type']:
            self.add_text_main('[!] 😿 Make data failed!')
            if json_data['error_type'] == 'timeout':
                self.add_text_main('[!] ' + json_data['error_info'])
                self.add_text_main('[!] Connect timeout! Please check your Proxy or Network!')
                return 'error'
            else:
                self.add_text_main('   [!]原因:' + json_data['error_info'])
                return json_data['error_type']
        elif json_data['title'] == '':
            self.add_text_main('   [!]原因:title is null!')
            return 'title is null'
        else:
            self.add_text_main('[!] 🍺 Make data successfully!')
        return 'ok'

    # ========================================================================输出调试信息
    def debug_mode(self, json_data):
        try:
            self.add_text_main('[+] ---Debug info---')
            self.add_text_main(json_data['log_info'].strip('\n'))
            # self.add_text_main('[+] ---Debug info---')
        except Exception as error_info:
            self.add_text_main('[-]Error in debug_mode: ' + str(error_info))

    # ========================================================================输出 Movie 信息
    def show_movieinfo(self, json_data):
        self.add_text_main('[+] ---Movie info---')
        try:
            for key, value in json_data.items():
                if value == '' or key == 'imagecut' or key == 'search_url' or key == 'log_info' or key == 'error_type' or key == 'error_info' or key == 'naming_media' or key == 'naming_file' or key == 'folder_name':
                    continue
                if len(str(value)) == 0:
                    continue
                elif key == 'tag':
                    value = str(json_data['tag']).strip(" ['']").replace('\'', '')
                self.add_text_main('   [+]-' + "%-13s" % key + ': ' + str(value))
                print('   [+]-' + "%-13s" % key + ': ' + str(value))
            # self.add_text_main('[+] ---Movie info---')
        except Exception as error_info:
            self.add_text_main('[-]Error in show_movieinfo: ' + str(error_info))

    # ========================================================================创建输出文件夹
    def creatFolder(self, success_folder, json_data, config, c_word):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        if len(actor.split(',')) >= 10:  # 演员过多取前五个
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        folder_name = json_data['folder_name']
        if not config['Name_Rule']['folder_name_C']:
            c_word = ''
        path = folder_name.replace('title', title).replace('studio', studio).replace('year', year).replace('runtime',
                                                                                                           runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number + c_word).replace(
            'series', series).replace('publisher', publisher)  # 生成文件夹名
        path = path.replace('--', '-').strip('-')
        if len(path) > 100:  # 文件夹名过长 取标题前70个字符
            self.add_text_main('[-]文件夹名过长，取前70个字符!')
            path = path.replace(title, title[0:70])
        path = success_folder + '/' + path
        path = path.replace('--', '-').strip('-')
        if not os.path.exists(path):
            path = escapePath(path, config)
            os.makedirs(path)
        return path

    # ========================================================================从指定网站获取json_data
    def get_json_data(self, mode, number, config, appoint_url):
        if mode == 3:  # javdb模式
            self.add_text_main('[!]Please Wait 3 Seconds！')
            time.sleep(3)
        json_data = getDataFromJSON(number, config, mode, appoint_url)
        return json_data

    # ========================================================================json_data添加到主界面
    def add_label_info(self, json_data):
        try:
            t = threading.Thread(target=self.add_label_info_Thread, args=(json_data,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_start_cap_clicked: ' + str(error_info))

    def add_label_info_Thread(self, json_data):
        self.Ui.label_number.setText(json_data['number'])
        if json_data.get('source'):
            self.Ui.label_source.setText('数据：' + json_data['source'].replace('.main_us','').replace('.main',''))
        self.laberl_number_url = json_data['website']
        self.Ui.label_actor.setText(json_data['actor'])
        self.Ui.label_title.setText(json_data['title'])
        self.Ui.label_outline.setText(json_data['outline'])
        self.Ui.label_tag.setText(str(json_data['tag']).strip(" [',']").replace('\'', ''))
        self.Ui.label_release.setText(json_data['release'])
        self.Ui.label_runtime.setText(json_data['runtime'] + ' 分钟')
        self.Ui.label_director.setText(json_data['director'])
        self.Ui.label_series.setText(json_data['series'])
        self.Ui.label_studio.setText(json_data['studio'])
        self.Ui.label_publish.setText(json_data['publisher'])
        if self.Ui.checkBox_cover.isChecked():
            poster_path = json_data['poster_path']
            thumb_path = json_data['thumb_path']
            if os.path.exists(poster_path):
                pix = QPixmap(poster_path)
                self.Ui.label_poster.setScaledContents(True)
                self.Ui.label_poster.setPixmap(pix)  # 添加封面图
            if os.path.exists(thumb_path):
                pix = QPixmap(thumb_path)
                self.Ui.label_thumb.setScaledContents(True)
                self.Ui.label_thumb.setPixmap(pix)  # 添加缩略图


    # ========================================================================检查更新
    def UpdateCheck(self):
        if self.Ui.radioButton_update_on.isChecked():
            self.add_text_main('[!]' + 'Update Checking!'.center(80))                 
            try:
                result, html_content = get_html('https://api.github.com/repos/Hermit10/temp/releases/latest')
                if result == 'error':
                    self.add_text_main('[-]' + ('UpdateCheck Failed! reason: ' + html_content).center(80))
                    self.add_text_main("[*]================================================================================")
                    return
                data = json.loads(html_content)
            except Exception as error_info1:
                self.add_text_main('[!]' + ('UpdateCheck Failed! Error info: ' + str(error_info1)).center(80))
                self.add_text_main("[*]================================================================================")
                return
            remote = int(data["tag_name"].replace(".",""))
            localversion = int(self.localversion.replace(".", ""))
            new_content = str(data["body"].replace(".","")).replace('====', '').replace('===', '').replace('\r\n', '\n   [+]')
            if localversion < remote:
                self.Ui.label_show_version.setText('🍉 New! update ' + str(data["tag_name"]))
                self.add_text_main('[*]' + ('* New update ' + str(data["tag_name"]) + ' is Available *').center(80))
                self.add_text_main("[*]" + ("").center(80, '='))
                self.add_text_main('   [+]更新内容:' + new_content)
                self.add_text_main('   [+]\n   [+]下载地址: https://github.com/Hermit10/temp/releases')
            else:
                self.add_text_main('[!]' + 'No Newer Version Available!'.center(80))
            self.add_text_main("[*]================================================================================")
        return

    def UpdateCheck_start(self):
        try:
            t = threading.Thread(target=self.UpdateCheck)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]update check error : ' + str(error_info))     

    def show_netstatus(self, proxy_info):
        self.add_net_text_main(time.strftime('%Y-%m-%d %H:%M:%S').center(80, '='))
        proxy_type = ''
        retry_count = 0
        proxy = ''
        timeout = 0
        try:
            proxy_type, proxy, timeout, retry_count = proxy_info
        except Exception as error_info:
            print('[-]get config failed when check net, error info: ! ' + str(error_info))
        if proxy == '' or proxy_type == '' or proxy_type == 'no':
            self.add_net_text_main(' 当前网络状态：❌ 未启用代理\n   类型： ' + str(proxy_type) + '    地址：' + str(proxy) + '    超时时间：' + str(timeout) + '    重试次数：' + str(retry_count))
        else:
            self.add_net_text_main(' 当前网络状态：✅ 已启用代理\n   类型： ' + proxy_type + '    地址：' + proxy + '    超时时间：' + str(timeout) + '    重试次数：' + str(retry_count))
        self.add_net_text_main('='*80)

    def NetResult(self):
        # 显示代理信息
        self.add_net_text_main('\n🛑 开始检测网络....')
        self.show_netstatus(self.current_proxy)
        # 检测网络连通性
        self.add_net_text_main(' 检测网络连通性...')
        net_info = [['github', 'https://raw.githubusercontent.com' , ''], ['javbus', 'https://www.javbus.com' , ''], ['javdb', 'https://www.javdb.com', ''], ['jav321', 'https://www.jav321.com' , ''], ['dmm', 'https://www.dmm.co.jp' , ''], ['avsox', 'https://avsox.website' , ''], ['xcity', 'https://xcity.jp' , ''], ['mgstage', 'https://www.mgstage.com', ''], ['fc2hub', 'https://fc2hub.com', '']]
        for each in net_info:
            error_info = '连接失败, 请检查网络或代理设置！'
            try:
                result, html_content = get_html(each[1])
                if result == 'error':
                    each[2] = '❌ ' + each[1] + ' ' + str(error_info)
                else:
                    if each[0] == 'dmm':
                        if re.findall('このページはお住まいの地域からご利用になれません', html_content):
                            error_info = '地域限制, 请使用日本节点访问！'
                            each[2] = '❌ ' + each[1] + ' ' + str(error_info)
                        else:
                            each[2] = '✅ 连接正常'
                    else:
                        each[2] = '✅ 连接正常'
            except Exception as error_info:
                each[2] = '测试连接时出现异常！信息:' + str(error_info)
            self.add_net_text_main('   ' + each[0].ljust(8) + each[2])
        self.add_net_text_main("================================================================================\n")
        self.Ui.pushButton_check_net.setEnabled(True)
        self.Ui.pushButton_check_net.setText('开始检测')
        self.Ui.pushButton_check_net.setStyleSheet('QPushButton#pushButton_check_net{background-color:#0066CC}QPushButton:hover#pushButton_check_net{background-color:#4C6EFF}QPushButton:pressed#pushButton_check_net{#4C6EE0}')
    # ========================================================================网络检查
    def NetCheck(self):
        self.Ui.pushButton_check_net.setEnabled(False)
        self.Ui.pushButton_check_net.setText('正在检测')
        self.Ui.pushButton_check_net.setStyleSheet('QPushButton#pushButton_check_net{color:#999999;background-color:#F0F0F0}')
        try:
            # self.count_claw += 1
            t = threading.Thread(target=self.NetResult)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_net_text_main('[-]Error in NetCheck: ' + str(error_info))        


    # ========================================================================新建失败输出文件夹
    def CreatFailedFolder(self, failed_folder):
        if self.Ui.radioButton_fail_move_on.isChecked() and not os.path.exists(failed_folder):
            try:
                os.makedirs(failed_folder + '/')
                self.add_text_main('[+]Created folder named ' + failed_folder + '!')
            except Exception as error_info:
                self.add_text_main('[-]Error in CreatFailedFolder: ' + str(error_info))

    # ========================================================================删除空目录
    def CEF(self, path):
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    try:
                        hidden_file = root.replace('\\', '/') + '/' + dir +'/.DS_Store'
                        if os.path.exists(hidden_file):
                            os.remove(hidden_file)  # 删除隐藏文件
                        os.removedirs(root.replace('\\', '/') + '/' + dir)  # 删除这个空文件夹
                        self.add_text_main('[*]' + '='*80)
                        self.add_text_main('[+]Deleting empty folder ' + root.replace('\\', '/') + '/' + dir)
                    except:
                        delete_empty_folder_failed = ''

    def ShowListName(self, filename, result, json_data, real_number=''):
        if result == 'succ':
            node = QTreeWidgetItem(self.item_succ)
            node.setText(0, filename)
            self.item_succ.addChild(node)
        else:
            node = QTreeWidgetItem(self.item_fail)
            node.setText(0, filename)
            self.item_fail.addChild(node)
        try:
            if not json_data.get('number'):
                json_data['number'] = real_number
        except:
            error_jsondata = json_data
            json_data = {}
            json_data['number'] = real_number
            json_data['error_info'] = 'json_data异常错误！' + error_jsondata       
        if not json_data.get('actor'):
            json_data['actor'] = 'unknown'
        if not json_data.get('title'):
            json_data['title'] = json_data['error_info']
        if not json_data.get('outline'):
            json_data['outline'] = 'unknown'
        if not json_data.get('tag'):
            json_data['tag'] = 'unknown'
        if not json_data.get('release'):
            json_data['release'] = 'unknown'
        if not json_data.get('runtime'):
            json_data['runtime'] = '0'
        if not json_data.get('director'):
            json_data['director'] = 'unknown'
        if not json_data.get('series'):
            json_data['series'] = 'unknown'
        if not json_data.get('publisher'):
            json_data['publisher'] = 'unknown'
        if not json_data.get('studio'):
            json_data['studio'] = 'unknown'
        if not json_data.get('poster_path'):
            json_data['poster_path'] = self.default_poster
        if not json_data.get('thumb_path'):
            json_data['thumb_path'] = self.default_thumb
        if not json_data.get('website'):
            json_data['website'] = ''
        if not json_data.get('source'):
            json_data['source'] = ''


        self.add_label_info(json_data)
        self.json_array[filename] = json_data

    def Core_Main(self, filepath, number, mode, count, succ_count=0, fail_count=0, appoint_url=''):
        # =======================================================================初始化所需变量
        leak = 0
        uncensored = 0
        cn_sub = 0
        sub_list = []
        c_word = ''
        multi_part = 0
        part = ''
        program_mode = 0
        config_file = 'config.ini'
        Config = RawConfigParser()
        Config.read(config_file, encoding='UTF-8')

        # =======================================================================判断刮削模式或整理模式
        if self.Ui.radioButton_common.isChecked():                             # 刮削模式
            program_mode = 1
        elif self.Ui.radioButton_sort.isChecked():                             # 整理模式
            program_mode = 2

        # =======================================================================获取媒体目录、失败成功输出目录, 准备用来移动文件
        movie_path = self.Ui.lineEdit_movie_path.text()                         # 用户设置的扫描媒体路径
        if movie_path == '':
            movie_path = os.getcwd().replace('\\', '/')                         # 主程序当前路径
        failed_folder = movie_path + '/' + self.Ui.lineEdit_fail.text()         # 失败输出路径
        success_folder = movie_path + '/' + self.Ui.lineEdit_success.text()     # 成功输出路径


        # =======================================================================判断-C,-CD后缀,无码,流出, 准备用来生成界面显示的文件名
        if '-CD' in filepath or '-cd' in filepath:
            multi_part = 1
            part = self.get_part(filepath, failed_folder)
        if '流出' in os.path.split(filepath)[1]:
            leak = 1
        if '-c.' in filepath or '-C.' in filepath or '中文' in filepath or '字幕' in filepath:                                                 
            if '無字幕' not in filepath and '无字幕' not in filepath:
                cn_sub = 1
                c_word = '-C'                                                   # 中文字幕影片后缀
                                                                                # 查找本地字幕文件
        path_old = filepath.replace(filepath.split('/')[-1], '')                # 去掉文件名的路径
        filename = filepath.split('/')[-1]                                      # 获取文件名（含扩展名）
        file_ex = filename.split('.')[-1]                                       # 获取扩展名（避免文件名有多个.）
        filename = filename.replace('.' + file_ex, '')                         # 获取文件名（不含扩展名）
        sub_type = self.Ui.lineEdit_sub_type.text().split('|')                  # 本地字幕后缀
        for sub in sub_type:
            if os.path.exists(path_old + '/' + filename + sub):                 # 查找本地字幕, 可能多个
                # local_subfile = path_old + '/' + filename + sub
                sub_list.append(sub)
                cn_sub = 1
                c_word = '-C'                                                   # 中文字幕影片后缀

        # =======================================================================这里生成成功或失败后在主界面上左侧栏目显示的文件名
        file_showName = str(number) + part + c_word
        succ_count += 1
        fail_count += 1
        succ_showName = str(self.count_claw) + '-' + str(succ_count) + '.' + file_showName
        fail_showName = str(self.count_claw) + '-' + str(fail_count) + '.' + file_showName

        # =======================================================================获取json_data
        json_data = self.get_json_data(mode, number, Config, appoint_url)

        # =======================================================================显示json_data日结果和日志
        data_result = self.show_dataResult(json_data)                          # 显示 make data 的结果
        if self.Ui.radioButton_debug_on.isChecked():                           # 调试模式打开时显示详细日志
            self.debug_mode(json_data)
        if self.Ui.radioButton_debug_on.isChecked():                           # 调试模式打开时显示data信息
            self.show_movieinfo(json_data)

        # =======================================================================如果获取json_data有问题, 在失败栏目显示文件名
        if data_result != 'ok':                                                # json_data 有问题, 在失败栏目显示文件名 
            self.ShowListName(fail_showName, 'fail', json_data, number)        # 在失败栏目显示文件名
            self.moveFailedFolder(filepath, failed_folder)                     # 移动文件到失败文件夹
            succ_count -= 1
            return 'error', json_data, succ_count, fail_count                  # 返回AVDC_main, 继续处理下一个文件


        # 开始处理当前文件
        # =======================================================================创建当前文件的文件夹
        try:
            path = self.creatFolder(success_folder, json_data, Config, c_word)
        except Exception as ex:
            self.add_text_main('[!]creatFolder error: ' + ex)
        self.add_text_main('[+]创建输出文件夹: ' + path)

        # =======================================================================更新文件命名规则
        number = json_data['number']
        naming_rule = str(self.get_naming_rule(json_data)).replace('--', '-').strip('-')
        if leak == 1:
            naming_rule += '-流出'
        if multi_part == 1:
            naming_rule += part
        if cn_sub == 1:
            naming_rule += c_word
        # =======================================================================生成文件及封面路径
        file_path = path + '/' + naming_rule + '.' + file_ex
        thumb_path = path + '/' + naming_rule + '-thumb.jpg'
        poster_path = path + '/' + naming_rule + '-poster.jpg'

        if os.path.exists(file_path):
            json_data['error_type'] = '输出目录已存在同名文件！ ' + file_path
            json_data['title'] = '输出目录已存在同名文件！ ' + file_path
            json_data['poster_path'] = poster_path
            json_data['thumb_path'] = thumb_path

            self.ShowListName(fail_showName, 'fail', json_data, number)         # 在失败栏目显示文件名
            self.add_text_main('[!]输出文件夹存在同名文件: ' + file_path)
            self.moveFailedFolder(filepath, failed_folder)                      # 移动文件到失败文件夹
            succ_count -= 1
            return 'error', json_data, succ_count, fail_count                   # 返回AVDC_main, 继续处理下一个文件

        # =======================================================================无码封面获取方式
        if json_data['imagecut'] == 3:  # imagecut=3为无码
            uncensored = 1
        if json_data['imagecut'] == 3 and self.Ui.radioButton_poster_cut.isChecked():
            json_data['imagecut'] = 0
        # =======================================================================刮削模式
        if program_mode == 1:
            # imagecut 0 判断人脸位置裁剪缩略图为封面, 1 裁剪右半面, 3 下载小封面
            self.thumbDownload(json_data, path, naming_rule, Config, filepath, thumb_path, poster_path, failed_folder)
            if self.Ui.checkBox_download_poster.isChecked():    #下载海报
                if self.smallCoverDownload(path, naming_rule, json_data, Config, filepath,
                                           failed_folder) == 'small_cover_error':       # 下载小封面
                    json_data['imagecut'] = 0
                self.cutImage(json_data['imagecut'], path, naming_rule)                 # 裁剪图
                self.fix_size(path, naming_rule)
            if self.Ui.checkBox_download_fanart.isChecked():                            # 下载剧照
                self.copyRenameJpgToFanart(path, naming_rule)
            self.deletethumb(path, naming_rule)                                         # 删除
            self.add_mark(poster_path, thumb_path, cn_sub, leak, uncensored, Config)    # 加水印
            if self.Ui.checkBox_download_nfo.isChecked():                          
                self.PrintFiles(path, naming_rule, cn_sub, leak, json_data, filepath, failed_folder)  # 输出nfo文件
            if self.Ui.radioButton_extrafanart_download_on.isChecked():
                self.extrafanartDownload(json_data, path, Config, filepath, failed_folder)
            self.pasteFileToFolder(filepath, path, naming_rule, failed_folder)          # 移动文件
            for sub in sub_list:
                shutil.move(path_old + '/' + filename + sub, path + '/' + naming_rule + sub) # 移动字幕
                self.add_text_main('[+]Sub moved!         ' + naming_rule + sub)

        # =======================================================================整理模式
        elif program_mode == 2:
            self.pasteFileToFolder(filepath, path, naming_rule, failed_folder)   # 移动文件

        # =======================================================================json添加封面项
        json_data['thumb_path'] = thumb_path
        json_data['poster_path'] = poster_path
        json_data['number'] = number

        self.ShowListName(succ_showName, 'succ', json_data)                      # 在成功栏目显示文件名
        fail_count -= 1
        return 'ok', json_data, succ_count, fail_count

    def AVDC_Main(self):
        # =======================================================================初始化所需变量
        os.chdir(os.getcwd())
        config_file = 'config.ini'
        config = RawConfigParser()
        config.read(config_file, encoding='UTF-8')
        movie_path = self.Ui.lineEdit_movie_path.text()
        if movie_path == '':
            movie_path = os.getcwd().replace('\\', '/')
        failed_folder = movie_path + '/' + self.Ui.lineEdit_fail.text()  # 失败输出目录
        escape_folder = self.Ui.lineEdit_escape_dir.text()  # 多级目录刮削需要排除的目录
        mode = self.Ui.comboBox_website_all.currentIndex() + 1
        movie_type = self.Ui.lineEdit_movie_type.text()
        escape_string = self.Ui.lineEdit_escape_string.text()
        # =======================================================================新建failed目录,获取影片列表
        if self.Ui.radioButton_fail_move_on.isChecked():
            self.CreatFailedFolder(failed_folder)  # 新建failed文件夹
        movie_list = movie_lists(escape_folder, movie_type, movie_path)  # 获取所有需要刮削的影片列表
        count = 0
        succ_count = 0
        fail_count = 0
        count_all = str(len(movie_list))
        json_data = ''
        self.add_text_main('[+]Find ' + count_all + ' movies')
        if config['common']['soft_link'] == '1':
            self.add_text_main('[!] --- Soft link mode is ENABLE! ----')
        if int(count_all) == 0:
            self.progressBarValue.emit(int(100))
        else:
            self.count_claw += 1
        # =======================================================================遍历电影列表 交给core处理
        for movie in movie_list:  # 遍历电影列表 交给core处理
            count += 1
            value = int(count / int(count_all) * 100)
            self.progressBarValue.emit(int(value))
            self.Ui.label_result.setText('成功：%s  失败：%s' % (succ_count, fail_count))
            percentage = str(count / int(count_all) * 100)[:4] + '%'
            if len(movie) > 55:     # 截断路径长度，以方便在主界面显示路径时能看到后面的文件名
                show_filepath = movie[-55:]
                show_filepath = '...' + show_filepath[show_filepath.find('/'):]
                if len(show_filepath) < 25:
                    show_filepath = '...' + movie[-45:]

            else:
                show_filepath = movie
            self.Ui.label_filepath.setText('正在刮削： ' + str(count) + '/' + str(count_all) + ' （' + str(value) + '%）\n' + show_filepath)
            self.add_text_main('[*]' + '='*80)
            self.add_text_main('[!]Round (' + str(self.count_claw) + ') - [' + str(count) + '/' + count_all + '] - ' + percentage)
            self.add_text_main('[*]' + '='*80)
            movie_number = os.path.splitext(movie.split('/')[-1])[0]
            try:
                movie_number = getNumber(movie, escape_string).upper()
                self.add_text_main("[!]Making Data for   [" + movie + "], the number is [" + movie_number + "]")
                result, json_data, succ_count, fail_count = self.Core_Main(movie, movie_number, mode, count, succ_count, fail_count)
            except Exception as error_info5:
                fail_count += 1
                fail_showName = str(self.count_claw) + '-' + str(fail_count) + '.' + os.path.splitext(movie.split('/')[-1])[0]
                self.ShowListName(fail_showName, 'fail', json_data, movie_number)
                self.add_text_main('[-]Error in AVDC_Main.Core_Main5: ' + str(error_info5))
                self.moveFailedFolder(movie, failed_folder)
                self.add_text_main("[*]================================================================================")
        self.Ui.label_result.setText('成功：%s  失败：%s' % (succ_count, fail_count))
        self.progressBarValue.emit(100)
        self.Ui.label_filepath.setText('🎉 恭喜！全部刮削完成！共 %s 个文件！' % count_all)
        self.CEF(movie_path)
        self.Ui.pushButton_start_cap.setEnabled(True)
        self.Ui.pushButton_start_cap2.setEnabled(True)
        self.Ui.pushButton_start_cap.setText('开始')
        self.Ui.pushButton_start_cap2.setText('开始')
        self.Ui.pushButton_start_cap.setStyleSheet('QPushButton#pushButton_start_cap{color:white;background-color:#0066CC;}QPushButton:hover#pushButton_start_cap{color:white;background-color:#4C6EFF}QPushButton:pressed#pushButton_start_cap{color:white;background-color:#4C6EE0}')
        self.Ui.pushButton_start_cap2.setStyleSheet('QPushButton#pushButton_start_cap2{color:white;background-color:#0066CC}QPushButton:hover#pushButton_start_cap2{color:white;background-color:#4C6EFF}QPushButton:pressed#pushButton_start_cap2{color:white;background-color:#4C6EE0}')
        self.add_text_main("[*]================================================================================")
        self.add_text_main("[+]Total %s , Success %s , Failed %s" % (count_all, succ_count, fail_count))
        self.add_text_main("[*]================================================================================")
        self.add_text_main("[+]All finished!!!")
        self.add_text_main("[*]================================================================================")


if __name__ == '__main__':
    '''
    主函数
    '''
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    # QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ui = MyMAinWindow()
    ui.show()

    sys.exit(app.exec_())
