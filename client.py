import socket

HOST = '127.0.0.1'
PORT = 65432

# Se connecter au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Recevoir la "clé publique" du serveur (fictive)
public_key = client_socket.recv(1024).decode()
print(f"Clé publique reçue : {public_key}")

# Envoi d'un message au serveur (sans chiffrement)
message = "Message simulé"
print(f"Envoi du message : {message}")
client_socket.sendall(message.encode())

client_socket.close()
