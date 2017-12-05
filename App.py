# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:41:42 2017

@author: Ben
"""
from flask import Flask
app=Flask(__name__)

import os
items = os.listdir ("satdata")

@app.route("/", methods=["GET"])
def filedisplay():
    for file in items:
        if file.endswith("nc"):
            items.append(file)
            
    return(items)