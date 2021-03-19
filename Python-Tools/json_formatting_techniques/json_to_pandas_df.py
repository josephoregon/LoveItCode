

# json to dataframe

with open('Assessor-Search-Results.json', 'r', encoding='utf-8') as \
    json_file:
    json_work = json.load(json_file)

df = pd.json_normalize(json_work)

df = pd.DataFrame([y for x in df['results'].values.tolist() for y in x])


