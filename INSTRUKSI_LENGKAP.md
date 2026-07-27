# 🚀 INSTRUKSI LENGKAP MENGGUNAKAN JOBSTREET SCRAPER

## ✅ Prasyarat

Pastikan Python 3.8+ sudah terinstall di sistem Anda.

## 📋 Langkah-langkah Instalasi

### 1. Install Dependencies

Buka terminal/CMD dan jalankan:

```bash
cd /workspace
pip install -r requirements.txt
```

Tunggu hingga semua package terinstall.

### 2. Install Playwright Browser

Jalankan perintah ini untuk menginstall browser Chromium yang dibutuhkan Playwright:

```bash
playwright install chromium
```

**CATATAN:** Jika terjadi error "ENOSPC" atau "no space left on device", pastikan ada cukup ruang penyimpanan.

### 3. Verifikasi Instalasi

Test apakah semua sudah terinstall dengan benar:

```bash
python -c "import run; print('✅ OK')"
```

Jika muncul `✅ OK`, instalasi berhasil!

---

## 🎯 CARA MENGGUNAKAN UI INTERAKTIF

### Langkah 1: Jalankan Program

```bash
python run.py
```

Anda akan melihat menu interaktif seperti ini:

```
============================================================
       JOBSTREET SCRAPER - INTERACTIVE CONFIGURATION
============================================================

--- KONFIGURASI SAAT INI ---
  TARGET_URL: https://www.jobstreet.co.id/id/job-search/
  HEADLESS: True
  LOG_LEVEL: INFO
  DOWNLOAD_DELAY: 3
  CONCURRENT_REQUESTS: 1
  RETRY_TIMES: 5
  PROXIES: []
  USER_AGENT: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...

--- MENU ---
  1. Ubah URL Target
  2. Ubah Mode Headless (True/False)
  3. Ubah Log Level (INFO/DEBUG/WARNING/ERROR)
  4. Ubah Download Delay (detik)
  5. Ubah Concurrent Requests
  6. Ubah Retry Times
  7. Atur Proxy (comma-separated)
  8. Set User Agent Custom
  9. Reset ke Default
  0. MULAI SCRAPING
  q. Keluar

Pilih opsi [0-9/q]: 
```

### Langkah 2: Konfigurasi (Opsional)

#### 🔹 Opsi 1: Ubah URL Target

Gunakan ini jika ingin mencari lowongan pekerjaan spesifik.

**Contoh:**
```
Pilih opsi [0-9/q]: 1
Masukkan URL target baru [https://www.jobstreet.co.id/id/job-search/]: https://www.jobstreet.co.id/id/job-search/python-developer-jobs/
✅ URL diubah menjadi: https://www.jobstreet.co.id/id/job-search/python-developer-jobs/
```

Tekan ENTER untuk menerima nilai default.

#### 🔹 Opsi 2: Ubah Mode Headless

- **True (Y)**: Browser berjalan di background (tidak terlihat, lebih cepat)
- **False (n)**: Browser terlihat di layar (untuk debugging)

**Contoh:**
```
Pilih opsi [0-9/q]: 2
Gunakan mode headless? [Y/n]: n
✅ Headless diubah menjadi: False
```

Gunakan `False` jika ingin melihat proses scraping secara visual.

#### 🔹 Opsi 3: Ubah Log Level

Pilihan yang tersedia:
- **INFO**: Log standar (default, direkomendasikan)
- **DEBUG**: Log sangat detail (untuk troubleshooting)
- **WARNING**: Hanya warning dan error
- **ERROR**: Hanya error

**Contoh:**
```
Pilih opsi [0-9/q]: 3
Pilihan Log Level: INFO, DEBUG, WARNING, ERROR
Masukkan Log Level [INFO]: DEBUG
✅ Log Level diubah menjadi: DEBUG
```

#### 🔹 Opsi 4: Ubah Download Delay

Delay antar request untuk menghindari blocking (dalam detik).

**Rekomendasi:**
- 1-3 detik: Cepat, tapi risiko block lebih tinggi
- 3-5 detik: Seimbang (default)
- 5-10 detik: Aman untuk scraping intensif

**Contoh:**
```
Pilih opsi [0-9/q]: 4
Masukkan Download Delay (detik) [3]: 5
✅ Download Delay diubah menjadi: 5.0 detik
```

#### 🔹 Opsi 5: Ubah Concurrent Requests

Jumlah request paralel yang dijalankan bersamaan.

**Rekomendasi:**
- **1**: Paling aman (default)
- **2-3**: Cukup aman untuk scraping medium
- **4+**: Risiko block tinggi, gunakan proxy

**Contoh:**
```
Pilih opsi [0-9/q]: 5
Masukkan Concurrent Requests [1]: 2
✅ Concurrent Requests diubah menjadi: 2
```

#### 🔹 Opsi 6: Ubah Retry Times

Berapa kali scraper akan retry jika request gagal.

**Contoh:**
```
Pilih opsi [0-9/q]: 6
Masukkan Retry Times [5]: 3
✅ Retry Times diubah menjadi: 3
```

#### 🔹 Opsi 7: Atur Proxy

Masukkan daftar proxy dipisahkan dengan koma. Format: `http://user:pass@host:port`

**Contoh dengan proxy:**
```
Pilih opsi [0-9/q]: 7
Masukkan daftar proxy dipisahkan koma (contoh: http://user:pass@proxy:port,http://...
Kosongkan jika tidak menggunakan proxy
Proxy list: http://user1:pass1@proxy1.com:8080,http://user2:pass2@proxy2.com:8080
✅ Proxy diatur: 2 proxy(s)
```

