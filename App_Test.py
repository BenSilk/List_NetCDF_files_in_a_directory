# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:59:10 2017

@author: Ben
"""

from App import filedisplay
import os

def test_filedisplay():
    assert  filedisplay(3)==(os.listdir ("/satdata"))