import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from components.colors import Colors


def create_layoffs_trend(
    df, selected_years=None, selected_industries=None, selected_countries=None
):
    """
    Membuat visualisasi tren layoffs per bulan

    Args:
        df (DataFrame): DataFrame berisi data layoffs
        selected_years (list): Daftar tahun yang dipilih
        selected_industries (list): Daftar industri yang dipilih
        selected_countries (list): Daftar negara yang dipilih

    Returns:
        Figure: Objek Figure Plotly
    """
    from components.data_processor import apply_filters

    # Apply filters
    filtered_df = apply_filters(
        df, selected_years, selected_industries, selected_countries
    )

    # Group by year and month
    monthly_data = (
        filtered_df.groupby("year_month")
        .agg(total_layoffs=("total_laid_off", "sum"), companies=("company", "count"))
        .reset_index()
    )
    monthly_data["year_month_date"] = pd.to_datetime(monthly_data["year_month"])
    monthly_data = monthly_data.sort_values("year_month_date")

    # Create figure with dual y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add layoffs line
    fig.add_trace(
        go.Scatter(
            x=monthly_data["year_month_date"],
            y=monthly_data["total_layoffs"],
            mode="lines+markers",
            name="Total Layoffs",
            line=dict(color=Colors.VIZ_PRIMARY_LINE, width=3),
            marker=dict(size=8),
        ),
        secondary_y=False,
    )

    # Add companies bar
    fig.add_trace(
        go.Bar(
            x=monthly_data["year_month_date"],
            y=monthly_data["companies"],
            name="Total Companies",
            marker=dict(color=Colors.VIZ_SECONDARY_BAR, opacity=0.6),
        ),
        secondary_y=True,
    )

    # Customize layout
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white",
        margin=dict(l=30, r=30, t=80, b=20),
        height=500,
        paper_bgcolor=Colors.BG_CARD,
        plot_bgcolor=Colors.TRANSPARENT,
        font_color=Colors.TEXT_WHITE,
    )

    # Set y-axes titles
    fig.update_yaxes(
        title_text="Total Layoffs", secondary_y=False, gridcolor=Colors.VIZ_GRID
    )
    fig.update_yaxes(
        title_text="Total Companies", secondary_y=True, gridcolor=Colors.VIZ_GRID
    )

    # Update x-axis
    fig.update_xaxes(
        tickformat="%b %Y",
        tickangle=-45,
        gridcolor=Colors.VIZ_GRID,
        title_text="Months",
    )

    return fig


