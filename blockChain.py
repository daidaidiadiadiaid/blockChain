import hashlib
hash_hello=hashlib.sha256(b"hello").hexdigest()
print(hash_hello)
