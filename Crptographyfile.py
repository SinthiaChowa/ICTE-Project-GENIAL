from cryptography.hazmat.primitives import hashes
import time
ts = time.time()
print(ts)


# create a SHA-256 hash object
hash_object = hashes.Hash(hashes.SHA256())
i = 0

while i < 10000000:
    # update the hash object with the message to be hashed
    message = b'This is the message to be hashed'
    hash_object.update(message)
    i += 1

# get the resulting hash value in bytes
hash_value = hash_object.finalize()

# alternatively, get the hash value in hexadecimal format
hex_value = hash_value.hex()

#print(f"SHA-256 hash value in bytes: {hash_value}")
print(hex_value)
ts = time.time()
print(ts)
