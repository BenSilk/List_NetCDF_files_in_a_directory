    # -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:41:42 2017

@author: Ben
"""
from flask import Flask, render_template, json, jsonify
from netCDF4 import Dataset
import numpy as np
import netCDF4
app=Flask(__name__)

import os
global dataset
items = os.listdir ("satdata")
nc_items = []

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, netCDF4._netCDF4.Dimension):
            return str(obj)
        elif isinstance(obj, netCDF4._netCDF4.Variable):
            return str(obj)
        elif isinstance(obj, np.ndarray):
            return list(obj)
        elif isinstance(obj, ):
            return list(obj)
        else:
            return super(MyEncoder, self).default(obj)

app.json_encoder = MyEncoder
##app.config["JSON_SORT_KEYS"] = False

for file in items:   
        if file.endswith("nc"):
            nc_items.append(file)

##def json_pretty_print(value):
##    return json.dumps(value, sort_keys=False,
##                      indent=4, separators=(',', ': ') ,cls=MyEncoder)
##
##app.jinja_env.filters['tojson_prettyprint'] = json_pretty_print

@app.route("/", methods=["GET"])
def filedisplay():
    return render_template("Index_Template.html", nc_items=nc_items)


@app.route("/data/<file>")
def printdata(file):
    filepath="satdata" + str(chr(92)) + (nc_items[int(file)]) 
    dataset = Dataset(filepath)
    jsn={}
    gdim = {}
    satfile = nc_items[int(file)]
    for item in dataset.dimensions.keys():
        gdim[item] = dataset.dimensions[item]
    jsn["Dimensions"] = gdim
    gatrl = {}
    for name in dataset.ncattrs():
        gatrl[name] = getattr(dataset, name)
    gvar = {}
    gvaratr = {}
    gvdata = {}
    for var in dataset.variables.keys():
        vatrs={}
        var1 = dataset.variables[var]
        for vatr in var1.ncattrs():
            vatrs[vatr] = getattr(var1, vatr)
        gvaratr[var] = vatrs
        if var == "lat" or var == "lon":
            gvdata[var] = dataset.variables[var][:]
        elif var == "Kd_490":
            gvdata[var] = dataset.variables[var][:][:].data
        else:
            gvdata[var] = dataset.variables[var][:][:]
    ##I would like to improve this bit of code so that it worked no matter what variables where present.
    gvar["Kd_490"]={"Shape" : "lat, lon", "Type" : "int", "Attributes" : gvaratr["Kd_490"], "Data" : gvdata["Kd_490"]}
    gvar["lat"]={"Shape" : "lat", "Type" : "float", "Attributes" : gvaratr["lat"], "Data" : gvdata["lat"]}
    gvar["lon"]={"Shape" : "lon", "Type" : "float", "Attributes" : gvaratr["lon"], "Data" : gvdata["lon"]}
    gvar["palette"]={"Shape" : "rgb, eightbitcolor", "Type" : "int", "Attributes" : gvaratr["palette"], "Data" : gvdata["palette"]}
    jsn["Variables"] = gvar
    jsn["Attributes"] = gatrl
    jsn=jsonify(jsn)
    return jsn
##    return render_template("File_Template.html",jsn = jsn,satfile = satfile )

##for file in items:   
##    if file.endswith("nc"):
##        nc_items.append(file)
##
