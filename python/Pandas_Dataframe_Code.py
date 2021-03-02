# Create unique ID for rows
df['id'] = df.groupby(['y','x']).ngroup()

# Add leading zeros to the integer column in Python
df['id']=df['id'].apply(lambda x: '{0:0>5}'.format(x))

# Search substrings for any string value in dataframe
df.apply(lambda row: row.astype(str).str.contains('STRING').any(), axis=1)
