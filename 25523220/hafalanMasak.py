#input jumlah hafalan masing masing anak
anak1 = int(input("msaukan hafalan anak1: "))
anak2 = int(input("msaukan hafalan anak2: "))
anak3 = int(input("msaukan hafalan anak3: "))

#kondisi unutuk memenuhi syarat makanan favorit masing masing anak
if anak1 > anak2 and anak1 > anak3:
    print("Makan Rawon")
elif anak2 > anak1 and anak2 > anak3:
    print("Makan Pecel")
else:
    print("Makan Gulai")
