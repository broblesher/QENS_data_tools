# -*- coding: utf-8 -*-

"""
Filename: QENStoCSV_Dlg.py
Author: Beatriz Robles Hernández
Date: 2025-03-10
Version: 1.0
Description:
    This script creates the class of the GUI that uses
    the app_QENStoCSV_Dlg application.

License: GLP
Contact: broblesher@gmail.com
Dependencies: os, PyQt5
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
# from PyQt5.QtGui import QIcon

import pyqtgraph as pg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 777)
        self.actionFrom_source = QAction(MainWindow)
        self.actionFrom_source.setObjectName(u"actionFrom_source")
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentNew")
        self.actionFrom_source.setIcon(icon)
        self.actionFrom_csv = QAction(MainWindow)
        self.actionFrom_csv.setObjectName(u"actionFrom_csv")
        icon1 = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentOpen")
        self.actionFrom_csv.setIcon(icon1)
        self.actionExport_data_as_csv = QAction(MainWindow)
        self.actionExport_data_as_csv.setObjectName(
            u"actionExport_data_as_csv")
        icon2 = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSaveAs")
        self.actionExport_data_as_csv.setIcon(icon2)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::ApplicationExit")
        self.actionExit.setIcon(icon3)
        self.actionIntegrate = QAction(MainWindow)
        self.actionIntegrate.setObjectName(u"actionIntegrate")
        self.actionFourier_transform = QAction(MainWindow)
        self.actionFourier_transform.setObjectName(u"actionFourier_transform")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_area = QtWidgets.QGroupBox(self.widget)
        self.groupBox_area.setObjectName(u"groupBox_area")
        self.groupBox_area.setEnabled(True)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_area)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_ROI5 = QtWidgets.QGroupBox(self.groupBox_area)
        self.groupBox_ROI5.setObjectName(u"groupBox_ROI5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_ROI5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_xmin_ROI5 = QtWidgets.QLineEdit(self.groupBox_ROI5)
        self.lineEdit_xmin_ROI5.setObjectName(u"lineEdit_xmin_ROI5")
        self.gridLayout_8.addWidget(self.lineEdit_xmin_ROI5, 2, 0, 1, 1)
        self.label_xmax_ROI5 = QtWidgets.QLabel(self.groupBox_ROI5)
        self.label_xmax_ROI5.setObjectName(u"label_xmax_ROI5")
        self.gridLayout_8.addWidget(self.label_xmax_ROI5, 0, 1, 1, 1)
        self.label_xmin_ROI5 = QtWidgets.QLabel(self.groupBox_ROI5)
        self.label_xmin_ROI5.setObjectName(u"label_xmin_ROI5")
        self.gridLayout_8.addWidget(self.label_xmin_ROI5, 0, 0, 1, 1)
        self.lineEdit_area_ROI5 = QtWidgets.QLineEdit(self.groupBox_ROI5)
        self.lineEdit_area_ROI5.setObjectName(u"lineEdit_area_ROI5")
        self.lineEdit_area_ROI5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_area_ROI5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.lineEdit_area_ROI5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_area_ROI5.setEnabled(False)
        self.gridLayout_8.addWidget(self.lineEdit_area_ROI5, 2, 3, 1, 1)
        self.label_area_ROI5 = QtWidgets.QLabel(self.groupBox_ROI5)
        self.label_area_ROI5.setObjectName(u"label_area_ROI5")
        self.gridLayout_8.addWidget(self.label_area_ROI5, 0, 3, 1, 1)
        self.lineEdit_xmax_ROI5 = QtWidgets.QLineEdit(self.groupBox_ROI5)
        self.lineEdit_xmax_ROI5.setObjectName(u"lineEdit_xmax_ROI5")
        self.gridLayout_8.addWidget(self.lineEdit_xmax_ROI5, 2, 1, 1, 1)
        self.horizontalSpacer_8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_ROI5, 5, 0, 1, 1)
        self.groupBox_ROI1 = QtWidgets.QGroupBox(self.groupBox_area)
        self.groupBox_ROI1.setObjectName(u"groupBox_ROI1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_ROI1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_xmin_ROI1 = QtWidgets.QLabel(self.groupBox_ROI1)
        self.label_xmin_ROI1.setObjectName(u"label_xmin_ROI1")
        self.gridLayout_3.addWidget(self.label_xmin_ROI1, 0, 0, 1, 1)
        self.label_xmax_ROI1 = QtWidgets.QLabel(self.groupBox_ROI1)
        self.label_xmax_ROI1.setObjectName(u"label_xmax_ROI1")
        self.gridLayout_3.addWidget(self.label_xmax_ROI1, 0, 1, 1, 1)
        self.horizontalSpacer_4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)
        self.lineEdit_xmax_ROI1 = QtWidgets.QLineEdit(self.groupBox_ROI1)
        self.lineEdit_xmax_ROI1.setObjectName(u"lineEdit_xmax_ROI1")
        self.gridLayout_3.addWidget(self.lineEdit_xmax_ROI1, 1, 1, 1, 1)
        self.lineEdit_area_ROI1 = QtWidgets.QLineEdit(self.groupBox_ROI1)
        self.lineEdit_area_ROI1.setObjectName(u"lineEdit_area_ROI1")
        self.lineEdit_area_ROI1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_area_ROI1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.lineEdit_area_ROI1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_area_ROI1.setEnabled(False)
        self.gridLayout_3.addWidget(self.lineEdit_area_ROI1, 1, 3, 1, 1)
        self.lineEdit_xmin_ROI1 = QtWidgets.QLineEdit(self.groupBox_ROI1)
        self.lineEdit_xmin_ROI1.setObjectName(u"lineEdit_xmin_ROI1")
        self.gridLayout_3.addWidget(self.lineEdit_xmin_ROI1, 1, 0, 1, 1)
        self.label_area_ROI1 = QtWidgets.QLabel(self.groupBox_ROI1)
        self.label_area_ROI1.setObjectName(u"label_area_ROI1")
        self.gridLayout_3.addWidget(self.label_area_ROI1, 0, 3, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_ROI1, 1, 0, 1, 1)
        self.groupBox_ROI2 = QtWidgets.QGroupBox(self.groupBox_area)
        self.groupBox_ROI2.setObjectName(u"groupBox_ROI2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_ROI2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_area_ROI2 = QtWidgets.QLabel(self.groupBox_ROI2)
        self.label_area_ROI2.setObjectName(u"label_area_ROI2")
        self.gridLayout_5.addWidget(self.label_area_ROI2, 0, 3, 1, 1)
        self.label_xmin_ROI2 = QtWidgets.QLabel(self.groupBox_ROI2)
        self.label_xmin_ROI2.setObjectName(u"label_xmin_ROI2")
        self.gridLayout_5.addWidget(self.label_xmin_ROI2, 0, 0, 1, 1)
        self.lineEdit_area_ROI2 = QtWidgets.QLineEdit(self.groupBox_ROI2)
        self.lineEdit_area_ROI2.setObjectName(u"lineEdit_area_ROI2")
        self.lineEdit_area_ROI2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_area_ROI2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.lineEdit_area_ROI2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_area_ROI2.setEnabled(False)
        self.gridLayout_5.addWidget(self.lineEdit_area_ROI2, 1, 3, 1, 1)
        self.lineEdit_xmin_ROI2 = QtWidgets.QLineEdit(self.groupBox_ROI2)
        self.lineEdit_xmin_ROI2.setObjectName(u"lineEdit_xmin_ROI2")
        self.gridLayout_5.addWidget(self.lineEdit_xmin_ROI2, 1, 0, 1, 1)
        self.lineEdit_xmax_ROI2 = QtWidgets.QLineEdit(self.groupBox_ROI2)
        self.lineEdit_xmax_ROI2.setObjectName(u"lineEdit_xmax_ROI2")
        self.gridLayout_5.addWidget(self.lineEdit_xmax_ROI2, 1, 1, 1, 1)
        self.label_xmax_ROI2 = QtWidgets.QLabel(self.groupBox_ROI2)
        self.label_xmax_ROI2.setObjectName(u"label_xmax_ROI2")
        self.gridLayout_5.addWidget(self.label_xmax_ROI2, 0, 1, 1, 1)
        self.horizontalSpacer_5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_ROI2, 2, 0, 1, 1)
        self.groupBox_ROI4 = QtWidgets.QGroupBox(self.groupBox_area)
        self.groupBox_ROI4.setObjectName(u"groupBox_ROI4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_ROI4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_area_ROI4 = QtWidgets.QLineEdit(self.groupBox_ROI4)
        self.lineEdit_area_ROI4.setObjectName(u"lineEdit_area_ROI4")
        self.lineEdit_area_ROI4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_area_ROI4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.lineEdit_area_ROI4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_area_ROI4.setEnabled(False)
        self.gridLayout_7.addWidget(self.lineEdit_area_ROI4, 1, 3, 1, 1)
        self.label_xmin_ROI4 = QtWidgets.QLabel(self.groupBox_ROI4)
        self.label_xmin_ROI4.setObjectName(u"label_xmin_ROI4")
        self.gridLayout_7.addWidget(self.label_xmin_ROI4, 0, 0, 1, 1)
        self.lineEdit_xmax_ROI4 = QtWidgets.QLineEdit(self.groupBox_ROI4)
        self.lineEdit_xmax_ROI4.setObjectName(u"lineEdit_xmax_ROI4")
        self.gridLayout_7.addWidget(self.lineEdit_xmax_ROI4, 1, 1, 1, 1)
        self.label_area_ROI4 = QtWidgets.QLabel(self.groupBox_ROI4)
        self.label_area_ROI4.setObjectName(u"label_area_ROI4")
        self.gridLayout_7.addWidget(self.label_area_ROI4, 0, 3, 1, 1)
        self.label_xmax_ROI4 = QtWidgets.QLabel(self.groupBox_ROI4)
        self.label_xmax_ROI4.setObjectName(u"label_xmax_ROI4")
        self.gridLayout_7.addWidget(self.label_xmax_ROI4, 0, 1, 1, 1)
        self.lineEdit_xmin_ROI4 = QtWidgets.QLineEdit(self.groupBox_ROI4)
        self.lineEdit_xmin_ROI4.setObjectName(u"lineEdit_xmin_ROI4")
        self.gridLayout_7.addWidget(self.lineEdit_xmin_ROI4, 1, 0, 1, 1)
        self.horizontalSpacer_7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_ROI4, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_nROIs = QtWidgets.QLabel(self.groupBox_area)
        self.label_nROIs.setObjectName(u"label_nROIs")
        self.horizontalLayout_4.addWidget(self.label_nROIs)
        self.spinBox_nROIs = QtWidgets.QSpinBox(self.groupBox_area)
        self.spinBox_nROIs.setObjectName(u"spinBox_nROIs")
        self.spinBox_nROIs.setMinimum(1)
        self.spinBox_nROIs.setMaximum(5)
        self.horizontalLayout_4.addWidget(self.spinBox_nROIs)
        self.horizontalSpacer_3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)
        self.gridLayout_9.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.groupBox_ROI3 = QtWidgets.QGroupBox(self.groupBox_area)
        self.groupBox_ROI3.setObjectName(u"groupBox_ROI3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_ROI3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_area_ROI3 = QtWidgets.QLineEdit(self.groupBox_ROI3)
        self.lineEdit_area_ROI3.setObjectName(u"lineEdit_area_ROI3")
        self.lineEdit_area_ROI3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_area_ROI3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.lineEdit_area_ROI3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_area_ROI3.setEnabled(False)
        self.gridLayout_6.addWidget(self.lineEdit_area_ROI3, 1, 3, 1, 1)
        self.lineEdit_xmin_ROI3 = QtWidgets.QLineEdit(self.groupBox_ROI3)
        self.lineEdit_xmin_ROI3.setObjectName(u"lineEdit_xmin_ROI3")
        self.gridLayout_6.addWidget(self.lineEdit_xmin_ROI3, 1, 0, 1, 1)
        self.lineEdit_xmax_ROI3 = QtWidgets.QLineEdit(self.groupBox_ROI3)
        self.lineEdit_xmax_ROI3.setObjectName(u"lineEdit_xmax_ROI3")
        self.gridLayout_6.addWidget(self.lineEdit_xmax_ROI3, 1, 1, 1, 1)
        self.label_xmax_ROI3 = QtWidgets.QLabel(self.groupBox_ROI3)
        self.label_xmax_ROI3.setObjectName(u"label_xmax_ROI3")
        self.gridLayout_6.addWidget(self.label_xmax_ROI3, 0, 1, 1, 1)
        self.label_xmin_ROI3 = QtWidgets.QLabel(self.groupBox_ROI3)
        self.label_xmin_ROI3.setObjectName(u"label_xmin_ROI3")
        self.gridLayout_6.addWidget(self.label_xmin_ROI3, 0, 0, 1, 1)
        self.label_area_ROI3 = QtWidgets.QLabel(self.groupBox_ROI3)
        self.label_area_ROI3.setObjectName(u"label_area_ROI3")
        self.gridLayout_6.addWidget(self.label_area_ROI3, 0, 3, 1, 1)
        self.horizontalSpacer_6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_ROI3, 3, 0, 1, 1)
        self.pushButton_CalcAreas = QtWidgets.QPushButton(self.groupBox_area)
        self.pushButton_CalcAreas.setObjectName(u"pushButton_CalcAreas")
        self.gridLayout_9.addWidget(self.pushButton_CalcAreas, 7, 0, 1, 1)
        self.verticalSpacer_5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_9.addItem(self.verticalSpacer_5, 8, 0, 1, 1)
        self.pushButton_ExportRes = QtWidgets.QPushButton(self.groupBox_area)
        self.pushButton_ExportRes.setObjectName(u"pushButton_ExportRes")
        self.gridLayout_9.addWidget(self.pushButton_ExportRes, 9, 0, 1, 1)
        self.groupBox_ROI1.raise_()
        self.groupBox_ROI2.raise_()
        self.groupBox_ROI3.raise_()
        self.groupBox_ROI4.raise_()
        self.groupBox_ROI5.raise_()
        self.pushButton_CalcAreas.raise_()
        self.pushButton_ExportRes.raise_()
        self.horizontalLayout_3.addWidget(self.groupBox_area)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        self.label_Q = QtWidgets.QLabel(self.widget)
        self.label_Q.setObjectName(u"label")
        self.horizontalLayout.addWidget(self.label_Q)
        self.comboBox_Q = QtWidgets.QComboBox(self.widget)
        self.comboBox_Q.setObjectName(u"comboBox_Q")
        self.horizontalLayout.addWidget(self.comboBox_Q)
        self.pushButton_Q_p = QtWidgets.QPushButton(self.widget)
        self.pushButton_Q_p.setObjectName(u"pushButton_Q_p")
        self.horizontalLayout.addWidget(self.pushButton_Q_p)
        self.pushButton_Q_m = QtWidgets.QPushButton(self.widget)
        self.pushButton_Q_m.setObjectName(u"pushButton_Q_m")
        self.horizontalLayout.addWidget(self.pushButton_Q_m)
        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        pg.setConfigOptions(antialias=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOption('leftButtonPan', False)
        self.graphicsView = pg.GraphicsLayoutWidget(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 22))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLoad_data = QtWidgets.QMenu(self.menuFile)
        self.menuLoad_data.setObjectName(u"menuLoad_data")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(
            QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuLoad_data.menuAction())
        self.menuFile.addAction(self.actionExport_data_as_csv)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuLoad_data.addAction(self.actionFrom_source)
        self.menuLoad_data.addAction(self.actionFrom_csv)
        self.menuAnalysis.addAction(self.actionIntegrate)
        self.menuAnalysis.addAction(self.actionFourier_transform)
        self.toolBar.addAction(self.actionFrom_source)
        self.toolBar.addAction(self.actionFrom_csv)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport_data_as_csv)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.actionFrom_source.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"From source...", None))
        self.actionFrom_csv.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"From csv...", None))
        self.actionExport_data_as_csv.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow", u"Export data as csv...", None))
        self.actionExit.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Exit", None))
        self.actionIntegrate.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Integrate", None))
        self.actionFourier_transform.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow", u"Fourier transform", None))
        self.groupBox_area.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"Area under curve", None))
        self.groupBox_ROI5.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"ROI 5", None))
        self.label_xmax_ROI5.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmax:", None))
        self.label_xmin_ROI5.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmin:", None))
        self.label_area_ROI5.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Area:", None))
        self.groupBox_ROI1.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"ROI 1", None))
        self.label_xmin_ROI1.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmin:", None))
        self.label_xmax_ROI1.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmax:", None))
        self.label_area_ROI1.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Area:", None))
        self.groupBox_ROI2.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"ROI 2", None))
        self.label_area_ROI2.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Area:", None))
        self.label_xmin_ROI2.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmin:", None))
        self.label_xmax_ROI2.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmax:", None))
        self.groupBox_ROI4.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"ROI 4", None))
        self.label_xmin_ROI4.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmin:", None))
        self.label_area_ROI4.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Area:", None))
        self.label_xmax_ROI4.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmax:", None))
        self.label_nROIs.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Number of ROIs", None))
        self.groupBox_ROI3.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"ROI 3", None))
        self.label_xmax_ROI3.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmax:", None))
        self.label_xmin_ROI3.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Xmin:", None))
        self.label_area_ROI3.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Area:", None))
        self.pushButton_CalcAreas.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow", u"Calculate Areas", None))
        self.pushButton_ExportRes.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow", u"Export Results", None))
        self.label_Q.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow", u"Q (\u00c5\u00af\u00b9):", None))
        self.pushButton_Q_p.setText(
            QtCore.QCoreApplication.translate("MainWindow", u"Q +", None))
        self.pushButton_Q_m.setText(QtCore.QCoreApplication.translate(
            "MainWindow", u"Q -", None))
        self.menuFile.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"File", None))
        self.menuLoad_data.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"&Load data", None))
        self.menuAnalysis.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"Analysis", None))
        self.menuHelp.setTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"toolBar", None))
    # retranslateUi
