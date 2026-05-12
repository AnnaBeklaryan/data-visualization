from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div("▶", className="brand-icon"),
                            width="auto"
                        ),
                        dbc.Col(
                            html.Div("Play Store Dashboard", className="brand-text"),
                            width="auto"
                        ),
                    ],
                    align="center",
                    className="g-2",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),

            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Overview", href="/overview", active="exact"),
                    dbc.NavLink("Popularity", href="/popularity", active="exact"),
                    dbc.NavLink("Ratings & Pricing", href="/ratings-pricing", active="exact"),
                ],
                pills=True,
                className="ms-auto nav-links"
            ),
        ],
        fluid=True
    ),
    className="top-navbar"
)

app.layout = html.Div(
    [
        navbar,
        html.Div(page_container, className="page-content")
    ]
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)