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
            line=dict(color="#FF5A5F", width=3),
            marker=dict(size=8),
        ),
        secondary_y=False,
    )

    # Add companies bar
    fig.add_trace(
        go.Bar(
            x=monthly_data["year_month_date"],
            y=monthly_data["companies"],
            name="Jumlah Perusahaan",
            marker=dict(color="#2C3E50", opacity=0.7),
        ),
        secondary_y=True,
    )

    # Customize layout
    fig.update_layout(
        title={
            "text": "Tren Layoffs Per Bulan",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=24, color="#2C3E50"),
        },
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white",
        margin=dict(l=20, r=20, t=80, b=20),
        height=500,
    )

    # Set y-axes titles
    fig.update_yaxes(
        title_text="Total Karyawan yang di-PHK", secondary_y=False, gridcolor="#EAEAEA"
    )
    fig.update_yaxes(
        title_text="Jumlah Perusahaan", secondary_y=True, gridcolor="#EAEAEA"
    )

    # Update x-axis
    fig.update_xaxes(
        tickformat="%b %Y", tickangle=-45, gridcolor="#EAEAEA", title_text="Bulan"
    )

    return fig


def create_industry_chart(
    df, selected_years=None, selected_industries=None, selected_countries=None
):
    """
    Membuat visualisasi industri dengan layoffs tertinggi

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

    # Group by industry
    industry_data = (
        filtered_df.groupby("industry")
        .agg(total_layoffs=("total_laid_off", "sum"), companies=("company", "nunique"))
        .reset_index()
        .sort_values("total_layoffs", ascending=False)
        .head(10)
    )

    # Create figure
    fig = px.bar(
        industry_data,
        x="industry",
        y="total_layoffs",
        color="companies",
        color_continuous_scale="Viridis",
        labels={
            "industry": "Industri",
            "total_layoffs": "Total Karyawan yang di-PHK",
            "companies": "Jumlah Perusahaan",
        },
        title="10 Industri dengan Layoffs Tertinggi",
    )

    # Customize layout
    fig.update_layout(
        title={
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=24, color="#2C3E50"),
        },
        xaxis_title="Industri",
        yaxis_title="Total Karyawan yang di-PHK",
        template="plotly_white",
        coloraxis_colorbar=dict(
            title="Jumlah<br>Perusahaan",
        ),
        margin=dict(l=20, r=20, t=80, b=100),
        height=500,
    )

    # Update x-axis
    fig.update_xaxes(
        tickangle=-45,
        gridcolor="#EAEAEA",
    )

    # Update y-axis
    fig.update_yaxes(
        gridcolor="#EAEAEA",
    )

    return fig


def create_companies_chart(
    df, selected_years=None, selected_industries=None, selected_countries=None
):
    """
    Membuat visualisasi perusahaan dengan layoffs tertinggi

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

    # Group by company
    company_data = (
        filtered_df.groupby(["company", "industry"])
        .agg(
            total_layoffs=("total_laid_off", "sum"),
        )
        .reset_index()
        .sort_values("total_layoffs", ascending=False)
        .head(10)
    )

    # Create figure
    fig = px.bar(
        company_data,
        x="company",
        y="total_layoffs",
        color="industry",
        labels={
            "company": "Perusahaan",
            "total_layoffs": "Total Karyawan yang di-PHK",
            "industry": "Industri",
        },
        title="10 Perusahaan dengan Layoffs Tertinggi",
    )

    # Customize layout
    fig.update_layout(
        title={
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=24, color="#2C3E50"),
        },
        xaxis_title="Perusahaan",
        yaxis_title="Total Karyawan yang di-PHK",
        template="plotly_white",
        legend=dict(
            title="Industri",
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5,
        ),
        margin=dict(l=20, r=20, t=80, b=200),
        height=550,
    )

    # Update x-axis
    fig.update_xaxes(
        tickangle=-45,
        gridcolor="#EAEAEA",
    )

    # Update y-axis
    fig.update_yaxes(
        gridcolor="#EAEAEA",
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
        .agg(total_layoffs=("total_laid_off", "sum"), companies=("company", "nunique"))
        .reset_index()
    )

    # Create figure
    fig = px.choropleth(
        country_data,
        locations="country",
        locationmode="country names",
        color="total_layoffs",
        hover_name="country",
        hover_data=["total_layoffs", "companies"],
        color_continuous_scale="Plasma",
        projection="natural earth",
        title="Distribusi Layoffs di Seluruh Dunia",
        labels={"total_layoffs": "Total Layoffs", "companies": "Jumlah Perusahaan"},
    )

    # Customize layout
    fig.update_layout(
        title={
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=24, color="#2C3E50"),
        },
        geo=dict(showframe=False, showcoastlines=True, projection_type="natural earth"),
        coloraxis_colorbar=dict(
            title="Total<br>Layoffs",
        ),
        margin=dict(l=20, r=20, t=80, b=20),
        height=550,
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
        "Consumer": "#FF5A5F",  # Merah
        "Retail": "#FFB400",  # Kuning
        "Transportation": "#007A87",  # Biru
        "Education": "#8CE071",  # Hijau
        "Finance": "#7B0051",  # Ungu
        "Healthcare": "#00D1C1",  # Turquoise
        "Technology": "#4CAF50",  # Hijau
        "Manufacturing": "#FFAA91",  # Oranye
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

    # Buat DataFrame dari list
    treemap_data = pd.DataFrame(treemap_rows)

    # Create figure
    fig = px.treemap(
        treemap_data,
        path=["industry", "company"],
        values="total_layoffs",
        color="industry",  # Warna berdasarkan industri
        color_discrete_map=industry_colors,  # Gunakan mapping warna yang sudah didefinisikan
        hover_data=["total_layoffs", "country"],
        title="Distribusi Layoffs berdasarkan Industri dan Perusahaan (Top 8 Industri)",
        labels={
            "total_layoffs": "Total Karyawan yang di-PHK",
            "country": "Negara",
        },
    )

    # Customize layout
    fig.update_layout(
        title={
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=24, color="#2C3E50"),
        },
        template="plotly_white",
        margin=dict(l=20, r=20, t=80, b=20),
        height=600,
    )

    return fig
