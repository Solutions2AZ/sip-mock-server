import socket

# Configuración del servidor SIP
SIP_IP = '0.0.0.0'
SIP_PORT = 5060

def start_sip_server():
    # Crear un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SIP_IP, SIP_PORT))

    print(f"Servidor SIP escuchando en {SIP_IP}:{SIP_PORT}")

    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Recibido de {addr}: {data.decode('utf-8')}")

        # Responder con un "OK" a cualquier solicitud
        response = "SIP/2.0 200 OK\r\n\r\n"
        sock.sendto(response.encode('utf-8'), addr)
        print(f"Respuesta enviada a {addr}: {response}")

if __name__ == "__main__":
    start_sip_server()
