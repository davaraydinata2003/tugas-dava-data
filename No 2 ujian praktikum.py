#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hitung_gaji_pokok(golongan):
    if golongan == 'A':
        return 10000000
    elif golongan == 'B':
        return 7000000
    elif golongan == 'C':
        return 5000000
    elif golongan == 'D':
        return 3000000
    else:
        return 0

def hitung_gaji_total(golongan, jam_kerja):
    gaji_pokok = hitung_gaji_pokok(golongan)
    if jam_kerja > 48:
        gaji_lembur = (jam_kerja - 40) * (gaji_pokok / 40) * 1.5
        gaji_total = gaji_pokok + gaji_lembur
    else:
        gaji_total = gaji_pokok
    return gaji_total

while True:
    golongan = input("Masukkan golongan karyawan (A/B/C/D): ")
    jam_kerja = float(input("Masukkan jam kerja per bulan: "))

    if golongan in ['A', 'B', 'C', 'D'] and jam_kerja >= 0:
        gaji_total = hitung_gaji_total(golongan, jam_kerja)
        print("Gaji pokok karyawan:", hitung_gaji_pokok(golongan))
        print("Gaji total karyawan:", gaji_total)
        break
    else:
        print("Input tidak valid. Silakan coba lagi.")


# In[ ]:




