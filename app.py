from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container(
    [
        html.H1("Google Play Store Dashboard", className="dashboard-title"),
        html.P(
            "Interactive dashboard for exploring app categories, popularity, ratings, and pricing.",
            className="dashboard-subtitle"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/", active="exact"),
                dbc.NavLink("Popularity", href="/popularity", active="exact"),
                dbc.NavLink("Ratings & Pricing", href="/ratings-pricing", active="exact"),
            ],
            pills=True,
            className="mb-4"
        ),
        page_container
    ],
    fluid=True,
    className="main-container"
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)