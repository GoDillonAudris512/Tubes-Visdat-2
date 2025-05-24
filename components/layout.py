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
            treemap
        ],
        className="min-h-screen bg-[#05050F]",
    )

    return layout
