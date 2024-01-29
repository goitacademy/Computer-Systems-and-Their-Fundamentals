import socket
import threading

# Налаштування сервера
host = "127.0.0.1"  # Локальна адреса
port = 12345  # Порт для прослуховування

# Створення сокета
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Список клієнтів та їхні нікнейми
clients = []
nicknames = []


# Відправка повідомлень усім підключеним клієнтам
def broadcast(message):
    for client in clients:
        client.send(message)


# Обробка повідомлень від клієнтів
def handle(client):
    while True:
        try:
            # Отримання повідомлень від клієнта
            message = client.recv(1024)
            broadcast(message)
        except:
            # Видалення та закриття клієнтів при виникненні помилки
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} вийшов з чату!".encode("utf-8"))
            nicknames.remove(nickname)
            break


# Основна функція для прийняття клієнтів
def receive():
    while True:
        client, address = server.accept()
        print(f"Підключено з {str(address)}")

        # Запит нікнейму
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Нікнейм клієнта: {nickname}")
        broadcast(f"{nickname} приєднався до чату!".encode("utf-8"))
        client.send("Підключено до сервера!".encode("utf-8"))

        # Початок обробки потоку для клієнта
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == "__main__":
    print("Сервер запущено...")
    receive()
