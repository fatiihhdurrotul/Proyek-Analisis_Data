import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Membaca dataset

data = pd.read_csv("dataset.csv")


# Menghitung rata-rata penyewaan sepeda berdasarkan hari libur dan hari kerja
holiday_workingday = data.groupby(['holiday', 'workingday'])['cnt'].mean().unstack()
fig, ax = plt.subplots(figsize=(8, 6))

# Membuat plot diagram batang untuk perbandingan hari libur dan hari kerja
holiday_workingday.plot(kind='bar', ax=ax, color=['lightcoral', 'mediumseagreen'])
st.title('Pola Penyewaan Sepeda berdasarkan Hari Kerja dan Libur')
ax.set_title('Average Rentals on Holidays vs Working Days')
ax.set_ylabel('Average Rentals')
ax.set_xlabel('Holiday (0 = No, 1 = Yes)')
ax.legend(['Not Working Day', 'Working Day'])
plt.tight_layout()

# Menampilkan plot pertama di Streamlit
st.pyplot(fig)

# Menghitung total penyewaan sepeda berdasarkan tahu
yearly_rentals = data.groupby('yr')['cnt'].sum().reset_index()

# Membuat plot garis untuk tren penyewaan sepeda setiap tahun
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='yr', y='cnt', data=yearly_rentals, marker='o', linewidth=2.5, color='b', ax=ax)
st.title('Tren Penyewaan Sepeda dari Tahun ke Tahun')
ax.set_title('Total Bike Rentals per Year', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Total Rentals', fontsize=12)

# Menampilkan plot kedua di Streamlit
ax.grid(True)
st.pyplot(fig)
