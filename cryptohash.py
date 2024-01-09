
from Crypto.Hash import SHA256
import time
ts = time.time()
print(ts)

hashObject = SHA256.new()
hashObject.update(b'Code Optimization is a program modification technique which aims to improve the quality and efficiency of the code written by a programmer (Agarwal et al, 2016). Code can be optimized for a number of reasons. This including: reducing the overall size of the program, reducing memory consumption, reducing CPU usage, improving execution time or improving energy efficiency (PVS-Studio, n.d). Whilst applying code optimization to a program it must be taken in to consideration that the end result of the program remains unchanged')

#expectedDigest = "648246ee43bdfc84da50120d50ee57fd88206cebc65db477fbe683d4aacfa1e7"

#ts = time.time()

i = 0
while i < 10000000:
    hash_ob = hashObject.hexdigest()
    i += 1


print(hash_ob)
ts = time.time()
print(ts)
#print(hashObject.hexdigest() == expectedDigest)
