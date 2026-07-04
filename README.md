# ✌️ Foto Kita Blur - Hand Gesture Detection

Aplikasi Python sederhana, ringan, dan siap pakai untuk mendeteksi gestur tangan secara *real-time* menggunakan kamera laptop atau PC. 

Ketika kamera mendeteksi gestur **"Peace" (dua jari/tanda V)**, sistem akan secara otomatis memberikan efek pemburaman (*Gaussian Blur*) pada seluruh tampilan layar. Proyek ini dibangun menggunakan teknologi **Google MediaPipe Tasks API** terbaru yang modern dan efisien, dipadukan dengan **OpenCV**.

---

## 🚀 Fitur Utama
- **Real-time Detection:** Mendeteksi gestur tangan tanpa jeda (mendukung 30+ FPS).
- **Modern API:** Menggunakan format model `.task` terbaru dari Google yang lebih ringan bagi memori (RAM) komputer.
- **User-Friendly:** Kode terstruktur rapi dan siap dijalankan (*plug and play*).

---

## 💻 Cara Instalasi & Penggunaan

Ikuti langkah-langkah mudah di bawah ini untuk menjalankan program di komputer Anda. Pastikan Anda sudah menginstal **Python** (versi 3.9 ke atas) dan **Git**.

### 1. Clone Repositori
Buka Terminal, Command Prompt (CMD), atau Git Bash Anda, lalu jalankan perintah ini untuk mengunduh kode ke komputer lokal:
```bash
git clone [https://github.com/RadjaAsnur/foto_kita_blur.git](https://github.com/RadjaAsnur/foto_kita_blur.git)
cd foto_kita_blur
```

### 2. Instal Library Pendukung
Agar program bisa berjalan, Anda perlu menginstal *library* yang dibutuhkan. Ketik perintah berikut:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Program
Setelah instalasi selesai, Anda bisa langsung membuka kamera dan menjalankan aplikasinya dengan perintah:
```bash
python blur.py
```

---

## 🎮 Cara Kerja Aplikasi
1. Setelah perintah dijalankan, jendela kamera baru bernama **"Peace Blur (Tasks API)"** akan terbuka.
2. Arahkan satu tangan Anda ke depan kamera.
3. Bentuk gestur **Peace** (hanya jari telunjuk dan jari tengah yang tegak lurus, sisanya ditekuk). Layar akan otomatis berubah menjadi blur.
4. Turunkan jari Anda, dan layar akan kembali jernih.
5. Untuk mematikan program dengan aman, klik jendela kamera tersebut lalu tekan tombol **`ESC`** pada keyboard Anda.

---

## 👨‍💻 Kredit
Dikembangkan dan dimodifikasi oleh **Muhammad Radja Asnur**. 
Proyek portofolio ini dikembangkan untuk mempermudah masyarakat awam dalam mencoba teknologi *Computer Vision* dan implementasi *Artificial Intelligence* (AI) tingkat dasar.
