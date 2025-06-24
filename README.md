# Wordle Solver – Brute Force vs Greedy Heuristik

**Wordle Solver** adalah program sederhana yang dirancang untuk menyelesaikan permainan **Wordle** secara otomatis menggunakan dua pendekatan algoritmik berbeda: **Brute Force** dan **Greedy Heuristik**.  
Permainan Wordle sendiri menantang pemain untuk menebak sebuah kata lima huruf dengan umpan balik warna hijau, kuning, dan abu-abu berdasarkan kecocokan tebakan.

## Deskripsi Algoritma

### Brute Force  
Strategi brute force mencoba semua kemungkinan kata dari kamus secara berurutan. Setelah setiap tebakan, program menyaring kandidat yang mungkin berdasarkan umpan balik, namun tetap menebak kata berikutnya sesuai urutan awal tanpa mempertimbangkan seberapa informatif tebakan sebelumnya.

### Greedy Heuristik  
Strategi greedy memilih kata yang dianggap paling informatif di setiap langkah, berdasarkan frekuensi huruf dan keberagaman karakter dari kata-kata kandidat saat ini. Tujuannya adalah untuk memperkecil ruang pencarian seefisien mungkin dalam jumlah langkah minimum.

## Cara Menjalankan Program

1. Pastikan Python telah terpasang.
2. Install pustaka `nltk` (jika belum):
   ```bash
   pip install nltk
    ```
3. Jalankan program pada folder root proyek dengan perintah :
   ```bash
   py src/main.py
   ```
4. Ikuti instruksi di terminal untuk:
    - Menentukan kata target (acak dari kamus atau input manual)
    - Memilih algoritma penyelesaian (Brute Force atau Greedy Heuristik)
5. Program akan menampilkan proses penyelesaian Wordle langkah demi langkah dengan pewarnaan huruf seperti di permainan aslinya.

## Identitas Penulis
- **Nama**: Anella Utari Gunadi
- **NIM**: 13523078
