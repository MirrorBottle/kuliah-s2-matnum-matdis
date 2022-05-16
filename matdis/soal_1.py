def main(a, b):
    gcd = cari_pbb(a,b, True)
    print("PBB(%d, %d) = %d" % (a,b,gcd))
    

def cari_pbb(a,b, denganLangkah = False):
    """
    Mencari PBB menggunakan Algoritma Eucledian
    Parameters
    ----------
    a : int
    b : int
    denganLangkah : boolean
        Kalau true maka menunjukkan langkah-langkah nya
    Kembalian
    -------
    int,
        PBB dari a dan b
    (int, int)
        Returned from find_extended_gcd
    """

    if denganLangkah:
        print("--------------- Persamaan Kombinasi Lanjar ---------------")
        
    # Pastikan a selalu lebih besar dari b
    if (b > a):
        b,a = a,b

    jumlah_persamaan = []
    while (a % b != 0):
        q,r = a//b, a%b
        jumlah_persamaan.append(q)
        if denganLangkah:
            print("%d = %d(%d) + %d" % (a,b,q,r))
        a = b
        b = r
        
    if denganLangkah:
        print("-------------- /Persamaan Kombinasi Lanjar ---------------")
        print()
        
    return r


if __name__ == '__main__':
    a = 1242
    b = 1986
    main(a, b)