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
                        "Layoffs Proportion",
                        className="text-2xl font-bold text-[#E4A959] px-4",
                    ),
                    dcc.Graph(
                        id="treemap-chart",
                        className="w-full py-0 px-2 rounded-lg shadow-lg",
                    ),
                ],
                className="w-full p-6 rounded-lg shadow-lg",
            ),
        ],
        className="w-7/12",
    )

    layout = html.Div(
        [
            # Header
            create_header(),
            # Main Content
            html.Div(
                [
                    # KPI Cards
                    html.Div(id="statistics"),
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
                                                                        className="rounded-lg shadow-custom card-hover p-2 bg-[#ffffff] mb-6 w-2/3",
                                                                    ),
                                                                    html.Div(
                                                                        [
                                                                            create_filters(
                                                                                available_years,
                                                                                available_industries,
                                                                                available_countries,
                                                                            ),
                                                                        ],
                                                                        className="px-2 w-1/4",
                                                                    ),
                                                                ],
                                                                className="flex flex-wrap justify-center gap-4",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.Div(
                                                                        dcc.Graph(
                                                                            id="layoffs-trend"
                                                                        ),
                                                                        className="rounded-lg shadow-custom card-hover bg-[#1F1F43] mb-6 w-5/12",
                                                                    ),
                                                                    treemap,
                                                                ],
                                                                className="flex flex-wrap justify-center w-full",
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

    layout = html.Div(
        [
            # Header
            create_header(),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(id="statistics"),
                            html.Div(
                                [
                                    create_filters(
                                        available_years,
                                        available_industries,
                                        available_countries,
                                    ),
                                ],
                                className="w-full px-4",
                            ),
                        ],
                        className="w-1/5"
                    ),
                    html.Div(
                        [
                            html.Div(
                                dcc.Graph(
                                    id="country-map"
                                ),
                                className="w-full",
                            ),
                            html.Div(
                                dcc.Graph(
                                    id="layoffs-trend"
                                ),
                                className="",
                            ),
                            treemap,
                        ],
                        className="w-4/5 h-screen overflow-y-scroll",
                    )
                ],
                className="flex w-full pt-4",
            ),

            # Store untuk menyimpan state filter
            dcc.Store(id="filter-store"),
            dcc.Store(id="active-tab", data="tab-1"),
        ],
        className="bg-[#05050F] h-screen",
    )

    return layout
