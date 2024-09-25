import pandas as pd

wine_reviews = pd.read_json("winemag-data-130k-v2.json")
print(wine_reviews.country.unique())
