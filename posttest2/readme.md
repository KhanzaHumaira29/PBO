# Sistem Manajemen Proyek Arsitektur - CV Zekarya (Posttest 2)

Lanjutan dari posttest 1, program ini menambahkan konsep Relasi UML (Asosiasi, Agregasi, Komposisi) dan Inheritance.

## Inheritance

Superclass `Pegawai` diturunkan ke 2 subclass: `Arsitek` dan `ManajerProyek`.

- Kedua subclass manggil `super().__init__(...)` buat ngewarisin atribut dasar (`nama`, `_gaji_pokok`, `__nomor_pegawai`) dari `Pegawai`.
- `Arsitek` punya atribut unik `spesialisasi`, `ManajerProyek` punya `jumlah_tim`.
- Method `hitung_bonus()` di-override di kedua subclass, formulanya beda: Arsitek dihitung dari jumlah proyek yang ditangani, ManajerProyek dari jumlah tim yang diawasi.
- `_gaji_pokok` dibuat protected karena perlu bisa diakses subclass. `__nomor_pegawai` dibuat private karena itu data identitas yang memang cuma urusan `Pegawai`, subclass gak perlu ngutak-ngatik.

## Relasi UML

**Asosiasi** - `Klien` dan `Proyek`
`Klien.ajukan_proyek(proyek)` nerima objek `Proyek` cuma lewat parameter method, gak disimpan jadi atribut tetap. Klien dan Proyek sama-sama bisa berdiri sendiri.

**Agregasi** - `Proyek` dan `Pegawai`
Objek `Arsitek`/`ManajerProyek` dibuat di luar, baru didaftarkan ke proyek lewat `tambah_pegawai()`. Kalau proyeknya dihapus, pegawainya tetap ada (dibuktikan di main code: `del proyek1` tapi `arsitek1` masih bisa dipanggil).

**Komposisi** - `Proyek` dan `DokumenProyek`
`DokumenProyek` dibuat otomatis di dalam `__init__` milik `Proyek`, gak pernah dibuat terpisah dari luar. Jadi dokumen ini nempel penuh ke proyeknya.

## Cara Menjalankan

```bash
python3 posttest2-2509106065-KhanzaHumaira.py
```

## Yang Diuji di Main Code

- Dibuat 2 subclass (`Arsitek` x2, `ManajerProyek` x1), dicek pakai `isinstance()` dan `issubclass()`
- `hitung_bonus()` dipanggil di kedua subclass, hasilnya beda karena override
- Proyek dibuat, otomatis bawa `DokumenProyek` (komposisi)
- Arsitek didaftarkan ke proyek (agregasi), lalu proyeknya dihapus buat buktiin arsitek tetap hidup
- Klien ngajuin proyek lewat parameter method (asosiasi)