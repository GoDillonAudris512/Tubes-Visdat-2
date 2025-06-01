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
    # Calculate metrics
    total_records = len(df)
    total_employee_layoffs = int(df["total_laid_off"].sum())
    total_companies = df["company"].nunique()
    total_countries = df["country"].nunique()

    # Tambahkan statistik
    statistics = html.Div(
        [
            html.Div(
                [
                    html.H2(
                        "General Statistics",
                        className="text-xl bg-gradient-to-r from-[#4CB6F0] to-[#5D9DB8] bg-clip-text text-transparent font-bold",
                    ),
                    html.Hr(className="my-2 border-[#fffff]"),
                    html.H3(
                        f"{total_records:,}",
                        className="text-4xl text-white mt-2",
                    ),
                    html.H6(
                        "Number of Layoffs",
                        className="text-[12px] text-white mt-1",
                    ),
                ],
            ),
            html.Div(
                [
                    html.Div(
                        html.Img(
                            src="assets/employee_icon.png",
                            className="h-12 w-auto",
                        ),
                        className="flex-shrink-0",
                    ),
                    html.Div(
                        [
                            html.H6(
                                "Employee Laid Off",
                                className="text-[14px] text-[#7DB2BF]",
                            ),
                            html.H3(
                                f"{total_employee_layoffs:,}",
                                className="text-2xl text-white",
                            ),
                        ],
                        className="flex-col ml-3 items-center justify-center",
                    ),
                ],
                className="flex justify-left items-center pt-4",
            ),
            html.Div(
                [
                    html.Div(
                        html.Img(
                            src="assets/company_icon.png",
                            className="h-12 w-auto",
                        ),
                        className="flex-shrink-0",
                    ),
                    html.Div(
                        [
                            html.H6(
                                "Company",
                                className="text-[14px] text-[#C1AB7B]",
                            ),
                            html.H3(
                                f"{total_companies:,}",
                                className="text-2xl text-white",
                            ),
                        ],
                        className="flex-col ml-3 items-center justify-center",
                    ),
                ],
                className="flex justify-left items-center pt-4",
            ),
            html.Div(
                [
                    html.Div(
                        html.Img(
                            src="assets/country_icon.png",
                            className="h-12 w-auto",
                        ),
                        className="flex-shrink-0",
                    ),
                    html.Div(
                        [
                            html.H6(
                                "Country",
                                className="text-[14px] text-[#FAA743]",
                            ),
                            html.H3(
                                f"{total_countries:,}",
                                className="text-2xl text-white",
                            ),
                        ],
                        className="flex-col ml-3 items-center justify-center",
                    ),
                ],
                className="flex justify-left items-center pt-4",
            ),
        ],
        id="statistics",
        className="justify-left mb-2 px-8",
    )

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

    # Layout utama
    layout = html.Div(
        [
            # Header
            create_header(),
            html.Div(
                [
                    html.Div(
                        [
                            statistics,
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
