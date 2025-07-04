#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""App to work with QENS data.

Filename: QENS_MainApp.py  
Author: Beatriz Robles Hernández  
Date: 2025-06-X  
Version: 1.0  
Description:
    This script runs an GUI app to work with QENS data.
    Data can be loaded, exported, viasualized and analysed
    in different ways.

License: GLP  
Contact: broblesher@gmail.com  
Dependencies: sys, FuncionesIntegrar, PyQt5, load_Dlg
"""
# mypy --check-untyped-defs
# Import statements
import sys
from typing_extensions import Self
from loadWindow import load_Dlg
from utilities.FuncionesIntegrar import FuncionesMenuIntegrar as fmi
# import csv
# from copy import deepcopy

from PyQt5.QtWidgets import (
    QApplication, QMainWindow)  # QMessageBox, QDialog, QFileDialog,
# from PyQt5.QtCore import QDateTime  # , Qt
# from PyQt5.QtGui import QColor

# from QENStoCSV_Dlg import Ui_Dialog_QENStoCSV
from ui_QENS_MainWindow import Ui_MainWindow


class MainWin(QMainWindow, Ui_MainWindow):
    """DLG window class.

    A class used to create the dialog window. Contains the methods
    to run the elements of the dlg.

    Attributes
    ----------
    _dataPlot: pg.GraphicsLayoutWidget
        to set the plotItem.
    _cur_plot: pg.plotItem
        to save the current plot item.
    _dataDic: dict
        to save, for each Q-value, the measured data, the calculated
        areas (list), the pg.LinearRegionItems for each plot (list),
        and the linear region limits (list).
    _popup_win_visible: bool
        to know it the pop-up window to browse the data files is
        visible (True) or not (False).
    _qChangeFromButton: bool
        to know if the change in the Q comboBox comes from the Q+ or
        Q- buttons (True), of from the comboBox itself (False).
    _nroiChangeFromCode: bool
        to know if the no. of ROIs in the spinBox in changed from the
        spinBox itself (True) or from code (False).

    Methods
    -------
    connectSignalsSlots()
        Connects signals and slots.
    loadFromSource()
        Loads the data form source files.
    main_win_visibility()
        Sets the main window visibility.
    changeQ_p()
        Changes the Q-value to a higher one when pressing button Q+.
    changeQ_m()
        Changes the Q-value to a lower one when pressing button Q-.
    comboChangePlot()
        Changes the data plot when the Q-value in the comboBox changes.
    nRoi_change()
        Adds or removes Linear ROIs from graph and the coresponding lineEdits.
    show_groupBoxRois(lroi_n)
        Shows the goupBox of the lroi_n.
    hide_groupBoxRois(lroi_n)
        Hides the goupBox of the lroi_n.
    integrate()
        Displays the groupBox_area and plot ROI1 for the given Q.
    update_edit_x_Rois(lroi_n)
        Updates the Xmin and Xmax values in the corresponding lineEdits.
    get_Roi1_xmin()
        Gets the value of the min lineEdit to set the graph linear ROI1.
    get_Roi1_xmax()
        Gets the value of the max lineEdit to set the graph linear ROI1.
    get_Roi2_xmin()
        Gets the value of the min lineEdit to set the graph linear ROI2.
    get_Roi2_xmax()
        Gets the value of the max lineEdit to set the graph linear ROI2.
    get_Roi3_xmin()
        Gets the value of the min lineEdit to set the graph linear ROI3.
    get_Roi3_xmax()
        Gets the value of the max lineEdit to set the graph linear ROI3.
    get_Roi4_xmin()
        Gets the value of the min lineEdit to set the graph linear ROI4.
    get_Roi4_xmax()
        Gets the value of the max lineEdit to set the graph linear ROI4.
    get_Roi5_xmin()
        Gets the value of the min lineEdit to set the graph linear ROI5.
    get_Roi5xmax()
        Gets the value of the max lineEdit to set the graph linear ROI5.
    update_graph_Rois()
        Updates the limits of the graphical linear region items in the plot.
    removeAreas(lroi_n)
        Clears the values in the correspoding lineEdit.
    displayArea(lroi_n)
        Displays de value of the area for the ROI in the lineEdit.
    connect_ROI_callback(lroi_n)
        Connects the linear ROI callback with the update_edit_x_Rois()
        function.
    """

    def __init__(self: Self, parent=None):
        """Class constructor.

        Atributtes
        ----------
            _cur_plot: pg.plotItem
        to save the current plot item.
        _dataDic: dict
            to save, for each Q-value, the measured data, the calculated
            areas (list), the pg.LinearRegionItems for each plot (list),
            and the linear region limits (list).
        _qChangeFromButton: bool
            to know if the change in the Q comboBox comes from the Q+ or
            Q- buttons (True), of from the comboBox itself (False). It is
            set to False by default.
        _nroiChangeFromCode: bool
            to know if the no. of ROIs in the spinBox in changed from the
            spinBox itself (True) or from code (Flase). It is set to False
            by default.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.widget.hide()
        self.loadDLG = load_Dlg.DLG()
        self.fmi = fmi()
        self.connectSignalsSlots()
        # Lo siguiente es para plotear. Defino las características por defecto
        self._dataPlot = self.graphicsView
        self._cur_plot = self.fmi.plot_init(self._dataPlot)
        self._popup_win_visible: bool
        self._popup_win_visible = False
        self._dataDic: dict
        self._saveDic: dict
        self._qChangeFromButton: bool
        self._nroiChangeFromCode: bool
        self._dataDic = dict()
        self._qChangeFromButton = False
        self._nroiChangeFromCode = False
        self._saveDic = dict()

    def connectSignalsSlots(self):
        """Connect signals and slots."""
        self.actionExit.triggered.connect(self.close)
        self.actionFrom_source.triggered.connect(self.loadFromSource)
        self.actionFrom_csv.triggered.connect(self.main_win_visibility)
        self.actionIntegrate.triggered.connect(self.integrate)
        self.pushButton_Q_p.clicked.connect(self.changeQ_p)
        self.pushButton_Q_m.clicked.connect(self.changeQ_m)
        self.comboBox_Q.currentIndexChanged.connect(self.comboChangePlot)
        self.spinBox_nROIs.valueChanged.connect(self.nRoi_change)
        self.pushButton_CalcAreas.clicked.connect(self.getAreas)
        self.lineEdit_xmin_ROI1.textEdited.connect(self.get_Roi1_xmin)
        self.lineEdit_xmax_ROI1.textEdited.connect(self.get_Roi1_xmax)
        self.lineEdit_xmin_ROI2.textEdited.connect(self.get_Roi2_xmin)
        self.lineEdit_xmax_ROI2.textEdited.connect(self.get_Roi2_xmax)
        self.lineEdit_xmin_ROI3.textEdited.connect(self.get_Roi3_xmin)
        self.lineEdit_xmax_ROI3.textEdited.connect(self.get_Roi3_xmax)
        self.lineEdit_xmin_ROI4.textEdited.connect(self.get_Roi4_xmin)
        self.lineEdit_xmax_ROI4.textEdited.connect(self.get_Roi4_xmax)
        self.lineEdit_xmin_ROI5.textEdited.connect(self.get_Roi5_xmin)
        self.lineEdit_xmax_ROI5.textEdited.connect(self.get_Roi5_xmax)
        self.pushButton_ExportRes.clicked.connect(self.exportAreas)
        # self.actionFrom_source.triggered.connect(self.hide)
        # self.action_About.triggered.connect(self.about)

    def loadFromSource(self: Self):
        """Load the data form source files.

        Other Parameters
        ----------------
        _pop_win_visible: bool
            to know it the pop-up window to browse the data files is
            visible (True) or not (False).
        qlist: list
            to save the list of Q-values (str) in the data file.
        """
        self.loadDLG.show()
        load_Dlg.QENS_data_load(view=self.loadDLG)
        if self.loadDLG.isEnabled() is True:
            self.statusbar.showMessage('Loading data')
            self._popup_win_visible = True
            self.main_win_visibility()
        self.loadDLG.exec()
        if self.loadDLG.result() == 1:
            self.statusbar.showMessage(self.loadDLG._last_msg)
            # Hago visible el widget de plotear
            self.widget.show()
            self.groupBox_area.hide()
            # voy a hacer un diccionario para meter los datos
            qlist: list
            qlist = self.fmi.fillqlist(self.loadDLG._dfS)
            i: int
            q: str
            for i, q in enumerate(qlist):
                self._dataDic[q] = {"measData":
                                    self.loadDLG._dfS.iloc[:, 3*i:3*i+3]}
            # Pongo las Qs en el combo box
            self.comboBox_Q.addItems(qlist)
            # Al poner el valor del combo, me crea la gráfica,
            # porque me llama a la función comboChangePlot
            self.comboBox_Q.setCurrentIndex(0)
        else:
            self.statusbar.showMessage('Failed to Load')
        self._popup_win_visible = False
        self.main_win_visibility()

    def main_win_visibility(self):
        """Set the main window visibility."""
        if self._popup_win_visible is True:
            self.setEnabled(False)
        else:
            self.setEnabled(True)

    def changeQ_p(self: Self):
        """Change the Q-value to a higher one when pressing button Q+.

        Other Parameters
        ----------------
        cur_item: int
            to save the index of the current item (Q) in the comboBox.
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        _qChangeFromButton: bool
            to know that the change in the comboBox is comming from
            pressing this button. It is set to True.
        next_qvalue: str
            the next Q-value that is going to appear in the comboBox.
         _nroiChangeFromCode: bool
            as the change in the spinBox is made from here ("code"),
            it is set to True.
        """
        self._qChangeFromButton = True
        cur_item: int
        cur_qvalue: str
        cur_item = self.comboBox_Q.currentIndex()
        cur_qvalue = self.comboBox_Q.currentText()
        # Si no es el último y además el siguiente en la lista es mayor que
        # el actual, pongo el siguiente
        if (
            cur_item != self.comboBox_Q.count()-1 and
            float(self.comboBox_Q.itemText(cur_item+1)) >
            float(self.comboBox_Q.itemText(cur_item))
        ):
            # ojo, que de esta llamada me va a la funcion de cambiar
            # el valor del comboBox
            self.comboBox_Q.setCurrentIndex(cur_item+1)
            next_qvalue = self.comboBox_Q.itemText(cur_item+1)
        # Si no es el primero de la lista y el anterior en la lista es mayor
        # que el actual, pongo el anterior
        elif (
            cur_item != 0 and
            float(self.comboBox_Q.itemText(cur_item-1)) >
            float(self.comboBox_Q.itemText(cur_item))
        ):
            self.comboBox_Q.setCurrentIndex(cur_item-1)
            next_qvalue = self.comboBox_Q.itemText(cur_item-1)
        # Si es o el primero o el último, no hago nada
        else:
            return True
        # Si estoy en la ventana de calcular las áreas
        if self.groupBox_area.isVisible() is True:
            lroi_n: int
            # Si no he pasado por esta Q entonces los items "lrois",
            # "lroisLimits" y "lareas" del dic están vacíos. Copio los
            # ROIs de la Q de la que vengo. Siempre tengo un ROI mínimo.
            # No cambio la visibilidad de los lineEdits porque es la misma
            # que la de la Q de la que vengo.
            if len(self._dataDic[next_qvalue]["lrois"]) == 0:
                self._dataDic[next_qvalue]["lroisLimits"] = \
                    self._dataDic[cur_qvalue]["lroisLimits"].copy()
                for lroi_n in range(
                        len(self._dataDic[next_qvalue]["lroisLimits"])
                ):
                    self.fmi.set_lrois(next_qvalue, self._dataDic, lroi_n)
            else:
                # Si ya he pasado por esa Q, ya tengo rellenos los items
                # "lrois", "lroisLimits" y "lareas" en el diccionario.
                # Puedo tener diferente numero de ROIs, así tengo que
                # cambiar la visibilidad de los lineEdits y del nRois
                # spinBox!
                self.groupBox_ROI2.hide()
                self.groupBox_ROI3.hide()
                self.groupBox_ROI4.hide()
                self.groupBox_ROI5.hide()
                for lroi_n in range(len(self._dataDic[next_qvalue]["lrois"])):
                    self.show_groupBoxRois(lroi_n)
                # También tengo que cambiar el número que aparece en el
                # spinBox
                self._nroiChangeFromCode = True
                self.spinBox_nROIs.setValue(
                    len(self._dataDic[next_qvalue]["lrois"]))
            # En ambos casos, tengo que añadir los ROIs a la gráfica, poner
            # los valores en los lineEdits y recalcular/colocar las áreas
            for lroi_n in range(len(self._dataDic[next_qvalue]["lrois"])):
                self.show_groupBoxRois(lroi_n)
                self._cur_plot.addItem(
                    self._dataDic[next_qvalue]["lrois"][lroi_n],
                    ignoreBounds=True)
                self.update_edit_x_Rois(lroi_n)
                self.connect_ROI_callback(lroi_n)
                # Recalculo las áreas para los datos a esa Q
                self.getAreas()

    def changeQ_m(self: Self):
        """Change the Q-value to a lower one when pressing button Q-.

        Other Parameters
        ----------------
        cur_item: int
            to save the index of the current item (Q) in the comboBox.
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        _qChangeFromButton: bool
            to know that the change in the comboBox is comming from
            pressing this button. It is set to True.
        next_qvalue: str
            the next Q-value that is going to appear in the comboBox.
         _nroiChangeFromCode: bool
            as the change in the spinBox is made from here ("code"),
            it is set to True.
        """
        self._qChangeFromButton = True
        cur_item: int
        cur_qvalue: str
        cur_item = self.comboBox_Q.currentIndex()
        cur_qvalue = self.comboBox_Q.currentText()
        # Si no es el primero y además el anterior en la lista es menor que
        # el actual, pongo el anterior
        if (
            cur_item != 0 and
            float(self.comboBox_Q.itemText(cur_item-1)) <
            float(self.comboBox_Q.itemText(cur_item))
        ):
            self.comboBox_Q.setCurrentIndex(cur_item-1)
            next_qvalue = self.comboBox_Q.itemText(cur_item-1)
        # Si no es el último de la lista y el siguiente en la lista es menor
        # que el actual, pongo el siguiente
        elif (
            cur_item != self.comboBox_Q.count()-1 and
            float(self.comboBox_Q.itemText(cur_item+1)) <
            float(self.comboBox_Q.itemText(cur_item))
        ):
            self.comboBox_Q.setCurrentIndex(cur_item+1)
            next_qvalue = self.comboBox_Q.itemText(cur_item+1)
        else:
            return True
        # Si estoy en la ventana de calcular las áreas
        if self.groupBox_area.isVisible() is True:
            lroi_n: int
            # Si no he pasado por esta Q entonces los items "lrois",
            # "lroisLimits" y "lareas" del dic están vacíos.
            # No puedo copiar los "lrois" del plot anterior, porque si lo
            # hago el callback está ligado al mismo ROI para todas las Qs!!!
            # Solo copio los límites!! Siempre tengo un ROI mínimo.
            # No cambio la visibilidad de los lineEdits porque es la misma
            # que la de la Q de la que vengo.
            if len(self._dataDic[next_qvalue]["lrois"]) == 0:
                # Copio los limites de los ROIs de la Q de la que vengo
                self._dataDic[next_qvalue]["lroisLimits"] = \
                    self._dataDic[cur_qvalue]["lroisLimits"].copy()
                for lroi_n in range(
                        len(self._dataDic[next_qvalue]["lroisLimits"])
                ):
                    self.fmi.set_lrois(next_qvalue, self._dataDic, lroi_n)
            else:
                # Si ya he pasado por esa Q, ya tengo rellenos los items
                # "lrois", "lroisLimits" y "lareas" en el diccionario.
                # Puedo tener diferente numero de ROIs, así tengo que
                # cambiar la visibilidad de los lineEdits y del nRois
                # spinBox!
                self.groupBox_ROI2.hide()
                self.groupBox_ROI3.hide()
                self.groupBox_ROI4.hide()
                self.groupBox_ROI5.hide()
                for lroi_n in range(len(self._dataDic[next_qvalue]["lrois"])):
                    self.show_groupBoxRois(lroi_n)
                # También tengo que cambiar el número que aparece en el
                # spinBox
                self._nroiChangeFromCode = True
                self.spinBox_nROIs.setValue(
                    len(self._dataDic[next_qvalue]["lrois"]))
            # En ambos casos, tengo que añadir los ROIs a la gráfica, poner
            # los valores en los lineEdits y recalcular/colocar las áreas
            for lroi_n in range(len(self._dataDic[next_qvalue]["lrois"])):
                self._cur_plot.addItem(
                    self._dataDic[next_qvalue]["lrois"][lroi_n],
                    ignoreBounds=True)
                self.update_edit_x_Rois(lroi_n)
                self.connect_ROI_callback(lroi_n)
                # Recalculo las áreas para los datos a esa Q
                self.getAreas()

    def comboChangePlot(self: Self):
        """Change the data plot when the Q-value in the comboBox changes.

        Other Parameters
        ----------------
        cur_index: int
            to save the index of the current item (Q) in the comboBox.
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        _qChangeFromButton: bool
            to know that the change in the comboBox is comming from
            pressing this button. if it was True, at the end of the function
            it is set to the default False value.
         _nroiChangeFromCode: bool
            as the change in the spinBox is made from here ("code"),
            it is set to True.
        """
        cur_index: int
        cur_qvalue: str
        cur_index = self.comboBox_Q.currentIndex()
        cur_qvalue = self.comboBox_Q.currentText()
        # Primero llamo a la función de dibujar los datos medidos
        self._cur_plot.clear()
        self.fmi.curPlot(self._cur_plot, self.loadDLG._dfS,
                         cur_index)
        # Si estoy en la pantalla de calcular las áreas y además el cambio
        # de Q en el comboBox no viene dado por los botones Q_p y Q_m
        if (
            self.groupBox_area.isVisible() is True and
            self._qChangeFromButton is False
        ):
            # Cambio la visibilidad de las casillas
            self.groupBox_ROI2.hide()
            self.groupBox_ROI3.hide()
            self.groupBox_ROI4.hide()
            self.groupBox_ROI5.hide()
            lroi_n: int
            # Si a esa Q ya tengo "lrois","lroisLimits" y "lareas" en el
            # diccionario
            if len(self._dataDic[cur_qvalue]["lrois"]) != 0:
                # y coloco los ROIs y los valores
                for lroi_n in range(len(self._dataDic[cur_qvalue]["lrois"])):
                    # Cambio la visibilidad de las casillas
                    self.show_groupBoxRois(lroi_n)
                    self._cur_plot.addItem(
                        self._dataDic[cur_qvalue]["lrois"][lroi_n],
                        ignoreBounds=True)
                    self.update_edit_x_Rois(lroi_n)
                    self.connect_ROI_callback(lroi_n)
                    # Recalculo las áreas para los datos a esa Q
                    self.getAreas()
            # Si no he pasado nunca por esa Q y no tengo ROIs en el
            # diccionario, coloco el ROI1
            else:
                lroi_n = 0
                self.show_groupBoxRois(lroi_n)
                self.removeAreas(lroi_n)
                self.fmi.set_lrois(cur_qvalue, self._dataDic, lroi_n)
                self.update_edit_x_Rois(lroi_n)
                self._cur_plot.addItem(
                    self._dataDic[cur_qvalue]["lrois"][lroi_n],
                    ignoreBounds=True)
                self.connect_ROI_callback(lroi_n)
            # En todos los casos tengo que cambiar el número que aparece en el
            # spinBox, y setear el valor de _qChangeFromButton a False
            self._nroiChangeFromCode = True
            self.spinBox_nROIs.setValue(
                len(self._dataDic[cur_qvalue]["lrois"]))
        else:
            self._qChangeFromButton = False

    def nRoi_change(self: Self):
        """Add or remove Linear ROIs from graph and the coresponding lineEdits.

        Other Parameters
        ----------------
        cur_nRois: int
            to save the number of ROIs in the spinBox.
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        _nroiChangeFromCode: bool
            to know if the change in the spinBox comes from the spinBox itself
            or from code. If it was True, at the end of the function it is set
            to the default value False.
        """
        cur_qvalue: str
        cur_nRois: int
        # Si el número de Rois lo cambio del spinbox (o es el ROI1)
        if self._nroiChangeFromCode is False:
            cur_qvalue = self.comboBox_Q.currentText()
            cur_nRois = self.spinBox_nROIs.value()
            # Si disminuyo el número de ROIs, borro los que me sobran del plot
            if cur_nRois < len(self._dataDic[cur_qvalue]["lrois"]):
                for i in range(
                    cur_nRois, len(self._dataDic[cur_qvalue]["lrois"])
                ):
                    self._cur_plot.removeItem(
                        self._dataDic[cur_qvalue]["lrois"][i])
                    # Borro las áreas correspondientes de las casillas
                    self.remove_edit_x_Rois(i)
                    self.removeAreas(i)
                    # Oculto los lineEdit correspondientes
                    self.hide_groupBoxRois(i)
                # y de diccionario
                del self._dataDic[cur_qvalue]["lrois"][cur_nRois:]
                del self._dataDic[cur_qvalue]["lroisLimits"][cur_nRois:]
                del self._dataDic[cur_qvalue]["lareas"][cur_nRois:]
            else:
                for lroi_n in range(len(self._dataDic[cur_qvalue]["lrois"]),
                                    cur_nRois):
                    self.show_groupBoxRois(lroi_n)
                    self.fmi.set_lrois(cur_qvalue, self._dataDic,
                                       lroi_n)
                    self.update_edit_x_Rois(lroi_n)
                    self._cur_plot.addItem(self._dataDic[cur_qvalue][
                        "lrois"][lroi_n], ignoreBounds=True)
                    self.connect_ROI_callback(lroi_n)
            # si el número de ROIs se cambia desde código, cuando acabo lo
            # pongo otra vez a False
        else:
            self._nroiChangeFromCode = False

    def show_groupBoxRois(self: Self, lroi_n: int):
        """Show the goupBox of the lroi_n.

        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the linear ROI (1-5)
            that is to be shown.
        """
        match lroi_n:
            case 0:
                self.groupBox_ROI1.show()
            case 1:
                self.groupBox_ROI2.show()
            case 2:
                self.groupBox_ROI3.show()
            case 3:
                self.groupBox_ROI4.show()
            case 4:
                self.groupBox_ROI5.show()

    def hide_groupBoxRois(self: Self, lroi_n: int):
        """Hide the goupBox of the lroi_n.

        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the linear ROI (1-5)
            that is to be hide.
        """
        match lroi_n:
            case 0:
                self.groupBox_ROI1.hide()
            case 1:
                self.groupBox_ROI2.hide()
            case 2:
                self.groupBox_ROI3.hide()
            case 3:
                self.groupBox_ROI4.hide()
            case 4:
                self.groupBox_ROI5.hide()

    def integrate(self: Self):
        """Display the groupBox_area and plot ROI1 for the given Q.

        Other Parameters
        ----------------
        lroi_n: int
            the index of the linear ROI. It is set to 0 (ROI1).
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        """
        self.groupBox_area.show()
        # Escondo todos menos el primero, porque el spinbox estará en 1
        self.groupBox_ROI2.hide()
        self.groupBox_ROI3.hide()
        self.groupBox_ROI4.hide()
        self.groupBox_ROI5.hide()
        # Relleno el diccionario con las listas lrois y areas para todas las Q
        qvalue: str
        for qvalue in self._dataDic:
            self._dataDic[qvalue]["lrois"] = list()
            self._dataDic[qvalue]["lareas"] = list()
            self._dataDic[qvalue]["lroisLimits"] = list()
        # Aquí voy ha hacer como si cambiase el número de ROIs DESDE EL SPINBOX
        # y llamo a esa función
        self.nRoi_change()

    def update_edit_x_Rois(self: Self, lroi_n: int):
        """Update the Xmin and Xmax values in the corresponding lineEdits.

        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the current linear ROI (1-5).

        Other Parameters
        ----------------
        cur_roi_range: list
            to save the limits of the current ROI.
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        """
        cur_qvalue: str
        cur_lroi_range: list
        cur_qvalue = self.comboBox_Q.currentText()
        # Obtengo el valor del linear ROI item
        cur_lroi_range = list(
            (self._dataDic[cur_qvalue]["lrois"][lroi_n].getRegion()))
        # Lo guardo en el diccionario
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n] = cur_lroi_range
        # Lo escribo en el lineEdit correspondiente
        match lroi_n:
            case 0:
                self.lineEdit_xmin_ROI1.setText(f"{cur_lroi_range[0]:0.2f}")
                self.lineEdit_xmax_ROI1.setText(f"{cur_lroi_range[1]:0.2f}")
            case 1:
                self.lineEdit_xmin_ROI2.setText(f"{cur_lroi_range[0]:0.2f}")
                self.lineEdit_xmax_ROI2.setText(f"{cur_lroi_range[1]:0.2f}")
            case 2:
                self.lineEdit_xmin_ROI3.setText(f"{cur_lroi_range[0]:0.2f}")
                self.lineEdit_xmax_ROI3.setText(f"{cur_lroi_range[1]:0.2f}")
            case 3:
                self.lineEdit_xmin_ROI4.setText(f"{cur_lroi_range[0]:0.2f}")
                self.lineEdit_xmax_ROI4.setText(f"{cur_lroi_range[1]:0.2f}")
            case 4:
                self.lineEdit_xmin_ROI5.setText(f"{cur_lroi_range[0]:0.2f}")
                self.lineEdit_xmax_ROI5.setText(f"{cur_lroi_range[1]:0.2f}")

    def get_Roi1_xmin(self: Self):
        """Get the value of the min lineEdit to set the graph linear ROI1.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (0) of the linear ROI1.
        new_xmin: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmin: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 0
        # Obtengo el valor inroducido en el lineEdit
        new_xmin = self.lineEdit_xmin_ROI1.text()
        # Lo guardo en el diccionario
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][0] = float(new_xmin)
        # llamo a la función que me actualiza los límites de los ROIs
        # en la gráfica
        self.update_graph_Rois()

    def get_Roi1_xmax(self: Self):
        """Get the value of the max lineEdit to set the graph linear ROI1.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (0) of the linear ROI1.
        new_xmax: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmax: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 0
        new_xmax = self.lineEdit_xmax_ROI1.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][1] = float(new_xmax)
        self.update_graph_Rois()

    def get_Roi2_xmin(self: Self):
        """Get the value of the min lineEdit to set the graph linear ROI2.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (1) of the linear ROI2.
        new_xmin: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmin: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 1
        new_xmin = self.lineEdit_xmin_ROI2.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][0] = float(new_xmin)
        self.update_graph_Rois()

    def get_Roi2_xmax(self: Self):
        """Get the value of the max lineEdit to set the graph linear ROI2.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (1) of the linear ROI2.
        new_xmax: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmax: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 1
        new_xmax = self.lineEdit_xmax_ROI2.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][1] = float(new_xmax)
        self.update_graph_Rois()

    def get_Roi3_xmin(self: Self):
        """Get the value of the min lineEdit to set the graph linear ROI3.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (2) of the linear ROI3.
        new_xmin: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmin: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 2
        new_xmin = self.lineEdit_xmin_ROI3.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][0] = float(new_xmin)
        self.update_graph_Rois()

    def get_Roi3_xmax(self: Self):
        """Get the value of the max lineEdit to set the graph linear ROI3.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (2) of the linear ROI3.
        new_xmax: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmax: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 2
        new_xmax = self.lineEdit_xmax_ROI3.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][1] = float(new_xmax)
        self.update_graph_Rois()

    def get_Roi4_xmin(self: Self):
        """Get the value of the min lineEdit to set the graph linear ROI4.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (3) of the linear ROI4.
        new_xmin: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmin: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 3
        new_xmin = self.lineEdit_xmin_ROI4.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][0] = float(new_xmin)
        self.update_graph_Rois()

    def get_Roi4_xmax(self: Self):
        """Get the value of the max lineEdit to set the graph linear ROI4.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (3) of the linear ROI4.
        new_xmax: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmax: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 3
        new_xmax = self.lineEdit_xmax_ROI4.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][1] = float(new_xmax)
        self.update_graph_Rois()

    def get_Roi5_xmin(self: Self):
        """Get the value of the min lineEdit to set the graph linear ROI5.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (4) of the linear ROI5.
        new_xmin: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmin: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 4
        new_xmin = self.lineEdit_xmin_ROI5.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][0] = float(new_xmin)
        self.update_graph_Rois()

    def get_Roi5_xmax(self: Self):
        """Get the value of the max lineEdit to set the graph linear ROI5.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (4) of the linear ROI5.
        new_xmax: str
            the text value input in the lineEdit.
        """
        cur_qvalue: str
        lroi_n: int
        new_xmax: str
        cur_qvalue = self.comboBox_Q.currentText()
        lroi_n = 4
        new_xmax = self.lineEdit_xmax_ROI5.text()
        self._dataDic[cur_qvalue]["lroisLimits"][lroi_n][1] = float(new_xmax)
        self.update_graph_Rois()

    def update_graph_Rois(self: Self):
        """Update the limits of the graphical linear region items in the plot.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        lroi_n: int
            the index (0-4) of the linear ROI (1-5).
        """
        cur_qvalue: str
        lroi_n: int
        cur_qvalue = self.comboBox_Q.currentText()
        for lroi_n in range(len(self._dataDic[cur_qvalue]["lrois"])):
            self._dataDic[cur_qvalue]["lrois"][lroi_n].setRegion(
                self._dataDic[cur_qvalue]["lroisLimits"][lroi_n])

    def remove_edit_x_Rois(self: Self, lroi_n: int):
        """Remove the Xmin and Xmax values in the corresponding lineEdits.

        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the current linear ROI (1-5).
        """
        match lroi_n:
            case 0:
                self.lineEdit_xmin_ROI1.clear()
                self.lineEdit_xmax_ROI1.clear()
            case 1:
                self.lineEdit_xmin_ROI2.clear()
                self.lineEdit_xmax_ROI2.clear()
            case 2:
                self.lineEdit_xmin_ROI3.clear()
                self.lineEdit_xmax_ROI3.clear()
            case 3:
                self.lineEdit_xmin_ROI4.clear()
                self.lineEdit_xmax_ROI4.clear()
            case 4:
                self.lineEdit_xmin_ROI5.clear()
                self.lineEdit_xmax_ROI5.clear()

    def removeAreas(self: Self, lroi_n: int):
        """Clear the values in the correspoding lineEdit.

        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the corresponding ROI (1-5)
        """
        match lroi_n:
            case 0:
                self.lineEdit_area_ROI1.clear()
            case 1:
                self.lineEdit_area_ROI2.clear()
            case 2:
                self.lineEdit_area_ROI3.clear()
            case 3:
                self.lineEdit_area_ROI4.clear()
            case 4:
                self.lineEdit_area_ROI5.clear()

    def getAreas(self: Self):
        """Calculate the area below the curve delimited by the ROI.

        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        """
        cur_qvalue: str
        lroi_n: int
        cur_qvalue = self.comboBox_Q.currentText()
        # voy a borrar las áreas del diccionario
        self._dataDic[cur_qvalue]["lareas"].clear()
        self.fmi.calcArea(cur_qvalue, self._dataDic)
        for lroi_n in range(len(self._dataDic[cur_qvalue]["lrois"])):
            self.displayArea(lroi_n)

    def displayArea(self: Self, lroi_n: int):
        """Display de value of the area for the ROI in the lineEdit.

        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the corresponding ROI (1-5)
        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        area: float
            the calculated value of the area below the curve for the
            corresponding lroi_n ROI
        """
        cur_qvalue: str
        cur_qvalue = self.comboBox_Q.currentText()
        area: float
        area = self._dataDic[cur_qvalue]["lareas"][lroi_n]
        match lroi_n:
            case 0:
                self.lineEdit_area_ROI1.setText(f"{area:0.4f}")
            case 1:
                self.lineEdit_area_ROI2.setText(f"{area:0.4f}")
            case 2:
                self.lineEdit_area_ROI3.setText(f"{area:0.4f}")
            case 3:
                self.lineEdit_area_ROI4.setText(f"{area:0.4f}")
            case 4:
                self.lineEdit_area_ROI5.setText(f"{area:0.4f}")

    def connect_ROI_callback(self: Self, lroi_n: int):
        """Connect the linear ROI callback with the update_edit_x function.

        I need to do this connection in a match/case because if I pass
        a parameter to the function the callback does not work.
        Parameters
        ----------
        lroi_n: int
            the index (0-4) of the corresponding ROI (1-5)
        Other Parameters
        ----------------
        cur_qvalue: str
            to save the text value of the current item of the comboBox
            the Q-value (str) is the key of the _dataDic dictionary.
        """
        cur_qvalue = self.comboBox_Q.currentText()
        match lroi_n:
            case 0:
                self._dataDic[cur_qvalue]["lrois"][0].\
                    sigRegionChanged.connect(
                        lambda: self.update_edit_x_Rois(0))
            case 1:
                self._dataDic[cur_qvalue]["lrois"][1].\
                    sigRegionChanged.connect(
                        lambda: self.update_edit_x_Rois(1))
            case 2:
                self._dataDic[cur_qvalue]["lrois"][2].\
                    sigRegionChanged.connect(
                        lambda: self.update_edit_x_Rois(2))
            case 3:
                self._dataDic[cur_qvalue]["lrois"][3].\
                    sigRegionChanged.connect(
                        lambda: self.update_edit_x_Rois(3))
            case 4:
                self._dataDic[cur_qvalue]["lrois"][4].\
                    sigRegionChanged.connect(
                        lambda: self.update_edit_x_Rois(4))

    def exportAreas(self: Self):
        """Export the results as a table to a csv file."""
        # self._saveDic = deepcopy(self._dataDic)
        for q_value in self._dataDic.keys():
            self._saveDic[q_value] = \
                {"lareas": self._dataDic[q_value]["lareas"].copy(),
                 "lroisLimits": self._dataDic[q_value]["lroisLimits"].copy()}
        self.fmi.dict_to_csv(self._saveDic)


if __name__ == "__main__":
    app: QApplication
    win: MainWin
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()

    sys.exit(app.exec())
