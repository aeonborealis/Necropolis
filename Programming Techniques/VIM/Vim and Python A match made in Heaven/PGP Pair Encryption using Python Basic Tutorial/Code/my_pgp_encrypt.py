# my_pgp_encrypt.py

# How to generate PGP Public Private key pair on MacOS or Linux
# gpg --full-generate-key
# gpg --list-keys

# How to export the public and private keys on MacOS
# in command line type: gpa -k      This will open graphical tools that allow you to export public and backup private key

# How to export ASCII Armored PGP public and private keys:
# gpg --export almir@test.com > mypublic.asc
# gpg --export-secret-key almir@test.com > myprivate.asc

import gnupg
import os

gpg = gnupg.GPG('/usr/local/bin/gpg')

# Change user Path directory

path = '/Users/amustafic/Documents/temp/python_pgp_examples/textfiles'
myfile = '/amir.txt'

with open(path + myfile, 'rb') as f:
        status = gpg.encrypt_file(f, ['almir@test.com'], output=path + myfile + ".encrypted")

print(status.ok)
print(status.stderr)