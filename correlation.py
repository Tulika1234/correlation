import csv
import plotly.express as plt

with open ("cups of coffee vs hours of sleep.csv") as f:
  fig = plt.scatter(x= "Coffee in ml", y= "sleep in hours", size = "sleep in hours")
  fig.show()
