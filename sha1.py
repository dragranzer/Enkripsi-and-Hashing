import struct

class SHA1Hash:
    def __init__(self, data):

        self.data = data
        "5 Buah variabel penyangga"
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    def CLS(self, n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def padding(self):
        """
        512 bit = 64 bytes
        b"\x80" = 8 bit awal dengan 1 diawal
        b"\x00" = 8 bit 0
        8 = 64 bit panjang string
        padding 0 sisanya => 64 - 1 - 8 - panjang data
        """
        padding = b"\x80" + b"\x00" * (63 - (len(self.data) + 8) % 64)
        padded_data = str.encode(self.data) + padding + \
                        struct.pack(">Q", 8 * len(self.data))

        return padded_data

    def split_blocks(self):
        "Split plain text menjadi block-block sebesar 512 bit"
        return [
            self.padded_data[i : i + 64] \
                for i in range(0, len(self.padded_data), 64)
        ]

    def create_w(self, block):
        """
        dibutuhkan 16 word
        L = 4 bytes = 32 bit
        """
        "W0 - W15"
        w = list(struct.unpack(">16L", block)) + [0] * 64
        "W16 - W80"
        for i in range(16, 80):
            w[i] = self.CLS((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        return w

    def hash(self):
        self.padded_data = self.padding()
        self.blocks = self.split_blocks()

        for block in self.blocks:
            w = self.create_w(block)
            "Inisiasi Penyangga"
            a, b, c, d, e = self.h

            "80 round pengolahan pesan"
            for i in range(0, 80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = (
                    self.CLS(a, 5) + f + e + w[i] + k & 0xFFFFFFFF,
                    a,
                    self.CLS(b, 30),
                    c,
                    d,
                )

            "Diambil 8 bit terakhir"
            self.h = (
                self.h[0] + a & 0xFFFFFFFF,
                self.h[1] + b & 0xFFFFFFFF,
                self.h[2] + c & 0xFFFFFFFF,
                self.h[3] + d & 0xFFFFFFFF,
                self.h[4] + e & 0xFFFFFFFF,
            )

        "40 bit hasil pengolahan"
        return "%08x%08x%08x%08x%08x" % tuple(self.h)

if __name__ == '__main__':
    plaintext = input("Masukkan Plaintext: ")
    print("Plaintext: "+plaintext)

    sha1_hash = SHA1Hash(plaintext)
    hash_result = sha1_hash.hash()

    print("SHA-1 Hashing: "+hash_result)
