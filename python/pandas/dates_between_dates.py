#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

A very helpful and fast approach towards getting a massive list if dates a range of two date columns. I used it to gather over 15 million
rows in less than a minute (this included adding minimal ETL code).

I found this code on https://stackoverflow.com/questions/59665876/fast-approach-to-add-rows-for-all-dates-between-two-columns-in-dataframe

'''

import itertools

# `date_range` is slow so we only call it once

all_dates = pd.date_range(df['start_date'].min(), df['end_date'].max())

# For each day in the range, number them as 0, 1, 2, 3, ...

rank = all_dates.to_series().rank().astype(np.int64) - 1

# Change from `2020-01-01` to "day 500 in the all_dates array", for example

start = df['start_date'].map(rank).values
end = df['end_date'].map(rank).values

# This is where the magic happens. For each row, instead of saying
# `start_date = Jan 1, 2020` and `end_date = Jan 10, 2020`, we are
# creating a range of days: [500, 501, ... 509]

indices = list(itertools.chain.from_iterable([range(s, e + 1) for (s,
               e) in zip(start, end)]))

# Now map day 500 back to Jan 1, 2020, day 501 back to Jan 2, 2020, and so on

dates = np.take(all_dates, indices)

# Align the rest of the columns to the expanded dates

duration = (end - start + 1).astype(np.int64)
ids = np.repeat(df['ID'], duration)
start_date = np.repeat(df['start_date'], duration)
end_date = np.repeat(df['end_date'], duration)

# Assemble the result

result = pd.DataFrame({
    'start_date': start_date,
    'end_date': end_date,
    'ID': ids,
    'Date': dates,
    })
