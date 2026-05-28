import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import os

# =====================================================================
# WAJIB DI BARIS PERTAMA: Set layout agar melebar penuh (Full Width)
# =====================================================================
st.set_page_config(
    page_title="Dashboard Pendidikan Jatim",
    layout="wide", # <--- Ini kunci utama agar full device/screen
    initial_sidebar_state="expanded"
)

# =====================================================================
# INJEKSI CSS: Menghilangkan padding bawaan Streamlit agar benar-benar mepet screen
# =====================================================================
st.markdown("""
    <style>
        /* Menghilangkan padding pada blok konten utama */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        /* Memastikan elemen markdown HTML bisa ditarik maksimal */
        div[data-testid="stVerticalBlock"] > div:has(div.banner-target) {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 1. FUNGSI UNTUK KONVERSI GAMBAR KE BASE64 (AGAR BISA DIJADIKAN HEADER)
# =====================================================================
def dapatkan_base64_gambar(jalur_gambar):
    with open(jalur_gambar, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Pastikan nama file sesuai dengan yang Anda simpan (misal: gg.jpg)
nama_file_gambar = "gg.jpg" 
# =====================================================================
# 2. IMPLEMENTASI HEADER BERGAMBAR PADA UTAMA DASHBOARD (FIXED)
# =====================================================================
if os.path.exists(nama_file_gambar):
    bin_str = dapatkan_base64_gambar(nama_file_gambar)
    
    st.markdown(f"""
        <div style="
            position: relative;
            background-image: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.65)), url('data:image/jpeg;base64,{bin_str}');
            background-size: cover;
            background-position: center 35%; /* Menggeser fokus gambar sedikit ke atas agar seimbang */
            padding: 40px 30px;
            border-radius: 16px;
            color: white;
            margin-bottom: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            text-align: left;
        ">
            <div style="display: flex; align-items: center; gap: 20px;">
                <span style="font-size: 40px; background: rgba(255,255,255,0.2); padding: 10px; border-radius: 50%;">🔮</span>
                <div style="max-width: 85%;">
                    <h1 style="
                        color: #FFFFFF; 
                        margin: 0; 
                        font-weight: 800; 
                        font-size: 38px; /* Diperkecil sedikit dari 50px agar proporsi wadah ideal dan gambar tidak terdorong ekstrem */
                        font-family: 'Source Sans Pro', sans-serif;
                        letter-spacing: 0.5px;
                        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
                        line-height: 1.2;
                    ">
                        Dashboard Kondisi Pendidikan Jawa Timur
                    </h1>
                    <p style="
                        color: #E8F5E9; 
                        margin: 8px 0 0 0; 
                        font-size: 16px; 
                        font-weight: 500;
                        text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
                        line-height: 1.4;
                    ">
                        Pengelompokan wilayah Jawa Timur berdasarkan kemiripan indikator pencapaian dan infrastruktur pendidikan menggunakan basis data.
                    </p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="
        background-color: #E8F5E9; border: 2px solid #81C784; border-radius: 14px; 
        padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); margin-bottom: 25px;
    ">
        <h2 style="color: #1B5E20; margin: 0; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
            🔮 Dashboard Pendidikan Jawa Timur
        </h2>
        <p style="color: #2E7D32; margin: 8px 0 0 0; font-size: 14px; line-height: 1.5;">
            Pengelompokan wilayah Jawa Timur berdasarkan kemiripan indikator pencapaian dan infrastruktur pendidikan.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# CUSTOM CSS FOR AESTHETIC GREEN SIDEBAR & PASTEL BUBBLE NAVIGATION
