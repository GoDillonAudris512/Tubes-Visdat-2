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
                                                                        className="bg-white rounded-lg shadow-custom card-hover p-4 mb-6",
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
                                                                        className=" bg-white rounded-lg shadow-custom card-hover p-4 mb-6",
                                                                    ),
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="companies-chart"
                                                                        ),
                                                                        className="bg-white rounded-lg shadow-custom card-hover p-4 ",
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
        className="min-h-screen bg-gray-50",
    )

    return layout
