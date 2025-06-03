from dash import html, dcc
from components.ui import create_filters
from components.colors import Colors


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
    # Header layout
    header = html.Nav(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                html.H1(
                                    "Global Layoffs Phenomenons",
                                    className=f"text-3xl font-bold bg-gradient-to-r from-[{Colors.GRADIENT_ORANGE_START}] to-[{Colors.GRADIENT_ORANGE_END}] bg-clip-text text-transparent py-1",
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
                    html.H6(
                        "Explore global layoff trends since 2020 — uncover which countries and industries were hit hardest, how patterns evolved over time, and the scale of their impact.",
                        className="text-sm text-white",
                    ),
                ],
                className="px-4 w-full flex-1",
            ),
            html.Div(
                html.A(
                    "Data Source",
                    href="https://www.kaggle.com/datasets/swaptr/layoffs-2022",
                    className="text-white font-semibold text-sm",
                ),
                className=f"w-32 px-2 py-1 rounded-lg flex justify-center items-center text-center border-white border-2 bg-[{Colors.BG_CARD}] hover:bg-[{Colors.BG_BUTTON_HOVER}] transition duration-300 flex-shrink-0",
            ),
        ],
        className="flex flex-row py-2 bg-black px-4 items-center justify-between",
    )

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
                        className=f"text-xl bg-gradient-to-r from-[{Colors.GRADIENT_BLUE_START}] to-[{Colors.GRADIENT_BLUE_END}] bg-clip-text text-transparent font-bold",
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
                                className=f"text-[14px] text-[{Colors.STAT_EMPLOYEE}]",
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
                                className=f"text-[14px] text-[{Colors.STAT_COMPANY}]",
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
                                className=f"text-[14px] text-[{Colors.STAT_COUNTRY}]",
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
        className="justify-left mb-2 px-4",
    )

    # Card untuk Country Map (tanpa judul di dalamnya)
    country_map_card = html.Div(
        [
            dcc.Graph(
                id="country-map",
                className="w-full rounded-lg",
            ),
        ],
        className=f"w-full mb-6 bg-[{Colors.BG_CARD}] rounded-lg shadow-custom card-hover",
    )

    # Card untuk Layoffs Trend (tanpa judul di dalamnya)
    layoffs_trend_card = html.Div(
        [
            dcc.Graph(
                id="layoffs-trend",
                className="w-full rounded-lg",
            ),
        ],
        className=f"w-1/2 bg-[{Colors.BG_CARD}] rounded-lg shadow-custom card-hover mr-2",
    )

    # Card untuk Treemap (tanpa judul di dalamnya)
    treemap_card = html.Div(
        [
            dcc.Graph(
                id="treemap-chart",
                className="w-full rounded-lg",
            ),
        ],
        className=f"w-1/2 bg-[{Colors.BG_CARD}] rounded-lg shadow-custom card-hover ml-2",
    )

    layout = html.Div(
        [
            # Header
            header,
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
                                className="w-full px-2",
                            ),
                        ],
                        className="w-1/5 min-w-0 overflow-y-auto max-h-[88vh] pb-4",
                    ),
                    html.Div(
                        [
                            # Judul di luar card country map
                            html.Div(
                                [
                                    html.Div(
                                        "Layoff Rate Around the World",
                                        className=f"text-2xl font-bold text-[{Colors.SECTION_TITLE}] mb-2 text-left w-full px-2",
                                    ),
                                ],
                                className="flex flex-row w-full justify-between items-end",
                            ),
                            html.Div(
                                [
                                    # Card untuk Country Map
                                    country_map_card,
                                ],
                                className="flex flex-row w-full justify-between items-stretch px-2",
                            ),
                            # Judul di luar card tren dan treemap
                            html.Div(
                                [
                                    html.Div(
                                        "Timely Layoffs Trend",
                                        className=f"text-2xl font-bold text-[{Colors.SECTION_TITLE}] mb-2 text-left w-1/2 px-2",
                                    ),
                                    html.Div(
                                        "Layoffs Proportion by Industry",
                                        className=f"text-2xl font-bold text-[{Colors.SECTION_TITLE}] mb-2 text-left w-1/2 px-2",
                                    ),
                                ],
                                className="flex flex-row w-full justify-between items-end",
                            ),
                            html.Div(
                                [
                                    layoffs_trend_card,
                                    treemap_card,
                                ],
                                className="flex flex-row w-full items-stretch mb-6 px-2",
                            ),
                        ],
                        className="w-4/5 h-[88vh] overflow-y-auto overflow-x-hidden min-w-0 flex-1",
                    ),
                ],
                className="flex w-full py-4 gap-4 min-h-0",
            ),
            # Store untuk menyimpan state filter
            dcc.Store(id="filter-store"),
            dcc.Store(id="active-tab", data="tab-1"),
        ],
        className=f"bg-[{Colors.BG_MAIN}] h-screen overflow-hidden",
    )

    return layout
