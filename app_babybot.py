import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

# USERNAME_PASSWORD_PAIRS = [["Bimbim", ""], ["username", "password"]]

df = pd.read_csv("C:/Users/Olabisi Oremade/Desktop/QU/df2babybot.csv")

print(df.head(10))

app = dash.Dash()
server= app.server

app.layout = html.Div(
    [
        html.Div([dcc.Graph(id="our_graph")]),
        html.Div(
            [
                html.Br(),
                html.Label(
                    ["Choose continent to compare:"],
                    style={"font-weight": "bold", "text-align": "center"},
                ),
                dcc.Dropdown(
                    id="Continents",
                    options=[
                        {"label": x, "value": x}
                        for x in df.sort_values("continent")["continent"].unique()
                    ],
                    value="African",
                    multi=False,
                    disabled=False,
                    clearable=True,
                    searchable=True,
                    placeholder="Choose continent...",
                    className="form-dropdown",
                    style={"width": "90%"},
                    persistence="string",
                    persistence_type="memory",
                ),
            ]
        ),
    ]
)


@app.callback(Output("our_graph", "figure"), [Input("Continents", "value")])
def update_figure(selected_continent):

    dff = df[(df["continent"] == selected_continent)]
    print(dff[:10])

    fig = px.line(dff, x="country", y="prevalence", color="continent", height=600)
    fig.update_layout(
        yaxis={"title": "Prevalence (%)"},
        xaxis={"title": "Countries"},
        title={
            "text": "Countries with depression in 2022",
            "font": {"size": 28},
            "x": 0.5,
            "xanchor": "center",
        },
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
