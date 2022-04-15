import pandas as pd
import plotly.graph_objects as go

dataFrame = pd.read_csv('data.csv')
studentDataframe = dataFrame.loc[dataFrame['student_id'] == 'TRL_987']
graph = go.Figure(go.Funnel(x = studentDataframe.groupby('level')['attempt'].mean(), y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation = 'h'))
graph.show()