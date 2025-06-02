# Sistem Manajemen Warna Terpusat

## 📋 Overview

Sistem ini dibuat untuk mengelola semua warna dalam aplikasi Global Layoffs Dashboard secara terpusat. Dengan sistem ini, Anda dapat dengan mudah mengganti tema warna seluruh aplikasi hanya dengan mengubah beberapa variabel di satu file.

## 🎨 Struktur File

```
components/
├── colors.py      # Konfigurasi warna utama (file yang digunakan aplikasi)
├── themes.py      # Koleksi tema warna alternatif
├── visualizations.py  # Menggunakan Colors dari colors.py
├── layout.py      # Menggunakan Colors dari colors.py
└── ui.py          # Menggunakan Colors dari colors.py
```

## 🔧 Cara Menggunakan

### 1. Mengubah Warna Individual

Untuk mengubah warna tertentu, edit file `components/colors.py`:

```python
class Colors:
    # Contoh: mengubah warna primary dari biru ke hijau
    PRIMARY_BLUE = "#4ECDC4"  # sebelumnya "#4CB6F0"

    # Mengubah background utama
    BG_MAIN = "#0F1419"  # sebelumnya "#05050F"
```

### 2. Mengganti Tema Lengkap

1. Buka file `components/themes.py`
2. Pilih salah satu tema yang tersedia (contoh: `DARK_GREEN_THEME`)
3. Salin semua properti dari tema tersebut
4. Tempelkan ke dalam class `Colors` di file `components/colors.py`
5. Restart aplikasi

### 3. Membuat Tema Baru

Anda dapat membuat tema baru dengan menambahkan dictionary baru di `components/themes.py`:

```python
MY_CUSTOM_THEME = {
    "PRIMARY_BLUE": "#YOUR_COLOR",
    "PRIMARY_ORANGE": "#YOUR_COLOR",
    "PRIMARY_RED": "#YOUR_COLOR",
    # ... tambahkan semua properti warna
}
```

## 🎨 Kategori Warna

### 1. Warna Dasar

-   `PRIMARY_BLUE` - Warna biru utama
-   `PRIMARY_ORANGE` - Warna oranye utama
-   `PRIMARY_RED` - Warna merah utama

### 2. Warna Background

-   `BG_MAIN` - Background utama aplikasi
-   `BG_CARD` - Background card/komponen
-   `BG_HOVER` - Background saat hover
-   `BG_BUTTON_HOVER` - Background button saat hover

### 3. Warna Teks

-   `TEXT_WHITE` - Teks putih
-   `TEXT_LIGHT_GRAY` - Teks abu-abu terang
-   `TEXT_MEDIUM_GRAY` - Teks abu-abu medium
-   `TEXT_DARK_GRAY` - Teks abu-abu gelap

### 4. Warna Gradient

-   `GRADIENT_BLUE_START` & `GRADIENT_BLUE_END` - Gradient biru
-   `GRADIENT_ORANGE_START` & `GRADIENT_ORANGE_END` - Gradient oranye

### 5. Warna Statistik

-   `STAT_EMPLOYEE` - Warna untuk statistik karyawan
-   `STAT_COMPANY` - Warna untuk statistik perusahaan
-   `STAT_COUNTRY` - Warna untuk statistik negara

### 6. Warna Visualisasi

-   `VIZ_PRIMARY_LINE` - Warna utama untuk line charts
-   `VIZ_SECONDARY_BAR` - Warna untuk bar charts
-   `VIZ_GRID` - Warna grid dalam chart
-   `VIZ_SEPARATOR` - Warna pemisah dalam tooltip

### 7. Warna Industri (Treemap)

-   Dictionary `INDUSTRY_COLORS` berisi mapping warna untuk setiap industri

## 🛠️ Metode Helper

### `get_map_colorscale()`

Mengembalikan colorscale untuk peta choropleth.

### `get_industry_color(industry_name, default_color=None)`

Mengembalikan warna untuk industri tertentu dengan fallback ke warna default.

### `get_gradient_colors(gradient_type="blue")`

Mengembalikan tuple (start_color, end_color) untuk gradient.

## 📦 Tema yang Tersedia

1. **ORIGINAL_THEME** - Tema default (biru-oranye gelap)
2. **DARK_GREEN_THEME** - Tema hijau gelap dengan aksen teal
3. **PURPLE_NIGHT_THEME** - Tema ungu malam yang elegan
4. **OCEAN_BLUE_THEME** - Tema biru laut yang fresh

## 💡 Tips dan Best Practices

### 1. Konsistensi Warna

Pastikan kontras yang cukup antara background dan teks untuk aksesibilitas.

### 2. Testing

Setelah mengubah tema, test semua komponen untuk memastikan readability.

### 3. Backup

Selalu backup konfigurasi warna lama sebelum mengubah tema.

### 4. Naming Convention

Gunakan nama yang deskriptif untuk warna custom:

```python
# ❌ Tidak deskriptif
COLOR_1 = "#FF0000"

# ✅ Deskriptif
DANGER_RED = "#FF0000"
SUCCESS_GREEN = "#00FF00"
```

## 🔄 Migrasi dari Hardcoded Colors

Jika Anda menemukan warna yang masih hardcoded dalam kode, ikuti langkah berikut:

1. **Identifikasi warna** - Catat hex code yang digunakan
2. **Kategorikan** - Tentukan kategori warna yang sesuai
3. **Tambah ke Colors class** - Jika belum ada, tambahkan sebagai konstanta baru
4. **Replace** - Ganti hardcoded hex dengan `Colors.NAMA_KONSTANTA`
5. **Test** - Pastikan tidak ada yang rusak

### Contoh Migrasi:

```python
# Sebelum
fig.update_layout(paper_bgcolor="#1F1F43")

# Sesudah
fig.update_layout(paper_bgcolor=Colors.BG_CARD)
```

## 🚀 Implementasi di Komponen Baru

Saat membuat komponen baru, selalu gunakan warna dari `Colors` class:

```python
from components.colors import Colors

def new_component():
    return html.Div(
        "Content",
        style={
            "backgroundColor": Colors.BG_CARD,
            "color": Colors.TEXT_WHITE,
            "borderColor": Colors.PRIMARY_BLUE
        }
    )
```

## 📞 Support

Jika Anda mengalami masalah dengan sistem warna atau ingin menambahkan tema baru, silakan buat issue atau diskusikan dengan tim development.

---

**Note**: Setelah mengubah tema, aplikasi perlu di-restart untuk melihat perubahan secara penuh.
