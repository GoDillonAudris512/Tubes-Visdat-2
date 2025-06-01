from dash import Input, Output, State, html
import dash
from components.visualizations import (
    create_layoffs_trend,
    create_industry_chart,
    create_country_map,
    create_treemap,
)
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

    # # Callback untuk update filtered data stats
    # @app.callback(
    #     Output("filtered-data-stats", "children"),
    #     [Input("filter-store", "data")],
    #     prevent_initial_call=False,
    # )
    # def update_filter_stats(filter_data):
    #     """Update statistik data terfilter"""
    #     if filter_data is None:
    #         return "Menampilkan semua data"

    #     filtered_df = df.copy()

    #     years = filter_data.get("years", None)
    #     industries = filter_data.get("industries", None)
    #     countries = filter_data.get("countries", None)

    #     filtered_df = apply_filters(filtered_df, years, industries, countries)

    #     return html.Div(
    #         [
    #             html.P(
    #                 f"Menampilkan {len(filtered_df)} data",
    #                 className="text-primary font-bold",
    #             ),
    #         ]
    #     )

    # Callback untuk update visualisasi
    @app.callback(
        [
            Output("layoffs-trend", "figure"),
            Output("country-map", "figure"),
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
                create_country_map(df),
            )

        filtered_df = df.copy()

        years = filter_data.get("years", None)
        industries = filter_data.get("industries", None)
        countries = filter_data.get("countries", None)

        filtered_df = apply_filters(filtered_df, years, industries, countries)

        return (
            create_layoffs_trend(df, years, industries, countries),
            create_country_map(df, years, industries, countries),
        )

    # Callback untuk treemap
    @app.callback(
        Output("treemap-chart", "figure"),
        [Input("filter-store", "data")],
        prevent_initial_call=False,
    )
    def update_treemap(filter_data):
        """Update treemap berdasarkan filter"""
        if filter_data is None:
            # Default treemap with all data
            return create_treemap(df)

        years = filter_data.get("years", None)
        industries = filter_data.get("industries", None)
        countries = filter_data.get("countries", None)

        return create_treemap(df, years, industries, countries)
