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
            print(f"[Ditolak] Anggaran '{self.nama_proyek}' harus angka positif.")
            return
        self.__anggaran = nilai_baru

    def tampilkan_info(self):
        print(f"Proyek: {self.nama_proyek} | {self.lokasi} | {self.kategori} | "
            f"Status: {self.status} | Anggaran: Rp{self.anggaran:,.0f}")

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
            print(f"[Ditolak] Saldo deposit '{self.nama_klien}' minimal Rp5.000.000.")
            return
        self.__saldo_deposit = nilai_baru

    def ajukan_proyek(self, proyek):
        proyek.status = "Diajukan"
        print(f"{self.nama_klien} mengajukan proyek '{proyek.nama_proyek}' -> status: {proyek.status}")


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
            print(f"[Ditolak] Gaji '{self.nama_arsitek}' minimal Rp6.000.000.")
            return
        self.__gaji = nilai_baru

    def tugaskan_ke_proyek(self, proyek):
        proyek.status = "Dikerjakan"
        print(f"{self.nama_arsitek} ditugaskan ke proyek '{proyek.nama_proyek}' -> status: {proyek.status}")

    @staticmethod
    def validasi_nama(nama):
        return bool(nama) and nama.replace(" ", "").isalpha()


if __name__ == "__main__":
    proyek1 = Proyek("Rumah Bu Sari", "Samarinda", "Residensial", 450_000_000)
    proyek2 = Proyek.dari_dict({
        "nama_proyek": "Kantor Zekarya Tower", "lokasi": "Balikpapan",
        "kategori": "Komersial", "anggaran": 2_500_000_000
    })
    klien1 = Klien("Sari Wulandari", "081234567890", "Individu", 25_000_000)
    klien2 = Klien("PT Nusantara Jaya", "0811223344", "Perusahaan", 100_000_000)
    arsitek1 = Arsitek("Raka Pratama", "Residensial", 8_500_000)
    arsitek2 = Arsitek("Dewi Anjani", "Komersial", 12_000_000)

    print(f"Total proyek: {Proyek.total_proyek} | klien: {Klien.total_klien} | arsitek: {Arsitek.total_arsitek}\n")

    proyek1.tampilkan_info()
    klien1.ajukan_proyek(proyek1)
    arsitek1.tugaskan_ke_proyek(proyek1)
    proyek1.tampilkan_info()

    print(f"\nProyek dari factory: {proyek2.nama_proyek}, anggaran Rp{proyek2.anggaran:,.0f}")

    print(f"Validasi nama 'Raka Pratama': {Arsitek.validasi_nama('Raka Pratama')}")
    print(f"Validasi nama '123': {Arsitek.validasi_nama('123')}")

    print(f"\nGaji arsitek1 sebelum: {arsitek1.gaji}")
    arsitek1.gaji = 9_000_000
    print(f"Setelah diubah (valid): {arsitek1.gaji}")
    arsitek1.gaji = 2_000_000
    print(f"Setelah dicoba diubah (tidak valid, tetap): {arsitek1.gaji}")

    print(f"\nSaldo klien1 sebelum: {klien1.saldo_deposit}")
    klien1.saldo_deposit = 30_000_000
    print(f"Setelah diubah (valid): {klien1.saldo_deposit}")
    klien1.saldo_deposit = -500_000
    print(f"Setelah dicoba diubah (tidak valid, tetap): {klien1.saldo_deposit}")