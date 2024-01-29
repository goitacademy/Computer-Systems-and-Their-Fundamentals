import socket

TCP_IP = "localhost"
TCP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f"Connection established {server}")
        for line in MESSAGE.split(" "):
            print(f"Send data: {line}")
            sock.send(line.encode())
            response = sock.recv(1024)
            print(f"Response data: {response.decode()}")
    print(f"Data transfer completed")


if __name__ == "__main__":
    run_client(TCP_IP, TCP_PORT)
