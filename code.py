# Simulasi Proses ERP: Pemesanan Produk
# Berdasarkan langkah-langkah: CRM -> Inventory -> (Ya: Finance) / (Tidak: Manufacturing -> HRM -> Manufacturing -> CRM -> Finance)

def simulate_erp():
    print("=== Simulasi ERP: Pemesanan Produk ===\n")
    
    # Langkah 1: CRM - Pelanggan memesan produk
    print("Langkah 1 - CRM: Pelanggan menghubungi sales.")
    customer_order = input("Masukkan nama produk yang dipesan: ")
    print(f"Sales Order dibuat untuk produk: {customer_order}")
    
    # CRM otomatis cek stok via Inventory
    print("CRM otomatis memeriksa stok melalui modul Inventory.")
    
    # Langkah 2: Inventory - Cek ketersediaan barang
    print("\nLangkah 2 - Inventory: Cek ketersediaan barang.")
    stock_available = int(input("Masukkan jumlah stok tersedia (misal: 10): "))
    required_quantity = int(input("Masukkan jumlah yang dipesan (misal: 5): "))
    
    if stock_available >= required_quantity:
        print("Stok cukup. Order diteruskan ke Finance untuk penagihan.")
        
        # Langkah 7: Finance - Proses penagihan dan rekaman
        print("\nLangkah 7 - Finance: Proses penagihan.")
        print("Semua transaksi (penjualan) otomatis tercatat.")
        print("ERP membuat laporan real-time tanpa input ulang data.")
        print("Status order: Completed.")
        
    else:
        print("Stok tidak cukup. Kirim sinyal ke modul Manufacturing.")
        
        # Langkah 3: Manufacturing - Perencanaan produksi
        print("\nLangkah 3 - Manufacturing: Perencanaan Produksi.")
        print("Sistem membuat Production Plan dan Work Order.")
        print("Modul MRP menghitung kebutuhan bahan baku.")
        raw_materials_needed = required_quantity * 2  # Asumsi sederhana
        print(f"Kebutuhan bahan baku: {raw_materials_needed} unit.")
        
        # Langkah 4: HRM - Penjadwalan tenaga kerja
        print("\nLangkah 4 - HRM: Penjadwalan Tenaga Kerja.")
        print("HRM mengatur alokasi karyawan (operator mesin, QC, gudang).")
        workers_allocated = input("Masukkan jumlah karyawan yang dialokasikan (misal: 3): ")
        print(f"Absensi & jam kerja untuk {workers_allocated} karyawan terekam otomatis untuk perhitungan gaji.")
        
        # Langkah 5: Manufacturing - Eksekusi produksi
        print("\nLangkah 5 - Manufacturing: Eksekusi Produksi.")
        print("Pabrik mulai proses produksi sesuai Work Order.")
        print("Hasil produksi masuk ke stok barang jadi (Inventory).")
        print(f"Produk {customer_order} siap sebanyak {required_quantity} unit.")
        
        # Langkah 6: CRM - Proses pengiriman & update pelanggan
        print("\nLangkah 6 - CRM: Proses Pengiriman & Update Pelanggan.")
        print("CRM mengirim notifikasi bahwa barang dikirim.")
        print("Status order pelanggan diperbarui menjadi 'Completed'.")
        
        # Langkah 7: Finance - Integrasi otomatis
        print("\nLangkah 7 - Finance: Integrasi Otomatis.")
        print("Semua transaksi (bahan baku, jam kerja, pengiriman, penjualan) otomatis tercatat.")
        print("ERP membuat laporan real-time tanpa input ulang data.")
    
    print("\n=== Simulasi Selesai ===")

# Jalankan simulasi
if __name__ == "__main__":
    simulate_erp()
