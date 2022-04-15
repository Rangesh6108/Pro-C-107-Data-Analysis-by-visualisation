import pandas as pd
import plotly.graph_objects as go

readFile = pd.read_csv('data.csv')
graph = go.Figure(go.Funnel(x = readFile.groupby('level')['attempt'].mean(), y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation = 'h'))
graph.show()