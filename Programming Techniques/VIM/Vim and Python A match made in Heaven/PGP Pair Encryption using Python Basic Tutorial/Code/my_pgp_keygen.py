# my_pgp_keygen.py

# How to install GnuPG on MacOS:
# brew install GnuPG
# brew install gpa

# How to install Python3 modules for GnuPG:
# pip3 install python-gnupg
# export GPG_TTY=$(tty)

from getopt import gnu_getopt


import gnupg
import os

gpg = gnupg.GPG('/usr/local/bin/gpg')
gpg.encoding = 'utf=8'

key_input_data = gpg.gen_key_input(
        name_email = 'almir@test.com',
        passphrase = 'almirtest1',
        key_type = 'RSA',
        key_length = 4096)

key = gpg.gen_key(key_input_data)

print(key)
