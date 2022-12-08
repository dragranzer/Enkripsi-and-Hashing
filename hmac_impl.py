class HMAC():
    def __init__(self, key, message, hash=None):
        self.hash = hash
        self.b_bits = 128

        self.key_b = ''.join(format(ord(i), '08b') for i in key)
        self.message_b = ''.join(format(ord(i), '08b') for i in message)

        #padding left
        self.key_plus = '0' * (self.b_bits-len(self.key_b)) + self.key_b
        wanting = len(self.message_b)%self.b_bits
        self.message_b = '0' * (self.b_bits-wanting) + self.message_b
        
        ipad =  '00110110'
        self.ipad = ipad * (self.b_bits // len(ipad))
        #xor binary
        self.Si = ''.join('0' if i == j else '1' for i, j in zip(self.key_plus,self.ipad))

        opad = '01011100'
        self.opad = opad * (self.b_bits // len(opad))
        self.So = ''.join('0' if i == j else '1' for i, j in zip(self.key_plus,self.opad))
    
    def bin_to_str(self, str_bins):
        #split binary per 8 bits untuk diubah ke string biasa
        val_bins = [str_bins[0+i:8+i] for i in range(0, len(str_bins), 8)]
        #diubah dlu menjadi integer lalu char dan char dijoinkan jadi string
        str_val = ''.join([chr(int(x, 2)) for x in val_bins])
        return str_val
    
    def digest(self):
        str1 = self.bin_to_str(self.Si + self.message_b)
        hash1 = self.hash(str1)
        str1_hash = hash1.hash()

        # #lef pad
        bin1_hash = ''.join(format(ord(i), '08b') for i in str1_hash)
        wanting = len(bin1_hash)%self.b_bits
        bin1_hash = '0' * (self.b_bits - wanting) + bin1_hash

        str2 = self.bin_to_str(self.So + bin1_hash)
        hash2 = self.hash(str2)
        str2_hash = hash2.hash()
        
        return str2_hash

if __name__ == '__main__':
    #sender
    msg = 'ini adalah hmac untuk mata kuliah KIJ'
    key = 'cobalagi'

    from sha1 import SHA1Hash as sha1

    hmac = HMAC(key, msg, sha1)
    hmac_sender = hmac.digest()
    print("message_sender:", msg)
    print("hmac_sender:", hmac_sender)

    print()

    #receiver
    key_rec = 'cobalagi'
    msg_rec = msg

    hmac_2 = HMAC(key_rec, msg_rec, sha1)
    hmac_receiver = hmac_2.digest()
    print("message receiver:", msg_rec)
    print("hmac_receiver:", hmac_receiver)

    print(hmac_sender==hmac_receiver)