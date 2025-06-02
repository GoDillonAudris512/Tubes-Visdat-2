"""
Konfigurasi warna terpusat untuk aplikasi Global Layoffs Dashboard
Semua warna yang digunakan dalam aplikasi didefinisikan di sini untuk memudahkan pemeliharaan
"""


class Colors:
    """Kelas yang berisi semua definisi warna untuk aplikasi"""

    # === WARNA DASAR ===
    PRIMARY_BLUE = "#4CB6F0"
    PRIMARY_ORANGE = "#FFA63E"
    PRIMARY_RED = "#FF2D2E"

    # === WARNA BACKGROUND ===
    BG_MAIN = "#05050F"  # Background utama aplikasi
    BG_CARD = "#1F1F43"  # Background card/komponen
    BG_HOVER = "#26264F"  # Background saat hover
    BG_BUTTON_HOVER = "#2A2A5C"  # Background button saat hover

    # === WARNA TEKS ===
    TEXT_WHITE = "#FFFFFF"
    TEXT_LIGHT_GRAY = "#B0B0B0"
    TEXT_MEDIUM_GRAY = "#808080"
    TEXT_DARK_GRAY = "#9E9E9E"

    # === WARNA GRADIENT ===
    GRADIENT_BLUE_START = "#4CB6F0"
    GRADIENT_BLUE_END = "#5D9DB8"
    GRADIENT_ORANGE_START = "#4CB6F0"
    GRADIENT_ORANGE_END = "#FFA63E"

    # === WARNA STATISTIK ===
    STAT_EMPLOYEE = "#7DB2BF"  # Warna untuk employee statistics
    STAT_COMPANY = "#C1AB7B"  # Warna untuk company statistics
    STAT_COUNTRY = "#FAA743"  # Warna untuk country statistics

    # === WARNA SECTION TITLES ===
    SECTION_TITLE = "#E4A959"

    # === WARNA UNTUK VISUALISASI ===
    VIZ_PRIMARY_LINE = "#FF2D2E"  # Warna utama untuk line charts
    VIZ_SECONDARY_BAR = "#E4A959"  # Warna untuk bar charts (diubah menjadi kuning)
    VIZ_GRID = "#808080"  # Warna grid dalam chart
    VIZ_SEPARATOR = "#4A4A70"  # Warna pemisah dalam tooltip

    # === WARNA MAP COLORSCALE ===
    MAP_COLORSCALE = [
        "#FFD6D6",  # Sangat terang
        "#FF9999",  # Terang
        "#FF4D4D",  # Sedang
        "#FF2D2E",  # Gelap (warna dasar)
    ]

    # === WARNA INDUSTRI UNTUK TREEMAP ===
    INDUSTRY_COLORS = {
        "Hardware": "#9B1BFA",  # Ungu
        "Other": "#4DC0F4",  # Biru muda
        "Retail": "#FFA63E",  # Oranye
        "Transportation": "#FF2D2E",  # Merah
        "Finance": "#3F9729",  # Hijau
        "Consumer": "#FFD63A",  # Kuning
        "Food": "#0C2E6B",  # Biru tua
        "Healthcare": "#D3d3d3",  # Abu-abu terang
    }

    # === WARNA TRANSPARAN ===
    TRANSPARENT = "rgba(0,0,0,0)"

    # === WARNA BUTTONS ===
    BUTTON_PRIMARY = "#4DC0F4"
    BUTTON_PRIMARY_HOVER = "blue-400"  # Untuk Tailwind CSS

    # === WARNA BORDER ===
    BORDER_WHITE = "white"
    BORDER_DEFAULT = "#FFFFFF"

    @classmethod
    def get_map_colorscale(cls):
        """Mengembalikan colorscale untuk peta"""
        return cls.MAP_COLORSCALE

    @classmethod
    def get_industry_color(cls, industry_name, default_color=None):
        """
        Mengembalikan warna untuk industri tertentu

        Args:
            industry_name (str): Nama industri
            default_color (str): Warna default jika industri tidak ditemukan

        Returns:
            str: Kode warna hex
        """
        if default_color is None:
            default_color = cls.TEXT_DARK_GRAY
        return cls.INDUSTRY_COLORS.get(industry_name, default_color)

    @classmethod
    def get_gradient_colors(cls, gradient_type="blue"):
        """
        Mengembalikan warna gradient

        Args:
            gradient_type (str): Tipe gradient ("blue" atau "orange")

        Returns:
            tuple: (start_color, end_color)
        """
        if gradient_type == "blue":
            return (cls.GRADIENT_BLUE_START, cls.GRADIENT_BLUE_END)
        elif gradient_type == "orange":
            return (cls.GRADIENT_ORANGE_START, cls.GRADIENT_ORANGE_END)
        else:
            return (cls.PRIMARY_BLUE, cls.PRIMARY_ORANGE)
