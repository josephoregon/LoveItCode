# stripping whitespace 

df_trimmed = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df_col_trimmed = df.rename(columns=lambda x: x.strip())
