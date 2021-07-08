#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logging import PercentStyle, error, exception
from socket import MsgFlag
import threading
import json
from PySide2 import QtWidgets
from PySide2.QtGui import QTextCursor, QCursor, QPixmap
from PySide2.QtWidgets import QMainWindow, QTreeWidgetItem, QApplication, QPushButton, QDialog, QFileDialog, QDialogButtonBox
from PySide2.QtCore import Signal, Qt, QCoreApplication, QPoint, QRect
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
from Function.Function import save_config, movie_lists, get_info, getDataFromJSON, escapePath, getNumber, check_pic, is_uncensored
from Function.getHtml import get_html, get_proxies, get_proxy
import socks
import urllib3
urllib3.disable_warnings()
# import faulthandler
# faulthandler.enable()
from lxml import etree
import urllib.parse
import random
import hashlib
import zhconv

#生成资源文件目录访问路径
def resource_path(relative_path):
    base_path = os.path.abspath(".")
    if os.path.exists(os.path.join(base_path, relative_path)):
        pass
    elif getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
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
        self.localversion = '20210708'
        self.Ui.label_show_version.setText('version ' + self.localversion)
        self.Ui.label_show_version.mousePressEvent = self.version_clicked
        self.thumb_path = ''
        self.poster_path = ''
        self.Ui.label_number.mousePressEvent = self.label_number_clicked
        self.Ui.label_source.mousePressEvent = self.label_number_clicked
        self.default_poster = resource_path('Img/default-poster.jpg')
        self.default_thumb = resource_path('Img/default-thumb.jpg')
        self.c_numuber_jsonfile = resource_path('Img/c_number.json')
        self.m_drag = False
        self.m_DragPosition = 0
        self.count_claw = 0  # 批量刮削次数
        self.item_succ = self.Ui.treeWidget_number.topLevelItem(0)
        self.item_fail = self.Ui.treeWidget_number.topLevelItem(1)
        self.select_file_path = ''
        self.json_array = {}
        self.current_proxy = ''  # 代理设置
        self.github_project_url = 'https://github.com/Hermit10/temp/'  # 项目主页
        self.Init()
        self.Load_config()
        self.Ui.label_file_path.setText('🎈 设置视频目录（设置-目录设置-视频目录），然后点击开始！\n')
        self.show_version() # 启动后在【日志】页面显示版本信息
        self.new_proxy = self.check_proxyChange()
        self.addNetTextMain('\n🏠 代理设置在:【设置】 - 【网络设置】 - 【代理设置】。\n') 
        self.show_netstatus(self.new_proxy) # 启动后在【检测网络】页面显示网络代理情况
        self.addNetTextMain('\n\n点击 【开始检测】以测试网络连通性。')
        self.updateCheckStart() # 检查更新


    def Init_Ui(self):
        ico_path = resource_path('Img/AVDC-ico.png')
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
            QLabel#label_file_path{
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

    # ======================================================================================按钮点击事件
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
        self.Ui.pushButton_check_net.clicked.connect(self.netCheck)
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
        self.Ui.label_thumb.mousePressEvent = self.test_clicked
        self.Ui.label_poster.mousePressEvent = self.test_clicked

    # ======================================================================================显示版本号
    def show_version(self):
        self.addTextMain('[*]' + 'AVDCx'.center(80, '='))
        self.addTextMain('[*]' + ('Current Version: ' + self.localversion).center(80))
        self.addTextMain('[*]' + '基于项目 https://github.com/moyy996/AVDC 修改'.center(80))
        self.addTextMain('[*]' + ('%sissues' % self.github_project_url).center(80))
        self.addTextMain('[*]================================================================================')

    def version_clicked(self, test):
        webbrowser.open('%sreleases' % self.github_project_url)

    def label_number_clicked(self, test):
        if self.laberl_number_url:
            webbrowser.open(self.laberl_number_url)

    def test_clicked(self, test):
        newWin2.showimage(self.thumb_path, self.poster_path)
        newWin2.show()

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
        config_file = 'config.ini'
        config = RawConfigParser()
        # config = RawConfigParser(comment_prefixes='$', allow_no_value=True)
        config.read(config_file, encoding='UTF-8')
        show_poster = config.getint('common', 'show_poster')

        if bool(self.Ui.checkBox_cover.isChecked()) != bool(show_poster):
            if self.Ui.checkBox_cover.isChecked():
                config.set('common', 'show_poster', 1)
            else:
                config.set('common', 'show_poster', 0)
            try:
                code = open(config_file, 'w')
                config.write(code)   
                code.close()
            except:
                pass
        os._exit(0)


    # def min_win(self):        # 最小化窗口
    #     self.setWindowState(Qt.WindowMinimized)

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
            self.addTextMain('[-]Error in pushButton_start_cap_clicked: ' + str(ex))

    # ======================================================================================恢复默认config.ini
    def pushButton_init_config_clicked(self):
        self.Ui.pushButton_init_config.setEnabled(False)
        try:
            t = threading.Thread(target=self.init_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('[-]Error in pushButton_init_config_clicked: ' + str(ex))

    def init_config_clicked(self):
        json_config = {
            'show_poster': 1,
            'main_mode': 1,
            'main_like': 1,
            'soft_link': 0,
            'switch_debug': 1,
            'failed_file_move': 1,
            'update_check': 1,
            'translate_language': 'zh_cn',
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
            'literals': '\|()',
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
            'uncensored_poster': 1,
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
        self.Load_config()
        self.Ui.pushButton_init_config.setEnabled(True)

    # ======================================================================================加载config
    def Load_config(self):
        config_file = 'config.ini'
        if os.path.exists(config_file):
            config = RawConfigParser()
            try:
                config.read(config_file, encoding='UTF-8')
                # ======================================================================================common
                if int(config['common']['main_mode']) == 1:
                    self.Ui.radioButton_common.setChecked(True)
                elif int(config['common']['main_mode']) == 2:
                    self.Ui.radioButton_sort.setChecked(True)
                try:
                    config.getint('common', 'main_like')
                except:
                    config.set('common', 'main_like', 1)
                if int(config['common']['main_like']) == 1:
                    self.Ui.radioButton_like_more.setChecked(True)
                elif int(config['common']['main_like']) == 0:
                    self.Ui.radioButton_like_speed.setChecked(True)
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
                elif config['common']['website'] == 'airav':
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
                elif config['common']['website'] == 'fc2hub':
                    self.Ui.comboBox_website_all.setCurrentIndex(9)
                # ======================================================================================translatelanguage
                if config['common']['translate_language'] == 'zh_cn':
                    self.Ui.radioButton_zh_cn.setChecked(True)
                elif config['common']['translate_language'] == 'zh_tw':
                    self.Ui.radioButton_zh_tw.setChecked(True)
                elif config['common']['translate_language'] == 'ja':
                    self.Ui.radioButton_ja.setChecked(True)
                # ======================================================================================proxy
                if config['proxy']['type'] == 'no' or config['proxy']['type'] == '':
                    self.Ui.radioButton_proxy_nouse.setChecked(True)
                elif config['proxy']['type'] == 'http':
                    self.Ui.radioButton_proxy_http.setChecked(True)
                elif config['proxy']['type'] == 'socks5':
                    self.Ui.radioButton_proxy_socks5.setChecked(True)
                self.Ui.lineEdit_proxy.setText(config['proxy']['proxy'])
                self.Ui.horizontalSlider_timeout.setValue(int(config['proxy']['timeout']))
                self.Ui.horizontalSlider_retry.setValue(int(config['proxy']['retry']))
                # ======================================================================================Cookies
                self.set_javdb_cookie.emit(config['Cookies']['javdb'])
                self.set_dmm_cookie.emit(config['Cookies']['dmm'])
                # ======================================================================================Name_Rule
                self.Ui.lineEdit_dir_name.setText(config['Name_Rule']['folder_name'])
                self.Ui.lineEdit_media_name.setText(config['Name_Rule']['naming_media'])
                self.Ui.lineEdit_local_name.setText(config['Name_Rule']['naming_file'])
                # ======================================================================================update
                if int(config['update']['update_check']) == 1:
                    self.Ui.radioButton_update_on.setChecked(True)
                elif int(config['update']['update_check']) == 0:
                    self.Ui.radioButton_update_off.setChecked(True)
                # ======================================================================================folder_name_C
                if int(config['Name_Rule']['folder_name_C']) == 1:
                    self.Ui.radioButton_foldername_C_on.setChecked(True)
                elif int(config['Name_Rule']['folder_name_C']) == 0:
                    self.Ui.radioButton_foldername_C_off.setChecked(True)
                # ======================================================================================log
                if int(config['log']['save_log']) == 1:
                    self.Ui.radioButton_log_on.setChecked(True)
                elif int(config['log']['save_log']) == 0:
                    self.Ui.radioButton_log_off.setChecked(True)
                # ======================================================================================media
                self.Ui.lineEdit_movie_path.setText(str(config['media']['media_path']))
                self.Ui.lineEdit_movie_type.setText(config['media']['media_type'])
                self.Ui.lineEdit_sub_type.setText(config['media']['sub_type'])
                self.Ui.lineEdit_success.setText(config['media']['success_output_folder'])
                self.Ui.lineEdit_fail.setText(config['media']['failed_output_folder'])
                # ======================================================================================escape
                self.Ui.lineEdit_escape_dir.setText(config['escape']['folders'])
                self.Ui.lineEdit_escape_char.setText(config['escape']['literals'])
                self.Ui.lineEdit_escape_dir_move.setText(config['escape']['folders'])
                self.Ui.lineEdit_escape_string.setText(config['escape']['string'])
                # ======================================================================================debug_mode
                if int(config['debug_mode']['switch']) == 1:
                    self.Ui.radioButton_debug_on.setChecked(True)
                elif int(config['debug_mode']['switch']) == 0:
                    self.Ui.radioButton_debug_off.setChecked(True)
                # ======================================================================================emby
                self.Ui.lineEdit_emby_url.setText(config['emby']['emby_url'])
                self.Ui.lineEdit_api_key.setText(config['emby']['api_key'])
                # ======================================================================================mark
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
                # ======================================================================================uncensored
                if int(config['uncensored']['uncensored_poster']) == 1:
                    self.Ui.radioButton_poster_cut.setChecked(True)
                elif int(config['uncensored']['uncensored_poster']) == 0:
                    self.Ui.radioButton_poster_official.setChecked(True)
                self.Ui.lineEdit_uncensored_prefix.setText(config['uncensored']['uncensored_prefix'])
                # ======================================================================================file_download
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
                # ======================================================================================extrafanart
                if int(config['extrafanart']['extrafanart_download']) == 1:
                    self.Ui.checkBox_download_extrafanart.setChecked(True)
                elif int(config['extrafanart']['extrafanart_download']) == 0:
                    self.Ui.checkBox_download_extrafanart.setChecked(False)
                self.Ui.lineEdit_extrafanart_dir.setText(config['extrafanart']['extrafanart_folder'])
            except:
                self.addTextMain('config.ini is corrupt, and has been reset now.\n')
                return self.init_config_clicked()
        else:
            # ini不存在，重新创建
            self.addTextMain('Create config file: config.ini\n')
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
                self.addNetTextMain('\n🌈 代理设置已改变：')
                self.show_netstatus(self.new_proxy)
        self.current_proxy = self.new_proxy
        return self.new_proxy

    # ======================================================================================读取设置页设置, 保存在config.ini
    def pushButton_save_config_clicked(self):
        try:
            t = threading.Thread(target=self.save_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('[-]Error in pushButton_save_config_clicked: ' + str(ex))

    def save_config_clicked(self):
        main_mode = 1
        main_like = 1
        failed_file_move = 1
        soft_link = 0
        show_poster = 0
        switch_debug = 0
        update_check = 0
        translate_language = ''
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
        # ======================================================================================common
        if self.Ui.radioButton_common.isChecked():  # 普通模式
            main_mode = 1
        elif self.Ui.radioButton_sort.isChecked():  # 整理模式
            main_mode = 2
        if self.Ui.radioButton_like_more.isChecked():  # 字段全
            main_like = 1
        elif self.Ui.radioButton_like_speed.isChecked():  # 快速
            main_like = 0
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
        if self.Ui.radioButton_zh_cn.isChecked():  # 翻译简体
            translate_language = 'zh_cn'
        elif self.Ui.radioButton_zh_tw.isChecked():  # 翻译繁体
            translate_language = 'zh_tw'
        elif self.Ui.radioButton_ja.isChecked():  # 翻译日文
            translate_language = 'ja'

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
        elif self.Ui.comboBox_website_all.currentText() == 'airav':  # airav
            website = 'airav'
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
        # ======================================================================================proxy
        if self.Ui.radioButton_proxy_http.isChecked():  # http proxy
            proxy_type = 'http'
        elif self.Ui.radioButton_proxy_socks5.isChecked():  # socks5 proxy
            proxy_type = 'socks5'
        elif self.Ui.radioButton_proxy_nouse.isChecked():  # nouse proxy
            proxy_type = 'no'
        # ======================================================================================水印
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
        # ======================================================================================下载文件，剧照
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
        if self.Ui.checkBox_download_extrafanart.isChecked():
            extrafanart_download = 1
        else:
            extrafanart_download = 0
        json_config = {
            'main_mode': main_mode,
            'main_like': main_like,
            'soft_link': soft_link,
            'switch_debug': switch_debug,
            'show_poster': show_poster,
            'failed_file_move': failed_file_move,
            'update_check': update_check,
            'translate_language': translate_language,
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

    # ======================================================================================小工具-单视频刮削
    def pushButton_select_file_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        if not path:
            path = os.getcwd()
        file_path, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取视频文件", path, "Movie Files(*.mp4 "
                                                                                         "*.avi *.rmvb *.wmv "
                                                                                         "*.mov *.mkv *.flv *.ts "
                                                                                         "*.webm *.MP4 *.AVI "
                                                                                         "*.RMVB *.WMV *.MOV "
                                                                                         "*.MKV *.FLV *.TS "
                                                                                         "*.WEBM);;All Files(*)")
        self.select_file_path = file_path.replace('\\', '/') 

    def pushButton_start_single_file_clicked(self):
        if self.select_file_path != '':
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
                self.addTextMain('[-]Error in pushButton_start_single_file_clicked: ' + str(ex))

    # ======================================================================================小工具-裁剪封面图
    def pushButton_select_thumb_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        if not path:
            path = os.getcwd()
        file_path, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取缩略图", path,
                                                                   "Picture Files(*.jpg);;All Files(*)")
        img_name, img_ex = os.path.splitext(file_path)
        if file_path != '':
            poster_path = file_path.replace('\\', '/').replace(('-fanart' + img_ex), '').replace(('-thumb' + img_ex), '').replace(('-poster' + img_ex), '').replace(img_ex, '') + '-poster' + img_ex
            self.thumb_path = file_path
            self.poster_path = poster_path
            newWin2.showimage(file_path, poster_path)
            newWin2.show()

    def image_cut(self, thumb_name, poster_name, thumb_path, poster_path, mode=1):
        try:
            if os.path.exists(poster_path):
                os.remove(poster_path)
        except Exception as ex:
            self.addTextMain("[!] 🔴 Failed to remove old poster!\n   >>> " + str(ex))
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
        # self.addTextMain("[+] 🟢 Poster created successfully!\n   >>> The poster name is '%s'\n   >>> Cut from the center of the thumb" % poster_name)
        self.addTextMain("[+] 🟢 Poster created successfully! Cut from the center of the thumb")
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
        # self.Ui.stackedWidget.setCurrentIndex(1)
        self.pushButton_show_log_clicked() # 点击开始移动按钮后跳转到日志页面
        try:
            t = threading.Thread(target=self.move_file_thread)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('[-]Error in move_file: ' + str(ex))

    def move_file_thread(self):
        movie_path = self.Ui.lineEdit_movie_path.text().replace('\\', '/')
        escape_dir = self.Ui.lineEdit_escape_dir_move.text().replace('\\', '/')
        movie_type = self.Ui.lineEdit_movie_type.text()
        sub_type = self.Ui.lineEdit_sub_type.text().split('|')
        if not movie_path:  # 没有输入视频目录时，获取程序当前路径
            movie_path = os.path.abspath(".")
        movie_list = movie_lists(escape_dir, movie_type, movie_path)
        des_path = movie_path + '/Movie_moved'
        if not os.path.exists(des_path):
            self.addTextMain('[+]Created folder Movie_moved!')
            os.makedirs(des_path)
        self.addTextMain('[+]Move Movies Start!')
        for movie in movie_list:
            if des_path in movie:
                continue
            sour = movie
            des = des_path + '/' + sour.split('/')[-1]
            try:
                shutil.move(sour, des)
                self.addTextMain('   [+]Move ' + sour.split('/')[-1] + ' to Movie_moved Success!')
                path_old = sour.replace(sour.split('/')[-1], '')
                filename = sour.split('/')[-1].split('.')[0]
                for sub in sub_type:
                    if os.path.exists(path_old + '/' + filename + sub):  # 字幕移动
                        shutil.move(path_old + '/' + filename + sub, des_path + '/' + filename + sub)
                        self.addTextMain('   [+]Sub moved! ' + filename + sub)
            except Exception as ex:
                self.addTextMain('[-]Error in move_file_thread: ' + str(ex))
        self.addTextMain("[+]Move Movies All Finished!!!")
        self.addTextMain("[*]================================================================================")

    # ======================================================================================小工具-emby女优头像
    def pushButton_add_actor_pic_clicked(self):  # 添加头像按钮响应
        self.pushButton_show_log_clicked() # 点击查看按钮后跳转到日志页面
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.addTextMain('[-]The emby_url is empty!')
            self.addTextMain("[*]================================================================================")
            return
        elif api_key == '':
            self.addTextMain('[-]The api_key is empty!')
            self.addTextMain("[*]================================================================================")
            return
        try:
            t = threading.Thread(target=self.found_profile_picture, args=(1,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('[-]Error in pushButton_add_actor_pic_clicked: ' + str(ex))

    def pushButton_show_pic_actor_clicked(self):  # 查看按钮响应
        self.pushButton_show_log_clicked() # 点击查看按钮后跳转到日志页面
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.addTextMain('[-]The emby_url is empty!')
            self.addTextMain("[*]================================================================================")
            return
        elif api_key == '':
            self.addTextMain('[-]The api_key is empty!')
            self.addTextMain("[*]================================================================================")
            return
        if self.Ui.comboBox_pic_actor.currentIndex() == 0:  # 可添加头像的女优
            try:
                t = threading.Thread(target=self.found_profile_picture, args=(2,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as ex:
                self.addTextMain('[-]Error in pushButton_show_pic_actor_clicked: ' + str(ex))
        else:
            try:
                t = threading.Thread(target=self.show_actor, args=(self.Ui.comboBox_pic_actor.currentIndex(),))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as ex:
                self.addTextMain('[-]Error in pushButton_show_pic_actor_clicked: ' + str(ex))

    def show_actor(self, mode):  # 按模式显示相应列表
        if mode == 1:  # 没有头像的女优
            self.addTextMain('[+]没有头像的女优!')
        elif mode == 2:  # 有头像的女优
            self.addTextMain('[+]有头像的女优!')
        elif mode == 3:  # 所有女优
            self.addTextMain('[+]所有女优!')
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.addTextMain("[*]================================================================================")
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
                self.addTextMain('[+]' + actor_list_temp)
                actor_list_temp = ''
        self.addTextMain("[*]================================================================================")

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
            self.addTextMain('[-]Error! Check your emby_url or api_key!')
            actor_list['TotalRecordCount'] = 0
        return actor_list

    def found_profile_picture(self, mode):  # mode=1, 上传头像, mode=2, 显示可添加头像的女优
        if mode == 1:
            self.addTextMain('[+]Start upload profile pictures!')
        elif mode == 2:
            self.addTextMain('[+]可添加头像的女优!')
        path = 'Actor'
        if not os.path.exists(path):
            self.addTextMain('[+]Actor folder not exist!')
            self.addTextMain("[*]================================================================================")
            return
        path_success = 'Actor/Success'
        if not os.path.exists(path_success):
            os.makedirs(path_success)
        profile_pictures = os.listdir(path)
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.addTextMain("[*]================================================================================")
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
                    except Exception as ex:
                        self.addTextMain('[-]Error in found_profile_picture! ' + str(ex))
                else:
                    self.addTextMain('[+]' + "%4s" % str(count) + '.Actor name: ' + actor['Name'] + '  Pic name: '
                                       + pic_name)
                count += 1
        if count == 1:
            self.addTextMain('[-]NO profile picture can be uploaded!')
        self.addTextMain("[*]================================================================================")

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
            self.addTextMain(
                '[+]' + "%4s" % str(count) + '.Success upload profile picture for ' + actor['Name'] + '!')
        except Exception as ex:
            self.addTextMain('[-]Error in upload_profile_picture! ' + str(ex))

    # ======================================================================================自定义文件名
    def getNamingRule(self, json_data, config):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        title = re.sub(r'[\\/:*?"<>|\r\n]+', '', title)
        if len(actor.split(',')) >= 10:  # 演员过多取前五个
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        file_name = json_data['naming_file'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                       year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        file_name = file_name.replace('//', '/').replace('--', '-').strip('-')
        file_name = re.sub(r'[\\/:*?"<>|\r\n]+', '', file_name)
        if len(file_name) > 100:  # 文件名过长 取标题前70个字符
            self.addTextMain('[-]提示：标题名过长，取前70个字作为标题!')
            file_name = file_name.replace(title, title[0:70])
        file_name = escapePath(file_name, config)   # 清除设置的异常字符
        return file_name

    # ======================================================================================语句添加到日志框
    def addTextMain(self, text):
        if self.Ui.radioButton_log_on.isChecked():  # 保存日志
            try:
                self.log_txt.write((str(text) + '\n').encode('utf8'))
            except:
                if not os.path.exists('Log'):
                    os.makedirs('Log')  
                log_name = 'Log/' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.txt'
                self.log_txt = open(log_name, "wb", buffering=0)
                self.addTextMain('Create log file: ' + log_name + '\n')
                self.addTextMain(text)
                print('Create log file: ' + log_name + '\n')
                print(text)
                return
        try:
            self.main_logs_show.emit(text)
            # print(text) # 同时打印日志，避免gui崩溃时看不到日志信息;lk x dghinop[o r  12 ]
        except Exception as ex:
            print('[-]Error in addTextMain' + str(ex))
            self.Ui.textBrowser_log_main.append('[-]Error in addTextMain' + str(ex))
    # ======================================================================================语句添加到日志框
    def addNetTextMain(self, text):
        try:
            self.net_logs_show.emit(text)
            # time.sleep(0.1)
            # self.Ui.textBrowser_net_main.append(text)
            # self.Ui.textBrowser_net_main.moveCursor(QTextCursor.End)
            # self.Ui.textBrowser_net_main.verticalScrollBar().setValue(self.Ui.textBrowser_net_main.verticalScrollBar().maximum())
        except Exception as ex:
            print('[-]Error in addNetTextMain' + str(ex))
            self.Ui.textBrowser_net_main.append('[-]Error in addNetTextMain' + str(ex))


    # ======================================================================================移动到失败文件夹
    def moveFailedFolder(self, file_path, failed_folder, config):
        if int(config.getint('common', 'failed_file_move')) == 1:
            if int(config.getint('common', 'soft_link')) == 0:
                file_new_path = os.path.join(failed_folder, os.path.split(file_path)[1])
                if not os.path.exists(failed_folder):
                    self.creatFailedFolder(failed_folder, config)  # 创建failed文件夹
                if failed_folder not in file_path:
                    if not os.path.exists(file_new_path):
                        try:
                            shutil.move(file_path, failed_folder)
                            self.addTextMain("   >>> Move file to the failed folder! \n   >>> The new path is '%s'" % file_new_path)
                        except Exception as ex:
                            self.addTextMain("   >>> Failed to move the file to the failed folder! \n   >>> " + str(ex))
                    else:
                        self.addTextMain("   >>> The failed path '%s' already exists \n   >>> The file will not be moved to the failed floder!\n   >>> The current path is '%s'" % (file_new_path, file_path))
                else:
                    self.addTextMain("   >>> The file is already in the failed folder, no need to move it again!\n   >>> The current path is '%s'" % file_path)

    # ======================================================================================下载文件
    def downloadFileWithFilename(self, url, filename, path):
        proxy_type = ''
        retry_count = 0
        proxy = ''
        timeout = 0
        if url == '' or url == 'unknown':
            self.addTextMain("[!] 🔴 The url '%s' is wrong, the file '%s' will skip download! " %(url, filename))
            return False
        try:
            proxy_type, proxy, timeout, retry_count = get_proxy()
        except Exception as ex:
            self.addTextMain("[!] 🔴 Error when get proxy config! Please check the file 'config.ini'!\n   >>> %s" % str(ex))
            return False
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
                return True
            except Exception as ex:
                i += 1
        self.addTextMain("[!] 🔴 Failed to download the file using the cover url '%s'\n   >>> %s" % (url, str(ex)))
        return False

    # ======================================================================================下载缩略图
    def thumbDownload(self, json_data, path, config, thumb_name, thumb_path):
        if int(config.getint('file_download', 'thumb')) == 0:
            return True
        # self.addTextMain("[!] ⏳ Start downloading the thumb... ")
        try:
            cover_url = str(json_data['cover'])
        except Exception as ex:
            self.addTextMain("[!] 🔴 Can't use the cover url to download thumb! beacuse the cover url is not exist! \n >>> %s" % str(ex))
            return False
        if os.path.exists(thumb_path):  # 移除已存在的thumb文件，重新下载
            os.remove(thumb_path)
        i = 1
        while i <= int(config['proxy']['retry']):
            self.downloadFileWithFilename(cover_url, thumb_name, path)
            if not check_pic(thumb_path):
                i = i + 1
            else:
                break
        if check_pic(thumb_path):
            # self.addTextMain("[+] 🟢 Thumb downloaded successfully! \n   >>> The thumb name is '%s'" % thumb_name)
            self.addTextMain("[+] 🟢 Thumb downloaded successfully!")
            return True
        else:
            self.addTextMain("[!] ⏳ Start downloading the thumb using cover small url... ")
            try:
                cover_small_url = json_data['cover_small']
            except Exception as ex:
                self.addTextMain("[!] 🔴 Can't use the cover small url to download thumb, beacuse the cover small url is not exist! \n >>> %s" % str(ex))
                return False
            if self.downloadFileWithFilename(cover_small_url, thumb_name, path):
                if check_pic(thumb_path):
                    # self.addTextMain("[+] 🟢 Thumb downloaded successfully! \n   >>> The thumb name is '%s'" % thumb_name)
                    self.addTextMain("[+] 🟢 Thumb downloaded successfully!")
                    return True
            if os.path.exists(thumb_path):  # 下载失败时，删除损坏的文件
                os.remove(thumb_path)
            self.addTextMain("[!] 🔴 Failed to download thumb")
            return False

    # ======================================================================================下载poster
    def posterDownload(self, json_data, path, config, thumb_name, poster_name, thumb_path, poster_path, cover_small_path):
        if int(config.getint('file_download', 'poster')) == 0:
            return True
        if os.path.exists(poster_path):
            os.remove(poster_path)
        if int(config.getint('uncensored', 'uncensored_poster')) == 0:     # 官方下载
            # self.addTextMain("[!] ⏳ Start downloading the poster... ")
            if not self.smallCoverDownload(json_data, path, config, thumb_name, poster_name, thumb_path, poster_path, cover_small_path):
                if json_data['imagecut'] == 3:  # 下载失败，使用裁剪，修改裁剪方式为0
                    json_data['imagecut'] = 0
        if not os.path.exists(poster_path): # 没有poster图时，进行裁剪
            # self.addTextMain("[!] ⏳ Start creating poster by clipping thumb... ")
            if not self.cutImage(json_data['imagecut'], path, thumb_name, poster_name, thumb_path, poster_path, cover_small_path):
                return False
        if not os.path.exists(poster_path): 
                return False
        return True

    # ======================================================================================删除缩略图
    def deletethumb(self, thumb_name, thumb_path, config):
        try:
            if int(config.getint('file_download', 'thumb')) == 0 and os.path.exists(thumb_path):
                os.remove(thumb_path)
                self.addTextMain("[!] 🟢 Delete the thumb '%s' successfully!" % thumb_name)
        except Exception as ex:
            self.addTextMain("[!] 🔴 Failed to delete the thumb '%s'\n   >>> %s" % (thumb_name, str(ex)))

    # ======================================================================================下载封面图
    def smallCoverDownload(self, json_data, path, config, thumb_name, poster_name, thumb_path, poster_path, cover_small_path):
        try:
            if json_data['cover_small'] == '' or json_data['cover_small'] == 'unknown':
                self.addTextMain('[+]Failed to download poster using the small cover url! beacuse cover url is not exist!')
                return False
        except Exception as ex:
            self.addTextMain("[!] 🔴 Can't use the cover small url to download poster! beacuse the cover small url is not exist! \n >>> %s" % str(ex))
            return False
        is_pic_open = 0
        if os.path.exists(poster_path):  # 移除已存在的tposter文件，重新下载
            os.remove(thumb_path)

        i = 1
        while i <= int(config['proxy']['retry']):
            self.downloadFileWithFilename(json_data['cover_small'], cover_small_path, path)
            if not check_pic(cover_small_path):
                i = i + 1
            else:
                break
        if not check_pic(cover_small_path):
            self.addTextMain('[!] 🔴 Poster download failed!')
            return False
        try:
            fp = open(cover_small_path, 'rb')
            is_pic_open = 1
            img = Image.open(fp)
            w = img.width
            h = img.height
            if not (1.3 <= h / w <= 1.6):
                fp.close()
                self.addTextMain('[!] 🔴 Poster size is not appropriate!')
                return False
            img.save(poster_path)
            fp.close()
            os.remove(cover_small_path)
            self.addTextMain("[+] 🟢 Poster downloded successfully!\n   >>> The poster name is '%s'" % poster_name)
            return True
        except Exception as ex:
            self.addTextMain('[!] 🔴 Fail to save poster!\n   >>> ' + str(ex))
            if is_pic_open:
                fp.close()
            os.remove(cover_small_path)
            return False

    # ======================================================================================下载剧照
    def extrafanartDownload(self, json_data, path, config):
        if int(config.getint('extrafanart', 'extrafanart_download')) == 0:
            return
        try:
            if len(json_data['extrafanart']) == 0 or json_data['extrafanart'] == 'unknown':
                return
        except:
            return
        self.addTextMain('[+] ⏳ ExtraFanart downloading!')
        extrafanart_folder = config.get('extrafanart', 'extrafanart_folder').replace('\\', '/')
        extrafanart_path = os.path.join(path, extrafanart_folder)
        extrafanart_list = json_data['extrafanart']
        if not os.path.exists(extrafanart_path):
            os.makedirs(extrafanart_path)
        extrafanart_count = 0
        extrafanart_count_succ = 0
        for extrafanart_url in extrafanart_list:
            extrafanart_count += 1
            if not os.path.exists(extrafanart_path + '/fanart' + str(extrafanart_count) + '.jpg'):
                i = 1
                while i <= int(config['proxy']['retry']):
                    self.downloadFileWithFilename(extrafanart_url, 'fanart' + str(extrafanart_count) + '.jpg',
                                                    extrafanart_path)
                    if not check_pic(extrafanart_path + '/fanart' + str(extrafanart_count) + '.jpg'):
                        print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + config['proxy']['retry'])
                        i = i + 1
                    else:
                        extrafanart_count_succ += 1
                        break
        self.addTextMain("[+] 🟢 ExtraFanart downloaded complete! Total %s , success %s " % (extrafanart_count, extrafanart_count_succ))

    # ======================================================================================打印NFO
    def PrintFiles(self, nfo_name, nfo_path, path, file_name, c_word, leak, json_data, file_path, failed_folder, config):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        if int(config.getint('file_download', 'nfo')) == 0:
            return True
        # self.addTextMain("[!] ⏳ Start creating nfo... ")
        # 获取在媒体文件中显示的规则，不需要过滤Windows异常字符
        name_media = json_data['naming_media'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                         year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)

        try:
            if not os.path.exists(path):
                os.makedirs(path)
            if os.path.exists(nfo_path):
                os.remove(nfo_path)
            with open(nfo_path, "wt", encoding='UTF-8') as code:
                print('<?xml version="1.0" encoding="UTF-8" ?>', file=code)
                print("<movie>", file=code)
                # 输出番号
                print("  <num>" + number + "</num>", file=code)
                # 输出标题
                print("  <title>" + name_media + "</title>", file=code)
                # 输出简介
                if outline != 'unknown':
                    print("  <outline>" + outline + "</outline>", file=code)
                    print("  <plot>" + outline + "</plot>", file=code)
                # 输出合集、系列
                print("  <set>" + series + "</set>", file=code)
                print("  <series>" + series + "</series>", file=code)
                # 输出发行日期
                if release != 'unknown':
                    print("  <premiered>" + release + "</premiered>", file=code)
                    print("  <release>" + release + "</release>", file=code)
                # 输出年代
                if str(year) != 'unknown':
                    print("  <year>" + year + "</year>", file=code)
                # 输出时长
                if str(runtime) != 'unknown':
                    print("  <runtime>" + str(runtime).replace(" ", "") + "</runtime>", file=code)
                # 输出评分
                try:
                    if str(json_data['score']) != 'unknown' and str(json_data['score']) != '' and float(
                            json_data['score']) != 0.0:
                        print("  <rating>" + str(json_data['score']) + "</rating>", file=code)
                except Exception as err:
                    print("Error in json_data score!" + str(err))
                # 输出导演
                if director != 'unknown':
                    print("  <director>" + director + "</director>", file=code)
                # 输出厂商
                if studio != 'unknown':
                    print("  <studio>" + studio + "</studio>", file=code)
                # 输出制作商
                if studio != 'unknown':
                    print("  <maker>" + studio + "</maker>", file=code)
                # 输出发行商
                if publisher != 'unknown':
                    print("  <maker>" + publisher + "</maker>", file=code)
                # 输出图片文件位置
                print("  <cover>" + cover + "</cover>", file=code)
                print("  <poster>" + file_name + "-poster.jpg</poster>", file=code)
                print("  <thumb>" + file_name + "-thumb.jpg</thumb>", file=code)
                print("  <fanart>" + file_name + "-fanart.jpg</fanart>", file=code)
                # 输出演员
                if actor_photo and actor_photo != 'unknown':
                    try:
                        for key, value in actor_photo.items():
                            if str(key) != 'unknown' and str(key) != '':
                                print("  <actor>", file=code)
                                print("   <name>" + key + "</name>", file=code)
                                if not value == '':  # or actor_photo == []:
                                    print("   <thumb>" + value + "</thumb>", file=code)
                                print("  </actor>", file=code)
                    except Exception as ex:
                        self.addTextMain('[!] 🔴 Error when print actor to nfo\n   >>> ' + str(ex))
                elif actor and actor != 'unknown':
                    actor_list = str(json_data.get('actor')).strip("[ ]").replace("'", '').split(',')  # 字符串转列表
                    actor_list = [actor.strip() for actor in actor_list]  # 去除空白
                    if actor_list:
                        for actor in actor_list:
                            print("  <actor>", file=code)
                            print("   <name>" + actor + "</name>", file=code)
                            print("  </actor>", file=code)
                print("  <label>", file=code)
                print("  </label>", file=code)
                # 输出tag and genre
                try:
                    for i in tag:
                        if i != 'unknown':
                            print("  <tag>" + i + "</tag>", file=code)
                except Exception as ex:
                    self.addTextMain('[-]Error in tag: ' + str(ex))
                if json_data['imagecut'] == 3:
                    print("  <tag>無碼</tag>", file=code)
                if leak:
                    print("  <tag>流出</tag>", file=code)
                if c_word:
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
                except Exception as ex:
                    self.addTextMain('[!] 🔴 Error when print genre to nfo\n   >>> ' + str(ex))
                if json_data['imagecut'] == 3:
                    print("  <genre>無碼</genre>", file=code)
                if leak:
                    print("  <genre>流出</genre>", file=code)
                if c_word:
                    print("  <genre>中文字幕</genre>", file=code)
                if series != 'unknown':
                    print("  <genre>" + '系列:' + series + "</genre>", file=code)
                if studio != 'unknown':
                    print("  <genre>" + '製作:' + studio + "</genre>", file=code)
                if publisher != 'unknown':
                    print("  <genre>" + '發行:' + publisher + "</genre>", file=code)
                print("  <website>" + website + "</website>", file=code)
                print("</movie>", file=code)
                # self.addTextMain("[+] 🟢 Nfo created successfully! \n   >>> The nfo file name is '%s'" % nfo_name)
                self.addTextMain("[+] 🟢 Nfo created successfully!")
        except Exception as ex:
            self.addTextMain('[!] 🔴 Failed to created nfo! \n   >>>  %s' % str(ex))
            # self.moveFailedFolder(file_path, failed_folder, config)

    # ======================================================================================thumb复制为fanart
    def copyRenameJpgToFanart(self, fanart_name, thumb_path, fanart_path, config):
        if int(config.getint('file_download', 'fanart')) == 1:
            # self.addTextMain("[!] ⏳ Start creating fanart by copying the thumb... ")
            if os.path.exists(thumb_path):
                if os.path.exists(fanart_path):
                    os.remove(fanart_path)
                shutil.copy(thumb_path, fanart_path)
                # self.addTextMain("[+] 🟢 Fanart created successfully! \n   >>> The fanart name is '%s'" % fanart_name)
                self.addTextMain("[+] 🟢 Fanart created successfully!")
                return True
            self.addTextMain('[!] 🔴 Failed to create fanart! the thumb is not exist!')
        return False

    # ======================================================================================移动视频、字幕
    def pasteFileToFolder(self, file_path, file_new_path, failed_folder, config):
        if int(config.getint('common', 'soft_link')) == 1:  # 如果使用软链接
            os.symlink(file_path, file_new_path)
            self.addTextMain("[+] 🟢 Movie Linked successfully! \n   >>> The new link is '%s'" % file_new_path)
            return True
        # self.addTextMain("[!] ⏳ Start move the movie file... ")
        try:
            if file_path == file_new_path:
                self.addTextMain("[!] 🟢 Movie file is already in success folder! no need to movie it again!\n   >>> The current path is '%s'" % file_new_path)
            elif file_path != file_new_path and not os.path.exists(file_new_path):
                shutil.move(file_path, file_new_path)
                self.addTextMain("[+] 🟢 Movie file moved successfully! \n   >>> The new path is '%s" % file_new_path)
            else:
                # self.moveFailedFolder(file_path, failed_folder, config)
                return False
            return True
        except PermissionError:
            self.addTextMain('[!] 🔴 Failed to move movie file to success folder! \n   >>> No permission! Please run as Administrator!')
        except Exception as ex:
            self.addTextMain('[!] 🔴 Failed to move movie file  to success folder! \n   >>> %s' % str(ex))
        return False

    # ======================================================================================有码片裁剪封面
    def cutImage(self, imagecut, path, thumb_name, poster_name, thumb_path, poster_path, cover_small_path):
        if imagecut != 3:
            if not os.path.exists(thumb_path):
                if os.path.exists(cover_small_path):
                    thumb_path = cover_small_path
                else:
                    self.addTextMain("[!] 🔴 Can't cut, beacuse thumb.jpg and cover_small.jpg are not exist!")
                    return False
            if os.path.exists(poster_path):
                os.remove(poster_path)
            if imagecut == 0:   # 中间裁剪
                if self.image_cut(thumb_name, poster_name, thumb_path, poster_path):
                    return True
            else:   # 右边裁剪
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
                    img2.save(path + '/' + poster_name)
                    # self.addTextMain("[+] 🟢 Poster created successfully!\n   >>> The poster name is '%s'\n   >>> Cut from the right side of the thumb" % poster_name)
                    self.addTextMain("[+] 🟢 Poster created successfully! Cut from the right side of the thumb")
                    return True
                except Exception as ex:
                    self.addTextMain('[!] 🔴 Poster cut failed!\n   >>> ' + str(ex))
                    return False
        else:
            self.addTextMain('[!] 🔴 Poster is not cut! beacuse imagecut=3, it mean only download!')
            return False

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
        except Exception as ex:
            self.addTextMain('[-]Error in fix_size: ' + str(ex))

    # ======================================================================================添加水印
    def add_mark(self, poster_path, thumb_path, c_word, leak, uncensored, config):
        mark_type = config.get('mark', 'mark_type')
        mark_type_list = mark_type.upper().split(',')
        mark_list = []
        for mark_type in mark_type_list:
            if mark_type.lower() == 'sub' and c_word:
                mark_list.append('字幕')
            elif mark_type.lower() == 'leak' and leak:
                mark_list.append('流出')
            elif mark_type.lower() == 'uncensored' and int(uncensored) == 1:
                mark_list.append('无码')
        if mark_list:
            mark_show_type = str(mark_list).strip(" ['']").replace("'", "")
            mark_pos = config.get('mark', 'mark_pos')
            mark_size = int(config.getint('mark', 'mark_size'))
            if config.getint('mark', 'thumb_mark') and config.getint('file_download', 'thumb') and os.path.exists(thumb_path):
                self.add_mark_thread(thumb_path, mark_list, mark_pos, mark_size)
                self.addTextMain('[+] 🟢 Thumb has been watermarked: ' + mark_show_type)
            if int(config.getint('mark', 'poster_mark')) and int(config.getint('file_download', 'poster')) and os.path.exists(poster_path):
                self.add_mark_thread(poster_path, mark_list, mark_pos, mark_size)
                self.addTextMain('[+] 🟢 Poster has been watermarked: ' + mark_show_type)

    def add_mark_thread(self, pic_path, mark_list, mark_pos, mark_size):
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


    # ======================================================================================更新进度条
    def set_processbar(self, value):
        self.Ui.progressBar_avdc.setProperty("value", value)

    def showDataResult(self, json_data, config):
        if json_data['error_type'] or json_data['title'] == '':
            self.addTextMain('[!] 🙊 Data request failed!')
            self.showDebugInfo(json_data, config)    # 调试模式打开时显示详细日志
            return False
        else:
            self.addTextMain('[!] 🙉 Data request successfully!')
            self.showDebugInfo(json_data, config)    # 调试模式打开时显示详细日志
            return True

    # ======================================================================================输出调试信息
    def showDebugInfo(self, json_data, config):
        if int(config.getint('debug_mode', 'switch')) == 1:    # 调试模式打开时显示详细日志
            try:
                self.addTextMain('[+] ****** Debug Info* *****')
                self.addTextMain(json_data['log_info'].strip('\n'))
            except Exception as ex:
                self.addTextMain('[!] 🔴 Error in showDebugInfo: ' + str(ex))

    # ======================================================================================输出 Movie 信息
    def showMovieInfo(self, json_data, config):
        if not config.getint('debug_mode', 'switch'):    # 调试模式打开时显示详细日志
            return
        try:
            for key, value in json_data.items():
                if value == '' or key == 'imagecut' or key == 'search_url' or key == 'log_info' or key == 'error_type' or key == 'error_info' or key == 'naming_media' or key == 'naming_file' or key == 'folder_name' or key == 'extrafanart' or key == 'actor_photo':
                    continue
                if len(str(value)) == 0:
                    continue
                elif key == 'tag':
                    value = str(json_data['tag']).strip(" ['']").replace('\'', '')
                self.addTextMain('   >>> ' + "%-13s" % key + ': ' + str(value))
        except Exception as ex:
            self.addTextMain('[!] 🔴 Error in showMovieInfo: ' + str(ex))

    # ======================================================================================创建输出文件夹
    def creatFolder(self, success_folder, json_data, config, c_word):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        title = re.sub(r'[\\/:*?"<>|\r\n]+', '', title)
        if len(actor.split(',')) >= 10:  # 演员过多取前五个
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        folder_name = json_data['folder_name'].replace('\\', '/')
        if str(config['Name_Rule']['folder_name_C']) != '1':
            c_word = ''
        folder_new_name = folder_name.replace('title', title).replace('studio', studio).replace('year', year).replace('runtime',
                                                                                                           runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number + c_word).replace(
            'series', series).replace('publisher', publisher)  # 生成文件夹名
        folder_new_name = folder_new_name.replace('--', '-').strip('-')
        folder_new_name = re.sub(r'[\\:*?"<>|\r\n]+', '', folder_new_name).strip('/')
        if len(folder_new_name) > 100:  # 文件夹名过长 取标题前70个字符
            self.addTextMain('[-]文件夹名过长，取前70个字符!')
            folder_new_name = folder_new_name.replace(title, title[0:70])
        folder_new_path = os.path.join(success_folder, folder_new_name)
        folder_new_path = folder_new_path.replace('--', '-').replace('\\', '/').strip('-')
        if not os.path.exists(folder_new_path):
            os.makedirs(folder_new_path)
        return folder_new_path

    # ======================================================================================从指定网站获取json_data
    def getJsonData(self, mode, number, config, appoint_url, translate_language):
        # if mode == 4:  # javdb模式
        #     ss = random.randint(0, 3)
        #     self.addTextMain('[!]Please Wait %s Seconds！' % str(ss))
        #     time.sleep(ss)
        json_data = getDataFromJSON(number, config, mode, appoint_url, translate_language)
        return json_data

    # ======================================================================================json_data添加到主界面
    def add_label_info(self, json_data):
        try:
            t = threading.Thread(target=self.add_label_info_Thread, args=(json_data,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('[-]Error add_label_info: ' + str(ex))

    def add_label_info_Thread(self, json_data):
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
            }
        self.Ui.label_number.setText(json_data['number'])
        self.laberl_number_url = json_data['website']
        self.thumb_path = json_data['thumb_path']
        self.poster_path = json_data['poster_path']
        self.Ui.label_actor.setText(json_data['actor'])
        if json_data.get('source'):
            self.Ui.label_source.setText('数据：' + json_data['source'].replace('.main_us','').replace('.main',''))
        else:
            self.Ui.label_source.setText('')
        self.Ui.label_title.setText(json_data['title'])
        self.Ui.label_outline.setText(json_data['outline'])
        self.Ui.label_tag.setText(str(json_data['tag']).strip(" [',']").replace('\'', ''))
        self.Ui.label_release.setText(json_data['release'])
        if json_data['runtime']:
            self.Ui.label_runtime.setText(json_data['runtime'] + ' 分钟')
        else:
            self.Ui.label_runtime.setText(json_data['runtime'])
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
            else:
                self.Ui.label_poster.setText("封面图")
            if os.path.exists(thumb_path):
                pix = QPixmap(thumb_path)
                self.Ui.label_thumb.setScaledContents(True)
                self.Ui.label_thumb.setPixmap(pix)  # 添加缩略图
            else:
                self.Ui.label_thumb.setText("缩略图")

    # ======================================================================================检查更新
    def updateCheck(self):
        if self.Ui.radioButton_update_on.isChecked():
            self.addTextMain('[!]' + 'Update Checking!'.center(80))                 
            try:
                result, html_content = get_html('https://api.github.com/repos/Hermit10/AVDCx/releases/latest')
                if not result:
                    self.addTextMain('[-]' + ('UpdateCheck Failed! reason: ' + html_content).center(80))
                    self.addTextMain("[*]================================================================================")
                    return False
                data = json.loads(html_content)
            except Exception as ex:
                self.addTextMain('[!]' + ('UpdateCheck Failed! Error info: ' + str(ex)).center(80))
                self.addTextMain("[*]================================================================================")
                return False
            if not data.get('tag_name'):
                try:
                    result, html_content = get_html('https://api.github.com/repos/Hermit10/temp/releases/latest')
                    if not result:
                        self.addTextMain('[-]' + ('UpdateCheck Failed! reason: ' + html_content).center(80))
                        self.addTextMain("[*]================================================================================")
                        return False
                    data = json.loads(html_content)
                except Exception as ex:
                    self.addTextMain('[!]' + ('UpdateCheck Failed! Error info: ' + str(ex)).center(80))
                    self.addTextMain("[*]================================================================================")
                    return False
            if data.get('tag_name'):
                if 'AVDCx' in data.get('url'):
                    self.github_project_url = 'https://github.com/Hermit10/AVDCx/'
                remote = int(data["tag_name"].replace(".",""))
                localversion = int(self.localversion.replace(".", ""))
                new_content = str(data["body"].replace(".","")).replace('====', '').replace('===', '').replace('\r\n', '\n   [+]')
                if localversion < remote:
                    self.Ui.label_show_version.setText('🍉 New! update ' + str(data["tag_name"]))
                    self.addTextMain('[*]' + ('* New update ' + str(data["tag_name"]) + ' is Available *').center(80))
                    self.addTextMain("[*]" + ("").center(80, '='))
                    self.addTextMain('   [+]更新内容:' + new_content)
                    self.addTextMain('   [+]\n   [+]下载地址: https://github.com/Hermit10/temp/releases')
                else:
                    self.addTextMain('[!]' + 'No Newer Version Available!'.center(80))
                self.addTextMain("[*]================================================================================")
            else:
                self.addTextMain('[-]' + ('UpdateCheck Failed!').center(80))
                self.addTextMain("[*]================================================================================")
        return True

    def updateCheckStart(self):
        try:
            t = threading.Thread(target=self.updateCheck)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addTextMain('[-]update check error : ' + str(ex))     

    def show_netstatus(self, proxy_info):
        self.addNetTextMain(time.strftime('%Y-%m-%d %H:%M:%S').center(80, '='))
        proxy_type = ''
        retry_count = 0
        proxy = ''
        timeout = 0
        try:
            proxy_type, proxy, timeout, retry_count = proxy_info
        except Exception as ex:
            print('[-]get config failed when check net, error info: ! ' + str(ex))
        if proxy == '' or proxy_type == '' or proxy_type == 'no':
            self.addNetTextMain(' 当前网络状态：❌ 未启用代理\n   类型： ' + str(proxy_type) + '    地址：' + str(proxy) + '    超时时间：' + str(timeout) + '    重试次数：' + str(retry_count))
        else:
            self.addNetTextMain(' 当前网络状态：✅ 已启用代理\n   类型： ' + proxy_type + '    地址：' + proxy + '    超时时间：' + str(timeout) + '    重试次数：' + str(retry_count))
        self.addNetTextMain('='*80)

    def netResult(self):
        # 显示代理信息
        self.addNetTextMain('\n🛑 开始检测网络....')
        self.show_netstatus(self.current_proxy)
        # 检测网络连通性
        self.addNetTextMain(' 检测网络连通性...')
        net_info = [['github', 'https://raw.githubusercontent.com' , ''], ['airav', 'https://www.airav.wiki' , ''], ['javbus', 'https://www.javbus.com' , ''], ['javdb', 'https://www.javdb.com', ''], ['jav321', 'https://www.jav321.com' , ''], ['dmm', 'https://www.dmm.co.jp' , ''], ['avsox', 'https://avsox.website' , ''], ['xcity', 'https://xcity.jp' , ''], ['mgstage', 'https://www.mgstage.com', ''], ['fc2hub', 'https://fc2hub.com', '']]
        for each in net_info:
            error_tips = '连接失败, 请检查网络或代理设置！'
            try:
                result, html_content = get_html(each[1])
                if not result:
                    each[2] = '❌ ' + each[1] + ' ' + str(error_tips)
                else:
                    if each[0] == 'dmm':
                        if re.findall('このページはお住まいの地域からご利用になれません', html_content):
                            error_tips = '地域限制, 请使用日本节点访问！'
                            each[2] = '❌ ' + each[1] + ' ' + str(error_tips)
                        else:
                            each[2] = '✅ 连接正常'
                    else:
                        each[2] = '✅ 连接正常'
            except Exception as ex:
                each[2] = '测试连接时出现异常！信息:' + str(ex)
            self.addNetTextMain('   ' + each[0].ljust(8) + each[2])
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
            # self.count_claw += 1
            t = threading.Thread(target=self.netResult)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as ex:
            self.addNetTextMain('[-]Error in netCheck: ' + str(ex))        


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
    def creatFailedFolder(self, failed_folder, config):
        if int(config.getint('common', 'failed_file_move')) == 1 and not os.path.exists(failed_folder):
            try:
                os.makedirs(failed_folder)
                # self.addTextMain("[!] 🟢 The failed folder created successfully! \n   >>> The folder path is '%s'" % failed_folder)
                self.addTextMain("[!] 🟢 The failed folder created successfully!")
            except Exception as ex:
                self.addTextMain('[-] 🔴 Error: Failed to create the failed folder\n   >>> ' + str(ex))

    # ======================================================================================删除空目录
    def CEF(self, path):
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    try:
                        hidden_file = root.replace('\\', '/') + '/' + dir +'/.DS_Store'
                        if os.path.exists(hidden_file):
                            os.remove(hidden_file)  # 删除隐藏文件
                        os.removedirs(root.replace('\\', '/') + '/' + dir)  # 删除这个空文件夹
                        self.addTextMain('[*]' + '='*80)
                        self.addTextMain('[+]Deleting empty folder: ' + root.replace('\\', '/') + '/' + dir)
                    except:
                        delete_empty_folder_failed = ''

    def showListName(self, filename, result, json_data, real_number=''):
        if result == 'succ':
            node = QTreeWidgetItem(self.item_succ)
            node.setText(0, filename)
            self.item_succ.addChild(node)
        else:
            node = QTreeWidgetItem(self.item_fail)
            node.setText(0, filename)
            self.item_fail.addChild(node)
        if not json_data.get('number'):
            json_data['number'] = real_number
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


    # =====================================================================================获取视频文件列表（区分文件夹刮削或单文件刮削）
    def getMovieList(self, file_mode, movie_path=''):
        movie_list = []
        appoint_number = ''
        appoint_url = ''
        escape_folder = self.Ui.lineEdit_escape_dir.text().replace('\\', '/')          # 多级目录刮削需要排除的目录
        movie_type = self.Ui.lineEdit_movie_type.text()
        if file_mode == 'default_folder':                                       # 刮削默认视频目录的文件
            mode = self.Ui.comboBox_website_all.currentIndex() + 1
            movie_list = movie_lists(escape_folder, movie_type, movie_path)     # 获取所有需要刮削的影片列表
            count_all = len(movie_list)

        elif file_mode == 'single_file':                                        # 刮削单文件（工具页面）
            mode = self.Ui.comboBox_website.currentIndex() + 1
            file_path = self.select_file_path
            appoint_number = self.Ui.lineEdit_movie_number.text().upper()
            appoint_url = self.Ui.lineEdit_appoint_url.text()
            movie_list.append(file_path)                                         # 把文件路径添加到movie_list
            count_all = 1
        return movie_list, count_all, mode, appoint_number, appoint_url


    # =====================================================================================获取视频路径设置
    def getMoviePathSetting(self):
        movie_path = self.Ui.lineEdit_movie_path.text()                         # 用户设置的扫描媒体路径
        if movie_path == '':
            movie_path = os.getcwd().replace('\\', '/')                         # 主程序当前路径
        failed_folder = movie_path + '/' + self.Ui.lineEdit_fail.text()         # 失败输出目录
        success_folder = movie_path + '/' + self.Ui.lineEdit_success.text()     # 成功输出路径
        return movie_path.replace('\\', '/'), failed_folder.replace('\\', '/'), success_folder.replace('\\', '/')

    # =====================================================================================获取文件的相关信息
    def getFileInfo(self, file_path, appoint_number=''):
        c_word = ''
        cd_part = ''
        leak = ''
        movie_number = ''
        sub_list = []
        # 获取文件名
        folder_path, file_full_name = os.path.split(file_path)  # 获取去掉文件名的路径、完整文件名（含扩展名）
        file_name, file_ex = os.path.splitext(file_full_name)  # 获取文件名（不含扩展名）、扩展名(含有.)
        # 获取番号
        if appoint_number:      # 如果指定了番号，则使用指定番号
            movie_number = appoint_number.upper()
        else:
            escape_string = self.Ui.lineEdit_escape_string.text()
            movie_number = getNumber(file_path, escape_string).upper()
        # 判断是否流出
        if '流出' in file_name:
            leak = '-流出'
        # 判断是否分集及分集序号
        if '-cd' in file_name.lower():
            part_list = re.search('-cd\d+', file_name.lower())
            if part_list:
                cd_part = part_list[0]
        # 判断是否中文字幕
        if '-C.' in file_full_name.upper() or '-C ' in file_full_name.upper() or '中文' in file_path or '字幕' in file_path:                                                 
            if '無字幕' not in file_path and '无字幕' not in file_path:
                c_word = '-C'   # 中文字幕影片后缀
        # 查找本地字幕文件
        sub_type = self.Ui.lineEdit_sub_type.text().split('|')  # 本地字幕后缀
        for sub in sub_type:    # 查找本地字幕, 可能多个
            if os.path.exists(folder_path + '/' + file_name + sub):
                sub_list.append(sub)
                c_word = '-C'

        file_show_name = str(movie_number) + cd_part + c_word
        file_show_path = self.showFilePath(file_path)
        return movie_number, folder_path, file_name, file_ex, leak, cd_part, c_word, sub_list, file_show_name, file_show_path

    # =====================================================================================有道翻译
    def youdao(self, msg, language='zh_cn'):
        proxy_type, proxy, timeout, retry_count = get_proxy()
        proxies = get_proxies(proxy_type, proxy)
        msg = msg
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        D = "Y2FYu%TNSbMCxc3t2u^XT"
        salt = str(int(time.time() * 1000) + random.randint(0, 10))
        sign = hashlib.md5(("fanyideskweb" + msg + salt + D).encode('utf-8')).hexdigest()
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
                self.addTextMain('   >>> 提示：有道翻译接口返回数据异常！将跳过翻译！返回内容：%s 错误：%s' % (req, str(ex)))
            else:
                # 找到翻译结果
                if 'translateResult' in translate_results:
                    translateResult = translate_results.get('translateResult')
                    msg = ''
                    for each in translateResult[0]:
                        msg += each.get('tgt')
        if language == 'zh_tw':
            msg = zhconv.convert(msg, 'zh-hant')
        elif language == 'zh_cn':
            msg = zhconv.convert(msg, 'zh-cn')
        return msg

    # =====================================================================================处理翻译
    def transLanguage(self, movie_number, jsonfile_data, json_data, translate_language):
        if translate_language != 'ja':
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
            if not movie_title:
                movie_title =json_data['title']

            if translate_language == 'zh_cn':
                json_data['title'] = self.youdao(movie_title, 'zh_cn')
                if json_data.get('outline').strip():
                    json_data['outline'] = self.youdao(json_data['outline'], 'zh_cn')

            elif translate_language == 'zh_tw':
                json_data['title'] = self.youdao(movie_title, 'zh_tw')
                if json_data.get('outline').strip():
                    json_data['outline'] = self.youdao(json_data['outline'], 'zh_tw')

    # =====================================================================================处理单个文件刮削
    def coreMain(self, file_path, movie_number, config, mode, count, succ_count=0, fail_count=0, appoint_number='', appoint_url='', jsonfile_data={}):
        # =====================================================================================初始化所需变量
        sub_list = []
        leak = ''
        cd_part = ''
        c_word = ''
        uncensored = 0
        config_file = 'config.ini'
        config = RawConfigParser()
        config.read(config_file, encoding='UTF-8')
        translate_language = config.get('common', 'translate_language')

        # 获取设置的媒体目录、失败目录、成功目录
        movie_path, failed_folder, success_folder = self.getMoviePathSetting()

        # 获取文件信息
        movie_number, folder_path, file_name, file_ex, leak, cd_part, c_word, sub_list, file_show_name, file_show_path = self.getFileInfo(file_path, appoint_number)

        # 获取json_data
        json_data = self.getJsonData(mode, movie_number, config, appoint_url, translate_language)

        # 处理json_data
        data_result = self.showDataResult(json_data, config)    # 显示 make data 的结果和日志
        if not data_result:
            return False, json_data                 # 返回AVDC_main, 继续处理下一个文件

        # 处理翻译
        self.transLanguage(movie_number, jsonfile_data, json_data, translate_language)
        self.showMovieInfo(json_data, config)   # 显示翻译后的json_data

        # 开始处理当前文件
        # =====================================================================================创建目标文件夹
        try:
            path = self.creatFolder(success_folder, json_data, config, c_word)
            # self.addTextMain("[+] 🟢 Folder created successfully! \n   >>> The folder path is '%s'" % path)
            self.addTextMain("[+] 🟢 Folder created successfully!")
        except Exception as ex:
            self.addTextMain('[!] 🔴 Failed to create folder! \n   >>> ' + str(ex))
            return False, json_data                    # 返回AVDC_main, 继续处理下一个文件


        # =====================================================================================更新实体文件命名规则
        number = json_data['number']
        naming_rule = str(self.getNamingRule(json_data, config)).replace('--', '-').strip('-')  # 用在保存文件时的名字，需要过滤window异常字符
        naming_rule = naming_rule + leak + cd_part + c_word

        # =====================================================================================生成文件和图片新路径路径
        file_new_path = os.path.join(path, (naming_rule + file_ex))
        thumb_name = naming_rule + '-thumb.jpg'
        poster_name = naming_rule + '-poster.jpg'
        fanart_name = naming_rule + '-fanart.jpg'
        nfo_name = naming_rule + '.nfo'
        cover_small_name = path + 'cover_small.jpg'
        thumb_path = os.path.join(path, thumb_name)
        poster_path = os.path.join(path, poster_name)
        fanart_path = os.path.join(path, fanart_name)
        nfo_path = os.path.join(path, nfo_name)
        cover_small_path = os.path.join(path, cover_small_name)

        # =====================================================================================判断目标文件夹文件是否已存在
        if os.path.exists(file_new_path):
            if file_new_path != file_path:
                json_data['error_info'] = "The success folder already has a same name file! \n   >>> The success path '%s' already exists \n   >>> The file will not be moved to the success floder!" % file_new_path
                json_data['title'] = "The success folder already has a same name file!"
                json_data['poster_path'] = poster_path
                json_data['thumb_path'] = thumb_path
                return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================整理模式
        if int(config.getint('common', 'main_mode')) == 2: # 整理模式（仅根据女优把电影命名为番号并分类到女优名称的文件夹下）
            if not self.pasteFileToFolder(file_path, file_new_path, failed_folder, config):   # 移动文件
                return False, json_data                   # 返回AVDC_main, 继续处理下一个文件
            else:
                return True, json_data
        # =====================================================================================刮削模式

        # =====================================================================================设置图片裁剪方式
        # imagecut: 0 裁剪中间, 1 裁剪右面, 2 工具页面裁剪, 3 仅下载小封面
        if json_data['imagecut'] == 3:  # imagecut=3为仅下载小封面(无码)
            uncensored = 1
            if int(config.getint('uncensored', 'uncensored_poster')) == 1: # 允许裁剪时3改成0
                json_data['imagecut'] = 0

        # =====================================================================================下载thumb
        if not self.thumbDownload(json_data, path, config, thumb_name, thumb_path):
            return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================下载poster
        if not self.posterDownload(json_data, path, config, thumb_name, poster_name, thumb_path, poster_path, cover_small_path):
            return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================下载艺术图
        self.copyRenameJpgToFanart(fanart_name, thumb_path, fanart_path, config)

        # =====================================================================================删除thumb.jpg(当选择不保存时)
        self.deletethumb(thumb_name, thumb_path, config)

        # =====================================================================================加水印
        self.add_mark(poster_path, thumb_path, c_word, leak, uncensored, config)

        # =====================================================================================输出nfo文件
        if self.PrintFiles(nfo_name, nfo_path, path, file_name, c_word, leak, json_data, file_path, failed_folder, config):
            return False, json_data                   # 返回AVDC_main, 继续处理下一个文件

        # =====================================================================================下载剧照
        self.extrafanartDownload(json_data, path, config)

        # =====================================================================================移动文件
        self.pasteFileToFolder(file_path, file_new_path, failed_folder, config)

        # =====================================================================================移动字幕
        for sub in sub_list:
            shutil.move(folder_path + '/' + file_name + sub, path + '/' + naming_rule + sub) 
            self.addTextMain("[+] 🟢 Sub file '%s' moved successfully! " % (naming_rule + sub))

        # =====================================================================================json添加封面项
        json_data['thumb_path'] = thumb_path
        json_data['poster_path'] = poster_path
        json_data['number'] = number

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
        self.add_label_info(json_data)
        config_file = 'config.ini'
        config = RawConfigParser()
        config.read(config_file, encoding='UTF-8')
        # 获取设置的媒体目录、失败目录、成功目录
        movie_path, failed_folder, success_folder = self.getMoviePathSetting()
        # 获取待刮削文件列表的相关信息
        movie_list, count_all, mode, appoint_number, appoint_url = self.getMovieList(file_mode, movie_path)
        # 日志页面显示信息
        self.addTextMain('[+]Find ' + str(count_all) + ' movies')
        if count_all == 0:
            self.progressBarValue.emit(int(100))
        else:
            self.count_claw += 1
            if config['common']['soft_link'] == '1':
                self.addTextMain('[!] --- Soft link mode is ENABLE! ----')
        with open(self.c_numuber_jsonfile, encoding='UTF-8') as data:
            jsonfile_data = json.load(data)            

        # 处理视频列表
        for file_path in movie_list:
            count += 1
            # 获取进度
            progress_value = count / count_all * 100    
            progress_percentage = '%.2f' % progress_value + '%'                     

            # 获取文件基础信息
            movie_number, folder_path, file_name, file_ex, leak, cd_part, c_word, sub_list, file_show_name, file_show_path = self.getFileInfo(file_path, appoint_number)

            # 显示刮削信息
            self.Ui.label_file_path.setText('正在刮削： ' + str(count) + '/' + str(count_all) + ' （' + progress_percentage + '）\n' + file_show_path)
            self.Ui.label_result.setText('成功：%s  失败：%s' % (succ_count, fail_count))
            self.progressBarValue.emit(int(progress_value))
            self.addTextMain('[*]' + '='*80)
            self.addTextMain('[!]Round (' + str(self.count_claw) + ') - [' + str(count) + '/' + str(count_all) + '] - ' + progress_percentage)
            self.addTextMain('[*]' + '='*80)
            if file_mode == 'single_file':
                self.addTextMain('[!]当前为单文件刮削模式: \n   >>> 指定番号：%s\n   >>> 刮削地址：%s\n   >>> 刮削网站：%s' % (appoint_number, appoint_url, str(mode)))
            self.addTextMain("[+] 🙈 Requesting Data for [" + file_path + "], the number is [" + movie_number + "]")
            succ_count += 1
            fail_count += 1
            succ_show_name = str(self.count_claw) + '-' + str(succ_count) + '.' + file_show_name
            fail_show_name = str(self.count_claw) + '-' + str(fail_count) + '.' + file_show_name
            # 处理文件
            try:
                result, json_data = self.coreMain(file_path, movie_number, config, mode, count, succ_count, fail_count, appoint_number, appoint_url, jsonfile_data)
            except Exception as ex:
                json_data = {}   # 清空数据，因为崩溃时json_data是上一个文件的数据
                json_data['error_info'] = 'getJsonData error : ' + str(ex)
                result = False
            if not result:
                succ_count -= 1
                self.showListName(fail_show_name, 'fail', json_data, movie_number)
                self.addTextMain('[!] 🔴 Error: ' + json_data['error_info'])
                self.moveFailedFolder(file_path, failed_folder, config)
            else:
                fail_count -= 1
                self.showListName(succ_show_name, 'succ', json_data, movie_number)
                self.addTextMain('[!] 💯 [%s] has been completed successfully!' % file_show_name)
        self.Ui.label_result.setText('成功：%s  失败：%s' % (succ_count, fail_count))
        self.progressBarValue.emit(100)
        self.Ui.label_file_path.setText('🎉 恭喜！全部刮削完成！共 %s 个文件！' % count_all)
        self.addTextMain("[*]================================================================================")
        self.addTextMain("[+]Total %s , Success %s , Failed %s" % (count_all, succ_count, fail_count))
        self.CEF(movie_path)
        self.addTextMain("[*]================================================================================")
        self.addTextMain("[+]All finished!!!")
        self.addTextMain("[*]================================================================================")
        self.Ui.pushButton_start_cap.setEnabled(True)
        self.Ui.pushButton_start_cap2.setEnabled(True)
        self.Ui.pushButton_start_cap.setText('开始')
        self.Ui.pushButton_start_cap2.setText('开始')
        self.Ui.pushButton_start_cap.setStyleSheet('QPushButton#pushButton_start_cap{color:white;background-color:#0066CC;}QPushButton:hover#pushButton_start_cap{color:white;background-color:#4C6EFF}QPushButton:pressed#pushButton_start_cap{color:white;background-color:#4C6EE0}')
        self.Ui.pushButton_start_cap2.setStyleSheet('QPushButton#pushButton_start_cap2{color:white;background-color:#0066CC}QPushButton:hover#pushButton_start_cap2{color:white;background-color:#4C6EFF}QPushButton:pressed#pushButton_start_cap2{color:white;background-color:#4C6EE0}')

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
        # 控件美化 左侧栏样式
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
        thumb_path = self.thumb_path
        poster_path = self.poster_path
        if not thumb_path or not poster_path:
            return
        # print('裁剪位置：', end='')
        # print(self.c_x, self.c_y, self.c_x2, self.c_y2)

        img = Image.open(thumb_path)
        img = img.convert('RGB')
        img_new_png = img.crop((self.c_x, self.c_y, self.c_x2, self.c_y2))
        # fp.close()
        try:
            if os.path.exists(poster_path):
                os.remove(poster_path)
        except Exception as ex:
            ui.addTextMain("[!] 🔴 Failed to remove old poster!\n   >>> " + str(ex))
            return False
        img_new_png.save(poster_path)
        ui.addTextMain("[+] 🟢 Poster cut successfully!")
        # 加水印
        mark_type = ''
        c_word = ''
        leak = ''
        uncensored = ''
        config_file = 'config.ini'
        config = RawConfigParser()
        config.read(config_file, encoding='UTF-8')

        if self.Ui.checkBox_add_sub.isChecked():
            c_word = True
            mark_type += 'SUB,'
        if self.Ui.checkBox_add_leak.isChecked():
            leak = True
            mark_type += 'LEAK,'
        if self.Ui.checkBox_add_uncensored.isChecked():
            uncensored = True
            mark_type += 'UNCENSORED,'
                                    
        config.set('mark', 'mark_type', mark_type)
        config.set('mark', 'thumb_mark', 0) 
        config.set('mark', 'poster_mark', 1) 

        ui.add_mark(poster_path, thumb_path, c_word, leak, uncensored, config)

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
        self.Ui.label_cut_ratio.setText('%.2f' % self.rect_h_w_ratio)

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
        self.Ui.label_cut_ratio.setText('%.2f' % self.rect_h_w_ratio)
        # 计算裁剪框大小
        if self.pic_h_w_ratio <= 1.5: # 如果高宽比小时，固定高度，右边水平移动
            self.rect_w = int (self.rect_h / self.rect_h_w_ratio)
        else:
            self.rect_h = int(self.rect_w * self.rect_h_w_ratio)
        self.Ui.pushButton_select_cutrange.setGeometry(QRect(self.rect_x, self.rect_y, self.rect_w, self.rect_h))   # 显示裁剪框
        self.getRealPos()  # 显示裁剪框实际位置

    # 打开图片选择框
    def openimage(self):
        img_path, img_type = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if img_path:
            img_name, img_ex = os.path.splitext(img_path)
            poster_path = img_path.replace(('-fanart' + img_ex), '').replace(('-thumb' + img_ex), '').replace(('-poster' + img_ex), '').replace(img_ex, '') + '-poster' + img_ex
            self.thumb_path = img_path
            self.poster_path = poster_path
            ui.thumb_path = img_path
            ui.poster_path = poster_path
            self.showimage(img_path, poster_path)

    # 显示要裁剪的图片
    def showimage(self, img_path='', poster_path=''):
        self.Ui.checkBox_add_sub.setChecked(True) if '-C-' in img_path else  self.Ui.checkBox_add_sub.setChecked(False)
        self.Ui.checkBox_add_leak.setChecked(True) if '-流出' in img_path.upper() else self.Ui.checkBox_add_leak.setChecked(False)
        movie_number, folder_path, file_name, file_ex, leak, cd_part, c_word, sub_list, file_show_name, file_show_path = ui.getFileInfo(img_path)
        self.Ui.checkBox_add_uncensored.setChecked(True) if is_uncensored(movie_number) else self.Ui.checkBox_add_uncensored.setChecked(False)
        
        self.poster_path = poster_path
        self.thumb_path = img_path
        if img_path:
            pic = QPixmap(img_path)
            self.pic_w = pic.width()
            self.pic_h = pic.height()
        self.Ui.label_origin_size.setText('%s, %s' % (str(self.pic_w), str(self.pic_h)))    # 显示宽高
        self.pic_h_w_ratio = self.pic_h / self.pic_w    # 图片高宽比
        self.rect_h_w_ratio = 536.6 / 379
        abc = (self.rect_h_w_ratio - 1) * 10000
        self.Ui.horizontalSlider_left.setValue(abc)
        self.Ui.horizontalSlider_right.setValue(10000 - abc)
        if img_path:
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
    # 显示窗口
    # window.collec_btn.clicked.connect(newWin2.show)
    # ui.Ui.label_thumb.mousePressEvent = newWin2.show
    # ui.Ui.label_poster.mousePressEvent = newWin2.show

    sys.exit(app.exec_())
