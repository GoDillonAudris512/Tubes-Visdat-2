from dash import html, dcc, dash_table
from components.ui import create_header, create_filters, create_footer


def create_layout(df, available_years, available_industries, available_countries):
    """
    Membuat layout utama aplikasi

    Args:
        df (DataFrame): DataFrame berisi data layoffs
        available_years (list): Daftar tahun yang tersedia
        available_industries (list): Daftar industri yang tersedia
        available_countries (list): Daftar negara yang tersedia

    Returns:
        Component: Layout utama aplikasi
    """
    layout = html.Div(
        [
            # Header
            create_header(),
            # Main Content
            html.Div(
                [
                    # KPI Cards
                    html.Div(id="kpi-cards"),
                    # Main content section
                    html.Div(
                        [
                            # Visualizations
                            html.Div(
                                [
                                    # Tabs for visualizations
                                    html.Div(
                                        [
                                            # Tab content
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Div(
                                                                [
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="country-map"
                                                                        ),
                                                                        className="rounded-lg shadow-custom card-hover p-4 mb-6",
                                                                    ),
                                                                    html.Div(
                                                                        [
                                                                            create_filters(
                                                                                available_years,
                                                                                available_industries,
                                                                                available_countries,
                                                                            ),
                                                                        ],
                                                                        className="w-1/3 px-2",
                                                                    ),
                                                                ],
                                                                className="flex flex-wrap  w-full",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="layoffs-trend"
                                                                        ),
                                                                        className="  rounded-lg shadow-custom card-hover p-4 mb-6",
                                                                    ),
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="companies-chart"
                                                                        ),
                                                                        className=" rounded-lg shadow-custom card-hover p-4 ",
                                                                    ),
                                                                ],
                                                                className="grid grid-cols-1 md:grid-cols-2 gap-4",
                                                            ),
                                                        ],
                                                        id="tab-1-content",
                                                        className="w-full",
                                                    ),
                                                ],
                                                id="tabs-content",
                                            ),
                                        ],
                                        id="tabs",
                                    ),
                                ],
                                className="w-full px-2",
                            ),
                        ],
                        className="flex flex-wrap -mx-2",
                    ),
                    # Footer
                    create_footer(),
                ],
                className="container mx-auto px-4",
            ),
            # Store untuk menyimpan state filter
            dcc.Store(id="filter-store"),
            dcc.Store(id="active-tab", data="tab-1"),
        ],
        className="min-h-screen bg-[#05050F]",
    )

    # Tambahkan treemap
    treemap = html.Div(
        [
            html.Div(
                [
                    html.H3(
                        "Distribusi Layoffs berdasarkan Industri dan Negara",
                        className="text-2xl font-bold text-gray-800 mb-4",
                    ),
                    dcc.Graph(
                        id="treemap-chart",
                        className="w-full h-[600px] rounded-lg shadow-lg",
                    ),
                ],
                className="w-full p-6  rounded-lg shadow-lg",
            ),
        ],
        className="w-full mb-8",
    )

    # Gabungkan semua komponen
    layout = html.Div(
        [
            # Header
            create_header(),
            # Main Content
            html.Div(
                [
                    # KPI Cards
                    html.Div(id="kpi-cards"),
                    # Main content section
                    html.Div(
                        [
                            # Filter sidebar
                            html.Div(
                                [
                                    create_filters(
                                        available_years,
                                        available_industries,
                                        available_countries,
                                    ),
                                ],
                                className="w-full md:w-1/4 px-2",
                            ),
                            # Visualizations
                            html.Div(
                                [
                                    # Tabs for visualizations
                                    html.Div(
                                        [
                                            # Tabs header
                                            html.Div(
                                                [
                                                    html.Button(
                                                        "Tren & Analisis",
                                                        id="tab-1-btn",
                                                        className="px-4 py-2 mr-2 tab-selected",
                                                        n_clicks=0,
                                                    ),
                                                    html.Button(
                                                        "Peta & Data",
                                                        id="tab-2-btn",
                                                        className="px-4 py-2 tab-normal",
                                                        n_clicks=0,
                                                    ),
                                                ],
                                                className="flex border-b mb-4",
                                            ),
                                            # Tab content
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Div(
                                                                dcc.Graph(
                                                                    id="layoffs-trend"
                                                                ),
                                                                className=" rounded-lg shadow-custom card-hover p-4 mb-6",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="industry-chart"
                                                                        ),
                                                                        className=" rounded-lg shadow-custom card-hover p-4",
                                                                    ),
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="companies-chart"
                                                                        ),
                                                                        className=" rounded-lg shadow-custom card-hover p-4",
                                                                    ),
                                                                ],
                                                                className="grid grid-cols-1 md:grid-cols-2 gap-4",
                                                            ),
                                                        ],
                                                        id="tab-1-content",
                                                        className="block",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.Div(
                                                                dcc.Graph(
                                                                    id="country-map"
                                                                ),
                                                                className=" rounded-lg shadow-custom card-hover p-4 mb-6",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.H4(
                                                                        "Data Lengkap",
                                                                        className="text-xl font-semibold mb-4",
                                                                    ),
                                                                    dash_table.DataTable(
                                                                        id="data-table",
                                                                        columns=[
                                                                            {
                                                                                "name": i,
                                                                                "id": i,
                                                                            }
                                                                            for i in df.drop(
                                                                                [
                                                                                    "month",
                                                                                    "year",
                                                                                    "month_name",
                                                                                    "year_month",
                                                                                ],
                                                                                axis=1,
                                                                            ).columns
                                                                        ],
                                                                        page_size=10,
                                                                        style_header={
                                                                            "backgroundColor": "#2C3E50",
                                                                            "color": "white",
                                                                            "fontWeight": "bold",
                                                                            "padding": "12px 15px",
                                                                        },
                                                                        style_data={
                                                                            "whiteSpace": "normal",
                                                                            "height": "auto",
                                                                            "padding": "10px 15px",
                                                                        },
                                                                        style_cell={
                                                                            "fontFamily": "Open Sans, sans-serif",
                                                                            "textAlign": "left",
                                                                        },
                                                                        style_data_conditional=[
                                                                            {
                                                                                "if": {
                                                                                    "row_index": "odd"
                                                                                },
                                                                                "backgroundColor": "#f8f9fa",
                                                                            }
                                                                        ],
                                                                        filter_action="native",
                                                                        sort_action="native",
                                                                    ),
                                                                ],
                                                                className="bg-white rounded-lg shadow-custom card-hover p-4",
                                                            ),
                                                        ],
                                                        id="tab-2-content",
                                                        className="hidden",
                                                    ),
                                                ],
                                                id="tabs-content",
                                            ),
                                        ],
                                        id="tabs",
                                    ),
                                ],
                                className="w-full md:w-3/4 px-2",
                            ),
                        ],
                        className="flex flex-wrap -mx-2",
                    ),
                    # Footer
                    create_footer(),
                ],
                className="container mx-auto px-4",
            ),
            # Store untuk menyimpan state filter
            dcc.Store(id="filter-store"),
            dcc.Store(id="active-tab", data="tab-1"),
            treemap,
        ],
        className="min-h-screen bg-[#05050F]",
    )

    return layout
