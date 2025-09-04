# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

the_90s = netflix_df[netflix_df["release_year"].between(1990, 1999)]
plt.hist(the_90s["duration"])
plt.show()

action = the_90s[the_90s["genre"] == "Action"]
short_movie_count = 0
for lab, row in action.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1
print(short_movie_count)