def create_country_map(
    df, selected_years=None, selected_industries=None, selected_countries=None
):
    """
    Membuat visualisasi peta distribusi layoffs

    Args:
        df (DataFrame): DataFrame berisi data layoffs
        selected_years (list): Daftar tahun yang dipilih
        selected_industries (list): Daftar industri yang dipilih
        selected_countries (list): Daftar negara yang dipilih

    Returns:
        Figure: Objek Figure Plotly
    """
    from components.data_processor import apply_filters

    # Apply filters
    filtered_df = apply_filters(
        df, selected_years, selected_industries, selected_countries
    )

    # Group by country
    country_data = (
        filtered_df.groupby("country")
        .agg(
            percentage_layoffs=("percentage_laid_off", "mean"),
            total_layoffs=("total_laid_off", "sum"),
            companies=("company", "nunique"),
        )
        .reset_index()
    )

    # Definisikan hovertemplate yang lebih profesional
    hovertemplate = (
        # judul negara
        f"<span style='font-size:14px; font-weight:600; color:{Colors.TEXT_WHITE};'>"
        "%{hovertext}</span><br>"
        # garis pemisah pakai blok span 1-px tinggi
        f"<span style='display:block; height:1px; "
        f"background:{Colors.VIZ_SEPARATOR}; margin:4px 0;'></span>"
        # tingkat PHK
        f"<span style='color:{Colors.TEXT_LIGHT_GRAY};'>Layoff Rate</span>: "
        f"<span style='font-weight:600; color:{Colors.TEXT_WHITE};'>%{{z:.2f}}%</span><br>"
        # total karyawan
        f"<span style='color:{Colors.TEXT_LIGHT_GRAY};'>Total Affected</span>: "
        f"<span style='font-weight:600; color:{Colors.TEXT_WHITE};'>%{{customdata[1]:,}} employees</span><br>"
        # jumlah perusahaan
        f"<span style='color:{Colors.TEXT_LIGHT_GRAY};'>Number of Companies</span>: "
        f"<span style='font-weight:600; color:{Colors.TEXT_WHITE};'>%{{customdata[2]}}</span>"
        "<extra></extra>"  # buang trace-name default
    )

    # Create figure
    fig = px.choropleth(
        country_data,
        locations="country",
        locationmode="country names",
        color="percentage_layoffs",
        hover_name="country",
        hover_data={
            "percentage_layoffs": ":.2f",
            "total_layoffs": ":,",
            "companies": True,
        },
        color_continuous_scale=Colors.get_map_colorscale(),
        range_color=(0, 100),
        projection="natural earth",
        labels={
            "country": "Negara",
            "percentage_layoffs": "Tingkat PHK (%)",
            "total_layoffs": "Total Karyawan Terdampak",
            "companies": "Jumlah Perusahaan",
        },
    )

    # Terapkan hovertemplate kustom
    fig.update_traces(hovertemplate=hovertemplate)

    # Customize layout
    fig.update_layout(
        title={
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=24, color=Colors.TEXT_WHITE),
        },
        geo=dict(
            showframe=False,
            showcoastlines=True,
            bgcolor=Colors.BG_CARD,
            projection_scale=1.2,
            center=dict(lat=10, lon=0),
        ),
        coloraxis_colorbar=dict(
            title=dict(
                text="Layoff<br>Rate<br>(%)<br>",
                font=dict(size=14, color=Colors.TEXT_WHITE),
            ),
            thickness=15,
            len=0.8,
            x=1.02,
            xanchor="left",
            y=0.5,
            yanchor="middle",
        ),
        margin=dict(l=20, r=20, t=20, b=0),
        paper_bgcolor=Colors.BG_CARD,
        plot_bgcolor=Colors.BG_CARD,
        font_color=Colors.TEXT_WHITE,
    )

    return fig


