__author__ = 'pretymoon'
import numpy as np
import pandas
import os
import webbrowser

ratings = np.array([1,2,3])
ratings *= 2
print(ratings)

data_table = pandas.read_csv("C:\\projects\\dataIncubator - challenge\\Q2\\CollegeScorecard_Raw_Data\\MERGED1996_97_PP.csv")
html = data_table[0:50].to_html()
with open("data.html","w") as f:
    f.write(html)
full_filename = os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))