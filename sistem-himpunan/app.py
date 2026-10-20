import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
st.title("Sistem klasifikasi Data Berbasis Teori Himpunan")

st.write(
    "Aplikasi untuk melakukan operasi himpunan"
    "berdasarkan data mahasiswa"
)
st.subheader("Pilih Dataset")

pilihan = st.selectbox(
    "Pilih kasus:",
    ["Kasus 1", "Kasus 2"]
)

if pilihan == "Kasus 1":
    df = pd.read_csv("dataset_kasus1.csv")
else:
    df = pd.read_csv("dataset_kasus2.csv")

st.write("Data yang digunakan:")
st.dataframe(df)
st.subheader("Pembentukan Himpunan")

kolom = df.columns.tolist()

kolom_a = st.selectbox(
    "Pilih kriteria untuk Himpunan A:",
    kolom,
    key="A"
)

kolom_b = st.selectbox(
    "Pilih kriteria untuk Himpunan B:",
    kolom,
    key="B"
)

kolom_c = st.selectbox(
    "Pilih kriteria untuk Himpunan C:",
    kolom,
    key="C"
)
st.subheader("Nilai Himpunan")

nilai_a = st.selectbox(
    "Pilih nilai untuk Himpunan A:",
    df[kolom_a].unique(),
    key="nilai_A"
)

nilai_b = st.selectbox(
    "Pilih nilai untuk Himpunan B:",
    df[kolom_b].unique(),
    key="nilai_B"
)

nilai_c = st.selectbox(
    "Pilih nilai untuk Himpunan C:",
    df[kolom_c].unique(),
    key="nilai_C"
)
st.subheader("Operasi Himpunan")

set_a = set(df[df[kolom_a] == nilai_a]["Nama"])
set_b = set(df[df[kolom_b] == nilai_b]["Nama"])
set_c = set(df[df[kolom_c] == nilai_c]["Nama"])

union = set_a | set_b | set_c

st.write("Hasil Union (A ∪ B ∪ C):")
st.write(sorted(union))
intersection = set_a & set_b & set_c

st.write("Hasil Intersection (A ∩ B ∩ C):")
st.write(sorted(intersection))
difference = set_a - set_b

st.write("Hasil Difference (A − B):")
st.write(sorted(difference))
universal = set(df["Nama"])

complement_a = universal - set_a
complement_b = universal - set_b
complement_c = universal - set_c

st.write("Hasil Complement Aᶜ:")
st.write(sorted(complement_a))

st.write("Hasil Complement Bᶜ:")
st.write(sorted(complement_b))

st.write("Hasil Complement Cᶜ:")
st.write(sorted(complement_c))
st.subheader("Diagram Venn")

fig, ax = plt.subplots()

venn3(
    [set_a, set_b, set_c],
    set_labels=("A", "B", "C"),
    ax=ax
)

st.pyplot(fig)
plt.close(fig)
st.subheader("Perhitungan Inclusion-Exclusion (PIE)")

ab = len(set_a & set_b)
ac = len(set_a & set_c)
bc = len(set_b & set_c)

abc = len(set_a & set_b & set_c)

pie = (
    len(set_a)
    + len(set_b)
    + len(set_c)
    - ab
    - ac
    - bc
    + abc
)

st.write("Jumlah A:", len(set_a))
st.write("Jumlah B:", len(set_b))
st.write("Jumlah C:", len(set_c))

st.write("A ∩ B:", ab)
st.write("A ∩ C:", ac)
st.write("B ∩ C:", bc)
st.write("A ∩ B ∩ C:", abc)

st.write("Hasil PIE |A ∪ B ∪ C|:", pie)