def create_treemap(
    df, selected_years=None, selected_industries=None, selected_countries=None
):
    """
    Membuat visualisasi treemap untuk melihat distribusi layoffs berdasarkan industri dan perusahaan
    dengan 8 kategori industri terbesar dan maksimal 10 sub-bagian per industri (9 teratas + Others)

    Args:
        df (DataFrame): DataFrame berisi data layoffs
        selected_years (list): Daftar tahun yang dipilih
        selected_industries (list): Daftar industri yang dipilih
        selected_countries (list): Daftar negara yang dipilih

    Returns:
        Figure: Objek Figure Plotly
    """
    from components.data_processor import apply_filters

    # Apply filters
    filtered_df = apply_filters(
        df, selected_years, selected_industries, selected_countries
    )

    # Hitung total layoffs per industri
    industry_totals = (
        filtered_df.groupby("industry")
        .agg(total_layoffs=("total_laid_off", "sum"))
        .reset_index()
        .sort_values("total_layoffs", ascending=False)
    )

    # Ambil top 8 industri
    top_industries = industry_totals.head(8)
    top_industry_list = top_industries["industry"].tolist()

    # Siapkan list untuk menyimpan data treemap
    treemap_rows = []

    # Proses top 8 industri
    for industry in top_industry_list:
        # Filter data untuk industri ini
        industry_data = filtered_df[filtered_df["industry"] == industry]

        # Group by company untuk industri ini
        company_data = (
            industry_data.groupby("company")
            .agg(
                total_layoffs=("total_laid_off", "sum"),
                country=("country", "first"),
            )
            .reset_index()
        )

        # Filter out zero values
        company_data = company_data[company_data["total_layoffs"] > 0]

        # Sort by total_layoffs descending
        company_data = company_data.sort_values("total_layoffs", ascending=False)

        # Ambil top 9 perusahaan
        top_companies = company_data.head(9)

        # Gabungkan sisanya ke dalam "Others"
        if len(company_data) > 9:
            others_data = company_data.iloc[9:]
            others_total = others_data["total_layoffs"].sum()
            others_countries = ", ".join(others_data["country"].unique())

            # Tambahkan data top 9
            for _, row in top_companies.iterrows():
                treemap_rows.append(
                    {
                        "industry": industry,
                        "company": row["company"],
                        "total_layoffs": row["total_layoffs"],
                        "country": row["country"],
                        "color": Colors.get_industry_color(industry),
                    }
                )

            # Tambahkan data Others
            treemap_rows.append(
                {
                    "industry": industry,
                    "company": "Others",
                    "total_layoffs": others_total,
                    "country": others_countries,
                    "color": Colors.get_industry_color(industry),
                }
            )
        else:
            # Jika kurang dari 10 perusahaan, tambahkan semua
            for _, row in company_data.iterrows():
                treemap_rows.append(
                    {
                        "industry": industry,
                        "company": row["company"],
                        "total_layoffs": row["total_layoffs"],
                        "country": row["country"],
                        "color": Colors.get_industry_color(industry),
                    }
                )

    # Buat DataFrame dari list dengan kolom yang eksplisit
    treemap_data = pd.DataFrame(
        treemap_rows,
        columns=["industry", "company", "total_layoffs", "country", "color"],
    )

    # Handle kasus data kosong
    if treemap_data.empty:
        fig = go.Figure()
        fig.update_layout(
            paper_bgcolor=Colors.BG_CARD,
            plot_bgcolor=Colors.BG_CARD,
            margin=dict(l=1, r=1, t=0, b=1),
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            annotations=[
                dict(
                    text="No data for current filter",
                    x=0.5,
                    y=0.5,
                    xref="paper",
                    yref="paper",
                    showarrow=False,
                    font=dict(size=14, color=Colors.TEXT_WHITE),
                )
            ],
        )
        return fig

    # Create figure
    fig = px.treemap(
        treemap_data,
        path=["industry", "company"],
        values="total_layoffs",
        color="industry",
        color_discrete_map=Colors.INDUSTRY_COLORS,
        custom_data=["total_layoffs"],
    )

    # Customize layout
    fig.update_layout(
        margin=dict(l=1, r=1, t=1, b=1),
        paper_bgcolor=Colors.TRANSPARENT,
        plot_bgcolor=Colors.TRANSPARENT,
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        font_color=Colors.TEXT_WHITE,
        autosize=True,
        height=500,
        width=None,
    )

    # Update traces untuk mengontrol font dan posisi teks lebih detail
    hovertemplate = (
        "<span style='font-size:13px; font-weight:600;'>%{label}</span><br>"
        f"<span style='color:{Colors.TEXT_LIGHT_GRAY};'>Total layoffs</span>: "
        "<span style='font-weight:600;'>%{customdata[0]:,} employees</span><br>"
        f"<span style='color:{Colors.TEXT_LIGHT_GRAY};'>Proportion</span>: "
        "<span style='font-weight:600;'>%{percentParent:.1%}</span>"
        "<extra></extra>"
    )

    fig.update_traces(
        hovertemplate=hovertemplate,
        hoverlabel=dict(
            bgcolor=Colors.BG_HOVER,
            bordercolor=Colors.TEXT_WHITE,
            font_size=12,
            font_family="Arial, sans-serif",
        ),
        textfont_size=10,
        selector=dict(type="treemap"),
    )

    # Ubah teks untuk menampilkan hanya 3 huruf pertama nama company
    for i, trace in enumerate(fig.data):
        if hasattr(trace, "labels") and trace.labels is not None:
            new_text = []
            for label in trace.labels:
                if label in treemap_data["company"].values:
                    # Ambil 3 huruf pertama dari nama company
                    new_text.append(label[:4].upper())
                else:
                    # Tetap tampilkan nama industri utuh
                    new_text.append(label)
            trace.text = new_text

    for d in fig.data:
        if hasattr(d, "marker"):
            d.marker.line = dict(color=Colors.BORDER_WHITE, width=0.5)

    # Ganti teks default → 3 huruf pertama (sudah dilakukan di loop sebelumnya)
    # Sekarang posisikan di tengah & perbesar font
    fig.update_traces(
        texttemplate="<b>%{text}</b><br><span style='font-size:12px'>%{percentParent:.1%}</span>",  # bold + persentase
        textposition="middle center",  # pusat kotak
        textfont_size=10,  # sedikit lebih besar
        selector=dict(type="treemap"),
    )

    # (opsional) pastikan label industri tetap muncul normal & cukup besar
    fig.update_traces(
        textfont_size=10,
        selector=lambda tr: tr.ids is not None and any("/" not in i for i in tr.ids),
    )

    return fig
