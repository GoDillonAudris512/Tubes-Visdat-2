from dash import Input, Output, State, html
import dash
from components.visualizations import (
    create_layoffs_trend,
    create_industry_chart,
    create_companies_chart,
    create_country_map,
)
from components.ui import create_kpi_cards
from components.data_processor import apply_filters


def register_callbacks(app, df):
    """
    Mendaftarkan semua callbacks ke aplikasi Dash

    Args:
        app (Dash): Aplikasi Dash
        df (DataFrame): DataFrame berisi data layoffs
    """

    # Callback untuk menyimpan filter
    @app.callback(
        Output("filter-store", "data"),
        [Input("apply-filter-btn", "n_clicks")],
        [
            State("year-slider", "value"),
            State("industry-dropdown", "value"),
            State("country-dropdown", "value"),
        ],
        prevent_initial_call=True,
    )
    def store_filters(n_clicks, year_range, industries, countries):
        """Menyimpan filter yang dipilih"""
        if n_clicks is None:
            return dash.no_update

        years = list(range(year_range[0], year_range[1] + 1))
        return {"years": years, "industries": industries, "countries": countries}

    # Callback untuk tab switching
    @app.callback(
        [
            Output("tab-1-btn", "className"),
            Output("tab-2-btn", "className"),
            Output("tab-1-content", "className"),
            Output("tab-2-content", "className"),
            Output("active-tab", "data"),
        ],
        [Input("tab-1-btn", "n_clicks"), Input("tab-2-btn", "n_clicks")],
        [State("active-tab", "data")],
    )
    def switch_tab(tab1_clicks, tab2_clicks, active_tab):
        """Switch between tabs"""
        ctx = dash.callback_context
        if not ctx.triggered:
            return (
                "px-4 py-2 mr-2 tab-selected",  # tab-1-btn class
                "px-4 py-2 tab-normal",  # tab-2-btn class
                "block",  # tab-1-content class
                "hidden",  # tab-2-content class
                "tab-1",  # active-tab data
            )

        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "tab-1-btn":
            return (
                "px-4 py-2 mr-2 tab-selected",  # tab-1-btn class
                "px-4 py-2 tab-normal",  # tab-2-btn class
                "block",  # tab-1-content class
                "hidden",  # tab-2-content class
                "tab-1",  # active-tab data
            )
        else:
            return (
                "px-4 py-2 mr-2 tab-normal",  # tab-1-btn class
                "px-4 py-2 tab-selected",  # tab-2-btn class
                "hidden",  # tab-1-content class
                "block",  # tab-2-content class
                "tab-2",  # active-tab data
            )

    # Callback untuk update KPI cards
    @app.callback(
        Output("kpi-cards", "children"),
        [Input("filter-store", "data")],
        prevent_initial_call=False,
    )
    def update_kpi_cards(filter_data):
        """Update KPI cards berdasarkan filter"""
        if filter_data is None:
            # Default KPI cards with all data
            return create_kpi_cards(df)

        years = filter_data.get("years", None)
        industries = filter_data.get("industries", None)
        countries = filter_data.get("countries", None)

        return create_kpi_cards(df, years, industries, countries)

    # Callback untuk update filtered data stats
    @app.callback(
        Output("filtered-data-stats", "children"),
        [Input("filter-store", "data")],
        prevent_initial_call=False,
    )
    def update_filter_stats(filter_data):
        """Update statistik data terfilter"""
        if filter_data is None:
            return "Menampilkan semua data"

        filtered_df = df.copy()

        years = filter_data.get("years", None)
        industries = filter_data.get("industries", None)
        countries = filter_data.get("countries", None)

        filtered_df = apply_filters(filtered_df, years, industries, countries)

        return html.Div(
            [
                html.P(
                    f"Menampilkan {len(filtered_df)} data",
                    className="text-primary font-bold",
                ),
            ]
        )

    # Callback untuk update visualisasi
    @app.callback(
        [
            Output("layoffs-trend", "figure"),
            Output("industry-chart", "figure"),
            Output("companies-chart", "figure"),
            Output("country-map", "figure"),
            Output("data-table", "data"),
        ],
        [Input("filter-store", "data")],
        prevent_initial_call=False,
    )
    def update_visualizations(filter_data):
        """Update semua visualisasi berdasarkan filter"""
        if filter_data is None:
            # Default visualizations with all data
            return (
                create_layoffs_trend(df),
                create_industry_chart(df),
                create_companies_chart(df),
                create_country_map(df),
                df.drop(["month", "year", "month_name", "year_month"], axis=1).to_dict(
                    "records"
                ),
            )

        filtered_df = df.copy()

        years = filter_data.get("years", None)
        industries = filter_data.get("industries", None)
        countries = filter_data.get("countries", None)

        filtered_df = apply_filters(filtered_df, years, industries, countries)

        return (
            create_layoffs_trend(df, years, industries, countries),
            create_industry_chart(df, years, industries, countries),
            create_companies_chart(df, years, industries, countries),
            create_country_map(df, years, industries, countries),
            filtered_df.drop(
                ["month", "year", "month_name", "year_month"], axis=1
            ).to_dict("records"),
        )
