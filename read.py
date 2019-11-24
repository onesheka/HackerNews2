import numpy as np
import pandas as pd
def load_data():
    data = pd.read_csv("hn_stories.csv")
    data.columns = ["submission_time","upvotes", "url", "headline"]
    print(data.head())
    return data
  
load_data()

