import plotly.express as pe
import pandas as pd

df=pd.read_csv("covid.csv")
graph=pe.line(df,x="date",y="cases",color="Country",title="incom graph")
graph.show()