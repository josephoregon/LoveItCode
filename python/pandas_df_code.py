# Create unique ID for rows
df['id'] = df.groupby(['y','x']).ngroup()

# Search substrings for any string value in dataframe
df.apply(lambda row: row.astype(str).str.contains('STRING').any(), axis=1)
