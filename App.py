    # -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:41:42 2017

@author: Ben
"""
from flask import Flask, render_template
from netCDF4 import Dataset
app=Flask(__name__)

import os
global nc_items, dataset
items = os.listdir ("satdata")
nc_items = []

@app.route("/", methods=["GET"])
def filedisplay():
    for file in items:   
        if file.endswith("nc"):
            nc_items.append(file)         
    return render_template("Index_Template.html", nc_items=nc_items,file=file)

@app.route("/data/<file>")
def printdata(file):
    filepath="satdata" + str(chr(92)) + (nc_items[int(file)]) 
    dataset = Dataset(filepath)
    f = dataset.dimensions.keys()
    g = dataset.variables.keys()
    return render_template("File_Template.html", g=g, file=file, f=f)

for file in items:   
    if file.endswith("nc"):
        nc_items.append(file)

@app.route("/data/<file>/<dimension>")
def printdimesion(file, dimension):
    filepath="satdata" + str(chr(92)) + (nc_items[int(file)]) 
    dataset = Dataset(filepath)
    dimension_data=dataset.dimensions[dimension]
    return render_template("Dimension_Template.html",dimension_data=dimension_data)

@app.route("/data/<file>/<variable>")
def printvariable(file, variable):
    filepath="satdata" + str(chr(92)) + (nc_items[int(file)]) 
    dataset = Dataset(filepath)
    variable_data=dataset.variables[variable]
    return render_template("Variable_Template.html",variable_data=variable_data)
