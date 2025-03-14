import socket

HOST = '127.0.0.1'
PORT = 65432

# "Clé publique" fictive pour la simulation
fake_public_key = "test"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Serveur en attente de connexion sur {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connexion établie avec {addr}")

# Envoyer la "clé publique" fictive au client
conn.sendall(fake_public_key.encode())

# Recevoir un message du client
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Message reçu : {data.decode()}")

conn.close()
server_socket.close()
