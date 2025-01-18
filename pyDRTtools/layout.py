#-*- coding: utf-8 -*-

__authors__ = 'Francesco Ciucci, Adeleke Maradesa, Baptiste Py, Ting Hei Wan'

__date__ = '12th June 2024'


from PyQt5 import (QtCore, QtGui, QtWidgets)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1625, 996)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(320, 0, 931, 951))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.plot_panel = QtWidgets.QGraphicsView(self.frame)
        self.plot_panel.setGeometry(QtCore.QRect(0, 40, 901, 901))
        self.plot_panel.setObjectName("plot_panel")
        self.show_layout = QtWidgets.QFrame(self.frame)
        self.show_layout.setGeometry(QtCore.QRect(0, 0, 921, 41))
        self.show_layout.setStyleSheet("")
        self.show_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_layout.setObjectName("show_layout")
        self.show_EIS = QtWidgets.QPushButton(self.show_layout)
        self.show_EIS.setGeometry(QtCore.QRect(0, 10, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_EIS.setFont(font)
        self.show_EIS.setObjectName("show_EIS")
        self.show_mag = QtWidgets.QPushButton(self.show_layout)
        self.show_mag.setGeometry(QtCore.QRect(100, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_mag.setFont(font)
        self.show_mag.setObjectName("show_mag")
        self.show_phase = QtWidgets.QPushButton(self.show_layout)
        self.show_phase.setGeometry(QtCore.QRect(230, 10, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_phase.setFont(font)
        self.show_phase.setObjectName("show_phase")
        self.show_re = QtWidgets.QPushButton(self.show_layout)
        self.show_re.setGeometry(QtCore.QRect(320, 10, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_re.setFont(font)
        self.show_re.setObjectName("show_re")
        self.show_im = QtWidgets.QPushButton(self.show_layout)
        self.show_im.setGeometry(QtCore.QRect(420, 10, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_im.setFont(font)
        self.show_im.setObjectName("show_im")
        self.show_re_res = QtWidgets.QPushButton(self.show_layout)
        self.show_re_res.setGeometry(QtCore.QRect(510, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_re_res.setFont(font)
        self.show_re_res.setObjectName("show_re_res")
        self.show_im_res = QtWidgets.QPushButton(self.show_layout)
        self.show_im_res.setGeometry(QtCore.QRect(630, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_im_res.setFont(font)
        self.show_im_res.setObjectName("show_im_res")
        self.show_DRT = QtWidgets.QPushButton(self.show_layout)
        self.show_DRT.setGeometry(QtCore.QRect(750, 10, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_DRT.setFont(font)
        self.show_DRT.setObjectName("show_DRT")
        self.show_score = QtWidgets.QPushButton(self.show_layout)
        self.show_score.setGeometry(QtCore.QRect(820, 10, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_score.setFont(font)
        self.show_score.setObjectName("show_score")
        self.General_frame = QtWidgets.QFrame(self.centralwidget)
        self.General_frame.setGeometry(QtCore.QRect(10, 10, 311, 931))
        self.General_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.General_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.General_frame.setObjectName("General_frame")
        self.settings_layout = QtWidgets.QGroupBox(self.General_frame)
        self.settings_layout.setGeometry(QtCore.QRect(10, 0, 281, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.settings_layout.setFont(font)
        self.settings_layout.setAutoFillBackground(False)
        self.settings_layout.setStyleSheet("QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color: black;\n"
"\n"
"}")
        self.settings_layout.setObjectName("settings_layout")
        self.import_button = QtWidgets.QPushButton(self.settings_layout)
        self.import_button.setGeometry(QtCore.QRect(90, 40, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.discre_label = QtWidgets.QLabel(self.settings_layout)
        self.discre_label.setGeometry(QtCore.QRect(10, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.discre_label.setFont(font)
        self.discre_label.setObjectName("discre_label")
        self.discre_choice = QtWidgets.QComboBox(self.settings_layout)
        self.discre_choice.setGeometry(QtCore.QRect(90, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.discre_choice.setFont(font)
        self.discre_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.discre_choice.setMinimumContentsLength(1)
        self.discre_choice.setObjectName("discre_choice")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.discre_choice.addItem("")
        self.data_used_label = QtWidgets.QLabel(self.settings_layout)
        self.data_used_label.setGeometry(QtCore.QRect(10, 120, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.data_used_label.setFont(font)
        self.data_used_label.setObjectName("data_used_label")
        self.induct_label = QtWidgets.QLabel(self.settings_layout)
        self.induct_label.setGeometry(QtCore.QRect(10, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.induct_label.setFont(font)
        self.induct_label.setObjectName("induct_label")
        self.der_label = QtWidgets.QLabel(self.settings_layout)
        self.der_label.setGeometry(QtCore.QRect(10, 210, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.der_label.setFont(font)
        self.der_label.setObjectName("der_label")
        self.induct_choice = QtWidgets.QComboBox(self.settings_layout)
        self.induct_choice.setGeometry(QtCore.QRect(90, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.induct_choice.setFont(font)
        self.induct_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.induct_choice.setMinimumContentsLength(1)
        self.induct_choice.setObjectName("induct_choice")
        self.induct_choice.addItem("")
        self.induct_choice.addItem("")
        self.induct_choice.addItem("")
        self.der_choice = QtWidgets.QComboBox(self.settings_layout)
        self.der_choice.setGeometry(QtCore.QRect(90, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.der_choice.setFont(font)
        self.der_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.der_choice.setMinimumContentsLength(1)
        self.der_choice.setObjectName("der_choice")
        self.der_choice.addItem("")
        self.der_choice.addItem("")
        self.data_used_choice = QtWidgets.QComboBox(self.settings_layout)
        self.data_used_choice.setGeometry(QtCore.QRect(90, 140, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.data_used_choice.setFont(font)
        self.data_used_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.data_used_choice.setMinimumContentsLength(1)
        self.data_used_choice.setObjectName("data_used_choice")
        self.data_used_choice.addItem("")
        self.data_used_choice.addItem("")
        self.data_used_choice.addItem("")
        self.lambda_choice_label = QtWidgets.QLabel(self.settings_layout)
        self.lambda_choice_label.setGeometry(QtCore.QRect(10, 270, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lambda_choice_label.setFont(font)
        self.lambda_choice_label.setObjectName("lambda_choice_label")
        self.lambda_choice = QtWidgets.QComboBox(self.settings_layout)
        self.lambda_choice.setGeometry(QtCore.QRect(90, 290, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lambda_choice.setFont(font)
        self.lambda_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.lambda_choice.setMinimumContentsLength(1)
        self.lambda_choice.setObjectName("lambda_choice")
        self.lambda_choice.addItem("")
        self.lambda_choice.addItem("")
        self.lambda_choice.addItem("")
        self.lambda_choice.addItem("")
        self.lambda_choice.addItem("")
        self.lambda_choice.addItem("")
        self.lambda_choice.addItem("")
        self.sample_no = QtWidgets.QLabel(self.settings_layout)
        self.sample_no.setGeometry(QtCore.QRect(10, 420, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.sample_no.setFont(font)
        self.sample_no.setObjectName("sample_no")
        self.sample_no_entry = QtWidgets.QLineEdit(self.settings_layout)
        self.sample_no_entry.setGeometry(QtCore.QRect(90, 440, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sample_no_entry.setFont(font)
        self.sample_no_entry.setObjectName("sample_no_entry")
        self.import_label = QtWidgets.QLabel(self.settings_layout)
        self.import_label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.import_label.setFont(font)
        self.import_label.setObjectName("import_label")
        self.reg_param_label = QtWidgets.QLabel(self.settings_layout)
        self.reg_param_label.setGeometry(QtCore.QRect(10, 320, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.reg_param_label.setFont(font)
        self.reg_param_label.setObjectName("reg_param_label")
        self.reg_param_entry = QtWidgets.QLineEdit(self.settings_layout)
        self.reg_param_entry.setGeometry(QtCore.QRect(90, 340, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.reg_param_entry.setFont(font)
        self.reg_param_entry.setObjectName("reg_param_entry")
        self.reg_param_label_2 = QtWidgets.QLabel(self.settings_layout)
        self.reg_param_label_2.setGeometry(QtCore.QRect(10, 370, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.reg_param_label_2.setFont(font)
        self.reg_param_label_2.setObjectName("reg_param_label_2")
        self.reg_param_entry_2 = QtWidgets.QLineEdit(self.settings_layout)
        self.reg_param_entry_2.setGeometry(QtCore.QRect(90, 390, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.reg_param_entry_2.setFont(font)
        self.reg_param_entry_2.setObjectName("reg_param_entry_2")
        self.RBF_frame = QtWidgets.QGroupBox(self.General_frame)
        self.RBF_frame.setGeometry(QtCore.QRect(10, 490, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.RBF_frame.setFont(font)
        self.RBF_frame.setStyleSheet("QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color: black;\n"
"\n"
"}")
        self.RBF_frame.setObjectName("RBF_frame")
        self.run_frame = QtWidgets.QGroupBox(self.RBF_frame)
        self.run_frame.setGeometry(QtCore.QRect(-10, 120, 271, 271))
        self.run_frame.setObjectName("run_frame")
        self.shape_control_label = QtWidgets.QLabel(self.RBF_frame)
        self.shape_control_label.setGeometry(QtCore.QRect(10, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.shape_control_label.setFont(font)
        self.shape_control_label.setObjectName("shape_control_label")
        self.FWHM_control_label = QtWidgets.QLabel(self.RBF_frame)
        self.FWHM_control_label.setGeometry(QtCore.QRect(10, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.FWHM_control_label.setFont(font)
        self.FWHM_control_label.setObjectName("FWHM_control_label")
        self.FWHM_entry = QtWidgets.QLineEdit(self.RBF_frame)
        self.FWHM_entry.setGeometry(QtCore.QRect(140, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.FWHM_entry.setFont(font)
        self.FWHM_entry.setObjectName("FWHM_entry")
        self.shape_control_choice = QtWidgets.QComboBox(self.RBF_frame)
        self.shape_control_choice.setGeometry(QtCore.QRect(140, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.shape_control_choice.setFont(font)
        self.shape_control_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.shape_control_choice.setMinimumContentsLength(1)
        self.shape_control_choice.setObjectName("shape_control_choice")
        self.shape_control_choice.addItem("")
        self.shape_control_choice.addItem("")
        self.run_layout = QtWidgets.QGroupBox(self.General_frame)
        self.run_layout.setGeometry(QtCore.QRect(10, 590, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.run_layout.setFont(font)
        self.run_layout.setTabletTracking(True)
        self.run_layout.setStyleSheet("QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color: black;\n"
"\n"
"}")
        self.run_layout.setObjectName("run_layout")
        self.simple_run_button = QtWidgets.QPushButton(self.run_layout)
        self.simple_run_button.setGeometry(QtCore.QRect(170, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.simple_run_button.setFont(font)
        self.simple_run_button.setObjectName("simple_run_button")
        self.simple_run_label = QtWidgets.QLabel(self.run_layout)
        self.simple_run_label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.simple_run_label.setFont(font)
        self.simple_run_label.setObjectName("simple_run_label")
        self.bayes_label = QtWidgets.QLabel(self.run_layout)
        self.bayes_label.setGeometry(QtCore.QRect(10, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bayes_label.setFont(font)
        self.bayes_label.setObjectName("bayes_label")
        self.HT_label = QtWidgets.QLabel(self.run_layout)
        self.HT_label.setGeometry(QtCore.QRect(10, 70, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.HT_label.setFont(font)
        self.HT_label.setObjectName("HT_label")
        self.bayesian_button = QtWidgets.QPushButton(self.run_layout)
        self.bayesian_button.setGeometry(QtCore.QRect(170, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bayesian_button.setFont(font)
        self.bayesian_button.setObjectName("bayesian_button")
        self.HT_button = QtWidgets.QPushButton(self.run_layout)
        self.HT_button.setGeometry(QtCore.QRect(170, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.HT_button.setFont(font)
        self.HT_button.setObjectName("HT_button")
        self.Peak_analysis_frame = QtWidgets.QGroupBox(self.General_frame)
        self.Peak_analysis_frame.setGeometry(QtCore.QRect(10, 700, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Peak_analysis_frame.setFont(font)
        self.Peak_analysis_frame.setStyleSheet("QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color: black;\n"
"\n"
"}")
        self.Peak_analysis_frame.setObjectName("Peak_analysis_frame")
        self.run_frame_2 = QtWidgets.QGroupBox(self.Peak_analysis_frame)
        self.run_frame_2.setGeometry(QtCore.QRect(-10, 120, 271, 271))
        self.run_frame_2.setObjectName("run_frame_2")
        self.Peak_decon_run = QtWidgets.QLabel(self.Peak_analysis_frame)
        self.Peak_decon_run.setGeometry(QtCore.QRect(10, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Peak_decon_run.setFont(font)
        self.Peak_decon_run.setObjectName("Peak_decon_run")
        self.peak_decon_button = QtWidgets.QPushButton(self.Peak_analysis_frame)
        self.peak_decon_button.setGeometry(QtCore.QRect(170, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.peak_decon_button.setFont(font)
        self.peak_decon_button.setObjectName("peak_decon_button")
        self.reg_param_2 = QtWidgets.QLabel(self.Peak_analysis_frame)
        self.reg_param_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.reg_param_2.setFont(font)
        self.reg_param_2.setObjectName("reg_param_2")
        self.peak_num_entry = QtWidgets.QLineEdit(self.Peak_analysis_frame)
        self.peak_num_entry.setGeometry(QtCore.QRect(170, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.peak_num_entry.setFont(font)
        self.peak_num_entry.setObjectName("peak_num_entry")
        self.peak_method_label = QtWidgets.QLabel(self.Peak_analysis_frame)
        self.peak_method_label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.peak_method_label.setFont(font)
        self.peak_method_label.setObjectName("peak_method_label")
        self.peak_method_choice = QtWidgets.QComboBox(self.Peak_analysis_frame)
        self.peak_method_choice.setGeometry(QtCore.QRect(170, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.peak_method_choice.setFont(font)
        self.peak_method_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.peak_method_choice.setMinimumContentsLength(1)
        self.peak_method_choice.setObjectName("peak_method_choice")
        self.peak_method_choice.addItem("")
        self.peak_method_choice.addItem("")
        self.export_frame = QtWidgets.QGroupBox(self.General_frame)
        self.export_frame.setGeometry(QtCore.QRect(10, 820, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.export_frame.setFont(font)
        self.export_frame.setStyleSheet("QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color: black;\n"
"\n"
"}")
        self.export_frame.setObjectName("export_frame")
        self.export_DRT_label = QtWidgets.QLabel(self.export_frame)
        self.export_DRT_label.setGeometry(QtCore.QRect(10, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.export_DRT_label.setFont(font)
        self.export_DRT_label.setObjectName("export_DRT_label")
        self.export_EIS_label = QtWidgets.QLabel(self.export_frame)
        self.export_EIS_label.setGeometry(QtCore.QRect(10, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.export_EIS_label.setFont(font)
        self.export_EIS_label.setObjectName("export_EIS_label")
        self.export_fig_label = QtWidgets.QLabel(self.export_frame)
        self.export_fig_label.setGeometry(QtCore.QRect(10, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.export_fig_label.setFont(font)
        self.export_fig_label.setObjectName("export_fig_label")
        self.export_DRT_button = QtWidgets.QPushButton(self.export_frame)
        self.export_DRT_button.setGeometry(QtCore.QRect(170, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.export_DRT_button.setFont(font)
        self.export_DRT_button.setObjectName("export_DRT_button")
        self.export_EIS_button = QtWidgets.QPushButton(self.export_frame)
        self.export_EIS_button.setGeometry(QtCore.QRect(170, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.export_EIS_button.setFont(font)
        self.export_EIS_button.setObjectName("export_EIS_button")
        self.export_fig_button = QtWidgets.QPushButton(self.export_frame)
        self.export_fig_button.setGeometry(QtCore.QRect(170, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.export_fig_button.setFont(font)
        self.export_fig_button.setObjectName("export_fig_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1625, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        from ezDRTtools import sMods
        sMods.addAboutMenu(self, MainWindow)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.discre_choice.setCurrentIndex(0)
        self.induct_choice.setCurrentIndex(0)
        self.der_choice.setCurrentIndex(0)
        self.data_used_choice.setCurrentIndex(0)
        self.lambda_choice.setCurrentIndex(0)
        self.shape_control_choice.setCurrentIndex(0)
        self.peak_method_choice.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyDRTtools"))
        self.show_EIS.setText(_translate("MainWindow", "EIS Data"))
        self.show_mag.setText(_translate("MainWindow", "Magnitude"))
        self.show_phase.setText(_translate("MainWindow", "Phase"))
        self.show_re.setText(_translate("MainWindow", "Re Part"))
        self.show_im.setText(_translate("MainWindow", "Im Part"))
        self.show_re_res.setText(_translate("MainWindow", "Re Residual"))
        self.show_im_res.setText(_translate("MainWindow", "Im Residual"))
        self.show_DRT.setText(_translate("MainWindow", "DRT"))
        self.show_score.setText(_translate("MainWindow", "EIS Score"))
        self.settings_layout.setTitle(_translate("MainWindow", "Settings"))
        self.import_button.setText(_translate("MainWindow", "Import "))
        self.discre_label.setText(_translate("MainWindow", "Method of Discretization"))
        self.discre_choice.setCurrentText(_translate("MainWindow", "Gaussian"))
        self.discre_choice.setItemText(0, _translate("MainWindow", "Gaussian"))
        self.discre_choice.setItemText(1, _translate("MainWindow", "C2 Matern"))
        self.discre_choice.setItemText(2, _translate("MainWindow", "C4 Matern"))
        self.discre_choice.setItemText(3, _translate("MainWindow", "C6 Matern"))
        self.discre_choice.setItemText(4, _translate("MainWindow", "Inverse Quadratic"))
        self.discre_choice.setItemText(5, _translate("MainWindow", "Inverse Quadric"))
        self.discre_choice.setItemText(6, _translate("MainWindow", "Cauchy"))
        self.discre_choice.setItemText(7, _translate("MainWindow", "PWL"))
        self.data_used_label.setText(_translate("MainWindow", "Data Used"))
        self.induct_label.setText(_translate("MainWindow", "Inductance"))
        self.der_label.setText(_translate("MainWindow", "Regularization Derivative"))
        self.induct_choice.setCurrentText(_translate("MainWindow", "Fitting w/o Inductance"))
        self.induct_choice.setItemText(0, _translate("MainWindow", "Fitting w/o Inductance"))
        self.induct_choice.setItemText(1, _translate("MainWindow", "Fitting with Inductance"))
        self.induct_choice.setItemText(2, _translate("MainWindow", "Discard Inductive Data"))
        self.der_choice.setCurrentText(_translate("MainWindow", "1st order"))
        self.der_choice.setItemText(0, _translate("MainWindow", "1st order"))
        self.der_choice.setItemText(1, _translate("MainWindow", "2nd order"))
        self.data_used_choice.setCurrentText(_translate("MainWindow", "Combined Re-Im Data"))
        self.data_used_choice.setItemText(0, _translate("MainWindow", "Combined Re-Im Data"))
        self.data_used_choice.setItemText(1, _translate("MainWindow", "Re Data"))
        self.data_used_choice.setItemText(2, _translate("MainWindow", "Im Data"))
        self.lambda_choice_label.setText(_translate("MainWindow", "Parameter Selection Method"))
        self.lambda_choice.setCurrentText(_translate("MainWindow", "custom"))
        self.lambda_choice.setItemText(0, _translate("MainWindow", "custom"))
        self.lambda_choice.setItemText(1, _translate("MainWindow", "GCV"))
        self.lambda_choice.setItemText(2, _translate("MainWindow", "mGCV"))
        self.lambda_choice.setItemText(3, _translate("MainWindow", "rGCV"))
        self.lambda_choice.setItemText(4, _translate("MainWindow", "LC"))
        self.lambda_choice.setItemText(5, _translate("MainWindow", "kf"))
        self.lambda_choice.setItemText(6, _translate("MainWindow", "re-im"))
        self.sample_no.setText(_translate("MainWindow", "Number of Samples"))
        self.sample_no_entry.setText(_translate("MainWindow", "1000"))
        self.import_label.setText(_translate("MainWindow", "Import Data"))
        self.reg_param_label.setText(_translate("MainWindow", "Regularization parameter"))
        self.reg_param_entry.setText(_translate("MainWindow", "0.001"))

        self.reg_param_label_2.setText(_translate("MainWindow", "Optimal Regularization parameter"))
        self.reg_param_entry_2.setObjectName("optima_reg_param")
        ##
        self.RBF_frame.setTitle(_translate("MainWindow", "Options for RBF"))
        self.run_frame.setTitle(_translate("MainWindow", "Options for RBF"))
        self.shape_control_label.setText(_translate("MainWindow", "RBF Shape Control"))
        self.FWHM_control_label.setText(_translate("MainWindow", "FWHM Control"))
        self.FWHM_entry.setText(_translate("MainWindow", "0.5"))
        self.shape_control_choice.setCurrentText(_translate("MainWindow", "FWHM Coefficient"))
        self.shape_control_choice.setItemText(0, _translate("MainWindow", "FWHM Coefficient"))
        self.shape_control_choice.setItemText(1, _translate("MainWindow", "Shape Factor"))
        self.run_layout.setTitle(_translate("MainWindow", "Run"))
        self.simple_run_button.setText(_translate("MainWindow", "Run"))
        self.simple_run_label.setText(_translate("MainWindow", "Simple Run"))
        self.bayes_label.setText(_translate("MainWindow", "Bayesian Run"))
        self.HT_label.setText(_translate("MainWindow", "Hilbert Transform"))
        self.bayesian_button.setText(_translate("MainWindow", "Run"))
        self.HT_button.setText(_translate("MainWindow", "Run"))
        self.Peak_analysis_frame.setTitle(_translate("MainWindow", "Peak Analysis "))
        self.run_frame_2.setTitle(_translate("MainWindow", "Options for RBF"))
        self.Peak_decon_run.setText(_translate("MainWindow", "Peak deconvolution"))
        self.peak_decon_button.setText(_translate("MainWindow", "Run"))
        self.reg_param_2.setText(_translate("MainWindow", "Number of peaks"))
        self.peak_num_entry.setText(_translate("MainWindow", "1"))
        self.peak_method_label.setText(_translate("MainWindow", "Peak method"))
        self.peak_method_choice.setCurrentText(_translate("MainWindow", "separate"))
        self.peak_method_choice.setItemText(0, _translate("MainWindow", "separate"))
        self.peak_method_choice.setItemText(1, _translate("MainWindow", "combine"))
        self.export_frame.setTitle(_translate("MainWindow", "Export Result"))
        self.export_DRT_label.setText(_translate("MainWindow", "DRT"))
        self.export_EIS_label.setText(_translate("MainWindow", "EIS Regression"))
        self.export_fig_label.setText(_translate("MainWindow", "Figure"))
        self.export_DRT_button.setText(_translate("MainWindow", "Export"))
        self.export_EIS_button.setText(_translate("MainWindow", "Export"))
        self.export_fig_button.setText(_translate("MainWindow", "Save"))
        


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    # Enable high DPI scaling (already done)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # Use high DPI icons (already done)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    # Set application scaling to be adaptive
    app = QtWidgets.QApplication(sys.argv)

    # Detect the current screen's DPI scaling
    screen = app.primaryScreen()
    logical_dpi = screen.logicalDotsPerInch()  # Fetch DPI for scaling
    scaling_factor = logical_dpi / 96.0  # Assuming 96 DPI is normal

    # Apply a custom scaling factor based on detected DPI
    if scaling_factor > 1:
        app.setStyleSheet(f"font-size: {12 * scaling_factor}px;")
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Adjust scaling for different screen resolutions
    if scaling_factor > 1.5:  # 4K scaling factor
        MainWindow.resize(int(1600 * scaling_factor), int(900 * scaling_factor))
    else:  # 2.5K or standard screens
        MainWindow.resize(int(1200 * scaling_factor), int(800 * scaling_factor))

    MainWindow.show()
    sys.exit(app.exec_())


