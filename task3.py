import itertools
import string
import hashlib
from cryptography.hazmat.backends import openssl
from cryptography.hazmat.primitives import hashes
import os
import time
def guess_passwordHash(returnline):
    chars = string.ascii_lowercase
    attempts = 0
    password_length = 0
    for password_length in range(3, 8):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            def encrypt_string(hash_string):
                sha_signature = \
                    hashlib.SHA3_256(hash_string.encode()).hexdigest()
                return sha_signature
            hash_string = guess
            sha_signature = encrypt_string(hash_string)
            if sha_signature == returnline:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print (guess,attempts)




def guess_passwordHashSalt(returnline):
    chars = string.ascii_lowercase
    attempts = 0
    for password_length in range(3, 8):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            def encrypt_string(hash_string):
                sha_signature = \
                    hashlib.SHA3_256(hash_string.encode()).hexdigest()
                return sha_signature
            hash_string = guess + salt
            sha_signature = encrypt_string(hash_string)
            print(sha_signature)
            if sha_signature == returnline:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print (guess,attempts)

print("1.Hash \n")
print("2.Hash with salt\n")
user = input("Please pick an option 1 or 2: \n")
if user == "1":
    start = time.time()
    with open('hashedpsswrd.txt') as f:
        firstline = f.readline()
    returnline = firstline.rpartition(':')[2]
    returnline = returnline.replace('\n','')
    print(returnline)
    print(guess_passwordHash(returnline))
    end = time.time()
    print(end - start)
if user == "2":
    start = time.time()
    with open('salthashedpsswrd.txt') as f:
        firstline = f.readline()
    salt = firstline.rpartition(':')[2]
    salt = salt.replace('\n','')
    print(salt)
    firstline = firstline.rpartition(':')[0]
    returnline = firstline.rpartition(':')[2]
    returnline = returnline.replace('\n','')
    print(returnline)
    print(guess_passwordHashSalt(returnline))
    end = time.time()
    print(end - start)

