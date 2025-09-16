#pip install pyencryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Generate key and data
key = get_random_bytes(16)  # AES-128
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt
data = b"Sensitive customer data"
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

# Display
print("Encrypted:", base64.b64encode(ciphertext))

# Decrypt
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
original_data = cipher_dec.decrypt(ciphertext)
print("Decrypted:", original_data.decode())

#  Iterative Spark
#