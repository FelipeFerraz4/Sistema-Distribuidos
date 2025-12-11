import socket
import threading
from datetime import datetime

host = '10.0.211.87'
port = 65432

def handle_client(client_socket, addr):
    print(f'Conectado por {addr}')

    try:
        while True:
            data = client_socket.recv(1024)

            # Cliente fechou a conexão ou mandou mensagem vazia
            if not data:
                print(f"Cliente {addr} desconectado.\n")
                break   # ← encerra o loop corretamente

            decoded = data.decode().strip()

            # Mensagem vazia enviada explicitamente
            if decoded == "":
                print(f"Cliente {addr} enviou mensagem vazia. Encerrando.\n")
                break

            datetime_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            resposta = f"{datetime_now} - {decoded}"

            print(f"Recebido de {addr}: {decoded}")
            client_socket.send(resposta.encode())

    except Exception as e:
        print(f"Erro com {addr}: {e}")

    finally:
        client_socket.close()
        print(f"Conexão com {addr} encerrada.\n")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f"Servidor escutando em {host}:{port}\n")

try:
    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
        thread.start()

except KeyboardInterrupt:
    print("\nServidor encerrado manualmente.")

finally:
    server_socket.close()
    print("Socket fechado.")
