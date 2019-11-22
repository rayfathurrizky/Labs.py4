NSL=[]
NIML=[]
NTSL=[]
NUTSL=[]
NUASL=[]
NAL=[]

jawab="y"
while jawab=="y":
    NS=input("Nama Siswa  : ")
    NIM=input("Nim Siswa   : ")
    TUGAS=int(input("Nilai Tugas : "))
    UTS=int(input("Nilai UTS   : "))
    UAS=int(input("Nilai UAS   : "))
    nilai=float(TUGAS)*30/100 + (UTS)*35/100 + (UAS)*35/100 #float Adalah fungsi Untuk Memecahkan Angka
        

    NSL.append(NS)
    NIML.append(NIM)
    NTSL.append(TUGAS)
    NUTSL.append(UTS)
    NUASL.append(UAS)
    NAL.append(nilai)

    jawab = input("Ingin Menambah Data(y/t)? ")
    if jawab=="t":
        break
        print()
print("==================================================================")
print("|","NO","|","   NAMA    ","|","  NIM  ","|"," TUGAS ","|"," UTS ","|"," UAS ","|"," AKHIR ","|")
print("==================================================================")

for j in range(len(NSL)):
    print("|", j+1, " | ", NSL[j] , " | ", NIML[j] ,"  | ", NTSL[j] , "    | ", NUTSL[j], "  | ", NUASL[j] , "  | ", NAL[j] , " |")
print("==================================================================")
