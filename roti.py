# Versi Sebelum Refactor
st = [] # list roti

def p():
    global st
    n = input("Nama roti: ")
    q = int(input("Jumlah: "))
    
    # Nested if yang membingungkan
    if n != "":
        found = False
        for i in st:
            if i[0] == n:
                if i[1] >= q:
                    i[1] -= q
                    print("Berhasil")
                else:
                    print("Stok kurang")
                found = True
        if not found:
            print("Roti tidak ada")