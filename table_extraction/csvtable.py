# read a .csv from  url using pandas

import pandas as pd

# reading 1 csv file from the website
dt_premier21 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")

# showning dataframe
print(dt_premier21)

# rename columns
dt_premier21.rename(columns = {'FTHG' : 'home_goals','FTAG' : 'away_goals'}, inplace='True')

print(dt_premier21)
