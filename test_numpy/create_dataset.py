__author__ = 'pretymoon'

import pandas as pd
import numpy as np

df = pd.read_csv("movie_ratings_data_set.csv")

ratings_df = pd.pivot_table(df, index='user_id', columns='movie_id', aggfunc=np.max)

ratings_df.to_csv("review_matrix.csv", na_rep="")