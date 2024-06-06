import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data
data = pd.read_csv('data_persediaan.csv')

# 1. Deskripsi Data
print("1. Deskripsi Data:")
print("   - Struktur data:")
print(data.head())
print("\n   - Jumlah entri data:", len(data))
print("   - Jumlah atribut:", len(data.columns))

# 2. Statistik Deskriptif
print("\n2. Statistik Deskriptif:")
print("   - Rata-rata jumlah barang yang tersedia:", data['jumlah_barang'].mean())
print("   - Median jumlah barang yang tersedia:", data['jumlah_barang'].median())
print("   - Standar deviasi jumlah barang yang tersedia:", data['jumlah_barang'].std())
print("   - Barang dengan jumlah tersedia tertinggi:", data['nama_barang'].loc[data['jumlah_barang'].idxmax()])
print("   - Barang dengan jumlah tersedia terendah:", data['nama_barang'].loc[data['jumlah_barang'].idxmin()])

# 3. Data yang Hilang
print("\n3. Data yang Hilang:")
print(data.isnull().sum())

# 4. Visualisasi Data
plt.figure(figsize=(10, 8))

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(data['usia'], data['gaji'], color='blue', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Usia')
plt.ylabel('Gaji')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(data['gaji'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Gaji')
plt.xlabel('Gaji')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(data['usia'].dropna())
plt.title('Box Plot of Usia')
plt.ylabel('Usia')

# Bar Plot
plt.subplot(2, 2, 4)
gender_data = data['jenis_kelamin'].value_counts()
plt.bar(gender_data.index, gender_data.values, color=['blue', 'pink'])
plt.title('Barplot Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
