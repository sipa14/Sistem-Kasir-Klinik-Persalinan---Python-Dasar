while True:
    print("\n" + "="*60)
    kp=input("Masukan Kode Pasien\t:")
    nama=input("Masukan Nama\t:")
    kls=input("Masukan Kelas(A/B/C)\t:").upper()
    li=int(input("Masukan Lama Inap\t:"))
    
    if kls =="A":
        p = "Bidan"
        b_m = 300000
    elif kls=="B":
        p="Bidan"
        b_m=350000
    elif kls=="C":
        p="Dokter"
        b_m=500000
    else:
        print("Kelas Tidak Terdeteksi")
        p="-"
        b_m=0
        
    tb=li*b_m
    print("-"*50)
    print(f"Kode Pasien\t: {kp}")
    print(f"Nama Pasien\t: {nama}")
    print(f"Kelas\t\t: {kls}")
    print(f"Penanganan\t: {p}")
    print(f"Lama Inap\t: {li}")
    print(f"Biaya/Malam\t: Rp{b_m:,}")
    print(f"Total Bayar\t: Rp{tb:,}")
    
    ask=input("Apakah Ingin Memasukan Data lagi? (Y/N)\t:").lower()
    if ask=="n":
        print("\nTerima Kasih!")
        break
    else:
        print("\n" + "="*60)

