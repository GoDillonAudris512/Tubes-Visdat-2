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
                html.Div(
                    [
                        html.Div(
                            html.H1(
                                "Global Layoffs Phenomenons",
                                className="text-3xl font-bold bg-gradient-to-r from-[#4CB6F0] to-[#FFA63E] bg-clip-text text-transparent py-1",
                            ),
                            className="mr-2",
                        ),
                        html.Div(
                            html.Img(
                                src="https://img.icons8.com/fluency/48/null/organization-chart-people.png",
                                className="h-10 w-auto",
                            ),
                            className="flex-shrink-0",
                        ),
                    ],
                    className="flex justify-left items-center",
                ),
            ],
            className="container px-8 w-full",
        ),
        className="py-3 bg-black",
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
                html.H4("Filter Data", className="text-xl bg-gradient-to-r from-[#4CB6F0] to-[#5D9DB8] bg-clip-text text-transparent font-bold mb-2"),
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
                            className="mb-1 mt-5",
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
                            className="mb-1 text-[#1F1F43]",

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
                            className="mb-1 text-[#1F1F43]",
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
                            className="bg-[#4DC0F4] hover:bg-blue-400 text-white font-bold py-2 px-4 rounded w-full",
                        ),
                        html.Div(id="filtered-data-stats", className="mt-3"),
                    ]
                ),
            ],
            className="p-4",
        ),
        className="text-white rounded-lg shadow-custom card-hover mb-6",
    )

    return filters

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
