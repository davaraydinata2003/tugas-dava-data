#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math

class BangunGeometri:
    def luas_trapesium(self, alas, tinggi, sisi_miring):
        return 0.5 * (alas + sisi_miring) * tinggi

    def luas_lingkaran(self, jari_jari):
        return math.pi * jari_jari ** 2

    def luas_balok(self, panjang, lebar, tinggi):
        return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

    def luas_segitiga(self, alas, tinggi):
        return 0.5 * alas * tinggi

    def luas_persegi_panjang(self, panjang, lebar):
        return panjang * lebar

    def luas_persegi(self, sisi):
        return sisi ** 2

bangun = BangunGeometri()

alas = 9
tinggi = 6
sisi_miring = 6
luas_trapesium = bangun.luas_trapesium(alas, tinggi, sisi_miring)
print("Luas trapesium:", luas_trapesium)


jari_jari = 12
luas_lingkaran = bangun.luas_lingkaran(jari_jari)
print("Luas lingkaran:", luas_lingkaran)


panjang = 10
lebar = 8
tinggi = 3
luas_balok = bangun.luas_balok(panjang, lebar, tinggi)
print("Luas balok:", luas_balok)


alas = 14
tinggi = 10
luas_segitiga = bangun.luas_segitiga(alas, tinggi)
print("Luas segitiga:", luas_segitiga)


panjang = 7
lebar = 4
luas_persegi_panjang = bangun.luas_persegi_panjang(panjang, lebar)
print("Luas persegi panjang:", luas_persegi_panjang)


sisi = 9
luas_persegi = bangun.luas_persegi(sisi)
print("Luas persegi:", luas_persegi)


# In[ ]:




