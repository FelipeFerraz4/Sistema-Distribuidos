import socket
from datetime import datetime

# host = '10.0.211.87'
host = '127.0.0.1'
port = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f'Servidor escutando no {host}:{port}\n')

try:
    while True:
        client_socket, addr = server_socket.accept()
        
        with client_socket:
            print(f'Conectado por {addr}')
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f'Recebido do cliente: {data.decode()}')
                
                datetime_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                new_data = datetime_now + ' - ' + data.decode()[::-1]
                client_socket.send(new_data.encode())
                print(f'Enviado para o cliente: {new_data.decode()}')

        print(f'Desconectado de {addr}\n')

except KeyboardInterrupt:
    print("\nServidor encerrado manualmente.")

finally:
    server_socket.close()
    print("Socket fechado.")
