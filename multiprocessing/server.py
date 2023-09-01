import socket  # A socket is a software abstraction that represents an endpoint
#  for sending or receiving data across a computer network
# It provides a way to run multiple tasks or functions concurrently,
import multiprocessing
# taking advantage of multiple CPU cores or processors to perform tasks in parallel.


def handle_client(client_socket):  # there is a loop that continuously receives data
    # from the client in chunks of 1024 bytes using client_socket.recv(1024).
    # If no data is received (meaning the client closed the connection), the loop breaks.
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # If data is received, it is immediately sent back to the client
        response = b"Server received: " + data
        client_socket.send(response)
    # is called to close the client's socket when the communication is finished.
    client_socket.close()


def main():
    # It is bound to the local hostname on port 1234 and set to listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        # An infinite loop is started to continuously accept incoming client connections
        client_sock, address = s.accept()
        print(f"Connection from {address} has been established!")
        client_handler = multiprocessing.Process(
            target=handle_client, args=(client_sock,))
        # The client handler process is started with
        client_handler.start()


#  block ensures that the code is only executed if the script is run as the main program.
if __name__ == '__main__':
    main()