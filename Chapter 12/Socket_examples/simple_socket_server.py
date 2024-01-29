import socket
import threading
from time import sleep


def echo_server(host, port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                print(f"From client: {data}")
                if not data:
                    break
                conn.send(data.upper())


def simple_client(host, port):
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, port))
                s.sendall(b"Hello, world")
                data = s.recv(1024)
                print(f"From server: {data}")
                break
            except ConnectionRefusedError:
                sleep(0.5)


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 55555

    server = threading.Thread(target=echo_server, args=(HOST, PORT))
    client = threading.Thread(target=simple_client, args=(HOST, PORT))

    server.start()
    client.start()
    server.join()
    client.join()
    print("Done!")
