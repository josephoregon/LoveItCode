DATAFRAME.apply(lambda row: row.astype(str).str.contains('STRING').any(), axis=1)
