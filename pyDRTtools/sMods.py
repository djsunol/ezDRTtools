# -*- coding: utf-8 -*-
__authors__ = 'Derek Johnson'

__date__ = '7th Jan 2025'

global_exDRTname: str  = "ezDRTtools"
global_ezDRTver: str = "1.00.000"
global_ezDRTcommit: str ="6c621c2"
global_ezDRTdate: str = "2025-01-07"

global_pyDRTcommit: str ="4d2817e"
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


def showAboutMessage(self):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle("About ezDRTtools")
    ezver = "ezDRTtools version: " + global_ezDRTver
    ezdate = "ezDRTtools date: " + global_ezDRTdate
    pydate = "pyDRTtools date: " + global_pyDRTdate
    pycommit = "pyDRTtools git commit: " + global_pyDRTcommit
    msg_box.setText(ezver +"\n"+ezdate+ "\n\n"+pydate + "\n"+pycommit)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.exec_()

def showReadMe(self):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readmeez_path = os.path.join(script_dir, 'readme_ezDRTtools.txt')
    readmepy_path = os.path.join(script_dir, 'readme_pyDRTtools.txt')
    licenseez_path = os.path.join(script_dir, 'license_ezDRTtools.txt')
    licensepy_path = os.path.join(script_dir, 'license_pyDRTtools.txt')

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
    manual_path = os.path.join(script_dir, 'pyDRTtools_manual.pdf')

    if manual_path:
        try:
            os.startfile(manual_path)
        except Exception as e:
            print(f"An error occurred: {e}")

def setCaption(self):
    importfile = global_importfile
    if len(importfile) > 0:
        importfile = "  -  " + importfile
    QtWidgets.QMainWindow.setWindowTitle(self, global_exDRTname  + importfile)
