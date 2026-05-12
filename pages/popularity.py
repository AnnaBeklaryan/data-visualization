import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from utils import load_data

dash.register_page(__name__, path="/popularity")

df = load_data()

layout = html.Div([
    html.H2("Popularity", className="dashboard-title"),
    html.P(
        "Explore installs and reviews across app categories.",
        className="dashboard-subtitle"
    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Select Category"),
                    dcc.Dropdown(
                        id="pop-category-dropdown",
                        options=[{"label": c, "value": c} for c in sorted(df["Category"].unique())],
                        value=None,
                        placeholder="All categories"
                    )
                ]),
                className="dashboard-card"
            ),
            md=6
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Minimum Rating"),
                    dcc.Slider(
                        id="pop-rating-slider",
                        min=1,
                        max=5,
                        step=0.5,
                        value=3.5,
                        marks={i: str(i) for i in range(1, 6)}
                    )
                ]),
                className="dashboard-card"
            ),
            md=6
        ),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="installs-chart"), md=6),
        dbc.Col(dcc.Graph(id="reviews-chart"), md=6),
    ])
])

@callback(
    Output("installs-chart", "figure"),
    Output("reviews-chart", "figure"),
    Input("pop-category-dropdown", "value"),
    Input("pop-rating-slider", "value")
)
def update_popularity(selected_category, min_rating):
    filtered = df[df["Rating"] >= min_rating].copy()

    if selected_category:
        filtered = filtered[filtered["Category"] == selected_category]

    installs_df = (
        filtered.groupby("Category", as_index=False)["Installs"]
        .sum()
        .sort_values("Installs", ascending=False)
    )

    reviews_df = (
        filtered.groupby("Category", as_index=False)["Reviews"]
        .sum()
        .sort_values("Reviews", ascending=False)
    )

    fig1 = px.bar(
        installs_df.head(10),
        x="Category",
        y="Installs",
        title="Top Categories by Total Installs"
    )
    fig1.update_layout(xaxis_tickangle=-30)

    fig2 = px.bar(
        reviews_df.head(10),
        x="Category",
        y="Reviews",
        title="Top Categories by Total Reviews"
    )
    fig2.update_layout(xaxis_tickangle=-30)

    return fig1, fig2