# stripping whitespace 

df_trimmed = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df_col_trimmed = df.rename(columns=lambda x: x.strip())


def panda_strip(x):
    r =[]
    for y in x:
        if isinstance(y, str):
            y = y.strip()

        r.append(y)
    return pd.Series(r)

df = df.apply(lambda x: panda_strip(x))
