monoalpha_cipher = {
  'a': 'm','b': 'n','c': 'b','d': 'v','e': 'c','f': 'x',
  'g': 'z','h': 'a','i': 's','j': 'd','k': 'f','l': 'g',
  'm': 'h','n': 'j','o': 'k','p': 'l','q': 'p','r': 'o',
  's': 'i','t': 'u','u': 'y','v': 't','w': 'r','x': 'e',
  'y': 'w','z': 'q',' ': ' ',
  'A': 'M','B': 'N','C': 'B','D': 'V','E': 'C','F': 'X',
  'G': 'Z','H': 'A','I': 'S','J': 'D','K': 'F','L': 'G',
  'M': 'H','N': 'J','O': 'K','P': 'L','Q': 'P','R': 'O',
  'S': 'I','T': 'U','U': 'Y','V': 'T','W': 'R','X': 'E',
  'Y': 'W','Z': 'Q',
}

def encrypt_monoalphabet(plaintext):
    """
    Substitusi tiap string dari plaintext untuk menghasilkan chipertext
    """
    tokenized = [x for x in plaintext] #tokenisasi
    chipertext_arr = [monoalpha_cipher[i] for i in tokenized] #substitusi
    chipertext = ""
    for i in chipertext_arr:
        chipertext += i # concat
    return chipertext

if __name__ == '__main__':
    print("Masukkan plaintext:")
    plaintext = input()

    print("Plaintext: " + plaintext)
    encrypted = encrypt_monoalphabet(plaintext)
    print("Chipertext: " + encrypted)