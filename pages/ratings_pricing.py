import dash
from dash import html, dcc, callback, Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px

from utils import load_data

dash.register_page(__name__, path="/ratings-pricing")

df = load_data()

layout = html.Div([
    html.H2("Ratings & Pricing", className="dashboard-title"),
    html.P(
        "Analyze ratings, installs, app type, and pricing patterns.",
        className="dashboard-subtitle"
    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("App Type"),
                    dcc.Dropdown(
                        id="rp-type-dropdown",
                        options=[{"label": t, "value": t} for t in sorted(df["Type"].unique())],
                        value=None,
                        placeholder="All types"
                    )
                ]),
                className="dashboard-card"
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Rating Range"),
                    dcc.RangeSlider(
                        id="rp-rating-range",
                        min=1,
                        max=5,
                        step=0.5,
                        value=[3, 5],
                        marks={i: str(i) for i in range(1, 6)}
                    )
                ]),
                className="dashboard-card"
            ),
            md=6
        ),
        dbc.Col(
            dbc.Button("Reset Filters", id="reset-button", color="primary", className="mt-4"),
            md=2
        )
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="rating-installs-chart"), md=8),
        dbc.Col(dcc.Graph(id="type-installs-chart"), md=4),
    ])
])

@callback(
    Output("rp-type-dropdown", "value"),
    Output("rp-rating-range", "value"),
    Input("reset-button", "n_clicks"),
    prevent_initial_call=True
)
def reset_filters(n_clicks):
    return None, [3, 5]

@callback(
    Output("rating-installs-chart", "figure"),
    Output("type-installs-chart", "figure"),
    Input("rp-type-dropdown", "value"),
    Input("rp-rating-range", "value")
)
def update_ratings_pricing(selected_type, rating_range):
    filtered = df[
        (df["Rating"] >= rating_range[0]) &
        (df["Rating"] <= rating_range[1])
    ].copy()

    if selected_type:
        filtered = filtered[filtered["Type"] == selected_type]

    fig1 = px.scatter(
        filtered,
        x="Rating",
        y="Installs",
        color="Type",
        hover_data=["App", "Category"],
        title="Rating vs Installs",
        log_y=True,
        opacity=0.6
    )

    type_installs = (
        filtered.groupby("Type", as_index=False)["Installs"]
        .sum()
    )

    fig2 = px.bar(
        type_installs,
        x="Type",
        y="Installs",
        title="Total Installs by App Type"
    )

    return fig1, fig2