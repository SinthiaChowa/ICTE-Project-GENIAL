import nacl.hash
import time
ts = time.time()
print(ts)


# Hash a message with SHA-256
message = b'Code Optimization is a program modification technique which aims to improve the quality and efficiency of the code written by a programmer (Agarwal et al, 2016). Code can be optimized for a number of reasons. This including: reducing the overall size of the program, reducing memory consumption, reducing CPU usage, improving execution time or improving energy efficiency (PVS-Studio, n.d). Whilst applying code optimization to a program it must be taken in to consideration that the end result of the program remains unchanged'
digest = nacl.hash.sha256(message)

i = 0
while i < 10000000:
    # Convert the digest to a hexadecimal string
    hex_digest = digest.hex()
    i += 1

print(hex_digest)
ts = time.time()
print(ts)
