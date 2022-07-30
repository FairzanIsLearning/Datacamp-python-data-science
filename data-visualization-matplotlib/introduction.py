import matplotlib.pyplot as plt
import numpy as py
import pandas as pd

seattle_weather = pd.read_csv("FairzanIsLearning/Datacamp-python-data-science/data-visualization-matplotlib/seattle_weather.csv")
austin_weather = pd.read_csv("FairzanIsLearning/Datacamp-python-data-science/data-visualization-matplotlib/austin_weather.csv")

fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

plt.show()