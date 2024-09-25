import pandas as pd

wine_reviews = pd.read_json("winemag-data-130k-v2.json")
wine_group = wine_reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

print(wine_group)

