import socket

host = '127.0.0.1'
port = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))
    
    message = input("Digite a mensagem para o servidor: ")
    client_socket.sendall(message.encode('utf-8'))
    print(f'Enviado para o servidor: {message}')

    client_socket.shutdown(socket.SHUT_WR)

    data = client_socket.recv(1024)
    print(f'Recebido do servidor: {data.decode("utf-8")}')

except Exception as e:
    print(f'Ocorreu um erro: {e}')    

finally:
    client_socket.close()
    print('Conexão encerrada.')
