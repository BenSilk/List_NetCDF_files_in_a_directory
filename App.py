# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:41:42 2017

@author: Ben
"""
from flask import Flask
from netCDF4 import Dataset
app=Flask(__name__)

import os
items = os.listdir ("satdata")

@app.route("/", methods=["GET"])
def filedisplay():
    for file in items:
        if file.endswith("nc"):
            items.append(file)         
    return(items)

@app.route("/data",methods=["GET"])
def printdata(file):
    dataset = Dataset("satdata\A2017332.L3m_DAY_KD490_Kd_490_4km.nc")
    f = dataset.dimensions.keys()
    data=[]
    data.append(f)
    data.append("\n")
    for item in f:
        data.append(dataset.dimensions[str(item)])
        data.append("\n")
    g = dataset.variables.keys()
    data.append(g)
    data.append("\n")
    for item in g:
        data.append(dataset.variables[item])
    return data
filedisplay()
printdata(1)
