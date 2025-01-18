# -*- coding: utf-8 -*-
__authors__ = 'Derek Johnson'

__date__ = '7th Jan 2025'

global_exDRTname: str  = "ezDRTtools"
global_ezDRTver: str = "1.02"
global_ezDRTdate: str = "2025-01-15"

global_pyDRTver: str ="0.2"
global_pyDRTdate: str = "2024-10-31"

global_importfile: str = ""

import os
import subprocess
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit

global_mainwindow =QtGui

def addAboutMenu(self,mainwindow):
    global_mainwindow = mainwindow
    help_menu = self.menubar.addMenu("&Help")
    about_action = QtWidgets.QAction("&About...",mainwindow)
    about_action.triggered.connect(showAboutMessage)
    help_menu.addAction(about_action)
    readme_action = QtWidgets.QAction("&ReadMe Files",mainwindow)
    readme_action.triggered.connect(showReadMe)
    help_menu.addAction(readme_action)
    manual_action = QtWidgets.QAction("pyDRTtools &Manual",mainwindow)
    manual_action.triggered.connect(showManual)
    help_menu.addAction(manual_action)
    appnote_action = QtWidgets.QAction("ezDRTtools &AppNote",mainwindow)
    appnote_action.triggered.connect(showAppNote)
    help_menu.addAction(appnote_action)
    datafolder_action = QtWidgets.QAction("Example &Data",mainwindow)
    datafolder_action.triggered.connect(showDataFolder)
    help_menu.addAction(datafolder_action)


def showAboutMessage(self):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle("About ezDRTtools")
    eztext = "ezDRTtools (c) 2025 Scribner LLC,\n based on pyDRTtools (c) 2023 ciuccislab\n Open Source MIT License"
    ezver = "ezDRTtools version: " + global_ezDRTver
    ezdate = "ezDRTtools date: " + global_ezDRTdate
    pydate = "pyDRTtools version: " + global_pyDRTver
    pycommit = "pyDRTtools github date: " + global_pyDRTdate
    msg_box.setText(eztext+"\n\n"+ezver +"\n"+ezdate+ "\n\n"+pydate + "\n"+pycommit)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.exec_()

def showReadMe(self):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.dirname(script_dir)  # up 2 folder levels
    script_dir = os.path.dirname(script_dir)
    readmeez_path = os.path.join(script_dir, 'Text\\readme_ezDRTtools.txt')
    readmepy_path = os.path.join(script_dir, 'Text\\readme_pyDRTtools.txt')
    licenseez_path = os.path.join(script_dir, 'Text\license_ezDRTtools.txt')
    licensepy_path = os.path.join(script_dir, 'Text\license_pyDRTtools.txt')

    #msg_box = QtWidgets.QMessageBox()
    #msg_box.setWindowTitle("Readme")
    #msg_box.setText(readmeez_path +" "+ readmepy_path)
    #msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #msg_box.setIcon(QtWidgets.QMessageBox.Information)
    #msg_box.exec_()

    if licensepy_path:
        try:
            os.startfile(licensepy_path)
        except Exception as e:
            print(f"An error occurred: {e}")
    if licenseez_path:
        try:
            os.startfile(licenseez_path)
        except Exception as e:
            print(f"An error occurred: {e}")
    if readmepy_path:
        try:
            os.startfile(readmepy_path)
        except Exception as e:
            print(f"An error occurred: {e}")
    if readmeez_path:
        try:
            os.startfile(readmeez_path)
        except Exception as e:
            print(f"An error occurred: {e}")

def showManual(self):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.dirname(script_dir)  # up 2 folder levels
    script_dir = os.path.dirname(script_dir)
    manual_path = os.path.join(script_dir, 'Manual\pyDRTtools_manual.pdf')

    if manual_path:
        try:
            os.startfile(manual_path)
        except Exception as e:
            print(f"An error occurred: {e}")

def showAppNote(self):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.dirname(script_dir)  # up 2 folder levels
    script_dir = os.path.dirname(script_dir)
    manual_path = os.path.join(script_dir, 'Text\ezDRTtools_AppNote.pdf')

    if manual_path:
        try:
            os.startfile(manual_path)
        except Exception as e:
            print(f"An error occurred: {e}")

def showDataFolder(self):
    data_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.dirname(data_dir)  # up 2 folder levels
    data_dir = os.path.dirname(data_dir)
    data_path = os.path.join(data_dir, 'EIS Data')

    if data_path:
        try:
            os.startfile(data_path)
        except Exception as e:
            print(f"An error occurred: {e}")

def setCaption(self):
    importfile = global_importfile
    if len(importfile) > 0:
        importfile = "  -  " + importfile
    QtWidgets.QMainWindow.setWindowTitle(self, global_exDRTname  + importfile)
