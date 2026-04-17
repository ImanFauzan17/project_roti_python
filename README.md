# 🍞 Bakery Inventory Manager (Refactored)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Clean Code](https://img.shields.io/badge/code--style-clean--code-green)

Proyek ini adalah sistem manajemen inventaris toko roti berbasis CLI yang telah diaudit dan diperbaiki berdasarkan prinsip **Clean Code**. [cite_start]Aplikasi ini merupakan hasil tugas mandiri untuk mata kuliah **Rekayasa Perangkat Lunak - Semester 4**[cite: 2].

## 📋 Deskripsi Proyek
Aplikasi ini memungkinkan pengelola toko untuk memantau stok roti, memproses pengurangan stok saat terjadi penjualan, dan memvalidasi ketersediaan barang. [cite_start]Fokus utama dari rilis ini adalah melakukan transisi dari kode prosedural (spaghetti code) menjadi arsitektur yang lebih bersih dan terorganisir[cite: 7].

## 🛠️ Audit Kode & Perbaikan
[cite_start]Berdasarkan hasil audit, berikut adalah poin-poin utama pelanggaran kode asal dan perbaikan yang telah diterapkan[cite: 4, 5]:

| No | Prinsip | Perbaikan yang Dilakukan |
| :--- | :--- | :--- |
| 1 | **Meaningful Naming** | [cite_start]Mengubah variabel satu huruf (`st`, `r`, `q`) menjadi nama deskriptif (`stok_roti`, `roti`, `kuantitas`)[cite: 5]. |
| 2 | **Single Responsibility (SRP)** | [cite_start]Memisahkan logika bisnis (kelas `InventarisRoti`) dari interaksi pengguna (kelas `KonsolUI`)[cite: 5]. |
| 3 | **Don't Repeat Yourself (DRY)** | [cite_start]Membuat fungsi pusat `cari_roti()` untuk menggantikan perulangan `for` yang ditulis berulang kali[cite: 5]. |
| 4 | **No Redundant Comments** | [cite_start]Menghapus komentar noise dan menggantinya dengan nama fungsi yang menjelaskan dirinya sendiri (*self-documenting code*)[cite: 5, 8]. |
| 5 | **Guard Clauses** | [cite_start]Mengganti *nested if-else* (percabangan bersarang) dengan pola *early return* agar alur logika linear dan mudah dibaca[cite: 5]. |

## 🚀 Langkah-Langkah Refactoring

### 1. Tahap Identifikasi (Legacy Code)
[cite_start]Awalnya, aplikasi memiliki fungsi `proses()` yang mencampur aduk pengambilan input, validasi stok, dan manipulasi data dalam satu blok kode yang sulit diuji[cite: 5].

### 2. Implementasi Struktur Data
[cite_start]Mengganti penyimpanan data berbasis *list-of-list* yang rawan kesalahan indeks menjadi `@dataclass` sehingga atribut diakses melalui nama properti yang jelas (misalnya `roti.stok`)[cite: 5].

### 3. Pembersihan Alur Logika
Menerapkan pengecekan kondisi gagal di awal fungsi (Guard Clauses). [cite_start]Jika roti tidak ditemukan atau stok kurang, fungsi langsung berhenti (`return`), sehingga logika utama tidak tertimbun di dalam blok `if` yang dalam[cite: 5].

## 📊 Hasil Akhir
[cite_start]Proses refactoring berhasil meningkatkan keterbacaan dan pemeliharaan (*maintainability*) aplikasi tanpa mengubah fungsionalitas aslinya[cite: 8]. [cite_start]Kode sekarang bebas dari duplikasi logika dan lebih siap untuk dikembangkan lebih lanjut (scalable)[cite: 7].