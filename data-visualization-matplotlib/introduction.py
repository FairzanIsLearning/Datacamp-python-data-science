#%%
# we are now importing the libraries and file required for this analysis
from calendar import calendar
import matplotlib.pyplot as plt
import numpy as py
import pandas as pd
import calendar

seattle_weather = pd.read_csv("seattle_weather.csv")
austin_weather = pd.read_csv("austin_weather.csv")


#%%
# We need to modify the csv file a bit to suit it with the analysis

# first, we need to select specific location for seattle
seattle_weather.set_index("NAME", inplace=True)
seattle_weather = seattle_weather.loc[['SEATTLE TACOMA INTERNATIONAL AIRPORT, WA US']]


# then, the modification about the month
seattle_weather = seattle_weather[['NAME', 'DATE', 'MLY-PRCP-NORMAL']]
seattle_weather_month = seattle_weather["DATE"].astype(int)
# seattle_weather_month = slice(seattle_weather_month)
# seattle_weather_month = calendar.month_name[seattle_weather_month]
austin_weather = austin_weather[['NAME', 'DATE', 'MLY-PRCP-NORMAL']]
austin_weather_month = austin_weather["DATE"].astype(int)


#%%
fig, ax = plt.subplots()
ax.plot(seattle_weather_month, seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather_month, austin_weather["MLY-PRCP-NORMAL"])

plt.show()

#%%



