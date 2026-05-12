import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div(
    className="home-page",
    children=[
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H1("Google Play Store Apps Dashboard", className="home-title"),
                                html.P(
                                    "Interactive dashboard for exploring app categories, popularity, ratings, installs, and pricing in the Google Play Store dataset.",
                                    className="home-subtitle"
                                ),
                                dbc.Button(
                                    "Explore Dashboard",
                                    href="/overview",
                                    color="primary",
                                    className="home-button"
                                )
                            ],
                            md=6,
                            className="home-text-col"
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("📱", className="floating-card card-1"),
                                    html.Div("📊", className="floating-card card-2"),
                                    html.Div("⭐", className="floating-card card-3"),
                                    html.Div("📈", className="floating-card card-4"),
                                    html.Div("💲", className="floating-card card-5"),
                                    html.Div("🧩", className="floating-card card-6"),
                                ],
                                className="home-visual"
                            ),
                            md=6
                        ),
                    ],
                    align="center",
                    className="home-row"
                )
            ],
            fluid=True
        )
    ]
)