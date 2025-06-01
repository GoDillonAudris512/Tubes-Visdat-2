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

    # Card untuk Layoffs Trend
    layoffs_trend_card = html.Div(
        [
            html.H3(
                "Tren Lay-Off dari Waktu ke Waktu",
                className="text-2xl font-bold text-[#E4A959] px-4 mb-2",
            ),
            dcc.Graph(
                id="layoffs-trend",
                className="w-full rounded-lg",
            ),
        ],
        className="w-1/2 bg-[#1F1F43] rounded-lg shadow-custom card-hover p-6 mx-2",
    )

    # Card untuk Treemap
    treemap_card = html.Div(
        [
            html.H3(
                "Proposi Lay-Off",
                className="text-2xl font-bold text-[#E4A959] px-4 mb-2",
            ),
            dcc.Graph(
                id="treemap-chart",
                className="w-full rounded-lg",
            ),
        ],
        className="w-1/2 bg-[#1F1F43] rounded-lg shadow-custom card-hover p-6 mx-2",
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
                        className="w-1/5",
                    ),
                    html.Div(
                        [
                            html.Div(
                                dcc.Graph(id="country-map"),
                                className="w-full mb-6",
                            ),
                            html.Div(
                                [
                                    layoffs_trend_card,
                                    treemap_card,
                                ],
                                className="flex flex-row w-full justify-between items-stretch mb-6",
                            ),
                        ],
                        className="w-4/5 h-screen overflow-y-scroll",
                    ),
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
