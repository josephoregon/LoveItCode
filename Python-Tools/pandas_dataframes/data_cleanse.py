# Only drop columns which have at least 90% non-NaNs
df.dropna(thresh=int(tube.shape[0] * 1), axis=1)
