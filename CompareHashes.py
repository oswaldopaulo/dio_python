import hashlib

hash1 = hashlib.new('ripemd160')
hash1.update("TESTHASH".encode())

hash2 = hashlib.new('ripemd160')
hash2.update("TESTHASH".encode())


if hash1.digest() != hash2.digest():
    print("Fai Ok")
else:
    print("Test OK")

