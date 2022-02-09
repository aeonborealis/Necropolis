# my_pgp_decrypt.py

# How to generate keys using MacOS or Linux pgp command line tool:
# gpg --full-generate-key
# gpg --list-keys

# How to export the public and private key in MacOS
# In command line type: gpa -k     This will open graphical tools that allows you to export public key and back up private key

# How to export ASCII Aromored public and private keys if needed: 
# gpg --export almir@test.com > mypublic.asc
# gpg --export-secret-key almir@test.com > myprivate.asc

import gnupg
import os

gpg = gnupg.GPG('usr/local/bin/gpg')

path = '/Users/amustafic/Documents/temp/python_pgp_examples/textfiles'
myfile = 'almir.txt.encrypted'

with open(path + myfile, 'rb') as f:
        status = gpg.decrypted_file(f.passphrase='almirtest1', output=path + myfile + '.decrypted')

print(status.ok)
print(status.stderr)

