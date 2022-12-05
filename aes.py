s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

rcond = [
    [1,0,0,0],[2,0,0,0],[4,0,0,0],[8,0,0,0],[16,0,0,0],
    [32,0,0,0],[64,0,0,0],[128,0,0,0],[27,0,0,0],[54,0,0,0],
]

def sub_bytes_single(s):
    for i in range(4):
        s[i] = s_box[s[i]]
    return s

def text2hexmatrix(plaintext):
    text_matrix = [list(plaintext[i:i+4]) for i in range(0, len(plaintext), 4)]
    hex_matrix = []
    for i in text_matrix:
        temp1D = []
        for j in i:
            temp1D.append(ord(j))

        hex_matrix.append(temp1D)

    return hex_matrix

def add_round_key(s, k):
    a = []
    for i in range(4):
        b = []
        for j in range(4):
            b.append(s[i][j] ^ k[i][j])
        a.append(b)
    return a

def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]
    return s

def inv_sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = inv_s_box[s[i][j]]

    return s

def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = \
    s[1][1], s[2][1], s[3][1], s[0][1]

    s[0][2], s[1][2], s[2][2], s[3][2] = \
    s[2][2], s[3][2], s[0][2], s[1][2]

    s[0][3], s[1][3], s[2][3], s[3][3] = \
    s[3][3], s[0][3], s[1][3], s[2][3]

    return s

def inv_shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = \
    s[3][1], s[0][1], s[1][1], s[2][1]

    s[0][2], s[1][2], s[2][2], s[3][2] = \
    s[2][2], s[3][2], s[0][2], s[1][2]

    s[0][3], s[1][3], s[2][3], s[3][3] = \
    s[1][3], s[2][3], s[3][3], s[0][3]

    return s

def mix_single_column(ri, ti):
    """
    Perkalian antar 1 kolom pada r[i] dan t[i]
    Untuk ri[i]:
    3 = 011 = X + 1
    2 = 010 = X
    1 = 001 = 1
    """
    arr = []
    for i in range(4):
        if ri[i] == 3:
            temp = 2*ti[i] # dikalikan dengan X
            "Jika setelah dikali X nilai lebih dari 8 bit"
            if temp > 255:
                "bit ke 9 atau X^9 dihilangkan"
                temp -= 256
                "di gantikan dengan xor (X^4 + X^3 + X + 1)"
                "ekivalen dengan 00011011 = 27"
                temp ^= 27
            "hasil temp kemudian di XOR dengan 1*ti[i] = t[i]"
            temp ^= ti[i]
            arr.append(temp)
        elif ri[i]==2:
            temp = 2*ti[i]
            "Dilakukan pengecekan apabila nilai leboh dari 8 bit"
            if temp > 255:
                temp -= 256
                temp ^= 27
            arr.append(temp)
        else:
            arr.append(ri[i]*ti[i])

    "XOR pada semua hasil perkalian cell pada kolom"
    r = arr[0]^arr[1]^arr[2]^arr[3]

    return r

