class HMAC():
    def __init__(self, key, message, hash=None):
        #masukan fungsi hash pada atribut hash dan set panjang bits 128
        self.hash = hash
        self.b_bits = 128

        #ubah key dan message menjadi representasi bit
        self.key_b = ''.join(format(ord(i), '08b') for i in key)
        self.message_b = ''.join(format(ord(i), '08b') for i in message)

        #lakukan padding left pada key_plus dan message binary sehingga panjangannya sama dgn b_bits
        self.key_plus = self.left_padding(self.key_b)
        self.message_b = self.left_padding(self.message_b)
        
        #set nilai binary ipad
        ipad =  '00110110'
        #ulangi nilai ipad sepanjang b_bits
        self.ipad = ipad * (self.b_bits // len(ipad))
        #xor ipad dan key_plus
        self.Si = ''.join('0' if i == j else '1' for i, j in zip(self.key_plus,self.ipad))

        #set nilai binary opad
        opad = '01011100'
        #ulangi nilai opad sepanjang b_bits
        self.opad = opad * (self.b_bits // len(opad))
        #xor opad dan key_plus
        self.So = ''.join('0' if i == j else '1' for i, j in zip(self.key_plus,self.opad))
    
    #fungsi untuk mengubah representasi binary to string
    def bin_to_str(self, str_bins):
        #split binary per 8 bits untuk diubah ke string biasa
        val_bins = [str_bins[0+i:8+i] for i in range(0, len(str_bins), 8)]
        #diubah menjadi integer lalu char ascii dan char dijoinkan jadi string
        str_val = ''.join([chr(int(x, 2)) for x in val_bins])
        return str_val
    
    #fungsi left pedding pada inputan binary agar panjangnya b_bits
    def left_padding(self, bin_inp):
        #hitung seberapa banyak bit yang akan ditambahkan
        wanting = len(bin_inp)%self.b_bits
        #tambahkan nol sepanjang 'wanting' di depan inputan binary
        bin_out = '0' * (self.b_bits-wanting) + bin_inp
        return bin_out

    #fungsi untuk mendapatkan intisari hmac dari message, key, dan Hashing algoritma
    def digest(self):
        #Concat Si dan message binary dan ubah menjadi string
        str1 = self.bin_to_str(self.Si + self.message_b)
        #hash dengan fungsi hash yang disediakan
        hash1 = self.hash(str1)
        str1_hash = hash1.hash()

        #ubah string hasil hash menjadi representasi binary pada python
        bin1_hash = ''.join(format(ord(i), '08b') for i in str1_hash)
        #left padding
        bin1_hash = self.left_padding(bin1_hash)

        #Concat So dan message binary dan ubah menjadi string
        str2 = self.bin_to_str(self.So + bin1_hash)
        #hash dengan fungsi hash yang disediakan
        hash2 = self.hash(str2)
        str2_hash = hash2.hash()
        
        #kembalikan hasil hash
        return str2_hash

if __name__ == '__main__':
    #representasi dari pengirim
    #pesan dan kunci dari pengirim
    msg = 'ini adalah hmac untuk mata kuliah KIJ'
    key = 'cobalagi'

    #import hash function yang digunakan
    from sha1 import SHA1Hash as sha1

    #panggil kelas HMAC dengan masukan kunci, pesan, dan fungsi hash
    hmac = HMAC(key, msg, sha1)
    #print hasil digest hmac dari pengirim
    hmac_sender = hmac.digest()
    print("message_sender:", msg)
    print("hmac_sender:", hmac_sender)

    print()

    #representasi dari penerima
    #pesan dan kunci dari penerima
    key_rec = 'cobalagi'
    msg_rec = msg

    #panggil kelas HMAC dengan masukan kunci, pesan, dan fungsi hash
    hmac_2 = HMAC(key_rec, msg_rec, sha1)
    #print hasil digest hmac penerima, 
    #jika pesan atau kunci berbeda dari pengirim maka hmac_sender dan hmac_penerima akan berbeda
    hmac_receiver = hmac_2.digest()
    print("message receiver:", msg_rec)
    print("hmac_receiver:", hmac_receiver)

    #check apakah hmac pengirim dan penerima berbeda atua sama
    print(hmac_sender==hmac_receiver)