import pandas as pd

wine_reviews = pd.read_json("winemag-data-130k-v2.json")
wine_group = wine_reviews.groupby('points').points.count()

print(wine_group)
