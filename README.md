# Dashboard Visualisasi Data Layoffs

Dashboard interaktif untuk menampilkan dan menganalisis data PHK (layoffs) dari berbagai perusahaan menggunakan Dash by Plotly.

## Fitur

-   Visualisasi tren layoffs berdasarkan waktu
-   Analisis layoffs berdasarkan industri
-   Perbandingan perusahaan dengan layoffs tertinggi
-   Peta distribusi layoffs secara global
-   Filter interaktif berdasarkan tahun, industri, dan negara

## Instalasi

```bash
# Clone repository
git clone https://github.com/username/layoffs-dashboard.git
cd layoffs-dashboard

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows
source venv/Scripts/activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Menjalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://127.0.0.1:8050/`

## Struktur Proyek

```
layoffs-dashboard/
├── app.py                 # File utama aplikasi
├── config.py              # Konfigurasi aplikasi
├── requirements.txt       # Dependency
├── data/                  # Data
│   └── layoffs.csv        # Dataset layoffs
├── assets/                # Asset statis
│   └── style.css          # Custom CSS
└── components/            # Komponen aplikasi
    ├── __init__.py
    ├── callbacks.py       # Callback interaktif
    ├── data_processor.py  # Proses dan filter data
    ├── layout.py          # Layout utama
    ├── ui.py              # Komponen UI
    └── visualizations.py  # Fungsi visualisasi
```

## Deployment

Untuk deployment ke Heroku:

```bash
# Login ke Heroku
heroku login

# Buat aplikasi Heroku
heroku create nama-aplikasi

# Push ke Heroku
git push heroku main
```

## Kontribusi

1. Fork repository
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request
