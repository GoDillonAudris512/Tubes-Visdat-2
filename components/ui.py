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

    # Calculate metrics
    total_records = len(df)
    total_employee_layoffs = int(df["total_laid_off"].sum())
    total_companies = df["company"].nunique()
    total_countries = df["country"].nunique()

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
    # # Create KPI cards
    # kpi_cards = html.Div(
    #     [
    #         html.Div(
    #             html.Div(
    #                 [
    #                     html.H6(
    #                         "Total Perusahaan",
    #                         className="text-sm text-gray-500 uppercase tracking-wider",
    #                     ),
    #                     html.H3(
    #                         f"{total_companies:,}",
    #                         className="text-2xl font-bold text-primary mt-2",
    #                     ),
    #                 ],
    #                 className="p-4 text-center",
    #             ),
    #             className="  rounded-lg shadow-custom card-hover",
    #         ),
    #         html.Div(
    #             html.Div(
    #                 [
    #                     html.H6(
    #                         "Total Karyawan di-PHK",
    #                         className="text-sm text-gray-500 uppercase tracking-wider",
    #                     ),
    #                     html.H3(
    #                         f"{total_layoffs:,.0f}",
    #                         className="text-2xl font-bold text-danger mt-2",
    #                     ),
    #                 ],
    #                 className="p-4 text-center",
    #             ),
    #             className="  rounded-lg shadow-custom card-hover",
    #         ),
    #         html.Div(
    #             html.Div(
    #                 [
    #                     html.H6(
    #                         "Total Data",
    #                         className="text-sm text-gray-500 uppercase tracking-wider",
    #                     ),
    #                     html.H3(
    #                         f"{total_records:,}",
    #                         className="text-2xl font-bold text-success mt-2",
    #                     ),
    #                 ],
    #                 className="p-4 text-center",
    #             ),
    #             className="  rounded-lg shadow-custom card-hover",
    #         ),
    #         html.Div(
    #             html.Div(
    #                 [
    #                     html.H6(
    #                         "Rata-rata PHK",
    #                         className="text-sm text-gray-500 uppercase tracking-wider",
    #                     ),
    #                     html.H3(
    #                         f"{avg_layoffs:,.0f}",
    #                         className="text-2xl font-bold text-info mt-2",
    #                     ),
    #                 ],
    #                 className="p-4 text-center",
    #             ),
    #             className="  rounded-lg shadow-custom card-hover",
    #         ),
    #     ],
    #     className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6",
    # )

    return statistics


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
