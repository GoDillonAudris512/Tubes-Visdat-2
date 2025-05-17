from dash import html, dcc
from components.data_processor import apply_filters


def create_header():
    """
    Membuat komponen header aplikasi

    Returns:
        Component: Komponen Dash header
    """
    header = html.Nav(
        html.Div(
            [
                html.A(
                    html.Div(
                        [
                            html.Div(
                                html.Img(
                                    src="https://img.icons8.com/fluency/48/null/organization-chart-people.png",
                                    className="h-8 w-auto",
                                ),
                                className="flex-shrink-0",
                            ),
                            html.Div(
                                html.H1(
                                    "Dashboard Visualisasi Data Layoffs",
                                    className="text-xl text-blue-500 font-semibold",
                                ),
                                className="ml-2",
                            ),
                        ],
                        className="flex items-center",
                    ),
                    href="#",
                    className="text-white",
                ),
            ],
            className="container mx-auto px-4",
        ),
        className="bg-primary text-white py-4 mb-6 shadow-md",
    )

    return header


def create_filters(available_years, available_industries, available_countries):
    """
    Membuat komponen filter

    Args:
        available_years (list): Daftar tahun yang tersedia
        available_industries (list): Daftar industri yang tersedia
        available_countries (list): Daftar negara yang tersedia

    Returns:
        Component: Komponen Dash card berisi filter
    """
    filters = html.Div(
        html.Div(
            [
                html.H4("Filter Data", className="text-lg font-semibold mb-3"),
                html.Hr(className="mb-4"),
                # Year Filter
                html.Div(
                    [
                        html.Label(
                            "Pilih Tahun:", className="block text-sm font-medium mb-1"
                        ),
                        dcc.RangeSlider(
                            id="year-slider",
                            min=min(available_years),
                            max=max(available_years),
                            value=[min(available_years), max(available_years)],
                            marks={str(year): str(year) for year in available_years},
                            step=None,
                            className="mb-1",
                        ),
                    ],
                    className="mb-4",
                ),
                # Industry Filter
                html.Div(
                    [
                        html.Label(
                            "Pilih Industri:",
                            className="block text-sm font-medium mb-1",
                        ),
                        dcc.Dropdown(
                            id="industry-dropdown",
                            options=[
                                {"label": i, "value": i} for i in available_industries
                            ],
                            multi=True,
                            placeholder="Pilih industri...",
                            className="mb-1",
                        ),
                    ],
                    className="mb-4",
                ),
                # Country Filter
                html.Div(
                    [
                        html.Label(
                            "Pilih Negara:", className="block text-sm font-medium mb-1"
                        ),
                        dcc.Dropdown(
                            id="country-dropdown",
                            options=[
                                {"label": c, "value": c} for c in available_countries
                            ],
                            multi=True,
                            placeholder="Pilih negara...",
                            className="mb-1",
                        ),
                    ],
                    className="mb-4",
                ),
                # Apply Filters Button
                html.Div(
                    [
                        html.Button(
                            "Terapkan Filter",
                            id="apply-filter-btn",
                            className="bg-primary bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded w-full",
                        ),
                        html.Div(id="filtered-data-stats", className="mt-3"),
                    ]
                ),
            ],
            className="p-4",
        ),
        className="bg-white rounded-lg shadow-custom card-hover mb-6",
    )

    return filters


def create_kpi_cards(
    df, selected_years=None, selected_industries=None, selected_countries=None
):
    """
    Membuat KPI cards

    Args:
        df (DataFrame): DataFrame berisi data layoffs
        selected_years (list): Daftar tahun yang dipilih
        selected_industries (list): Daftar industri yang dipilih
        selected_countries (list): Daftar negara yang dipilih

    Returns:
        Component: Komponen Dash row berisi KPI cards
    """
    # Apply filters to get filtered dataframe
    filtered_df = apply_filters(
        df, selected_years, selected_industries, selected_countries
    )

    # Calculate metrics
    total_companies = filtered_df["company"].nunique()
    total_layoffs = filtered_df["total_laid_off"].sum()
    total_records = len(filtered_df)
    avg_layoffs = filtered_df["total_laid_off"].mean()

    # Create KPI cards
    kpi_cards = html.Div(
        [
            html.Div(
                html.Div(
                    [
                        html.H6(
                            "Total Perusahaan",
                            className="text-sm text-gray-500 uppercase tracking-wider",
                        ),
                        html.H3(
                            f"{total_companies:,}",
                            className="text-2xl font-bold text-primary mt-2",
                        ),
                    ],
                    className="p-4 text-center",
                ),
                className="bg-white rounded-lg shadow-custom card-hover",
            ),
            html.Div(
                html.Div(
                    [
                        html.H6(
                            "Total Karyawan di-PHK",
                            className="text-sm text-gray-500 uppercase tracking-wider",
                        ),
                        html.H3(
                            f"{total_layoffs:,.0f}",
                            className="text-2xl font-bold text-danger mt-2",
                        ),
                    ],
                    className="p-4 text-center",
                ),
                className="bg-white rounded-lg shadow-custom card-hover",
            ),
            html.Div(
                html.Div(
                    [
                        html.H6(
                            "Total Data",
                            className="text-sm text-gray-500 uppercase tracking-wider",
                        ),
                        html.H3(
                            f"{total_records:,}",
                            className="text-2xl font-bold text-success mt-2",
                        ),
                    ],
                    className="p-4 text-center",
                ),
                className="bg-white rounded-lg shadow-custom card-hover",
            ),
            html.Div(
                html.Div(
                    [
                        html.H6(
                            "Rata-rata PHK",
                            className="text-sm text-gray-500 uppercase tracking-wider",
                        ),
                        html.H3(
                            f"{avg_layoffs:,.0f}",
                            className="text-2xl font-bold text-info mt-2",
                        ),
                    ],
                    className="p-4 text-center",
                ),
                className="bg-white rounded-lg shadow-custom card-hover",
            ),
        ],
        className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6",
    )

    return kpi_cards


def create_footer():
    """
    Membuat komponen footer aplikasi

    Returns:
        Component: Komponen Dash footer
    """
    footer = html.Footer(
        [
            html.Hr(className="my-6"),
            html.P(
                "Dashboard ini dibuat menggunakan Dash by Plotly untuk visualisasi dataset layoffs.",
                className="text-center text-gray-500 text-sm",
            ),
        ],
        className="mt-12",
    )

    return footer
