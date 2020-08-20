#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create a MSSQL Connection, import from SQL to pandas dataframe

import pyodbc
import pandas as pd

config = dict(server='SERVER', port=PORT, database='DATABASE',
              username='USERNAME', password='PASSWORD')

cxn_str = 'SERVER={server},{port};' + 'DATABASE={database};' \
    + 'UID={username};' + 'PWD={password}'

cxn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};'
                     + cxn_str.format(**config))

df = pd.read_sql('SELECT * FROM TABLE;', cxn)
