# SHA256: Comparing the energy consumption of different implementations

This project aims to compare the energy consumption of the SHA256 algorithm. For that, the SHA256 hashing algorithm has been implemented in the Visual Studio IDE in Python using four libraries named Hashlib, CryptoHash, Cryptography, and PyNacl and the power consumption has been calculated using the Intel Power Gadget software. 

## Result
Mean power consumption of the four SHA256 Libraries
![Mean power consumption of the four SHA256 Libraries](/Images/Mean_execution_time_vs_power.png)

Mean Execution time vs Processor Power mean
![Mean Execution time vs Processor Power mean](/Images/Mean_power_SHA256.png)

So, it can be concluded that PyNacl Library is the most energy-efficient library when implementing the SHA256 algorithm.
