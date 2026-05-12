import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from utils import load_data

dash.register_page(__name__, path="/overview")

df = load_data()

def make_card(title, value):
    return dbc.Card(
        dbc.CardBody([
            html.H5(title, className="card-title"),
            html.H3(value, className="card-value")
        ]),
        className="dashboard-card"
    )

layout = html.Div([
    html.H2("Overview", className="dashboard-title"),
    html.P(
        "General summary of the Google Play Store dataset.",
        className="dashboard-subtitle"
    ),
    dbc.Row([
        dbc.Col(make_card("Total Apps", f"{len(df):,}"), md=3),
        dbc.Col(make_card("Average Rating", f"{df['Rating'].mean():.2f}"), md=3),
        dbc.Col(make_card("Total Installs", f"{df['Installs'].sum():,}"), md=3),
        dbc.Col(make_card("Free Apps Share", f"{(df['Type'].eq('Free').mean()*100):.1f}%"), md=3),
    ], className="mb-4"),

    dbc.Card(
        dbc.CardBody([
            html.Label("Select Category"),
            dcc.Dropdown(
                id="overview-category-dropdown",
                options=[{"label": c, "value": c} for c in sorted(df["Category"].unique())],
                value=None,
                placeholder="All categories"
            )
        ]),
        className="dashboard-card mb-4"
    ),

    dbc.Row([
        dbc.Col(dcc.Graph(id="overview-category-chart"), md=6),
        dbc.Col(dcc.Graph(id="overview-type-chart"), md=6),
    ])
])

@callback(
    Output("overview-category-chart", "figure"),
    Output("overview-type-chart", "figure"),
    Input("overview-category-dropdown", "value")
)
def update_overview(selected_category):
    filtered = df.copy()

    if selected_category:
        filtered = filtered[filtered["Category"] == selected_category]

    category_counts = filtered["Category"].value_counts().reset_index()
    category_counts.columns = ["Category", "Count"]

    fig1 = px.bar(
        category_counts.head(10),
        x="Category",
        y="Count",
        title="Top Categories by Number of Apps"
    )
    fig1.update_layout(xaxis_tickangle=-30)

    type_counts = filtered["Type"].value_counts().reset_index()
    type_counts.columns = ["Type", "Count"]

    fig2 = px.pie(
        type_counts,
        names="Type",
        values="Count",
        title="Free vs Paid Apps"
    )

    return fig1, fig2