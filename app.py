import pandas as pd 
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

fig = px.line(df, x="date", y="sales", color="region",
              title="Sales of Pink Morsels Over Time")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )

])

if __name__ == "__main__":
    app.run(debug=True)