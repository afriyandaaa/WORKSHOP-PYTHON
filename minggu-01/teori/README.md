Ringkasan Materi:

BAB 1 - 
Python adalah bahasa pemograman. Anda dapat menulis skrip shell Unix atau file batch Windows dapat menulis program C/C++/Java, Python lebih mudah digunakan, tersedia di sistem operasi Windows, macOS, dan Unix, dan akan membantu menyelesaikan pekerjaan lebih cepat.
Python adalah bahasa pemrograman nyata, menawarkan lebih banyak struktur dan dukungan untuk program besar Di sisi lain, Python juga menawarkan lebih banyak pemeriksaan kesalahan daripada C, Python memungkinkan Anda membagi program Anda menjadi modul yang dapat digunakan kembali di program Python lainnya.
Python adalah bahasa yang ditafsirkan, Python memungkinkan program ditulis dengan kompak dan mudah dibaca.

BAB 2 
-Invoking the Interpreter
Interpreter beroperasi seperti shell Unix: ketika dipanggil dengan input standar yang terhubung ke perangkat tty, ia membaca dan mengeksekusi perintah secara interaktif; ketika dipanggil dengan argumen nama file atau dengan file sebagai input standar, ia membaca dan mengeksekusi skrip dari file itu.

-Argument Passing
nama skrip dan argumen tambahan selanjutnya diubah menjadi daftar string dan ditetapkan ke variabel argv di modul sys.ketika tidak ada skrip dan tidak ada argumen yang diberikan, sys.argv[0] adalah string kosong. Ketika nama skrip diberikan sebagai '-' (artinya input standar), sys.argv[0] disetel ke '-'. Ketika perintah -c digunakan, sys.argv[0] disetel ke '-c'. Saat modul -m digunakan, sys.argv[0] disetel ke nama lengkap modul yang berada. Opsi yang ditemukan setelah perintah -c atau modul -m tidak dikonsumsi oleh pemrosesan opsi juru bahasa Python tetapi ditinggalkan di sys.argv untuk ditangani oleh perintah atau modul.

-Interactive Mode
Ketika perintah dibaca dari tty, interpreter dikatakan dalam mode interaktif. Dalam mode ini ia meminta perintah berikutnya dengan prompt utama, biasanya tiga tanda lebih besar dari (>>>); untuk baris lanjutan diminta dengan prompt sekunder, secara default tiga titik (...).

BAB 3
-An Informal Introduction to Python
input dan output dibedakan dengan ada atau tidaknya prompt (>>>)  
Komentar dalam Python dimulai dengan karakter hash, # dan diperpanjang hingga akhir baris fisik. Sebuah komentar mungkin muncul di awal baris atau setelah spasi putih atau kode, tetapi tidak dalam literal string. komentar dapat dihilangkan saat mengetikkan contoh.

spam = 1  # and this is the second comment
          # ... and now a third!
text =  "# This is not a comment because it's inside quotes."

-Numbers
dapat mengetikkan ekspresi dan itu akan menulis nilainya. Sintaks ekspresi langsung: operator +, -, * dan / tanda kurung (()) dapat Misalnya:
>>>2 + 2
4
>>>50 - 5*6
20
>>>(50 - 5*6) / 4
5.0
>>>8 / 5  # division always returns a floating point number
1.6

-String
Selain angka, Python juga bisa memanipulasi string, Mereka dapat diapit dengan tanda kutip tunggal ('...') atau tanda kutip ganda ("...") dengan hasil yang sama 2.
misalnya:
>>>'spam eggs'  # single quotes
'spam eggs'
>>>'"Yes," they said.'
'"Yes," they said.'