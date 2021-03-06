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
@app.route("/data/<file>")
def printdata(file):
    filepath="satdata" + str(chr(92)) + (nc_items[int(file)]) 
    dataset = Dataset(filepath)
    f = dataset.dimensions.keys()
    variable = []
    dimension = []
    for item in f:
        dimension.append(dataset.dimensions[str(item)])
    g = dataset.variables.keys()
    for item in g:
        variable.append(dataset.variables[item])
    return render_template("File_Template.html", variable=variable, file=file, dimension=dimension, g=g, f=f, dataset=dataset)

for file in items:   
    if file.endswith("nc"):
        nc_items.append(file)

