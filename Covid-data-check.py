import pandas as pd
import plotly.express as px
df = pd.read_csv("covidata.csv")
fig = px.line(df,x = "country",y = "cases", color = "country",title = "cases" )
fig.show()