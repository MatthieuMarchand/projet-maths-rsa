from core.encryption import encrypt, decrypt
from core.key import generate_keys

public_key, private_key = generate_keys()

message = "bonjour. attention la derniere version du samsung pro est desormais en vente libre sans le protocole new generation. il se peut qu'une version plus moderne soit mise sur le marche mais pour l'instant nous le laissons tel quel pour voir si les consommateurs l'achetent et si oui a quelle quantite. nous lancerons un plan de restructuration du reseau courant janvier ce qui nous permettra de tester ce nouveau produit de facon plus precise. a noter aussi que le nokia a perdu enormement de points sur le marche japonnais. il faudrait peut etre parler aussi de ce point lors de la prochaine reunion. bien a vous."
print("Encryption")
encrypted = encrypt(message, public_key)
print("Message encrypté:", encrypted)
print("Décryptage")
decrypted = decrypt(encrypted, private_key, public_key[0])
print("Message décrypté:", decrypted)
