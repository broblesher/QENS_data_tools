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
Dependencies: pandas, pyqtgraph, numpy
"""

import pandas as pd
import pyqtgraph as pg
import numpy as np
import numpy.typing as npt


class FuncionesMenuIntegrar:
    """FuncionesMenuIntegrar class.

    A class used to colect the methos needed for the Integrate menu.

    Methods
    -------
    fillqlist(dfS)
        Takes the Q-values from the column titles from the dfS pandas
        DataFrame and saves them in a list
    curPlot(pitem, dfS, cur_index)
        Adds to pitem pg.PlotItem the plot of the data in dfS for
        cur_index
    plot_init(plw)
        Creates a pg.PlotIntem y lo añade al plw pg.GraphicsLayoutWidget
    find_nearest(x_arr, x_value)
        finds the nearest value to x_value in the x_arr array
    set_lrois(cur_qvalue, dataDic, x, lroi_n)
        sets the pg.LinearRegionItem for the lroi_n index for the cur_qvalue,
        adds the item to the pg.PlotItem and saves it to the dataDic

    """

    def __init__(self):
        """Class constructor."""
        print('FuncionesMenuIntegrar constructor')

    def fillqlist(self, dfS: pd.DataFrame) -> list:
        """Take Q-values (as str) from DataFrame and save them to a list.

        Parameters
        ----------
        dfS: pd.DataFrame
            Where the imported data is saved.

        Other Parameters
        ----------------
        qstr: str
            To save the Q-value as a string
        columns: pd.Index
            To save the title of the DataFrame columns
        qnumber: int
            The number of Q-values in the DataFrame

        Returns
        -------
        qlist: list
            A list with the Q-values.
        """
        qlist: list
        qlist = []
        qstr: str
        columns: pd.Index
        columns = dfS.columns
        qnumber: int
        qnumber = int(columns.size / 3)
        for i in range(qnumber):
            qstr = columns[3 * i + 1]
            qstr = qstr[qstr.rfind('_') + 1:-3]
            qlist.append(qstr)
        return qlist

    def curPlot(self, pitem: pg.PlotItem, dfS: pd.DataFrame, cur_index: int):
        """Plot the data for the desired Q-value.

        Parameters
        ----------
        pitem: pg.PlotItem
            The item that contains the scatter plot to be displayed.
        dfS: pd.DataFrame
            Where the imported data is stored.
        cur_index: int
            The index of the Q-value to be ploted.

        Other Parameters
        ----------------
        legend: str
            The text to be shown as legend in the plot.
        x: pd.Series
            The x-values of the data to be plot.
        y: pd.Series
            The y-values of the data to be plot.
        height_err: pd.Series
            The y error of the data to ble plot.
        err_bar: pg.ErrorBarItem
            The item that contains the y error to add the error bars to the
            plot.
        """
        legend: str
        legend = dfS.columns[3 * cur_index + 1]
        x: pd.Series
        y: pd.Series
        height_err: pd.Series
        x = dfS.iloc[:, 3 * cur_index]
        y = dfS.iloc[:, 3 * cur_index + 1]
        height_err = dfS.iloc[:, 3 * cur_index + 2]
        pitem.addLegend()
        err_bar: pg.ErrorBarItem
        err_bar = pg.ErrorBarItem(x=x, y=y, height=height_err, beam=0.05)
        pitem.addItem(err_bar)
        pitem.plot(x, y, name=legend, pen=None, symbol='o', symbolPen=None,
                   symbolSize=10)  # setting pen=None disables line drawing

    def plot_init(self, plw: pg.GraphicsLayoutWidget) -> pg.PlotItem:
        """Create the pg.PlotItem to display the data.

        Parameters
        ----------
        plw: pg.GraphicsLayoutWidget
            The layout where the PlotItem is going to be set.

        Return
        ------
        pitem: pg.PlotItem
            where the data plot is going to be set.
        """
        pitem: pg.PlotItem
        pitem = plw.addPlot(title='pòr fiiiiiinnnnnnnnn')
        pitem.addLegend()
        pitem.setXRange(-6, 6, padding=0)
        pitem.setYRange(0, 1, padding=0)
        pitem.setLabel('left', "Scattered Intensity")
        pitem.setLabel('bottom', "Energy", units='meV')
        return pitem

    def find_nearest(self, x_arr: npt.NDArray, x_value: float) -> int:
        """Find the nearest value to x_value in the x_arr array.

        Parameters
        ----------
        x_arr: np.array
            The array with the x-value data.
        x_value: float
            The input x-value.

        Return
        ------
        idx: int
            the index of the nearest value to x_value in the x_arr array.
        """
        idx: int
        idx = int((np.abs(x_arr - x_value)).argmin())
        return idx

    def set_lrois(self, cur_qvalue: str, dataDic: dict,
                  lroi_n: int):
        """Set the linear region of interest item and save it to a dict.

        Parameters
        ----------
        cur_qvalue: str
            The Q-value for which the ROI is going to be set.
        dataDic: dict
            Where the ROI items are going to be saved.
        x: pd.Series
            The series with the x-values.
        lroi_n: int
            The index of the ROI to be set.

        Other Parameters
        ----------------
        sbrush: tuple
            To save the RGBA values of the color or the ROI.
        shoverBrush: tuple
            To save the RGBA values of the color of the Roi when the mouse
            is in the ROI.
        lcolor: tuple
            To save the RGBA values of the color of the labels in the ROI.
        """
        sbrush: tuple
        shoverBrush: tuple
        lcolor: tuple
        # Asigno un color a cada ROI
        match lroi_n:
            case 0:
                sbrush = (100, 100, 255, 127)
                shoverBrush = (0, 0, 255, 127)
                lcolor = (0, 0, 255, 255)
            case 1:
                # Rojo
                sbrush = (255, 100, 100, 127)
                shoverBrush = (255, 0, 0, 127)
                lcolor = (255, 0, 0, 255)
            case 2:
                # Verde
                sbrush = (100, 255, 100, 127)
                shoverBrush = (0, 255, 0, 127)
                lcolor = (0, 200, 0, 255)
            case 3:
                # Amarillo
                sbrush = (255, 255, 100, 127)
                shoverBrush = (255, 255, 0, 127)
                lcolor = (255, 200, 0, 255)
            case 4:
                # Morado
                sbrush = (255, 100, 255, 127)
                shoverBrush = (255, 0, 255, 127)
                lcolor = (255, 0, 255, 255)
        # Pongo las lineas verticales del ROI en el plot
        x = dataDic[cur_qvalue]["measData"].iloc[:, 0]
        # Si no tengo limites guardados para ese ROI
        if (len(dataDic[cur_qvalue]["lroisLimits"]) == lroi_n):
            values = [x.iloc[0], x.iloc[-1]]
            dataDic[cur_qvalue]["lroisLimits"].append(
                values)
        else:
            values = dataDic[cur_qvalue]["lroisLimits"][lroi_n]
        dataDic[cur_qvalue]["lrois"].append(pg.LinearRegionItem(
            values, brush=sbrush, hoverBrush=shoverBrush,
            bounds=[x.iloc[0], x.iloc[-1]]))  # =[x.iloc[0], x.iloc[-1]]
        dataDic[cur_qvalue]["lrois"][lroi_n].setZValue(10)
        # Add the LinearRegionItem to the ViewBox, but tell the ViewBox to
        # exclude this item when doing auto-range calculations.
        pg.InfLineLabel(
            dataDic[cur_qvalue]["lrois"][lroi_n].lines[0],
            text="ROI " + str(lroi_n + 1),
            rotateAxis=(1, 0),
            position=0.95,
            color=lcolor,
            movable=True)
        pg.InfLineLabel(
            dataDic[cur_qvalue]["lrois"][lroi_n].lines[0],
            text="x1: {value:0.2f}",
            position=0.85,
            color=lcolor,
            movable=True)
        pg.InfLineLabel(
            dataDic[cur_qvalue]["lrois"][lroi_n].lines[1],
            text="x2: {value:0.2f}",
            position=0.85,
            color=lcolor,
            movable=True)

    def calcArea(self, cur_qvalue: str, dataDic: dict):
        """Calculate the areas under the curve in the ROIs.

        Parameters
        ----------
        cur_qvalue: str

        dataDic: dict

        Other Parameters
        ----------------
        x: npt.NDArray
            The complete x array.
        y: npt.NDArray
            The complete y array.
        lroi_n: int
            The index of ROI to be considered.
        cur_xmin: float
            The xmin limit of the ROI.
        xmin_index: int
            The index of xmin limit of the ROI y the x array.
        cur_xmax: float
            The xmax limit of the ROI.
        xmax_index: int
            The index of xmax limit of the ROI y the x array.
        x_lroi: npt.NDArray
            The x array chopped to the ROI limits.
        y_lroi: npt.NDArray
            The y array chopped to the ROI limits.
        area: np.float
            The computed area under the curve inside the ROI.
        """
        # Especifico los valores de x e y
        x: npt.NDArray
        y: npt.NDArray
        cur_xmin: float
        cur_xmax: float
        xmin_index: int
        xmax_index: int
        x_lroi: npt.NDArray
        y_lroi: npt.NDArray
        x = np.array(dataDic[cur_qvalue]["measData"].iloc[:, 0])
        y = np.array(dataDic[cur_qvalue]["measData"].iloc[:, 1])
        for lroi_n in range(len(dataDic[cur_qvalue]["lrois"])):
            # Corto x e y para considerar solo los valores dentro del ROI
            cur_xmin = dataDic[cur_qvalue]["lroisLimits"][lroi_n][0]
            xmin_index = self.find_nearest(x, cur_xmin)
            cur_xmax = dataDic[cur_qvalue]["lroisLimits"][lroi_n][1]
            xmax_index = self.find_nearest(x, cur_xmax)
            x_lroi = x[xmin_index:xmax_index]
            y_lroi = y[xmin_index:xmax_index]
            # Uso esta función de numpy para calcular el área
            area = np.trapezoid(y_lroi, x_lroi)
            # y la guardo en el diccionario
            dataDic[cur_qvalue]["lareas"].append(area)

    def dict_to_csv(self, dic: dict):
        """Export dictionary to csv.

        Parameters
        ----------
        dic: dict
            The dictionary with the data to be saved.

        Other parameters
        ----------------
        dfDic: pd.DataFrame
        n_ROIs: pd.Series
        n_ROIs_arr: list
        emin: list
        emax: list
        area: list
        emin_h: str
        emax_h: str
        area_h: str
        """
        dfDic: pd.DataFrame
        n_ROIs: pd.Series
        n_ROIs_arr: list
        dfDic = pd.DataFrame()
        n_ROIs_arr = []
        emin: list
        emax: list
        area: list
        emin = []
        emax = []
        area = []
        emin_h: str
        emax_h: str
        area_h: str
        q_values = pd.Series(
            list(dic.keys()),
            name='Q (' + chr(197) + chr(175) + chr(185) + ')')  # Å-1
        for q_value in dic.keys():
            n_ROIs_arr.append(len(dic[q_value]["lareas"]))
        n_ROIs = pd.Series(n_ROIs_arr, name='no.ROIs')
        dfDic = pd.concat([q_values, n_ROIs], axis=1)
        for roi_index in range(5):  # range(len(dic[q_value]["lareas"])):
            emin_h = 'E_min_' + str(roi_index+1) + ' (meV)'
            emax_h = 'E_max_' + str(roi_index+1) + ' (meV)'
            area_h = 'Area_' + str(roi_index+1)
            for q_value in dic.keys():
                if len(dic[q_value]["lareas"]) < roi_index + 1:
                    emin.append(None)
                    emax.append(None)
                    area.append(None)
                else:
                    emin.append(dic[q_value]["lroisLimits"][roi_index][0])
                    emax.append(dic[q_value]["lroisLimits"][roi_index][1])
                    area.append(dic[q_value]["lareas"][roi_index])
            dsemin = pd.Series(emin, name=emin_h)
            dsemax = pd.Series(emax, name=emax_h)
            dsarea = pd.Series(area, name=area_h)
            dfDic = pd.concat([dfDic, dsemin, dsemax, dsarea], axis=1)
            emin.clear()
            emax.clear()
            area.clear()
            del emin_h, emax_h, area_h
        dfDic.dropna(axis=1, how='all', inplace=True)  # thresh=thresholdVal,
        dfDic.to_csv('dict_areas.csv', sep='\t', float_format='%.4f',
                     index=False, encoding='utf-8')
