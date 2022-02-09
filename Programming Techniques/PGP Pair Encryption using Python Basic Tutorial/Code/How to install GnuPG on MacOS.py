# How to install GnuPG on MacOS
# brew install GnuPG
# brew install gpa

# How to install Python3 modules for GnuPG:
# pip3 install python-gnupg
# export GPG_TTY=$(tty)

# How to generate PGP Public Private key pair on MacOS and Linux:
# gpg --full-generate-key
# gpg --list-keys

# How to export the public and private keys on MacOS
# In command line type: gpa -k    This will open graphical tools that allow you to export thew public key and backup private key

# How to export ASCII armored PGP public and private keys: 
# gpg --export almir@test.com  > mypublic.asc
# gpg --export-secret-key almit@test.com > myprivate.asc

# If you want to generate the PGP key into the key store using Python 3.9.3+, 
# you would first need to pip install GnuPG module for Python 3:

# pip3 install python-gnupg

