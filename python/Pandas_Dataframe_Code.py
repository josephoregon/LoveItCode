# Rename dataframe column names
df_new = df.rename(columns={'column1': 'col1'})

# Add a list as a new column 
dfnew['Column1'] = ['value1','value2','value3','value4','value5']

# Add an array as a new column 
ar = np.array([1,2,3,4,5])
df_new['Calling code'] = ar

# Create unique ID for rows
df['id'] = df.groupby(['y','x']).ngroup()

# Add leading zeros to the integer column in Python
df['id']=df['id'].apply(lambda x: '{0:0>5}'.format(x))

# Search substrings for any string value in dataframe
df.apply(lambda row: row.astype(str).str.contains('STRING').any(), axis=1)
