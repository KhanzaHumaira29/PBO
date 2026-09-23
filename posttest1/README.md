# Sistem Manajemen Proyek Arsitektur - CV Zekarya

Program ini dibuat menggunakan Python dengan pendekatan OOP, tujuannya untuk mengelola proyek arsitektur di CV Zekarya. Dari data proyek yang masuk, klien yang mengajukan, sampai arsitek yang ditugaskan menanganinya. Ada 3 class utama: Proyek, Klien, dan Arsitek. Ketiganya tidak berdiri sendiri, karena Klien dan Arsitek sama-sama berinteraksi dengan objek Proyek untuk mengubah statusnya seiring berjalannya alur kerja (Perencanaan → Diajukan → Dikerjakan).


## Struktur Class

Ada 3 class, berdiri sendiri tanpa inheritance, saling berinteraksi lewat objek.

**Proyek**
- Atribut kelas: `nama_instansi`, `total_proyek`, `kategori_tersedia`
- Atribut private: `__anggaran`
- Method: `tampilkan_info()` (instance), `dari_dict()` (classmethod, factory)

**Klien**
- Atribut kelas: `total_klien`, `jenis_klien_valid`, `diskon_member`
- Atribut private: `__saldo_deposit`
- Method: `ajukan_proyek()` (instance, mengubah status proyek)

**Arsitek**
- Atribut kelas: `total_arsitek`, `tarif_dasar_perjam`, `spesialisasi_valid`
- Atribut private: `__gaji`
- Method: `tugaskan_ke_proyek()` (instance), `validasi_nama()` (staticmethod)

Atribut `__anggaran`, `__saldo_deposit`, dan `__gaji` diakses lewat `@property` dan `@setter`, dengan validasi (tidak boleh negatif/di bawah nilai minimum).

## Cara Menjalankan

```bash
python3 sistem_manajemen_proyek_arsitektur.py
```

## Yang Diuji di Main Code

- 2 objek per class
- Instance method, class method, dan static method masing-masing dipanggil
- Interaksi antar objek: klien mengajukan proyek, arsitek ditugaskan ke proyek (status proyek berubah)
- Setter diuji dengan data valid dan tidak valid (nilai yang tidak valid ditolak, nilai lama tetap dipakai)