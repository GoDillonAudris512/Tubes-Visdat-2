import dash
from dash import Dash
import warnings

# Filter warning dari Plotly
warnings.filterwarnings("ignore", category=FutureWarning, module="_plotly_utils")

# Import konfigurasi
from config import APP_TITLE, DATA_PATH

# Import komponen
from components.data_processor import load_data, get_filter_options
from components.layout import create_layout
from components.callbacks import register_callbacks

# Inisialisasi app tanpa Bootstrap
external_scripts = [{"src": "https://cdn.tailwindcss.com"}]

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_scripts=external_scripts,
)

# Konfigurasi aplikasi
app.title = APP_TITLE
server = app.server

# Load data
df = load_data()

# Dapatkan opsi filter
available_years, available_industries, available_countries = get_filter_options(df)

# Setup layout
app.layout = create_layout(
    df, available_years, available_industries, available_countries
)

# Daftarkan callbacks
register_callbacks(app, df)

# Run server
if __name__ == "__main__":
    app.run_server(debug=True)
