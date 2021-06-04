from google.colab import files
uploaded=files.upload()

import csv
import pandas as pd
import plotly.express as px

df=pd.read_csv("GRE.csv")
TOEFL=df["TOEFL Score"].tolist()
chance=df["Chance of Admit "].tolist()
fig=px.scatter(x=TOEFL,y=chance)
fig.show()

import numpy as np
m,c=np.polyfit(TOEFL,chance,1)
y=[]
for x in TOEFL:
  y_value=m*x+c
  y.append(y_value)

fig=px.scatter(x=TOEFL,y=chance)
fig.update_layout(shapes=[
                          dict(
                              type="line",x0=min(TOEFL),x1=max(TOEFL),y0=min(y),y1=max(y)
                          )
                          ])

fig.show()

x=900
y=m*x+c
print(f"Chance of Admit Based on TOEFL Score {x} is {y}")