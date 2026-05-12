# Data Visualization Project

This project analyzes the Google Play Store Apps dataset as part of a data visualization course project.

## Dataset Source
Google Play Store Apps dataset:  
https://www.kaggle.com/datasets/lava18/google-play-store-apps

## Project Contents

### 1. Exploratory Data Analysis (EDA)
Initial exploration of the dataset, including:
- dataset structure
- missing values
- outliers
- distributions
- early visualizations

### 2. Story & Insights
A more focused analysis using interactive Plotly visualizations to identify the main patterns in the data and prepare for the final dashboard.

### 3. Dashboard Draft
A multi-page interactive dashboard built with Dash.  
The dashboard is based on the insights from the previous assignments and allows users to explore app categories, popularity, ratings, installs, and pricing.

## Main Focus

The project explores app categories, popularity, ratings, and pricing in order to better understand the structure of the Google Play Store and support the design of an interactive dashboard.

## Dashboard Pages

The dashboard includes the following pages:

- **Home** — landing page with project introduction
- **Overview** — general summary of the dataset with KPI cards and category-level insights
- **Popularity** — analysis of installs and reviews across app categories
- **Ratings & Pricing** — analysis of ratings, app type, installs, and pricing patterns

## Dashboard Features

The dashboard includes:
- multi-page navigation
- interactive dropdowns
- sliders and range sliders
- buttons
- Plotly charts
- Dash callbacks for dynamic updates
- card-based layout and custom styling

## How to Run the Dashboard

1. Clone the repository:

```bash
git clone https://github.com/AnnaBeklaryan/data-visualization.git
cd data-visualization
```

2. Install the required packages:
   
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
   
```bash
python app.py
```

4. Open the local link shown in the terminal, usually:
```bash
http://127.0.0.1:8050/  
```

## Project Structure

```bash
data-visualization/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── pages/
│   ├── home.py
│   ├── overview.py
│   ├── popularity.py
│   └── ratings_pricing.py
│
├── notebooks/
│   ├── playstore_eda.ipynb
│   └── playstore_story_insights.ipynb
│
├── data/
│   └── raw/
│       ├── googleplaystore.csv
│       └── googleplaystore_user_reviews.csv
```
