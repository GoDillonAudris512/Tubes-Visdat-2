import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


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
            line=dict(color="#FF2D2E", width=3),
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
            marker=dict(color="#FFA63E", opacity=0.6),
        ),
        secondary_y=True,
    )

    # Customize layout
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white",
        margin=dict(l=30, r=30, t=80, b=20),
        height=500,
        paper_bgcolor="#1F1F43",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
    )

    # Set y-axes titles
    fig.update_yaxes(title_text="Total Layoffs", secondary_y=False, gridcolor="#808080")
    fig.update_yaxes(
        title_text="Total Companies", secondary_y=True, gridcolor="#808080"
    )

    # Update x-axis
    fig.update_xaxes(
        tickformat="%b %Y", tickangle=-45, gridcolor="#808080", title_text="Months"
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

    custom_colorscale = [
        "#FFD6D6",  # sangat terang
        "#FF9999",
        "#FF4D4D",
        "#FF2D2E",  # warna dasar
    ]

    # Definisikan hovertemplate yang lebih profesional
    hovertemplate = (
        # judul negara
        "<span style='font-size:14px; font-weight:600; color:#FFFFFF;'>"
        "%{hovertext}</span><br>"
        # garis pemisah pakai blok span 1-px tinggi
        "<span style='display:block; height:1px; "
        "background:#4A4A70; margin:4px 0;'></span>"
        # tingkat PHK
        "<span style='color:#B0B0B0;'>Layoff Rate</span>: "
        "<span style='font-weight:600; color:#FFFFFF;'>%{z:.2f}%</span><br>"
        # total karyawan
        "<span style='color:#B0B0B0;'>Total Affected</span>: "
        "<span style='font-weight:600; color:#FFFFFF;'>%{customdata[1]:,} employees</span><br>"
        # jumlah perusahaan
        "<span style='color:#B0B0B0;'>Number of Companies</span>: "
        "<span style='font-weight:600; color:#FFFFFF;'>%{customdata[2]}</span>"
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
        color_continuous_scale=custom_colorscale,
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
            "font": dict(size=24, color="#ffffff"),
        },
        geo=dict(
            showframe=False,
            showcoastlines=True,
            bgcolor="#1F1F43",
            projection_scale=1.2,
            center=dict(lat=10, lon=0),
        ),
        coloraxis_colorbar=dict(
            title=dict(
                text="Layoff<br>Rate<br>(%)<br>",
                font=dict(size=14, color="#ffffff"),
            ),
            thickness=15,
            len=0.8,
            x=1.02,
            xanchor="left",
            y=0.5,
            yanchor="middle",
        ),
        margin=dict(l=20, r=20, t=20, b=0),
        paper_bgcolor="#1F1F43",
        plot_bgcolor="#1F1F43",
        font_color="#FFFFFF",
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

    # Definisikan warna untuk setiap industri
    industry_colors = {
        "Hardware": "#9B1BFA",  # Merah
        "Other": "#4DC0F4",  # Kuning
        "Retail": "#FFA63E",  # Biru
        "Transportation": "#FF2D2E",  # Hijau
        "Finance": "#3F9729",  # Ungu
        "Consumer": "#FFD63A",  # Turquoise
        "Food": "#0C2E6B",  # Hijau
        "Healthcare": "#D3d3d3",  # Oranye
    }

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
                        "color": industry_colors.get(
                            industry, "#9E9E9E"
                        ),  # Default abu-abu jika warna tidak ditemukan
                    }
                )

            # Tambahkan data Others
            treemap_rows.append(
                {
                    "industry": industry,
                    "company": "Others",
                    "total_layoffs": others_total,
                    "country": others_countries,
                    "color": industry_colors.get(industry, "#9E9E9E"),
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
                        "color": industry_colors.get(industry, "#9E9E9E"),
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
            paper_bgcolor="#1F1F43",
            plot_bgcolor="#1F1F43",
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
                    font=dict(size=14, color="#FFFFFF"),
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
        color_discrete_map=industry_colors,
        custom_data=["total_layoffs"],
    )

    # Customize layout
    fig.update_layout(
        margin=dict(l=1, r=1, t=0, b=1),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        font_color="#FFFFFF",
    )

    # Update traces untuk mengontrol font dan posisi teks lebih detail
    hovertemplate = (
        "<span style='font-size:13px; font-weight:600;'>%{label}</span><br>"
        "<span style='color:#B0B0B0;'>Total layoffs</span>: "
        "<span style='font-weight:600;'>%{customdata[0]:,} employees</span><br>"
        "<span style='color:#B0B0B0;'>Proportion</span>: "
        "<span style='font-weight:600;'>%{percentParent:.1%}</span>"
        "<extra></extra>"
    )

    fig.update_traces(
        hovertemplate=hovertemplate,
        hoverlabel=dict(
            bgcolor="#26264F",
            bordercolor="#FFFFFF",
            font_size=12,
            font_family="Arial, sans-serif",
        ),
        textfont_size=10,
        selector=dict(type="treemap"),
    )

    for d in fig.data:
        if hasattr(d, "marker"):
            d.marker.line = dict(color="white", width=0.5)

    return fig
