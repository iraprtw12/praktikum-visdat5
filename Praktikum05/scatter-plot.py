import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# dataset utama
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# dataset penjualan
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# data analisis
data = {
    'Suhu': suhu,
    'Penjualan_Cokelat': [40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanila': [82, 80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Stroberi': [55, 50, 55, 60, 65, 60, 65, 70, 72],
    'Kelembapan': [50, 60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

# layout utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header("Pengaturan Visualisasi")

option = st.sidebar.selectbox(
    "Pilih contoh Scatter Plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# Identitas
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
Kelompok 34:
- Chika Karena
- Chery Renata
- Ira Pratiwi
""")

# -------------------------------------------
# 1. Basic Scatter Plot
# -------------------------------------------
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# -------------------------------------------
# 2. Kustomisasi Scatter Plot
# -------------------------------------------
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# -------------------------------------------
# 3. Multiple Scatter Plot
# -------------------------------------------
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekend, label='Akhir Pekan', s=80)
    ax.set_title('Perbandingan Penjualan Hari Kerja vs Akhir Pekan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# -------------------------------------------
# 4. Analisis Scatter Plot
# -------------------------------------------
def scatter_3_variabel():
    st.subheader("4. Analisis Scatter Plot")

    jenis_eskrim = st.selectbox(
        'Pilih Jenis Es Krim',
        ['Cokelat', 'Vanila', 'Stroberi']
    )

    if jenis_eskrim == 'Cokelat':
        penjualan_x = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        penjualan_x = df['Penjualan_Vanila']
    else:
        penjualan_x = df['Penjualan_Stroberi']

    st.subheader("Data Penjualan & Suhu")
    st.dataframe(df)

    fig, ax = plt.subplots()
    scatter = ax.scatter(
        df['Suhu'], penjualan_x,
        c=df['Kelembapan'], s=100,
        cmap='coolwarm', alpha=0.7
    )

    ax.set_title(f'Penjualan {jenis_eskrim} vs Suhu & Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')

    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    st.subheader("Analisis Hubungan")
    st.write(
        f"Grafik menunjukkan hubungan antara suhu, kelembapan, "
        f"dan penjualan es krim **{jenis_eskrim}**."
    )

# ROUTING
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variabel()
