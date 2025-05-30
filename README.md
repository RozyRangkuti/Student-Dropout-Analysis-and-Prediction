# Student-Dropout-Analysis-and-Prediction
# Menyelesaikan Permasalahan Institusi Pendidikan - Jaya Jata Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

## Bussiness Problem

Jaya Jaya Institut menghadapi masalah serius terkait tingginya angka dropout di kalangan siswanya. Hal ini dapat berdampak negatif pada reputasi dan akreditasi institusi, serta mengurangi kepercayaan masyarakat terhadap mutu pendidikan yang diberikan. Kurangnya kemampuan untuk mengidentifikasi siswa berisiko dropout sejak dini menghambat langkah pencegahan dan pendampingan khusus, sehingga membahayakan keberlanjutan dan daya saing institusi di tengah persaingan dunia pendidikan yang semakin sengit.

Untuk mengatasi hal ini, institusi perlu mengembangkan sistem yang mampu mendeteksi dan memprediksi siswa yang berpotensi dropout sedini mungkin. Dengan demikian, intervensi yang tepat dapat diberikan untuk meningkatkan angka kelulusan dan menjaga kualitas pendidikan.

## Project Scope

- Melakukan tahap awal data preparation dan data cleaning.
- Melaksanakan Exploratory Data Analysis (EDA) untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap tingginya angka dropout melalui visualisasi data.
- Membangun dashboard bisnis yang menampilkan faktor-faktor utama penyebab meningkatnya tingkat dropout.
- Mengembangkan model machine learning guna memprediksi status siswa berdasarkan variabel-variabel yang menjadi penyebab utama dropout.
- Melakukan deployment model machine learning agar dapat digunakan untuk memprediksi apakah seorang siswa berpotensi dropout atau berhasil menyelesaikan studi.

## Preparation

