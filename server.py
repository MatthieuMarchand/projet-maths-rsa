import socket

import core.encryption
import core.key

HOST = input('IP du serveur: ')
PORT = 65432

# "Clé publique" et privée générées par le serveur
public_key, private_key = core.key.generate_keys()
print(f"Public : {public_key}")
print(f"Private : {private_key}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Serveur en attente de connexion sur {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connexion établie avec {addr}")

# Envoyer la "clé publique" (en tant que tuple) au client
conn.sendall(str(public_key).encode())  # Convertir la clé publique en chaîne et l'envoyer

# Recevoir un message du client
message_length = 1024  # Taille du buffer de réception (ajuste si nécessaire)
received_data = b''  # Variable pour accumuler les données reçues

while True:
    data = conn.recv(message_length)
    received_data += data
    if len(data) < message_length:  # Si on reçoit moins que la taille du buffer, cela signifie qu'on a terminé
        break

# Convertir la chaîne reçue en une liste
try:
    encrypted_message = eval(received_data.decode())  # Convertir la chaîne reçue en liste
    decrypted = core.encryption.decrypt(encrypted_message, private_key, public_key)
    print("Message décrypté:", decrypted)
except Exception as e:
    print(f"Erreur lors du traitement du message : {e}")

conn.close()
server_socket.close()