**Contoh menghapus proxy:**
```
Proxy list: 
✅ Proxy dihapus (tidak menggunakan proxy)
```

#### 🔹 Opsi 8: Set User Agent Custom

Ubah User Agent jika diperlukan (jarang perlu diubah).

**Contoh:**
```
Pilih opsi [0-9/q]: 8
Masukkan User Agent custom [Mozilla/5.0...]: [paste user agent baru]
✅ User Agent diubah
```

#### 🔹 Opsi 9: Reset ke Default

Mengembalikan SEMUA pengaturan ke nilai default.

```
Pilih opsi [0-9/q]: 9
✅ Konfigurasi direset ke default!
```

### Langkah 3: Mulai Scraping

Setelah konfigurasi selesai, pilih **0** untuk memulai:

```
Pilih opsi [0-9/q]: 0

============================================================
                  KONFIRMASI MULAI
============================================================

Konfigurasi yang akan digunakan:
  TARGET_URL: https://www.jobstreet.co.id/id/job-search/
  HEADLESS: True
  LOG_LEVEL: INFO
  DOWNLOAD_DELAY: 3
  CONCURRENT_REQUESTS: 1
  RETRY_TIMES: 5
  PROXIES: []
  USER_AGENT: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...

Apakah Anda yakin ingin memulai scraping? [Y/n]: y

🚀 Memulai scraping...
------------------------------------------------------------
```

Scraper akan mulai berjalan. Anda akan melihat log progress sesuai dengan LOG_LEVEL yang dipilih.

### Langkah 4: Lihat Hasil

Setelah scraping selesai (atau tidak ada halaman lagi), hasil akan tersimpan otomatis:

```
============================================================
✅ SCRAPING SELESAI!
============================================================

Hasil disimpan di:
  - output.json
  - output.csv
```

**Lokasi file:** `/workspace/output.json` dan `/workspace/output.csv`

---

## 🛠️ TROUBLESHOOTING

### ❌ Error: "ModuleNotFoundError: No module named 'scrapy'"

**Solusi:**
```bash
pip install -r requirements.txt
```

### ❌ Error: "playwright not installed" atau "Browser not found"

**Solusi:**
```bash
playwright install chromium
```

### ❌ Error: "ENOSPC" atau "No space left on device" saat install Playwright

**Solusi:**
1. Cek ruang disk: `df -h`
2. Hapus file tidak perlu
3. Coba install ulang: `playwright install chromium --force`

### ❌ Scraping terlalu lambat

**Solusi:**
1. Turunkan DOWNLOAD_DELAY (opsi 4) ke 1-2 detik
2. Naikkan CONCURRENT_REQUESTS (opsi 5) ke 2-3
3. Pastikan HEADLESS = True (opsi 2)

### ❌ Terkena block/banned (Error 403, 429)

**Solusi:**
1. Naikkan DOWNLOAD_DELAY ke 5-10 detik (opsi 4)
2. Gunakan proxy rotation (opsi 7)
3. Turunkan CONCURRENT_REQUESTS ke 1 (opsi 5)
4. Test dengan HEADLESS = False (opsi 2) untuk debug

### ❌ Ingin menghentikan scraping di tengah jalan

**Solusi:** Tekan `Ctrl+C` di keyboard

### ❌ Output kosong/tidak ada data

**Kemungkinan penyebab:**
1. Selector tidak cocok (website berubah)
2. Terlalu banyak request yang diblock
3. Halaman butuh waktu load lebih lama

**Solusi:**
1. Set LOG_LEVEL = DEBUG (opsi 3) untuk lihat detail
2. Set HEADLESS = False (opsi 2) untuk lihat browser
3. Cek apakah URL target valid

---

## 📝 TIPS PENGGUNAAN

### Untuk Pemula:
1. Gunakan setting default dulu
2. Set HEADLESS = False untuk melihat proses
3. Jangan ubah CONCURRENT_REQUESTS dari 1
4. Gunakan LOG_LEVEL = INFO

### Untuk Advanced Users:
1. Gunakan proxy rotation untuk scraping besar
2. Set HEADLESS = True untuk performa maksimal
3. Adjust DOWNLOAD_DELAY dan CONCURRENT_REQUESTS sesuai kebutuhan
4. Gunakan LOG_LEVEL = WARNING atau ERROR untuk log minimal

### Best Practices:
1. ⚠️ **Jangan scraping terlalu agresif** - Gunakan delay yang wajar
2. ⚠️ **Gunakan proxy** - Untuk scraping lebih dari 100 halaman
3. ⚠️ **Test dulu** - Dengan HEADLESS = False sebelum running besar-besaran
4. ⚠️ **Hormati website** - Jangan overload server target

---

## 📂 Struktur File Output

### output.json
```json
[
  {
    "title": "Python Developer",
    "company": "PT Tech Indonesia",
    "location": "Jakarta",
    "salary": "Rp 10.000.000 - Rp 15.000.000",
    "url": "https://www.jobstreet.co.id/job/...",
    "scraped_at": "https://www.jobstreet.co.id/id/job-search/"
  }
]
```

### output.csv
```csv
title,company,location,salary,url,scraped_at
Python Developer,PT Tech Indonesia,Jakarta,Rp 10.000.000 - Rp 15.000.000,https://...,https://...
```

---

## 🆘 Butuh Bantuan?

Jika masih ada masalah:
1. Set LOG_LEVEL = DEBUG (opsi 3)
2. Jalankan ulang scraper
3. Screenshot error yang muncul
4. Cek log detail untuk diagnosa

---

**Selamat Menggunakan! 🎉**
