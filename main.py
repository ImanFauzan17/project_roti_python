def kurangi_stok(self, nama: str, jumlah: int):
        roti = self.cari_roti(nama)
        
        # Guard Clauses: Cek kondisi gagal di awal
        if not roti:
            print("Error: Roti tidak ditemukan.")
            return
            
        if roti.stok < jumlah:
            print(f"Error: Stok {nama} tidak mencukupi.")
            return

        # Alur utama (happy path) berada di level indentasi terendah
        roti.stok -= jumlah
        print(f"Sukses: Stok {nama} telah diperbarui.")