#TUGAS BESAR KONSEP PEMROGRAMAN SEM_2
print("=============================================================================")
print("_____________________APLIKASI PENDAFTARAN ANTRIAN ONLINE_____________________")
print("                           RUMAH SAKIT HAPPY ENDING")
print("=============================================================================")
print()
print()

print("Selamat Datang Di Layanan Pendaftaran Antrian Online Rumah Sakit Happy Ending")
print()

kondisi = "sakit"

while kondisi == "sakit":

  #def option():
  print("Daftar Pilihan: ")
  print("Kategori_Pasien:")
  print("      1. Pasien Baru")
  print("      2. Pasien Lama")
  print("Kategori_Layanan:")
  print("      A. BPJS sejenisnya")
  print("      B. UMUM")
  print("Contoh : (pasien.layanan) ==> 1.B")
  pilihan=str(input("Silahkan Masukkan Pilihan Anda: "))


  def poli():
    print("Daftar Poli:")
    print("    A. Poli UMUM")
    print("    B. Poli ANAK")
    print("    C. Poli SYARAF")
    print("    D. Poli JANTUNG")
    print("    E. Keluar")
    menupoli=str(input("Masukkan pilihan Anda: "))
    return menupoli
    if menupoli == "A" or menupoli == "a":
      poli_umum()
    elif menupoli == "B" or menupoli == "b":
      poli_anak()
    elif menupoli == "C" or menupoli == "c":
      poli_syaraf()
    elif menupoli == "D" or menupoli == "d":
      poli_jantung()
    elif menupoli == "E" or menupoli == "e":
      exit()
    else:
      print("Menu tidak tersedia!")


  def form():
    print(".................Formulir Pendaftaran Pasien Baru................")
    nik=int(input("NIK : "))
    nama=str(input("Nama : "))
    jk=str(input("L/P : "))
    ttl=str(input("Tempat, Tanggal Lahir : "))
    alt=str(input("Alamat : "))
    rwt=str(input("Riwayat:"))
    rjk=str(input("Apakah Anda memiliki rujukan?(Y/N) : "))
    if(rjk=="Y") or (rjk=="y"):
      Rs=str(input("RS rujukan: "))
   

  if pilihan == "1.B" or pilihan == "1.b" or pilihan == "1.A" or pilihan == "1.a":
    formulir=form()
    poli=poli()
  elif pilihan == "2.B" or pilihan == "2.b" or pilihan == "2.A" or pilihan == "2.a":
    poli=poli()
  elif pilihan == "0":
    exit()
  else:
    print("Menu tidak tersedia!")


  import random
   

  def loket():
    if pilihan == "1.B" or pilihan == "1.b" or  pilihan == "2.B" or pilihan == "2.b":
      print("lOKET 3")
    elif pilihan == "1.A" or pilihan == "1.a" or pilihan == "2.A" or pilihan == "2.a":
      print("lOKET 4")


  def struk():
    print("=================================================================")
    print("               RUMAH SAKIT HAPPY ENDINGPERCO")
    print("                 Kota Terdepan di Abbadnya")
    print("             Jl Hallu Bareng No.210 Kompas Utara")
    print("=================================================================")
    print()
    print("                         NOMER ANTRIAN")
    print("                             ",random.randint(30,200))
    print("                          loket",loket())
    print("                            Poli",poli)
    print()
    print("                  Terimakasih Atas Kunjungan Anda")
    print ("                        Semoga Lekas Sembuh")
    print("                     Senin, 22 Maret 2021 09.35")

  print(struk())

  periksa = str(input("Anda akan mendaftar antrian kembali (Y/N): "))

  if(periksa=="Y") or (periksa=="y"):
    pass
  else:
    break

