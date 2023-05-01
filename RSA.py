
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


#  Taking input


fs, data = wavfile.read('utkarsh_audio.wav')
plt.plot(data)            # fs = sampling frequency = 44.1kHz
plt.title("Original Audio Plot")
data_1 = np.asarray(data, dtype = np.int32)


# ## Playing that sound

sd.play(data, fs)


# ## Generating public and private keys for RSA algorithm

# Select two prime no's. Suppose P = 53 and Q = 59.
# 
# Now First part of the Public key  : n = P*Q = 3127.
# 
# We also need a small exponent say e : 
# But e Must be 
# 
#     1) An integer.
# 
#     2) Not be a factor of n.
#  
#     3) 1 < e < Φ(n) [Φ(n) is discussed below], 
#     Let us now consider it to be equal to 3.
#     
# Our Public Key is made of n and e

# 1) We need to calculate Φ(n):
#     
#     Such that Φ(n) = (P-1)(Q-1)     
#       so,  Φ(n) = 3016
# 
#     
# 2) Now calculate Private Key, d : 
#     
#     d = (k*Φ(n) + 1) / e for some integer k
#     For k = 2, value of d is 2011.



p1 = int(input("Enter a prime number: "))
p2 = int(input("Enter another prime number: "))

n = p1*p2
print("n = p1*p2 = ",n)



e = int(input("Enter a small, odd number, co-prime with n: "))
k = int(input("Enter value of k:"))


phi = (p1-1)*(p2-1)
print("phi = ",phi)
d = int((k*phi+1)/e)
print("d= ",d)


public_key = n,e
private_key = n,d

print("Public Key = ", public_key)
print("Private Key = ",private_key)


# Encrpytion of audio file

encrypted = (data**e)%n
plt.plot(encrypted)
plt.title("Encrypted Audio Plot")


# Saving the saved file


encrypted = np.asarray(encrypted, dtype=np.int16)
wavfile.write('encrypted_rsa.wav', fs, encrypted)
print("A file titled 'encrypted_rsa.wav' is generated which is the encrypted audio to be communicated")


# Loading and decrypting

fs, Data = wavfile.read('encrypted_rsa.wav')
plt.plot(Data)
plt.title("Encrypted Audio Plot")


# Decryption of data

decrypted = (Data**d)%n
plt.plot(decrypted)
plt.title('Decrypted Audio Plot')


sd.play(encrypted, fs)





