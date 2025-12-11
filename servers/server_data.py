import socket
import threading
from datetime import datetime

host = '127.0.0.1'
port = 65432

def handle_client(client_socket, addr):
    print(f'Conectado por {addr}')

    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f'Recebido do cliente {addr}: {data.decode()}')

        datetime_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        client_socket.send(datetime_now.encode())
        print(f'Enviado para {addr}: {datetime_now}')

    print(f'Desconectado de {addr}\n')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f'Servidor escutando no {host}:{port}\n')

try:
    while True:
        client_socket, addr = server_socket.accept()

        thread = threading.Thread(target=handle_client, args=(client_socket, addr))

        thread.daemon = True
        thread.start()

except KeyboardInterrupt:
    print("\nServidor encerrado manualmente.")

finally:
    server_socket.close()
    print("Socket fechado.")
