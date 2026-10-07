class Pegawai:
    nama_instansi = "CV Zekarya"
    total_pegawai = 0
    tunjangan_tetap = 500_000

    def __init__(self, nama, nomor_pegawai, gaji_pokok):
        self.nama = nama
        self._gaji_pokok = gaji_pokok          # protected, boleh diakses subclass
        self.__nomor_pegawai = nomor_pegawai   # private, eksklusif milik Pegawai
        Pegawai.total_pegawai += 1

    def tampilkan_info(self):
        print(f"  {self.nama} | No: {self.__nomor_pegawai} | Gaji pokok: Rp{self._gaji_pokok:,} | "
            f"Bonus: Rp{self.hitung_bonus():,}")

    def hitung_bonus(self):
        return self.tunjangan_tetap


class Arsitek(Pegawai):
    def __init__(self, nama, nomor_pegawai, gaji_pokok, spesialisasi):
        super().__init__(nama, nomor_pegawai, gaji_pokok)
        self.spesialisasi = spesialisasi
        self.proyek_ditangani = []

    def tugaskan_ke_proyek(self, proyek):
        proyek.tambah_pegawai(self)  # Agregasi
        self.proyek_ditangani.append(proyek.nama_proyek)
        print(f"  {self.nama} (Arsitek {self.spesialisasi}) ditugaskan ke '{proyek.nama_proyek}'")

    def hitung_bonus(self):  # override
        return self.tunjangan_tetap + len(self.proyek_ditangani) * 300_000


class ManajerProyek(Pegawai):
    def __init__(self, nama, nomor_pegawai, gaji_pokok, jumlah_tim):
        super().__init__(nama, nomor_pegawai, gaji_pokok)
        self.jumlah_tim = jumlah_tim

    def hitung_bonus(self):  # override
        return self.tunjangan_tetap + self.jumlah_tim * 750_000


class DokumenProyek:
    def __init__(self, nomor_dokumen, nama_proyek):
        self.nomor_dokumen = nomor_dokumen
        self.nama_proyek = nama_proyek

    def __str__(self):
        return f"Dokumen {self.nomor_dokumen} milik proyek '{self.nama_proyek}'"


class Proyek:
    nama_instansi = "CV Zekarya"
    total_proyek = 0
    kategori_tersedia = ["Residensial", "Komersial", "Industrial"]

    def __init__(self, nama_proyek, lokasi, kategori, anggaran):
        self.nama_proyek = nama_proyek
        self.lokasi = lokasi
        self.kategori = kategori
        self.status = "Perencanaan"
        self.__anggaran = 0
        self.anggaran = anggaran
        self._tim = []  # Agregasi
        self._dokumen = DokumenProyek(f"DOC-{Proyek.total_proyek + 1:03d}", nama_proyek)  # Komposisi
        Proyek.total_proyek += 1

    @property
    def anggaran(self):
        return self.__anggaran

    @anggaran.setter
    def anggaran(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"  [Ditolak] Anggaran '{self.nama_proyek}' harus angka positif.")
            return
        self.__anggaran = nilai_baru

    def tambah_pegawai(self, pegawai):
        if pegawai not in self._tim:
            self._tim.append(pegawai)

    def tampilkan_info(self):
        print(f"  Proyek: {self.nama_proyek} ({self.lokasi})")
        print(f"    Kategori : {self.kategori}")
        print(f"    Status   : {self.status}")
        print(f"    Anggaran : Rp{self.anggaran:,.0f}")
        print(f"    Tim      : {len(self._tim)} orang")
        print(f"    Dokumen  : {self._dokumen}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_proyek"], data["lokasi"], data["kategori"], data["anggaran"])


class Klien:
    total_klien = 0
    jenis_klien_valid = ["Individu", "Perusahaan"]
    diskon_member = 0.05

    def __init__(self, nama_klien, kontak, jenis_klien, saldo_deposit):
        self.nama_klien = nama_klien
        self.kontak = kontak
        self.jenis_klien = jenis_klien
        self.__saldo_deposit = 0
        self.saldo_deposit = saldo_deposit
        Klien.total_klien += 1

    @property
    def saldo_deposit(self):
        return self.__saldo_deposit

    @saldo_deposit.setter
    def saldo_deposit(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 5_000_000:
            print(f"  [Ditolak] Saldo deposit '{self.nama_klien}' minimal Rp5.000.000.")
            return
        self.__saldo_deposit = nilai_baru

    def ajukan_proyek(self, proyek):  # Asosiasi
        proyek.status = "Diajukan"
        print(f"  {self.nama_klien} mengajukan proyek '{proyek.nama_proyek}' -> status: {proyek.status}")


# Main
if __name__ == "__main__":
    arsitek1 = Arsitek("Raka Pratama", "ARS-01", 8_500_000, "Residensial")
    arsitek2 = Arsitek("Dewi Anjani", "ARS-02", 9_000_000, "Komersial")
    manajer1 = ManajerProyek("Fajar Hidayat", "MGR-01", 12_000_000, jumlah_tim=3)

    proyek1 = Proyek("Rumah Bu Sari", "Samarinda", "Residensial", 450_000_000)
    proyek2 = Proyek.dari_dict({
        "nama_proyek": "Kantor Zekarya Tower", "lokasi": "Balikpapan",
        "kategori": "Komersial", "anggaran": 2_500_000_000
    })

    print("\nPenugasan pegawai ke proyek (Agregasi):")
    arsitek1.tugaskan_ke_proyek(proyek1)
    arsitek2.tugaskan_ke_proyek(proyek2)
    proyek1.tambah_pegawai(manajer1)

    print("\nKlien mengajukan proyek (Asosiasi):")
    klien1 = Klien("Sari Wulandari", "081234567890", "Individu", 25_000_000)
    klien1.ajukan_proyek(proyek1)

    print("\nInfo pegawai (Inheritance - method hitung_bonus() di-override):")
    arsitek1.tampilkan_info()
    manajer1.tampilkan_info()

    print("\nInfo proyek (Komposisi - dokumen otomatis ikut terbentuk):")
    proyek1.tampilkan_info()
    proyek2.tampilkan_info()

    del proyek1
    print(f"\nProyek1 dihapus, arsitek1 tetap ada: {arsitek1.nama}, "
        f"proyek yang pernah ditangani: {arsitek1.proyek_ditangani}")