# =====================================================================
st.markdown("""
<style>
    /* 1. Mengubah Latar Belakang Sidebar Menjadi Hijau Sangat Muda */
    [data-testid="stSidebar"] {
        background-color: #F0F7F4 !important;
        border-right: 1px solid #C8E6C9;
    }
    
    /* 2. Mengubah Judul Navigasi di Sidebar */
    [data-testid="stSidebar"] h1 {
        color: #1B5E20 !important;
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: 800;
        font-size: 22px;
        margin-bottom: 20px;
    }

    /* 3. Menghilangkan radio button bulat bawaan dan mendesain ulang teks menjadi baris menu bubble */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 12px;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        background-color: #E8F5E9; /* Hijau mint pastel lembut */
        border: 1px solid #C8E6C9; 
        border-radius: 12px;
        padding: 12px 16px !important;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        cursor: pointer;
    }

    /* Efek Hover */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background-color: #E3F2FD !important; 
        border-color: #90CAF9 !important; 
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(33, 150, 243, 0.15);
    }

    /* Efek Active */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%) !important;
        border-color: #1B5E20 !important;
        box-shadow: 0 4px 10px rgba(27, 94, 32, 0.3);
    }

    /* Mengubah warna teks menu aktif */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"] div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 15px !important; 
    }

    /* Mengubah warna teks menu biasa */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {
        color: #1B5E20 !important; 
        font-size: 15px !important;
        font-weight: 600;
    }

    /* Sembunyikan lingkaran kecil radio button asli bawaan streamlit */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div:first-child:not([data-testid="stMarkdownContainer"]) {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)


# 2. Fungsi Pembantu: Format Angka Gaya Indonesia
def format_angka_id(nilai):
    if pd.isna(nilai):
        return "-"
    
    if isinstance(nilai, str):
        nilai = nilai.strip()
        if "," in nilai and "." not in nilai:
            nilai = nilai.replace(",", ".")
        try:
            nilai = float(nilai)
        except ValueError:
            return nilai 

    if isinstance(nilai, (int, float)):
        if nilai == int(nilai):
            return f"{int(nilai):,}".replace(",", ".")
        else:
            teks_us = f"{nilai:,.2f}"
            teks_id = teks_us.replace(",", "X").replace(".", ",").replace("X", ".")
            return teks_id
            
    return str(nilai)


# 3. Kamus Koordinat Geografis Presisi (38 Kabupaten/Kota Jawa Timur Lengkap)
koordinat_jatim = {
    'kabupaten bangkalan': [-7.05, 112.93], 'kabupaten banyuwangi': [-8.22, 114.36],
    'kabupaten blitar': [-8.10, 112.17], 'kota blitar': [-8.06, 112.16],
    'kabupaten bojonegoro': [-7.15, 111.88], 'kabupaten bondowoso': [-7.91, 113.82],
    'kabupaten gresik': [-7.16, 112.65], 'kabupaten jember': [-8.17, 113.70],
    'kabupaten jombang': [-7.55, 112.23], 'kabupaten kediri': [-7.85, 112.10],
    'kota kediri': [-7.82, 112.02], 'kabupaten lamongan': [-7.12, 112.42],
    'kabupaten lumajang': [-8.13, 113.22], 'kabupaten madiun': [-7.55, 111.65],
    'kota madiun': [-7.63, 111.53], 'kabupaten magetan': [-7.65, 111.33],
    'kabupaten malang': [-8.15, 112.62], 'kota malang': [-7.98, 112.62],
    'kabupaten mojokerto': [-7.55, 112.50], 'kota mojokerto': [-7.47, 112.43],
    'kabupaten nganjuk': [-7.60, 111.90], 'kabupaten ngawi': [-7.40, 111.45],
    'kabupaten pacitan': [-8.20, 111.10], 'kabupaten pamekasan': [-7.16, 113.48],
    'kabupaten pasuruan': [-7.75, 112.95], 'kota pasuruan': [-7.64, 112.91],
    'kabupaten ponorogo': [-7.87, 111.47], 'kabupaten probolinggo': [-7.90, 113.35],
    'kota probolinggo': [-7.75, 113.22], 'kabupaten sampang': [-7.20, 113.25],
    'kabupaten sidoarjo': [-7.45, 112.72], 'kabupaten situbondo': [-7.70, 114.01],
    'kabupaten sumenep': [-7.01, 113.86], 'kabupaten trenggalek': [-8.05, 111.72],
    'kabupaten tuban': [-6.90, 112.06], 'kabupaten tulungagung': [-8.07, 111.90],
    'kota surabaya': [-7.25, 112.75], 'kota batu': [-7.87, 112.52]
}

def ambil_lat_lon(nama_wilayah):
    nama_clean = str(nama_wilayah).lower().strip()
    return koordinat_jatim.get(nama_clean, [-7.5360, 112.2384])


# 4. Fungsi Memuat Data & Membersihkan Angka Desimal
@st.cache_data
def load_data():
    df_tahunan = pd.read_excel("Tahun.xlsx")
    df_kondisi = pd.read_excel("dttp.xlsx")
    
    # Membaca file hasil klastering hkc.xlsx
    try:
        df_hkc = pd.read_excel("hkc.xlsx")
        df_kondisi['Kabupaten/kota_clean'] = df_kondisi['Kabupaten/kota'].astype(str).str.lower().str.strip()
        df_hkc['Kabupaten/kota_clean'] = df_hkc['Kabupaten/kota'].astype(str).str.lower().str.strip()
        df_hkc_minimal = df_hkc[['Kabupaten/kota_clean', 'Cluster']]
        df_kondisi = pd.merge(df_kondisi, df_hkc_minimal, on='Kabupaten/kota_clean', how='left')
        df_kondisi = df_kondisi.drop(columns=['Kabupaten/kota_clean'])
    except Exception as e:
        df_kondisi['Cluster'] = 0
        
    # Proses pembersihan angka desimal bawaan dttp
    for col in df_kondisi.columns:
        if col not in ['Kabupaten/kota', 'Cluster']:
            if df_kondisi[col].dtype == object:
                df_kondisi[col] = df_kondisi[col].astype(str).str.replace(',', '.').str.strip()
            df_kondisi[col] = pd.to_numeric(df_kondisi[col], errors='coerce')
            
    # 🌟 MEMBACA DATA TREN SPASIAL KABUPATEN/KOTA (YANG SUDAH DIPERBAIKI)
    dict_tren = {}
    try:
        dict_tren['Indeks Pendidikan'] = pd.read_excel("ip.xlsx")
        dict_tren['Indeks Literasi'] = pd.read_excel("ipl.xlsx")
        dict_tren['Jumlah Murid'] = pd.read_excel("mr.xlsx")
        dict_tren['Rata-rata Lama Sekolah'] = pd.read_excel("rr.xlsx")
        dict_tren['Jumlah Sekolah'] = pd.read_excel("SK.xlsx")
        dict_tren['Jumlah Guru'] = pd.read_excel("gr.xlsx")
        
        # Standardisasi nama kolom & penyamaan istilah singkatan wilayah
        for key in dict_tren:
            # Bersihkan spasi pada nama kolom
            dict_tren[key].columns = [c.strip() if isinstance(c, str) else c for c in dict_tren[key].columns]
            
            # Cari kolom kabupaten/kota tanpa sensitif huruf besar/kecil
            kolom_target = None
            for c in dict_tren[key].columns:
                if str(c).lower().strip() in ['kabupaten/kota', 'kabupaten/kota']:
                    kolom_target = c
                    break
            
            if kolom_target is not None:
                # 🌟 KUNCI PERBAIKAN: Mengubah "kab." menjadi "kabupaten" secara otomatis di memori
                dict_tren[key]['Kabupaten/kota_clean'] = (
                    dict_tren[key][kolom_target].astype(str)
                    .str.lower()
                    .str.replace(r'^kab\.', 'kabupaten', regex=True) # Mengubah kab. di awal kalimat
                    .str.replace(r'^kab ', 'kabupaten ', regex=True) # Mengubah kab tanpa titik di awal kalimat
                    .str.replace(r'^kta\.', 'kota', regex=True)      # Mengubah kta. jika ada
                    .str.strip()
                )
    except Exception as e:
        st.sidebar.error(f"Gagal memuat beberapa file tren spasial. Pastikan format nama file excel sesuai: {e}")
            
    return df_tahunan, df_kondisi, dict_tren

df_tahunan, df_kondisi, dict_tren = load_data()

# =====================================================================
# 5. NAVIGASI DI SEBELAH KIRI (SIDEBAR)
# =====================================================================
with st.sidebar:
    st.title("🧩 Menu Navigasi")
    menu_pilihan = st.radio(
        "Pilih Halaman Analisis:",
        [
            "Informasi Pendidikan Jawa Timur", 
            "Dashboard Kondisi Pendidikan", 
            "Cluster Kabupaten/kota"
        ],
        label_visibility="collapsed" 
    )
    st.markdown("---")
    st.caption("Dashboard Pendidikan Jatim by Ulva 2.5")


# =====================================================================
# KONTEN UNTUK HALAMAN 1
# =====================================================================
if menu_pilihan == "Informasi Pendidikan Jawa Timur":
    st.markdown("""
    <div style="
        background-color: #E8F5E9; border: 1px solid #A5D6A7; border-radius: 14px; 
        padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); margin-bottom: 25px;
    ">
        <h2 style="color: #1B5E20; margin: 0; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
            Sebaran Geografis & Tabel Data Utama Jawa Timur
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # =====================================================================
    # 🟢 PROFILE RINGKAS JAWA TIMUR (BUBBLE INFO CARDS DI SINI)
    # =====================================================================
    col_b1, col_b2, col_b3, col_b4 = st.columns(4)

    with col_b1:
        st.markdown("""
        <div style="
            background-color: #0D47A1; border-radius: 20px; padding: 22px 15px; text-align: center;
            box-shadow: 15 4px 10px rgba(15,15,0,0.08); display: flex; flex-direction: column; 
            justify-content: center; align-items: center; min-height: 125px; margin-bottom: 25px;
        ">
            <span style="font-size: 15px; color: #BBDEFB; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px;">
                Ibu Kota Provinsi
            </span>
            <span style="font-size: 24px; color: #FFFFFF; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
                SURABAYA
            </span>
        </div>
        """, unsafe_allow_html=True)

    with col_b2:
        st.markdown("""
        <div style="
            background-color: #1B5E20; border-radius: 20px; padding: 22px 15px; text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08); display: flex; flex-direction: column; 
            justify-content: center; align-items: center; min-height: 125px; margin-bottom: 25px;
        ">
            <span style="font-size: 15px; color: #C8E6C9; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px;">
                Jumlah Wilayah
            </span>
            <span style="font-size: 24px; color: #FFFFFF; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
                38 Kab/Kota
            </span>
            <span style="font-size: 15px; color: #E8F5E9; font-weight: 500; margin-top: 2px;">
                (29 Kabupaten & 9 Kota)
            </span>
        </div>
        """, unsafe_allow_html=True)

    with col_b3:
        st.markdown("""
        <div style="
            background-color: #E65100; border-radius: 20px; padding: 22px 15px; text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08); display: flex; flex-direction: column; 
            justify-content: center; align-items: center; min-height: 125px; margin-bottom: 25px;
        ">
            <span style="font-size: 15px; color: #FFE0B2; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px;">
                Jumlah Penduduk
            </span>
            <span style="font-size: 24px; color: #FFFFFF; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
                42.089.300	
            </span>
            <span style="font-size: 15px; color: #FFF3E0; font-weight: 500; margin-top: 2px;">
                Jiwa
            </span>
        </div>
        """, unsafe_allow_html=True)

    with col_b4:
        st.markdown("""
        <div style="
            background-color: #4A148C; border-radius: 20px; padding: 22px 15px; text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08); display: flex; flex-direction: column; 
            justify-content: center; align-items: center; min-height: 125px; margin-bottom: 25px;
        ">
            <span style="font-size: 15px; color: #E1BEE7; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px;">
                Luas Wilayah Daratan
            </span>
            <span style="font-size: 24px; color: #FFFFFF; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
                48.055.880 Km²
            </span>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------------------
    # SEKSI MAPS (PETA INTERAKTIF)
    # -----------------------------------------------------------------
    st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                Peta Interaktif Distribusi Variabel
            </h3>
        </div>
        """, unsafe_allow_html=True)
    
    daftar_variabel_peta = [col for col in df_kondisi.columns if col != 'Kabupaten/kota']
    variabel_peta_terpilih = st.selectbox("Pilih Indikator yang Ingin Dilihat pada Peta:", daftar_variabel_peta, key="filter_peta")
    
    df_peta = df_kondisi.copy()
    df_peta['lat'] = df_peta['Kabupaten/kota'].apply(lambda x: ambil_lat_lon(x)[0])
    df_peta['lon'] = df_peta['Kabupaten/kota'].apply(lambda x: ambil_lat_lon(x)[1])
    df_peta['Nilai Terformat'] = df_peta[variabel_peta_terpilih].apply(format_angka_id)
    
    fig_map = px.scatter_mapbox(
        df_peta, lat="lat", lon="lon", hover_name="Kabupaten/kota",
        hover_data={"lat": False, "lon": False, variabel_peta_terpilih: False, "Nilai Terformat": True},
        color=variabel_peta_terpilih, size=variabel_peta_terpilih,
        color_continuous_scale="YlGnBu", size_max=18, zoom=7.1,
        center={"lat": -7.68, "lon": 112.6}, mapbox_style="open-street-map", height=550
    )
    fig_map.update_layout(margin={"r":0,"t":10,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)
    
    # -----------------------------------------------------------------
    # SEKSI TABULAR DATA
    # -----------------------------------------------------------------
    st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                Data Tabular Kondisi Pendidikan Seluruh Wilayah
            </h3>
        </div>
        """, unsafe_allow_html=True)
    
    df_tabel_tampil = df_kondisi.copy()
    for col in df_tabel_tampil.columns:
        if col != 'Kabupaten/kota':
            df_tabel_tampil[col] = df_tabel_tampil[col].apply(format_angka_id)
            
    st.dataframe(df_tabel_tampil, use_container_width=True, hide_index=True)

# =====================================================================
# KONTEN UNTUK HALAMAN 2 (VERSI HIJAU BOLD SEGAR & BAYANGAN HITAM NYATA)
# =====================================================================
elif menu_pilihan == "Dashboard Kondisi Pendidikan":
    st.markdown("""
    <div style="
        background-color: #2E7D32; border-radius: 14px; 
        padding: 20px; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.45); margin-bottom: 25px;
    ">
        <h2 style="color: #FFFFFF; margin: 0; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
            Dashboard Analisis & Tren Kondisi Pendidikan
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    daftar_tahun = [col for col in df_tahunan.columns if col != 'Fitur']
    tahun_terpilih = st.selectbox("Pilih Tahun Analisis:", daftar_tahun, index=len(daftar_tahun)-1)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Grid untuk Metric Cards Utama
    kolom_grid = st.columns(4)
    for idx, row in df_tahunan.iterrows():
        nama_variabel = row['Fitur']
        nilai_mentah = row[tahun_terpilih]
        nilai_terformat = format_angka_id(nilai_mentah)
        
        card_html = f"""
        <div style="
            background-color: #184332; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 14px; 
            padding: 20px 15px; text-align: center; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.45);
            margin-bottom: 20px; min-height: 130px; display: flex; flex-direction: column;
            justify-content: center; align-items: center;
        ">
            <span style="font-size: 13px; color: #FFFFFF; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; line-height: 1.3; margin-bottom: 8px; display: block;">
                {nama_variabel}
            </span>
            <span style="font-size: 26px; color: #FFFFFF; font-weight: 800; font-family: 'Source Sans Pro', sans-serif; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
                {nilai_terformat}
            </span>
        </div>
        """
        with kolom_grid[idx % 4]:
            st.markdown(card_html, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------
    # 📉 1. GRAFIK GARIS TREN PERTUMBUHAN HISTORIS (FORMAL & PERBAIKAN DESIMAL)
    # -----------------------------------------------------------------
    st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                Analisis Tren Pertumbuhan dari Tahun ke Tahun
            </h3>
        </div>
        """, unsafe_allow_html=True)
    
    daftar_fitur_tren = df_tahunan['Fitur'].unique().tolist()
    fitur_tren_terpilih = st.selectbox("Pilih Fitur untuk Melihat Grafik Tren Garis:", daftar_fitur_tren)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    df_row_tren = df_tahunan[df_tahunan['Fitur'] == fitur_tren_terpilih]
    
    if not df_row_tren.empty:
        df_line = df_row_tren.melt(id_vars=['Fitur'], value_vars=daftar_tahun, var_name='Tahun', value_name='Nilai')
        
        # 🛠️ INTERVENSI KHUSUS UNTUK INDEKS PENDIDIKAN AGAR TIDAK TERBALIK 🛠️
        # Mengubah string '0,66' menjadi float 0.66 agar grafik naik secara matematis
        df_line['Nilai_Numerik'] = df_line['Nilai'].astype(str).str.replace(',', '.', regex=False)
        df_line['Nilai_Numerik'] = pd.to_numeric(df_line['Nilai_Numerik'], errors='coerce')
        
        # Simpan format teks asli Indonesia untuk label di atas titik grafik
        df_line['Nilai Terformat'] = df_line['Nilai']
        
        # Gambar grafik menggunakan Nilai_Numerik yang sudah valid secara matematika
        fig_line = px.line(
            df_line, x='Tahun', y='Nilai_Numerik',  # Menggunakan nilai numerik asli
            markers=True, 
            text='Nilai Terformat',                 # Tetap menampilkan teks format asli (0,66)
            labels={'Nilai_Numerik': fitur_tren_terpilih}
        )
        
        fig_line.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',   
            paper_bgcolor='rgba(0,0,0,0)',  
            margin=dict(l=30, r=30, t=40, b=30),
            xaxis=dict(
                tickfont={'color': '#111111', 'size': 12, 'weight': 'bold'},
                showline=False, showgrid=True, gridcolor='#E2E8F0' 
            ),
            yaxis=dict(
                tickfont={'color': '#111111', 'size': 12, 'weight': 'bold'},
                showline=False, showgrid=True, gridcolor='#E2E8F0',
                # Berikan ruang ekstra batas atas agar teks nilai tidak terpotong garis tepi
                range=[df_line['Nilai_Numerik'].min() * 0.98, df_line['Nilai_Numerik'].max() * 1.02]
            ),
            height=380
        )
        fig_line.update_traces(
            line=dict(color='#2E7D32', width=3), 
            marker=dict(size=8, color='#1B5E20', line=dict(color='#FFFFFF', width=2)),
            textposition='top center',
            textfont=dict(color='#111111', size=12, family='Arial Black')
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("Data tren untuk variabel terpilih tidak ditemukan.")

    # Garis pemisah soft bawaan streamlit
    st.divider()

    # =====================================================================
    # 📊 2. GRAFIK FITUR KABUPATEN
    # =====================================================================
    # Garis pemisah soft bawaan streamlit sebelum masuk fitur baru
    st.divider()
        
        # =====================================================================
        # 📈 3. FITUR BARU: ANALISIS FLUKTUASI TAHUNAN PER KABUPATEN/KOTA
        # =====================================================================
    
    st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                Analisis Historis & Fluktuasi per Wilayah
            </h3>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px; color:#4A5568; margin-bottom:20px;'>Pilih wilayah spesifik beserta variabel indikator untuk melihat pola pergerakan dan fluktuasi tren data dari tahun ke tahun.</p>", unsafe_allow_html=True)
        
        # Kolom Filter Berdampingan
    col_filter_wilayah, col_filter_var = st.columns(2)
        
    with col_filter_wilayah:
        daftar_kab_kota = sorted(df_kondisi['Kabupaten/kota'].unique().tolist())
        default_index_kab = daftar_kab_kota.index("Kabupaten Banyuwangi") if "Kabupaten Banyuwangi" in daftar_kab_kota else 0
        kab_terpilih = st.selectbox("Pilih Kabupaten / Kota:", daftar_kab_kota, index=default_index_kab)
            
    with col_filter_var:
        daftar_var_tren = list(dict_tren.keys())
        var_tren_terpilih = st.selectbox("Pilih Fitur Analisis:", daftar_var_tren, index=2 if "Jumlah Murid" in daftar_var_tren else 0)
            
    if var_tren_terpilih in dict_tren:
        df_sumber_var = dict_tren[var_tren_terpilih]
        kab_clean_target = str(kab_terpilih).lower().strip()
            
        df_baris_kab = df_sumber_var[df_sumber_var['Kabupaten/kota_clean'] == kab_clean_target]
            
        if not df_baris_kab.empty:
            kolom_tahun_tren = [col for col in df_sumber_var.columns if col not in ['Kabupaten/kota', 'Kabupaten/Kota', 'Kabupaten/kota_clean']]
                
            df_melt_tren_kab = df_baris_kab.melt(
                value_vars=kolom_tahun_tren, 
                var_name='Tahun', 
                value_name='Nilai_Mentah'
            )
                
            df_melt_tren_kab['Tahun'] = df_melt_tren_kab['Tahun'].astype(str)
            df_melt_tren_kab = df_melt_tren_kab.sort_values(by='Tahun')
                
                # 🌟 FORMAT ADIL: Mengonversi langsung sesuai karakter angka murni bawaan file Excel Anda
            df_melt_tren_kab['Nilai_Bersih'] = pd.to_numeric(df_melt_tren_kab['Nilai_Mentah'], errors='coerce')
            df_melt_tren_kab['Nilai_Teks'] = df_melt_tren_kab['Nilai_Bersih'].apply(format_angka_id)
                
            fig_fluktuasi = px.line(
                df_melt_tren_kab, 
                x='Tahun', 
                y='Nilai_Bersih',
                markers=True,
                text='Nilai_Teks',
                labels={'Nilai_Bersih': var_tren_terpilih}
            )
                
            fig_fluktuasi.update_layout(
                title=dict(
                    text=f"📊 Grafik Tren Tahunan {var_tren_terpilih} - {kab_terpilih}",
                    font=dict(size=14, color="#1B5E20", family="Arial, sans-serif"),
                    pad=dict(b=10)
                ),
                plot_bgcolor='rgba(0,0,0,0)',   
                paper_bgcolor='rgba(0,0,0,0)',  
                margin=dict(l=20, r=20, t=50, b=30),
                xaxis=dict(
                    tickfont={'color': '#111111', 'size': 12, 'weight': 'bold'},
                    showline=False, showgrid=True, gridcolor='#E2E8F0' 
                ),
                yaxis=dict(
                        tickfont={'color': '#111111', 'size': 12, 'weight': 'bold'},
                        showline=False, showgrid=True, gridcolor='#E2E8F0',
                        range=[
                            df_melt_tren_kab['Nilai_Bersih'].min() * 0.95, 
                            df_melt_tren_kab['Nilai_Bersih'].max() * 1.15  # <--- Diubah dari 1.05 ke 1.15
                        ]
                    ),
                height=390
            )
                
            fig_fluktuasi.update_traces(
                line=dict(color='#1B5E20', width=3.5), 
                marker=dict(size=9, color='#2E7D32', line=dict(color='#FFFFFF', width=2)),
                textposition='top center',
                textfont=dict(color='#1B5E20', size=11, family='Arial Black')
            )
                
            st.plotly_chart(fig_fluktuasi, use_container_width=True)
        else:
            st.warning(f"Data untuk {kab_terpilih} tidak ditemukan dalam catatan historis {var_tren_terpilih}.")
    else:
        st.warning("Variabel analisis tidak termuat dengan sempurna.")

    # -----------------------------------------------------------------
    # 3. GRAFIK BATANG PERBANDINGAN WILAYAH (WARNA CUSTOM & SOLID BG)
    # -----------------------------------------------------------------
    st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 22px; font-family: 'Source Sans Pro', sans-serif;">
                Analisis Perbandingan Tingkat Kabupaten/Kota
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
    daftar_variabel = [col for col in df_kondisi.columns if col != 'Kabupaten/kota' and col != 'Cluster']
    variabel_terpilih = st.selectbox("Pilih Variabel yang Ingin Ditampilkan pada Grafik Batang:", daftar_variabel)
    
    mode_grafik = st.radio(
        "Pilih Cakupan Wilayah pada Grafik Batang:",
        ["5 Tertinggi & Terendah", "Tampilkan Seluruh 38 Kabupaten/Kota"], horizontal=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)

    if mode_grafik == "5 Tertinggi & Terendah":
        top_5 = df_kondisi.nlargest(5, variabel_terpilih).copy()
        bottom_5 = df_kondisi.nsmallest(5, variabel_terpilih).copy()
        
        top_5['label_format'] = top_5[variabel_terpilih].apply(format_angka_id)
        bottom_5['label_format'] = bottom_5[variabel_terpilih].apply(format_angka_id)
        
        col_grafik_kiri, col_grafik_kanan = st.columns(2)
        
        with col_grafik_kiri:
            st.markdown("""
                <div style="background-color: #1B5E20; padding: 8px 15px; border-radius: 6px; margin-bottom: 12px;">
                    <h5 style="color: #FFFFFF; margin: 0; font-weight: 700; font-size: 15px; text-transform: uppercase;">
                        Lima Kabupaten/Kota Nilai Tertinggi
                    </h5>
                </div>
                """, unsafe_allow_html=True)
            
            # Gradasi warna Top 5: Hijau ke Kuning ('Greens_r' atau custom skala warna)
            fig_top = px.bar(
                top_5, x=variabel_terpilih, y="Kabupaten/kota", orientation='h', 
                color=variabel_terpilih, 
                color_continuous_scale=['#FFD600', '#4CAF50', '#1B5E20'], # Kuning ke Hijau Tua
                text='label_format'
            )
            fig_top.update_layout(
                plot_bgcolor='#ECEFF1',   # Latar belakang dalam grafik (Abu-abu gelap pekat, bukan putih)
                paper_bgcolor='#ECEFF1',  # Latar belakang luar grafik
                margin=dict(l=15, r=15, t=15, b=15), 
                xaxis=dict(
                    range=[0, top_5[variabel_terpilih].max() * 1.15], 
                    tickfont={'color': '#111111', 'size': 11, 'weight': 'bold'},
                    showline=False, showgrid=True, gridcolor='#CFD8DC'
                ),
                yaxis=dict(
                    categoryorder='total ascending',
                    tickfont={'color': '#111111', 'size': 12, 'weight': 'bold'},
                    showline=False, showgrid=False
                ),
                coloraxis_showscale=False,
                showlegend=False,
                height=350 
            )
            fig_top.update_traces(textposition='outside', textfont=dict(color='#111111', size=12, family='Arial Black'))
            st.plotly_chart(fig_top, use_container_width=True)
            
        with col_grafik_kanan:
            st.markdown("""
                <div style="background-color: #4A148C; padding: 8px 15px; border-radius: 6px; margin-bottom: 12px;">
                    <h5 style="color: #FFFFFF; margin: 0; font-weight: 700; font-size: 15px; text-transform: uppercase;">
                        Lima Kabupaten/Kota Nilai Terendah
                    </h5>
                </div>
                """, unsafe_allow_html=True)
            
            # Gradasi warna Bottom 5: Biru ke Ungu
            fig_bottom = px.bar(
                bottom_5, x=variabel_terpilih, y="Kabupaten/kota", orientation='h', 
                color=variabel_terpilih, 
                color_continuous_scale=['#2979FF', '#7C4DFF', '#4A148C'], # Biru ke Ungu Tua
                text='label_format'
            )
            fig_bottom.update_layout(
                plot_bgcolor='#ECEFF1',   # Latar belakang dalam grafik (Abu-abu gelap pekat, bukan putih)
                paper_bgcolor='#ECEFF1',  # Latar belakang luar grafik
                margin=dict(l=15, r=15, t=15, b=15),
                xaxis=dict(
                    range=[0, bottom_5[variabel_terpilih].max() * 1.15], 
                    tickfont={'color': '#111111', 'size': 11, 'weight': 'bold'},
                    showline=False, showgrid=True, gridcolor='#CFD8DC'
                ),
                yaxis=dict(
                    categoryorder='total descending',
                    tickfont={'color': '#111111', 'size': 12, 'weight': 'bold'},
                    showline=False, showgrid=False
                ),
                coloraxis_showscale=False,
                showlegend=False,
                height=350
            )
            fig_bottom.update_traces(textposition='outside', textfont=dict(color='#111111', size=12, family='Arial Black'))
            st.plotly_chart(fig_bottom, use_container_width=True)
            
    else:
        df_seluruh = df_kondisi.sort_values(by=variabel_terpilih, ascending=True).copy()
        df_seluruh['label_format'] = df_seluruh[variabel_terpilih].apply(format_angka_id)
        
        st.markdown(f"""
            <div style="background-color: #1B5E20; padding: 10px 18px; border-radius: 6px; margin-bottom: 15px;">
                <h4 style="color: #FFFFFF; margin: 0; font-weight: 700; font-size: 16px; text-transform: uppercase;">
                    Seluruh Wilayah ({variabel_terpilih})
                </h4>
            </div>
            """, unsafe_allow_html=True)
        
        fig_all = px.bar(
            df_seluruh, x=variabel_terpilih, y="Kabupaten/kota", orientation='h', 
            color=variabel_terpilih, 
            color_continuous_scale='Cividis', 
            text='label_format'
        )
        fig_all.update_layout(
            height=900,
            plot_bgcolor='#ECEFF1',   # Latar belakang solid pekat
            paper_bgcolor='#ECEFF1',  # Latar belakang solid pekat
            margin=dict(l=15, r=15, t=15, b=15),
            xaxis=dict(
                range=[0, df_seluruh[variabel_terpilih].max() * 1.12], 
                tickfont={'color': '#111111', 'size': 11, 'weight': 'bold'},
                showline=False, showgrid=True, gridcolor='#CFD8DC'
            ),
            yaxis=dict(
                tickfont={'color': '#111111', 'size': 11, 'weight': 'bold'},
                showline=False, showgrid=False
            ),
            coloraxis_showscale=False,
            showlegend=False
        )
        fig_all.update_traces(textposition='outside', textfont=dict(color='#111111', size=11, family='Arial Black'))
        st.plotly_chart(fig_all, use_container_width=True)


# =====================================================================
# KONTEN UNTUK HALAMAN 3 (WARNA KLASTER: 0=MERAH, 1=BIRU, 2=HIJAU)
# =====================================================================
elif menu_pilihan == "Cluster Kabupaten/kota":
    st.markdown("""
    <div style="
        background-color: #E8F5E9; border: 2px solid #81C784; border-radius: 14px; 
        padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); margin-bottom: 25px;
    ">
        <h2 style="color: #1B5E20; margin: 0; font-weight: 800; font-family: 'Source Sans Pro', sans-serif;">
            Analisis Hasil Clustering Wilayah
        </h2>
        <p style="color: #2E7D32; margin: 8px 0 0 0; font-size: 14px; line-height: 1.5;">
            Pengelompokan wilayah Jawa Timur berdasarkan kemiripan indikator pencapaian dan infrastruktur pendidikan.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'Cluster' not in df_kondisi.columns:
        st.warning("Kolom 'Cluster' tidak ditemukan di data utama. Pastikan dataset 'dttp.xlsx' sudah memiliki hasil klaster.")
    else:
        df_cluster = df_kondisi.copy()
        df_cluster['Cluster'] = df_cluster['Cluster'].astype(str).apply(lambda x: f"Klaster {x}")
        df_cluster = df_cluster.sort_values(by='Cluster')

        # 🎨 DEFINISI PEMETAAN WARNA KLASTER SESUAI PERMINTAAN
        peta_warna_klaster = {
            "Klaster 1": "#E53E3E",  # Merah
            "Klaster 2": "#3182CE",  # Biru
            "Klaster 3": "#38A169"   # Hijau
        }

        # -----------------------------------------------------------------
        # BAGIAN 1: PETA SEBARAN KLASTER
        # -----------------------------------------------------------------
        st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                📍 Peta Geografis Distribusi Cluster
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        df_peta_cluster = df_cluster.copy()
        df_peta_cluster['lat'] = df_peta_cluster['Kabupaten/kota'].apply(lambda x: ambil_lat_lon(x)[0])
        df_peta_cluster['lon'] = df_peta_cluster['Kabupaten/kota'].apply(lambda x: ambil_lat_lon(x)[1])
        
        fig_map_cluster = px.scatter_mapbox(
            df_peta_cluster, lat="lat", lon="lon", 
            hover_name="Kabupaten/kota",
            hover_data={"lat": False, "lon": False, "Cluster": True},
            color="Cluster",
            color_discrete_map=peta_warna_klaster, # <--- Menggunakan peta warna kustom
            zoom=7.1, center={"lat": -7.68, "lon": 112.6}, 
            mapbox_style="open-street-map", height=450
        )
        fig_map_cluster.update_layout(
            margin={"r":0,"t":10,"l":0,"b":0},
            legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.02, bgcolor="rgba(255,255,255,0.8)")
        )
        st.plotly_chart(fig_map_cluster, use_container_width=True)
        
        st.divider()

        # -----------------------------------------------------------------
        # 🟢 SEKSI BARU: DIAGRAM DONAT & FITUR INTERAKTIF PILIHAN DAERAH
        # -----------------------------------------------------------------
        st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                Proporsi & Eksplorasi Anggota Cluster
            </h3>
        </div>
        """, unsafe_allow_html=True)

        df_counts = df_cluster['Cluster'].value_counts().reset_index()
        df_counts.columns = ['Cluster', 'Jumlah']
        df_counts = df_counts.sort_values(by='Cluster')

        col_donut, col_select = st.columns([1, 1])

        with col_donut:
            st.markdown("<h5 style='color: #1B5E20; font-weight:700; margin-bottom:10px;'>Persentase Jumlah Kabupaten/Kota</h5>", unsafe_allow_html=True)
            
            fig_donut = px.pie(
                df_counts, 
                values='Jumlah', 
                names='Cluster',
                hole=0.45,  
                color='Cluster',
                color_discrete_map=peta_warna_klaster, # <--- Menggunakan peta warna kustom
            )
            fig_donut.update_traces(textposition='inside', textinfo='percent+label')
            fig_donut.update_layout(
                margin=dict(t=10, b=10, l=10, r=10),
                showlegend=False,
                height=320
            )
            st.plotly_chart(fig_donut, use_container_width=True)

        with col_select:
            st.markdown("<h5 style='color: #1B5E20; font-weight:700; margin-bottom:10px;'>Daftar Wilayah Anggota Cluster</h5>", unsafe_allow_html=True)
            
            pilihan_cluster = sorted(df_cluster['Cluster'].unique())
            cluster_terpilih = st.selectbox(
                "Silakan pilih cluster untuk melihat daerah di dalamnya:", 
                options=pilihan_cluster
            )
            
            daerah_terfilter = df_cluster[df_cluster['Cluster'] == cluster_terpilih]['Kabupaten/kota'].tolist()
            daerah_terfilter = sorted(daerah_terfilter)
            
            st.markdown(f"Total: **{len(daerah_terfilter)} Wilayah** terdaftar di `{cluster_terpilih}`")
            
            html_table_rows = ""
            for idx, daerah in enumerate(daerah_terfilter, start=1):
                bg_color = "#FFFFFF" if idx % 2 == 0 else "#F8F9FA"
                html_table_rows += f"""
                <tr style='background-color: {bg_color}; border-bottom: 1px solid #E2E8F0;'>
                    <td style='padding: 8px 12px; width: 50px; color: #718096; text-align: center;'>{idx}</td>
                    <td style='padding: 8px 12px; font-weight: 500; color: #2D3748;'>{daerah}</td>
                </tr>
                """
            
            st.markdown(f"""
                <div style="
                    background-color: #FFFFFF; 
                    border: 1px solid #CBD5E1; 
                    border-radius: 8px; 
                    max-height: 215px; 
                    overflow-y: auto;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
                ">
                    <table style="width: 100%; border-collapse: collapse; font-family: sans-serif; font-size: 14px;">
                        <thead>
                            <tr style="background-color: #EDF2F7; border-bottom: 2px solid #CBD5E1; text-align: left;">
                                <th style="padding: 10px 12px; color: #4A5568; font-weight: 600; text-align: center;">No</th>
                                <th style="padding: 10px 12px; color: #4A5568; font-weight: 600;">Nama Kabupaten / Kota</th>
                            </tr>
                        </thead>
                        <tbody>
                            {html_table_rows}
                        </tbody>
                    </table>
                </div>
            """, unsafe_allow_html=True)

        st.divider()

        # -----------------------------------------------------------------
        # BAGIAN 2: SCATTER PLOT ANALISIS KORELASI ANTAR VARIABEL
        # -----------------------------------------------------------------
        st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                📊 Scatter Plot Analisis Karakteristik Cluster
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        kolom_fitur = [col for col in df_kondisi.columns if col not in ['Kabupaten/kota', 'Cluster']]
        
        col_x, col_y = st.columns(2)
        with col_x:
            sumbu_x = st.selectbox("Pilih Indikator Sumbu X:", kolom_fitur, index=0)
        with col_y:
            sumbu_y = st.selectbox("Pilih Indikator Sumbu Y:", kolom_fitur, index=len(kolom_fitur)-1 if len(kolom_fitur) > 1 else 0)
            
        fig_scatter = px.scatter(
            df_cluster, x=sumbu_x, y=sumbu_y, 
            color="Cluster",
            hover_name="Kabupaten/kota",
            color_discrete_map=peta_warna_klaster, # <--- Menggunakan peta warna kustom
            text="Kabupaten/kota"
        )
        fig_scatter.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',   
            paper_bgcolor='rgba(0,0,0,0)',  
            margin=dict(l=20, r=20, t=20, b=40),
            xaxis=dict(title=dict(text=sumbu_x, font=dict(weight='bold')), showgrid=True, gridcolor='#E2E8F0'),
            yaxis=dict(title=dict(text=sumbu_y, font=dict(weight='bold')), showgrid=True, gridcolor='#E2E8F0'),
            height=480
        )
        fig_scatter.update_traces(
            marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')),
            textposition='top center',
            textfont=dict(size=9, color='#4A5568')
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        st.divider()

        # -----------------------------------------------------------------
        # BAGIAN 3: KARAKTERISTIK HASIL CLUSTER (STATISTIK DESKRIPTIF LENGKAP)
        # -----------------------------------------------------------------
        st.markdown("""
        <div style="background-color: #1B5E20; padding: 12px 20px; border-radius: 50px; margin-bottom: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #FFFFFF; font-weight: bold; margin: 0; font-size: 25px; font-family: 'Source Sans Pro', sans-serif;">
                📋 Karakteristik & Profil Statistik Hasil Cluster
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='font-size:14px; color:#4A5568; margin-top:10px; margin-bottom:20px;'>Analisis makro komparatif nilai sebaran (Mean, Median, Min, Max) bersandarkan klasifikasi acuan BPS dan Dinas Perpustakaan.</p>", unsafe_allow_html=True)
        
        # Penyesuaian label warna tab agar selaras (0=Merah, 1=Biru, 2=Hijau)
        tab0, tab1, tab2 = st.tabs([
            "🔴 Cluster 1: Kapasitas Sedang & Literasi Kritikal", 
            "🔵 Cluster 2: Pusat Urban Mutu Tinggi", 
            "🟢 Cluster 3: Mega-Infrastruktur & Murid Masif"
        ])
        
        with tab0:
            st.markdown("""
            <div style='background-color: #FAFAFA; border-left: 5px solid #E53E3E; padding: 15px; border-radius: 4px;'>
                <h5 style='color: #9B2C2C; margin-top:0; font-weight:700;'>📌 Profil: Wilayah Pendukung dengan Tantangan Capaian Output</h5>
                <p style='font-size: 14px; line-height: 1.6; color: #2D3748;'>
                    Cluster ini mengelompokkan wilayah dengan ketersediaan sarana fisik tingkat menengah namun memiliki urgensi tinggi pada peningkatan mutu literasi masyarakat.
                </p>
                <table style='width:100%; font-size:13px; border-collapse: collapse; margin-top:10px;'>
                    <tr style='background-color: #FFF5F5; font-weight:bold; color:#9B2C2C; border-bottom:2px solid #E53E3E;'>
                        <th style='padding:8px; text-align:left;'>Indikator Pendidikan</th>
                        <th style='padding:8px; text-align:center;'>Rerata (Mean)</th>
                        <th style='padding:8px; text-align:center;'>Median</th>
                        <th style='padding:8px; text-align:center;'>Min</th>
                        <th style='padding:8px; text-align:center;'>Max</th>
                        <th style='padding:8px; text-align:left;'>Keterangan</th>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Indeks Pendidikan</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.626</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.625</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.520</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.730</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#D69E2E; font-weight:600;'>Kategori Sedang (60 - 69.9 BPS)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Indeks Literasi</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>11.695</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>10.350</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>2.520</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>30.520</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#E53E3E; font-weight:600;'>Kategori Sangat Rendah (&lt; 29.9)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Rata-rata Lama Sekolah (Th)</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>8.265</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>8.315</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>6.240</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>10.350</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#D69E2E; font-weight:600;'>Kategori Sedang (Setara Kelas 2 SMP)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Jumlah Sekolah</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>1936.96</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>1932.5</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>1198</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>3362</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'>1198-3362 (Kapasitas kelembagaan tingkat menengah)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Jumlah Murid</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>161.528</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>161.559</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>79.994</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>282.910</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'>(79.994-282.910) Populasi siswa binaan stabil-tinggi</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Rasio Murid/Guru</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>14.794</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>14.638</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>10.264</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>18.056</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#2F855A; font-weight:600;'>1 guru mengajar 10-18 murid (Interaksi kelas kondusif)</td>
                    </tr>
                </table>
                <p style='font-size: 13px; color: #718096; margin-top: 12px; font-style: italic;'>
                    💡 <b>Rekomendasi Kebijakan:</b> Memprioritaskan program stimulasi non-fisik (revitalisasi minat baca daerah, penambahan ruang baca publik) guna mendongkrak ketimpangan indeks literasi makro yang masih tertinggal.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with tab1:
            st.markdown("""
            <div style='background-color: #FAFAFA; border-left: 5px solid #2B6CB0; padding: 15px; border-radius: 4px;'>
                <h5 style='color: #2B6CB0; margin-top:0; font-weight:700;'>📌 Profil: Wilayah Pusat Perkotaan (Urban) Efisiensi Tinggi</h5>
                <p style='font-size: 14px; line-height: 1.6; color: #2D3748;'>
                    Klaster ini mencerminkan karakteristik wilayah urban/kota. Infrastruktur kuantitas bangunan sekolah relatif sedikit, namun memiliki efisiensi tinggi serta luaran SDM unggul.
                </p>
                <table style='width:100%; font-size:13px; border-collapse: collapse; margin-top:10px;'>
                    <tr style='background-color: #EBF8FF; font-weight:bold; color:#2B6CB0; border-bottom:2px solid #2B6CB0;'>
                        <th style='padding:8px; text-align:left;'>Indikator Pendidikan</th>
                        <th style='padding:8px; text-align:center;'>Rerata (Mean)</th>
                        <th style='padding:8px; text-align:center;'>Median</th>
                        <th style='padding:8px; text-align:center;'>Min</th>
                        <th style='padding:8px; text-align:center;'>Max</th>
                        <th style='padding:8px; text-align:left;'>Keterangan</th>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Indeks Pendidikan</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.768</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.770</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.710</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.820</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#2B6CB0; font-weight:600;'>Kategori Tinggi (Mendekati Sangat Tinggi)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Indeks Literasi</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>25.359</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>24.330</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>9.340</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>42.870</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#D69E2E; font-weight:600;'>Kategori Rendah-Sedang (Tertinggi antar Klaster)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Rata-rata Lama Sekolah (Th)</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>10.811</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>10.930</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>9.730</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>11.660</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#2B6CB0; font-weight:600;'>Kategori Sedang-Tinggi (Mayoritas Lulus SMA)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Jumlah Sekolah</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>452.50</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>338.0</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>231</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>1278</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'>231-1278 (Dominasi sekolah terpusat)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Jumlah Murid</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>66.075</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>45.260</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>36.426</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>191.188</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'>Jumlah murid 36.426-191.188 (Populasi padat terpusat wilayah urban)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Rasio Murid/Guru</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>16.444</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>16.225</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>15.645</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>18.202</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'>1 guru mengajar 15-18 murid (Standar perkotaan)</td>
                    </tr>
                </table>
                <p style='font-size: 13px; color: #718096; margin-top: 12px; font-style: italic;'>
                    💡 <b>Rekomendasi Kebijakan:</b> Mempertahankan mutu keunggulan, melakukan digitalisasi sistem pendidikan, serta menyebarluaskan kualitas kompetensi tenaga didik ke kawasan sub-urban di sekelilingnya.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with tab2:
            st.markdown("""
            <div style='background-color: #FAFAFA; border-left: 5px solid #38A169; padding: 15px; border-radius: 4px;'>
                <h5 style='color: #276749; margin-top:0; font-weight:700;'>📌 Profil: Wilayah Kabupaten Besar dengan Aglomerasi Masif</h5>
                <p style='font-size: 14px; line-height: 1.6; color: #2D3748;'>
                    Klaster ini diisi oleh daerah administrasi kabupaten besar yang menampung beban pelayanan pendidikan skala makro dengan jumlah siswa terbanyak.
                </p>
                <table style='width:100%; font-size:13px; border-collapse: collapse; margin-top:10px;'>
                    <tr style='background-color: #E6FFFA; font-weight:bold; color:#276749; border-bottom:2px solid #38A169;'>
                        <th style='padding:8px; text-align:left;'>Indikator Pendidikan</th>
                        <th style='padding:8px; text-align:center;'>Rerata (Mean)</th>
                        <th style='padding:8px; text-align:center;'>Median</th>
                        <th style='padding:8px; text-align:center;'>Min</th>
                        <th style='padding:8px; text-align:center;'>Max</th>
                        <th style='padding:8px; text-align:left;'>Keterangan</th>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Indeks Pendidikan</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.705</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.715</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.600</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>0.790</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#2F855A; font-weight:600;'>Kategori Tinggi (Pencapaian Sangat Baik)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Indeks Literasi</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>23.570</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>8.395</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>5.590</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>71.900</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#D69E2E; font-weight:600;'>Kategori Rendah (Variansi sebaran lebar)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Rata-rata Lama Sekolah (Th)</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>9.600</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>9.825</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>7.290</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>11.460</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#D69E2E; font-weight:600;'>Kategori Sedang (Setara Lulus Lulus SMP)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Jumlah Sekolah</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>3395.75</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>3548.5</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>2638</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>3848</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#276749; font-weight:600;'>2638-3848 (Infrastruktur Sangat Masif)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Jumlah Murid</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>422.759</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>397.604</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>363.617</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>532.214</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#276749; font-weight:600;'> 363.617-532.214 (Beban Layanan Publik Sangat Ekstrem)</td>
                    </tr>
                    <tr>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0;'><b>Rasio Murid/Guru</b></td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>17.593</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>17.632</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>16.847</td>
                        <td style='padding:8px; text-align:center; border-bottom:1px solid #E2E8F0;'>18.260</td>
                        <td style='padding:8px; border-bottom:1px solid #E2E8F0; color:#E53E3E; font-weight:600;'>1 guru mengajar 16-18 murid (Beban mengajar berat)</td>
                    </tr>
                </table>
                <p style='font-size: 13px; color: #718096; margin-top: 12px; font-style: italic;'>
                    💡 <b>Rekomendasi Kebijakan:</b> Mengakselerasi penambahan jumlah guru/tendik guna mereduksi beban kerja rasio kelas, serta memperkuat daya dukung fasilitas agar mutu keluaran tidak tergradasi oleh besarnya jumlah murid.
                </p>
            </div>
            """, unsafe_allow_html=True)