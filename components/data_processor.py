import pandas as pd
import numpy as np
from datetime import datetime


def load_data():
    """
    Load dan pra-proses dataset layoffs

    Returns:
        DataFrame: Pandas DataFrame berisi data layoffs yang telah diproses
    """
    df = pd.read_csv("data/layoffs.csv")

    # Konversi kolom date menjadi datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Mengisi nilai NaN dengan 0 untuk kolom numerik
    numeric_cols = ["total_laid_off", "percentage_laid_off", "funds_raised"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Ekstrak tahun dan bulan dari date
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%b")
    df["year_month"] = df["date"].dt.strftime("%Y-%m")

    return df


def get_filter_options(df):
    """
    Mendapatkan nilai unik untuk opsi filter

    Args:
        df (DataFrame): DataFrame berisi data layoffs

    Returns:
        tuple: (available_years, available_industries, available_countries)
    """
    available_years = sorted(df["year"].dropna().unique())
    available_industries = sorted(df["industry"].dropna().unique())
    available_countries = sorted(df["country"].dropna().unique())

    return available_years, available_industries, available_countries


def apply_filters(df, years=None, industries=None, countries=None):
    """
    Menerapkan filter ke DataFrame

    Args:
        df (DataFrame): DataFrame berisi data layoffs
        years (list): Daftar tahun untuk filter
        industries (list): Daftar industri untuk filter
        countries (list): Daftar negara untuk filter

    Returns:
        DataFrame: DataFrame yang telah difilter
    """
    filtered_df = df.copy()

    if years:
        min_year = min(years)
        max_year = max(years)
        filtered_df = filtered_df[
            (filtered_df["year"] >= min_year) & (filtered_df["year"] <= max_year)
        ]

    if industries and industries != []:
        filtered_df = filtered_df[filtered_df["industry"].isin(industries)]

    if countries and countries != []:
        filtered_df = filtered_df[filtered_df["country"].isin(countries)]

    return filtered_df