**Data source:**
- [Students' Performance data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance 'Dicoding GitHub - Students Performance data')


## Setup Environment - Anaconda

1. Clone Repository
   ```bash
   git clone https://github.com/RozyRangkuti/Student-Dropout-Analysis-and-Prediction.git
   ```

2. Buka Terminal Anaconda, jalankan perintah berikut untuk membuat environment baru
   ```bash
   conda create --name myenv python=3.11
   ```
   
3. Aktifkan virtual environment dengan menjalankan perintah berikut ini
   ```bash
   conda activate myenv
   ```
   
4. Install semua requirements di dalam file "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard

 Untuk melihat isi dashboard secara langsung, kita dapat menggunakan metabase dengan bantuan Docker (pastikan Docker sudah terinstall).

1. Jalankan perintah berikut
   ```bash
   docker pull metabase/metabase:v0.46.4
   ```

2. Jalankan container Metabase menggunakan perintah
   ```bash
   docker run -p 3000:3000 --name metabase metabase/metabase
   ```

3. Login ke Metabase menggunakan username dan password berikut
   ```bash
   Username : muhammadrozy37@gmail.com
   Pass     : *************
   ```

## Bussiness Dashbord Using Metabase

Jaya Jaya Institut Students Dashboard dirancang secara efektif untuk memberikan wawasan yang relevan kepada para pengajar dan pihak internal institusi terkait tingginya tingkat siswa yang mengalami dropout yaitu mencapai angka 32%. Berikut adalah tampilan dashboard yang dibuat menggunakan Metabase.

![muhammadrozy-dashboard](https://github.com/user-attachments/assets/de199f4b-ce26-47ff-96ff-9b3067398b4e)

## Penjelasan Bussiness Dashboard Jaya Jaya Institut Students Performance

1. Grafik Average of Age

   <img width="278" alt="average of age" src="https://github.com/user-attachments/assets/695d7eca-a975-4040-9dce-b8cddfd40b75" />

   Grafik ini menjelaskan tentang rata-rata umur siswa, yaitu sebesar 23,27 tahun.

2. Grafik Average of Admission Grade

   <img width="279" alt="average of admission grade" src="https://github.com/user-attachments/assets/9f5c5a23-ca90-4cb2-8aec-951b5fa2d0da" />

   Grafik ini menjelaskan tentang rata-rata nilai penerimaan siswa, yaitu sebesar 126,98

3. Grafik International Students

   <img width="278" alt="international students" src="https://github.com/user-attachments/assets/ce2fbd63-5eac-4bb1-a217-41674533341c" />

   Grafik ini menjelaskan tentang jumlah international students, yaitu sebanyak 110 siswa dan 4,314 siswa lokal

4. Grafik Row Chart (Distribution of Status by Attendance Type)

   ![Distribution of Status by Attendance Type-5_29_2025, 6_20_34 AM](https://github.com/user-attachments/assets/b66630ec-4ba3-47cd-ac2f-16c1f6fe8968)

   Grafik ini menjelaskan tentang distribusi status siswa (Graduate, Enrolled, Dropout) berdasarkan jenis kehadiran yang mereka pilih yaitu antara daytime (kelas siang     
   hari) atau evening (kelas sore hari). Kelas siang hari merupakan pilihan yang paling disukai oleh sebagian besar siswa, secara konsisten di antara status Graduates,
   Dropouts, dan Enrolled.

5. Grafik Pie Chart (Distribution of Gender)

   ![Distribution of Gender-5_29_2025, 6_15_51 AM](https://github.com/user-attachments/assets/6e564426-7cf0-4649-9670-9326996d2cf5)

   Grafik ini menjelaskan tentang distribusi jenis kelamin siswa, laki-laki sebanyak 1.556 siswa (35.17%) dan perempuan sebanyak 2.868 siswa (64.83%)

6. Grafik Row Chart (Distribution of Status by Scholarship Holder Status)

   ![Distribution of Status by Scholarship Holder Status-5_29_2025, 6_21_30 AM](https://github.com/user-attachments/assets/2ec2fe30-4cd6-40a8-b589-12d722018c97)

   Grafik ini menjelaskan tentang distribusi status siswa (Graduate, Enrolled, Dropout) berdasarkan status scholarship mereka, yes artinya mendapatkan scholarship dan no
   artinya tidak dapat scholarship. Di antara siswa yang menerima beasiswa, jumlah graduates lebih banyak daripada yang dropouts. Jumlah penerima beasiswa yang dropouts 
   hampir sama dengan yang saat ini masih enrolled.

7. Grafik Pie Chart (Distribution of Status)

   ![Distribution of Status-5_29_2025, 6_20_21 AM](https://github.com/user-attachments/assets/5ae7cfa0-7f3b-4120-9e45-8cfbcf66b663)

   Grafik ini menjelaskan tentang distribusi status siswa (Graduate, Enrolled, Dropout). Siswa dengan status graduates merupakan kelompok terbesar dengan persentase 49,93%, 
   diikuti oleh siswa yang dropouts sebesar 32,12%, dan siswa yang enrolled merupakan kelompok terkecil dengan persentase hanya 17,95%.

8. Grafik Row Chart (Distribution of Status by Debtor)

   ![Distribution of Status by Debtor-5_29_2025, 6_20_57 AM](https://github.com/user-attachments/assets/46089e23-e252-4fe3-ae73-ba062458b61f)

   Grafik ini menjelaskan tentang distribusi status siswa (Graduate, Enrolled, Dropout) berdasarkan apakah siswa memiliki utang atau tidak. Berdasarkan plot diatas, di 
   antara siswa yang memiliki utang, kelompok yang dropout merupakan kelompok terbesar, jauh lebih banyak dibandingkan dengan mereka yang graduates atau enrolled. Temuan 
   ini secara kuat menunjukkan bahwa faktor keuangan merupakan faktor utama yang mendorong dropouts dan mempengaruhi tingkat kelulusan.

9. Grafik Pie Chart (Distribution of Scholarship Holder)

   ![Distribution of Scholarship Holder-5_29_2025, 6_19_45 AM](https://github.com/user-attachments/assets/ae73fee2-f69c-4630-8ac2-c6b1ffa49654)

   Grafik ini menjelaskan tentang distribusi siswa yang mendapatkan beasiswa. Penerima beasiswa hanya menyumbang 24,84% (hampir seperempat) dari total siswa, dibandingkan 
   dengan 75,16% yang tidak menerima beasiswa.

10. Grafik Bar Chart (Distribution of Age at Enrollment)

    ![Distribution of Age At Enrollment-5_29_2025, 6_16_13 AM](https://github.com/user-attachments/assets/da34871c-3bb4-4c35-8aa3-1f8efaeb798e)

    Grafik ini menjelaskan tentang distribusi umur siswa pada Jaya Jaya Institut. Sebagian besar siswa yang mendaftar berusia antara 18 dan 21 tahun.

11. Grafik Pie Chart (Distribution of Debtor Status)

    ![Distribution of Debtor Status-5_29_2025, 6_18_56 AM](https://github.com/user-attachments/assets/8ac6b670-3ac2-40a8-b64c-b3c99388ba2f)

    Grafik ini menjelaskan tentang distribusi siswa yang memiliki utang. Sebagian kecil siswa (11,37%) memiliki utang, sementara mayoritas besar (88,63%) tidak memiliki     
    utang.

12. Grafik Bar Chart (Distribution of Course by Gender)

    ![Distribution of Course by Gender-5_29_2025, 6_17_37 AM](https://github.com/user-attachments/assets/b6a638b7-5afa-4422-85cc-0cd83085840c)

    Grafik ini menjelaskan tentang course yang diambil siswa berdasarkan jenis kelamin. Nursing adalah program studi dengan jumlah data terbanyak dan didominasi oleh 
    siswa perempuan, sementara  Biofuel Production Technologies memiliki jumlah data terendah dan didominasi oleh siswa laki-laki. Selain itu, jumlah siswa laki-laki 
    terbanyak terdapat pada program studi Informatics Engineering dan Management.

13. Grafik Row Chart (Distribution of Marital Status)

    ![Distribution of Marital Status-5_29_2025, 6_19_16 AM](https://github.com/user-attachments/assets/235ab8b5-54fc-4bec-8bcd-dfdfa622e17b)

    Grafik ini menjelaskan tentang distribusi status pernikahan siswa. Sebagian besar siswa adalah single dengan jumlah 3.919, diikuti oleh yang sudah menikah sebanyak 379, 
    yang bercerai sebanyak 91, dan seterusnya.

14. Grafik Row Chart (Distribution of Nationality)

    ![Distribution of Nationality-5_29_2025, 6_19_32 AM](https://github.com/user-attachments/assets/5abbdd96-5779-4c3a-90fe-7092818b8c07)

    Grafik ini menjelaskan tentang distribusi kewarganegaraan siswa. Portugal adalah kewarganegaraan siswa yang paling sering ditemukan dalam dataset ini, dengan persentase 
    97,51% dari total record.

15. Grafik Bar Chart (Distribution of Course by International Status)

    ![Distribution of Course by International Status-5_29_2025, 6_17_58 AM](https://github.com/user-attachments/assets/d1e9180a-6682-4564-86a2-e61f911bc242)

    Grafik ini menjelaskan tentang distribusi siswa yang internasional dan yang tidak. Mereka mengambil jurusan apa saja di Jaya Jaya Institut. Sebagian besar siswa adalah 
    siswa lokal. Siswa internasional, yang jumlahnya lebih sedikit, lebih cenderung memilih program studi Journalism and Communication. 

## Machine Learning Prediction System
Untuk mendukung institusi dalam mengantisipasi potensi siswa yang berisiko dropout dan melakukan pencegahan secara lebih awal, telah dikembangkan sebuah sistem prediksi. Sistem ini dibangun menggunakan platform Streamlit. Untuk menjalankan aplikasi ini secara lokal, pengguna dapat menjalankan perintah berikut di Terminal:

```bash
streamlit run students_performance_app.py
```

Sementara itu, untuk menghentikan aplikasi Streamlit yang sedang berjalan, cukup tekan Ctrl + C pada Terminal.

Sistem prediksi tersebut juga tersedia secara online dan dapat diakses langsung melalui tautan yang telah di-deploy ke Streamlit Cloud pada link berikut ini: https://student-dropout-analysis-and-prediction-id.streamlit.app

## Conclusion
Berikut adalah sejumlah poin utama yang dapat disimpulkan:

1. Status Akademik Siswa: Dari total 4.424 siswa, sekitar 32,12% tidak menyelesaikan studi (dropout). Siswa yang berhasil lulus umumnya berusia 20–25 tahun dan memiliki nilai penerimaan tinggi (120–160), sedangkan siswa berusia lebih tua dengan nilai rendah lebih cenderung mengalami dropout.
2. Demografi Siswa: Sebagian besar siswa adalah perempuan (64,83%) dan mayoritas berasal dari dalam negeri (97,51%), sementara siswa internasional hanya mencakup 2,49% dari total populasi.
3. Dampak Beasiswa: Siswa penerima beasiswa menunjukkan tingkat kelulusan yang lebih tinggi (37,79%) dibandingkan tingkat dropout mereka (9,43%), menandakan bahwa beasiswa berperan penting dalam keberhasilan akademik.
4. Distribusi Berdasarkan Program Studi: Program studi Nursing menjadi yang paling diminati dengan dominasi siswa perempuan, sedangkan Biofuel Production Technologies memiliki jumlah siswa paling sedikit, didominasi oleh laki-laki.
5. Aspek Keuangan: Sebagian besar siswa yang dropout (61,99%) memiliki status sebagai debitur, yang mengindikasikan bahwa tekanan finansial dapat menjadi faktor utama dalam kegagalan menyelesaikan pendidikan.


## Recommendation Action Items
Berikut beberapa rekomendasi yang dapat diimplementasikan Jaya Jaya Institut untuk mengatasi masalah tingginya tingkat dropout pada siswa:

1. Mengadakan Kelas Tambahan atau Bimbingan Belajar, terutama untuk siswa dengan nilai rendah, usia lebih tua, atau yang sudah berkeluarga.
2. Menawarkan Skema Pembayaran Fleksibel, seperti cicilan tanpa bunga atau pengurangan utang bagi siswa berprestasi yang menunggak biaya kuliah.
3. Memperluas Program Beasiswa, khususnya bagi siswa yang berpotensi dropout karena kesulitan keuangan.
4. Membangun Layanan Konseling dan Dukungan Psikologis, guna membantu siswa menghadapi tekanan finansial maupun akademik.
5. Menerapkan Sistem Pemantauan dan Prediksi Risiko Dropout, dengan memanfaatkan teknologi machine learning melalui platform prediksi yang telah tersedia.
6. Menyelenggarakan Program Gap Year, dilengkapi dengan orientasi khusus bagi siswa yang kembali, agar mereka dapat beradaptasi dengan perubahan lingkungan, teknologi, atau kurikulum.








    



   



   




   




