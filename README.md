# Description

Just a quick shot at automating XOR plaintext attacks with a simple command-line program, using Python 3.

## Usage

```
usage: plain_text.py [-h] [-o O] (-c C | --cipherfile CIPHERFILE) (-p P | --plainfile PLAINFILE) [--output OUTPUT] keylength

Simple yet useful tool to automate XOR Plaintext attacks.

positional arguments:
  keylength             Length of the key used for encryption all excess bytes will be ignored.

optional arguments:
  -h, --help            show this help message and exit
  -o O                  Offset at which the ciphered plaintext is located within the ciphertext, defaults to 0.
  -c C                  Ciphertext as string.
  --cipherfile CIPHERFILE
                        Name of the file containing the ciphertext.
  -p P                  Plaintext as string.
  --plainfile PLAINFILE
                        Name of the file containing the plaintext.
  --output OUTPUT       Name of the output deciphered file, defaults to out.file.
```

## Example

To use with strings : 
```bash
python3 plain_text.py 4 --cipherfile ./cipherfile  -p 'Hello' --output out.file
```

The output should be : 
```
Found key : b'Test', also wrote to ./key.txt in case key contains non printable characters
```

out.file then contains our deciphered payload : 

```
Hello World
```

### TODO
Add key length guessing using entropy / result of binwalk for file extraction.

## License
[MIT](https://choosealicense.com/licenses/mit/)
