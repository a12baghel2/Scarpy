import pandas as pd
import json

df = pd.read_json("./books.json")

df.to_csv("./books.csv",index=False)