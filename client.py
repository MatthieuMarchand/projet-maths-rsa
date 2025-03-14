import socket

import core.encryption

HOST = input('IP du serveur: ')
PORT = 65432

# Se connecter au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Recevoir la "clé publique" du serveur (fictive)
public_key_data = client_socket.recv(1024)
public_key = eval(public_key_data.decode())  # Convertir la chaîne reçue en tuple (N, c)
print(f"Clé publique reçue : {public_key}")

# Demander à l'utilisateur de rentrer un message
message = input("Entrez le message à envoyer au serveur : ")
print("Encryption")

# Encrypter le message avec la clé publique
encrypted = core.encryption.encrypt(message, public_key)
print("Message encrypté:", encrypted)

# Convertir le message en chaîne et l'envoyer au serveur
client_socket.sendall(str(encrypted).encode())

client_socket.close()
