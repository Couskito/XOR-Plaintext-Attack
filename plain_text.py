import argparse


class Cracker():
    def __init__(self, _ciphertext, _plaintext, _offset, _key_length):
        self.ciphertext = _ciphertext
        self.plaintext = _plaintext
        self.offset = _offset
        self.key_length = _key_length
        self.key = bytes([x ^ y for x, 
                                    y in zip(self.plaintext,
                                             self.ciphertext[self.offset:self.offset+len(self.plaintext[:])][:self.key_length])])

    def decipher(self):
        return bytes([self.ciphertext[i] ^ self.key[i % len(self.key)] for i in range(len(self.ciphertext))])


def main():
    parser = argparse.ArgumentParser(description='Simple yet useful tool to automate\
                                                    XOR Plaintext attacks.')
    parser.add_argument('-o', type=int, help='Offset at which the ciphered plaintext\
                                              is located within the ciphertext, defaults to 0.', default=0)
    cipher_group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('keylength', help='Length of the key used for encryption \
                                          all excess bytes will be ignored.', default=4, type=int)
    cipher_group.add_argument('-c', help='Ciphertext as string.')
    cipher_group.add_argument('--cipherfile', help='Name of the file\
                                                    containing the ciphertext.')
    plain_group = parser.add_mutually_exclusive_group(required=True)
    plain_group.add_argument('-p', help='Plaintext as string.')
    plain_group.add_argument('--plainfile', help='Name of the \
                                                  file containing the plaintext.')
    parser.add_argument('--output', help='Name of the \
                                          output deciphered file, defaults to out.file.', default='out.file')

    args = vars(parser.parse_args())

    if args['cipherfile'] is not None:
        try:
            with open(args['cipherfile'], 'rb') as f:
                ciphertext = f.read()
        except FileNotFoundError:
            print("Could not find ciphertext file.")
    else:
        ciphertext = args['c'].encode('utf-8')

    if args['plainfile'] is not None:
        try:
            with open(args['plainfile'], 'rb') as f:
                plaintext = f.read()
        except FileNotFoundError:
            print("Could not find plaintext file.")
    else:
        plaintext = args['p'].encode('utf-8')

    c = Cracker(ciphertext, plaintext, args['o'],args['keylength'])
    print(f"Found key : {c.key}, also wrote to ./key.txt in case key contains non printable characters")
    
    with open(args['output'], 'wb') as f:
        f.write(c.decipher())
    with open('key.txt', 'wb') as f:
        f.write(c.key)

if __name__ == '__main__':
    main()
