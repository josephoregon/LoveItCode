#!/usr/bin/python
# -*- coding: utf-8 -*-

# useful column reordering function for pandas df

def order(frame, var):
    if type(var) is str:
        var = [var]  # let the command take a string or list
    varlist = [w for w in frame.columns if w not in var]
    frame = frame[var + varlist]
    return frame


