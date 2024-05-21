import socket

# Définir l'adresse IP et le port de destination
ip_address = "192.168.150.3"  # Remplacez par l'adresse IP cible
port = 405  # Remplacez par le port cible

# Créer un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Message à envoyer
message = "Hellooooooooo"

# Envoyer le message
udp_socket.sendto(message.encode(), (ip_address, port))

# Fermer le socket
udp_socket.close()

print(f"Message envoyé à {ip_address}:{port} via UDP")
