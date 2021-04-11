# Rename dataframe column names
df_new = df.rename(columns={'column1': 'col1'})

# Add a list as a new column 
dfnew['Column1'] = ['value1', 'value2', 'value3', 'value4', 'value5']

# Add an array as a new column 
ar = np.array([1, 2, 3, 4, 5])
df_new['Calling code'] = ar


# useful column reordering function for pandas df

def order(frame, var):
    if type(var) is str:
        var = [var]  # let the command take a string or list
    varlist = [w for w in frame.columns if w not in var]
    frame = frame[var + varlist]
    return frame


# Delete using del
del df_new['Column1']

# Delete using drop() 
df_new = df_new.drop(['Column1'], axis=1)

# Note that the first column is in position with index '0'
ser = pd.Series(['es', 'it', 'fr', 'pt', 'gr'], index=['ESP', 'ITA', 'FRA', 'PRT', 'GRC'])
df_new.insert(1, 'Column1', ser)

# Get the DataFrame column names as a list
clist = list(df_new.columns)

# Rearrange list the way you like 
clist_new = clist[-1:] + clist[:-1]  # brings the last column in the first place

# Pass the new list to the DataFrame - like a key list in a dict 
df_new = df_new[clist_new]

clist = ['country', 'capital city', 'Internet domains', 'population', 'percent', 'Calling code']
df_new = df_new[clist]

# Use the [ ] notation to assign new values to a column. New value can either be scalar (it 'propagates' throughout
# the column cells) or a vector (array-like object) of the same size as the column
data = {'country': ['Italy', 'Spain', 'Greece', 'France', 'Portugal'],
        'popu': [61, 46, 11, 65, 10],
        'percent': [0.83, 0.63, 0.15, 0.88, 0.14]}

df = pd.DataFrame(data, index=['ITA', 'ESP', 'GRC', 'FRA', 'PRT'])
df.percent = '-'  # A single value 'propagates' to all column cells
df.percent = 0.001 * df.popu  # Data in 'percent' and 'popu' columns are autonatically aligned

# Create unique ID for rows
df['id'] = df.groupby(['y', 'x']).ngroup()

# Add leading zeros to the integer column in python
df['id'] = df['id'].apply(lambda x: '{0:0>5}'.format(x))

# Search substrings for any string value in dataframe
df.apply(lambda row: row.astype(str).str.contains('STRING').any(), axis=1)
