import time
ts = time.time()
print(ts)
import hashlib

hash_object = hashlib.sha256()

i = 0

while i < 10000000:

    hash_object.update(b'Code Optimization is a program modification technique which aims to improve the quality and efficiency of the code written by a programmer (Agarwal et al, 2016). Code can be optimized for a number of reasons. This including: reducing the overall size of the program, reducing memory consumption, reducing CPU usage, improving execution time or improving energy efficiency (PVS-Studio, n.d). Whilst applying code optimization to a program it must be taken in to consideration that the end result of the program remains unchanged')
    hex_digest = hash_object.hexdigest()

    i += 1

print("output", hex_digest)
ts = time.time()
print(ts)
