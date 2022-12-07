def blum_blum_shub(seed=77):
    #modulus yang digunakan di algoritma BBS
    #angkanya bebas, tp di sini diisi oleh hasil kali 2 bilangan prima
    n = 11*19
    #nilai dari angka seed, dan angkanya bebas di sini saya mengisinya tergantung dari user
    #tapi nilai defaultnya adalah 77
    s = seed

    #algoritma blum blum shub
    store = ""
    for _ in range(10): #diiterasi 10 kali
        s = (s**2) % n
        store += str(s%2)
    return store

if __name__ == '__main__':
    print(blum_blum_shub(31))