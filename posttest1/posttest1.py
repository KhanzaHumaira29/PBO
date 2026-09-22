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
        Proyek.total_proyek += 1

    @property
    def anggaran(self):
        return self.__anggaran

    @anggaran.setter
    def anggaran(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"[Ditolak] Anggaran proyek '{self.nama_proyek}' harus angka positif.")
            return
        self.__anggaran = nilai_baru


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
            print(f"[Ditolak] Saldo deposit '{self.nama_klien}' minimal Rp5.000.000.")
            return
        self.__saldo_deposit = nilai_baru


class Arsitek:
    total_arsitek = 0
    tarif_dasar_perjam = 150_000
    spesialisasi_valid = ["Residensial", "Komersial", "Industrial", "Interior"]

    def __init__(self, nama_arsitek, spesialisasi, gaji):
        self.nama_arsitek = nama_arsitek
        self.spesialisasi = spesialisasi
        self.__gaji = 0
        self.gaji = gaji
        Arsitek.total_arsitek += 1

    @property
    def gaji(self):
        return self.__gaji

    @gaji.setter
    def gaji(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 6_000_000:
            print(f"[Ditolak] Gaji '{self.nama_arsitek}' minimal Rp6.000.000 (standar junior architect).")
            return
        self.__gaji = nilai_baru