from core.encryption import encrypt, decrypt
from core.key import generate_keys

public_key, private_key = generate_keys()

print("Public key:", public_key)
print("Private key:", private_key)

message = "ce message est encrypte avec une methode revolutionnaire"
print("Encryption")
encrypted = encrypt(message, public_key)
print("Message encrypté:", encrypted)

f = open("encrypted.txt", "w")
f.write("\n".join([str(i) for i in encrypted]))
f.close()

print("Décryptage")
decrypted = decrypt(encrypted, private_key, public_key)
print("Message décrypté:", decrypted)