def inv_mix_single_column(ri, ti):
    """
    Tabel r inverse memiliki value 9,11,13,14
    9 = 1001 = X^3 + 1
    11 = 1011 = X^3 + X + 1
    13 = 1101 = X^3 + X^2 + 1
    14 = 1110 = X^3 + X^2 + X

    Karena suku tertinggi adalah X^3 maka bisa disimpulkan
    bit tertinggi adalah X^7 * X^3 = X^10 = 10000000000 = 1024
    Supaya bilangan tetap dalam 8 bit maka:
    X^10 = X^8 * X^2
    Dengan menggunakan Irreducible Polynomial Theorem, GF(2^3)
    X^8 = X^4 + X^3 + X + 1 = 11011 = 27
    Jadi apabila muncul bit ke X^8 atau bit ke 8 dapat di replace
    dengan melakukan XOR dengan bilangan 27
    """
    arr = []
    for i in range(4):
        replace = 0
        res = 0
        if ri[i] == 9:
            "X^3"
            temp = 8*ti[i]
            "Pengecekan apabila ada yang > X^10"
            if temp >= 1024:
                temp -= 1024
                """
                jika ada maka X^10 di replace dengan
                X^10 = X^8 * X^2
                X^10 = (X^4 + X^3 + X + 1) * X^2
                X^10 = X^6 + X^5 + X^3 + X^2
                X^10 = 1101100 = 108
                """
                replace ^= 108
            "Pengecekan apabila ada yang > X^9"
            if temp >= 512:
                "X^9 = X^8 * X"
                temp -= 512
                replace ^= 54
            "Pengecekan apabila ada yang > X^8"
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res = temp ^ replace
            "1"
            res ^= ti[i]
            arr.append(res)
        elif ri[i] == 11:
            "X^3"
            temp = 8*ti[i]
            if temp >= 1024:
                temp -= 1024
                replace ^= 108
            if temp >= 512:
                temp -= 512
                replace ^= 54
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res = temp ^ replace
            "X"
            temp = 2*ti[i]
            replace = 0
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res ^= temp
            res ^= replace
            "1"
            res ^= ti[i]
            arr.append(res)
        elif ri[i] == 13:
            "X^3"
            temp = 8*ti[i]
            if temp >= 1024:
                temp -= 1024
                replace ^= 108
            if temp >= 512:
                temp -= 512
                replace ^= 54
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res = temp ^ replace
            "X^2"
            temp = 4*ti[i]
            replace = 0
            if temp >= 512:
                temp -= 512
                replace ^= 54
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res ^= temp
            res ^= replace
            "1"
            res ^= ti[i]
            arr.append(res)
        
        elif ri[i] == 14:
            "X^3"
            temp = 8*ti[i]
            if temp >= 1024:
                temp -= 1024
                replace ^= 108
            if temp >= 512:
                temp -= 512
                replace ^= 54
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res = temp ^ replace
            "X^2"
            temp = 4*ti[i]
            replace = 0
            if temp >= 512:
                temp -= 512
                replace ^= 54
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res ^= temp
            res ^= replace
            "X"
            temp = 2*ti[i]
            replace = 0
            if temp >= 256:
                temp -= 256
                replace ^= 27
            res ^= temp
            res ^= replace

            arr.append(res)

    r = arr[0]^arr[1]^arr[2]^arr[3]

    return r


def mix_columns(t):
    "tabel r"
    r = [
        [2,3,1,1],
        [1,2,3,1],
        [1,1,2,3],
        [3,1,1,2]
    ]
    mc = []
    for i in range(4):
        temp = []
        for j in range(4):
            "perkalian single column antara tabel r dan text"
            a = mix_single_column(r[j], t[i])            
            temp.append(a)
        mc.append(temp)

    return mc

def inv_mix_columns(t):
    "inverse dari table r"
    r = [
        [14,11,13,9],
        [9,14,11,13],
        [13,9,14,11],
        [11,13,9,14]
    ]
    mc = [] # hasil perkalian dari tabel r dan text
    for i in range(4):
        temp = []
        for j in range(4):
            "perkalian single column antara tabel r(invers) dan text"
            a = inv_mix_single_column(r[j], t[i])            
            temp.append(a)
        mc.append(temp)

    return mc

def int2hex(s):
    a = []
    for i in range(4):
        b = []
        for j in range(4):
            b.append(hex(s[i][j]))
            # s[i][j] = hex(s[i][j])
        a.append(b)
    print(a)

