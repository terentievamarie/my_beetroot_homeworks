import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))

message = input("Please, enter a message to send to the server: ")
while message != 'exit':
    # 'encode()'is used to convert the string into bytes before sending
    client_socket.send(message.encode())
    # The client waits to receive data from the server (up to 1024 bytes)
    data = client_socket.recv(1024)
    # The received data is decoded from bytes to a string
    print(f"Received data from the server: {data.decode()}")
    # requests the user to input a new message for sending
    message = input(
        "Please, enter a message to send to the server(type 'exit' to quit): ")
# After finishing its tasks, the client closes the socket and terminates the program.
client_socket.close()
