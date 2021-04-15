# Only drop columns which have at least 90% non-NaNs
df.dropna(thresh=int(tube.shape[0] * 1), axis=1)

# Filter dataframe to view NaNs
def nans(df): return df[df.isnull().any(axis=1)]