class AES:
    
    def __init__(self, master_key):
        """
        Initializes the object with a given key.
        """
        self._key_matrices = self._expand_key(master_key)

    def _expand_key(self, key):
        """
        Pembuatan 10 round key berdasarkan 16 byte key awal
        """
        hex_key = text2hexmatrix(key)

        keys = [] # keys terdiri dari 11 key dari key[0] - key[10]

        keys.append(hex_key) # key[0] adalah chiperkey

        "Generate key[1] - key[10]"
        for i in range(1,11):
            result = [] # key ke - i
            temp_key = keys[i-1].copy() # mengambil key i-1

            rotword = temp_key[3].copy() # mengambil kolom ke 4 dari key i-1

            "rotword = penggeseran keatas 4 cell pada kolom ke 4 dari key i-1"
            rotword[0], rotword[1], rotword[2], rotword[3] = \
            rotword[1], rotword[2], rotword[3], rotword[0]

            "rotword kemudian di sub-byte berdasarkan s-box"
            sub_byte_key = sub_bytes_single(rotword)

            xor_key = [] # kolom pertama pada key ke i
            for j in range(4):
                xor_key.append(sub_byte_key[j] ^ temp_key[0][j] ^ rcond[i-1][j])
            
            result.append(xor_key)

            "generate kolom ke 1-3 dari key ke i"
            for k in range(1,4):
                r_temp = []
                for j in range(4):
                    r_temp.append(result[k-1][j] ^ temp_key[k][j])
                result.append(r_temp)
            keys.append(result)

        return keys

    def encrypt_block(self, plaintext):
        hex_matrix = text2hexmatrix(plaintext)
        "Initial Round"
        chipertext = add_round_key(hex_matrix, self._key_matrices[0])

        "9 Main Rounds"
        for i in range(9):
            sb1 = sub_bytes(chipertext.copy())
            sr1 = shift_rows(sb1.copy())
            mc = mix_columns(sr1.copy())
            chipertext = add_round_key(mc.copy(), self._key_matrices[i+1])
        
        "Final Round"
        sb = sub_bytes(chipertext.copy())
        sr = shift_rows(sb.copy())
        chipertext = add_round_key(sr, self._key_matrices[10])

        return chipertext

    def decrypt_block(self, ciphertext):
        hex_matrix = text2hexmatrix(ciphertext)

        "Initial Round"
        plaintext = add_round_key(hex_matrix, self._key_matrices[10])
        plaintext = inv_shift_rows(plaintext.copy())
        plaintext = inv_sub_bytes(plaintext.copy())

        "9 Main Round"
        for i in range(9, 0, -1):
            ark = add_round_key(plaintext.copy(), self._key_matrices[i])
            imc = inv_mix_columns(ark.copy())
            isr = inv_shift_rows(imc.copy())
            plaintext = inv_sub_bytes(isr.copy())

        "Final Round"
        plaintext = add_round_key(plaintext, self._key_matrices[0])

        return plaintext
        
def padded_plaintext(plaintext):
    """
    Apabila plaintext bukan kelipatan 16 maka akan ditambah
    dengan spasi " " di akhir kalimat sehingga menjadi kelipatan 16
    """
    counter = int(len(plaintext)/16)
    add_pad = 0
    if counter*16 < len(plaintext):
        add_pad = counter*16 + 16 - len(plaintext)
    else:
        add_pad = counter*16
    if add_pad != 0:
        counter += 1
        for i in range(add_pad):
            plaintext += " "

    return plaintext, counter

def padded_key(key):
    """
    Apabila key kurang dari 16 karakter maka akan ditambah dengan z
    di akhir kalimat
    """
    if len(key) < 16:
        for i in range(16-len(key)):
            key += "z"

    """
    Apabila key lebih dari 16 karakter maka char ke 16 akan di xor
    dengan char ke j, j=16+i lalu char ke j akan dihapus
    sehingga key tepat 16 karakter
    """
    if len(key) > 16:
        new_key = [x for x in key]
        new_key[15] = ord(new_key[15])
        for i in range(16, len(new_key)):
            new_key[15] ^= ord(new_key[i])
        new_key[15] = chr(new_key[15])
        new_key = new_key[0:16]
        key = ""
        for i in range(len(new_key)):
            key += new_key[i]

    return key

if __name__ == '__main__':
    plaintext = input("Masukkan Plaintext: ")
    key = input("Masukkan 16 char key: ")

    print("Plaintext: " + plaintext)
    print("Key: " + key)
    print()

    "Pemrosesan apabila input belum sesuai"
    plaintext, counter = padded_plaintext(plaintext)
    key = padded_key(key)
    
    aes = AES(key)
    
    res_chipertext = ""
    res_decrypted = ""
    for i in range(counter):
        "Pemisahan plaintext menjadi 1 atau lebih block dan enkripsi"
        chipertext = aes.encrypt_block(plaintext[i*16:(i+1)*16])

        str_chippertext = ""
        for i in range(4):
            for j in range(4):
                str_chippertext += chr(chipertext[i][j])
        
        res_chipertext += str_chippertext

        "Dekripsi"
        decrypted = aes.decrypt_block(str_chippertext)

        "Concat block yang telah dipisah"
        str_decrypted = ""
        for i in range(4):
            for j in range(4):
                str_decrypted += chr(decrypted[i][j])
        res_decrypted += str_decrypted

    print("Enkripsi: ", end='')
    print(res_chipertext)
    print()

    print("Dekripsi: ", end='')
    print(res_decrypted)