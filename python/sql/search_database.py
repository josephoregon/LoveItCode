# This function searches several databases that are connected to the notebook 

def search(database, table_column, search_word):

    import pyodbc
    import numpy as np
    import pandas as pd
    import datetime as datetime, dt
    
    from pandas import DataFrame
    from tqdm import tqdm, tqdm_notebook

    # DATABASE 1
    
    config = dict(server='000.000.000.00', # server name here
                  port=1433, # port here
                  database='database_name',
                  username='user_name_here',
                  password='password_here')
                  
    cxn = ('SERVER={server},{port};' + 'DATABASE={database};' +
           'UID={username};' + 'PWD={password}')
           
    cxn1 = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};' +
                             cxn.format(**config))
    sql = '''

            SELECT     Schema_name(tab.schema_id) AS schema_name, 
                       tab.NAME                   AS table_name, 
                       col.column_id, 
                       col.NAME AS column_name, 
                       t.NAME   AS data_type, 
                       col.max_length, 
                       col.PRECISION 
            FROM       sys.tables  AS tab 
            INNER JOIN sys.columns AS col 
            ON         tab.object_id = col.object_id 
            LEFT JOIN  sys.types AS t 
            ON         col.user_type_id = t.user_type_id 
            ORDER BY   schema_name, 
                       table_name

        '''

    # DATABASE 2
    
    cxn2 = pyodbc.connect('DSN=db_name;Trusted_Connection=yes;')
    
    sql = '''

                SELECT     Schema_name(tab.schema_id) AS schema_name, 
                           tab.NAME                   AS table_name, 
                           col.column_id, 
                           col.NAME AS column_name, 
                           t.NAME   AS data_type, 
                           col.max_length, 
                           col.PRECISION 
                FROM       sys.tables  AS tab 
                INNER JOIN sys.columns AS col 
                ON         tab.object_id = col.object_id 
                LEFT JOIN  sys.types AS t 
                ON         col.user_type_id = t.user_type_id 
                ORDER BY   schema_name, 
                           table_name

            '''

    # DATABASE 3
    
    cxn3 = pyodbc.connect('DSN=db_name;Trusted_Connection=yes;')
    
    sql = '''

                SELECT     Schema_name(tab.schema_id) AS schema_name, 
                           tab.NAME                   AS table_name, 
                           col.column_id, 
                           col.NAME AS column_name, 
                           t.NAME   AS data_type, 
                           col.max_length, 
                           col.PRECISION 
                FROM       sys.tables  AS tab 
                INNER JOIN sys.columns AS col 
                ON         tab.object_id = col.object_id 
                LEFT JOIN  sys.types AS t 
                ON         col.user_type_id = t.user_type_id 
                ORDER BY   schema_name, 
                           table_name

            '''

    db1 = pd.read_sql(sql, cxn1)
    db2 = pd.read_sql(sql, cxn2)
    db3 = pd.read_sql(sql, cxn3)

    if database == 'db1':
        if table_column == 't':
            df = db1[db1['table_name'].str.contains(search_word, case=False)]
        else:
            df = db1[db1['column_name'].str.contains(search_word, case=False)]
    elif database == 'db2':
        if table_column == 't':
            df = db2[db2['table_name'].str.contains(search_word, case=False)]
        else:
            df = db2[db2['column_name'].str.contains(search_word, case=False)]
    else:
        if table_column == 't':
            df = db3[db3['table_name'].str.contains(search_word, case=False)]
        else:
            df = db3[db3['column_name'].str.contains(search_word, case=False)]
            
    return df
