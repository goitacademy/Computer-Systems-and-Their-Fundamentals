import socket
import threading
import signal

# Вибір нікнейму
nickname = None

# Підключення до сервера
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

# Змінна для контролю потоку
running = True


def handle_signal(signum, frame):
    global running
    running = False
    client.close()
    print("\nЗавершення програми...")


# Прослуховування сервера та відправка нікнейму
def receive():
    global running
    while running:
        try:
            # Отримання повідомлення від сервера
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except socket.error:
            # Закриття з'єднання при виникненні помилки
            print("Помилка з'єднання з сервером, не вдалося отримати повідомлення!")
            running = False
            break


# Відправка повідомлень серверу
def write():
    global running
    while running:
        try:
            message = input(">>> ")
            if message.lower() == "exit":
                client.send(f"{nickname} вийшов із чату.".encode("utf-8"))
                running = False
                break
            message = f"{nickname}: {message}"
            client.send(message.encode("utf-8"))
        except (EOFError, KeyboardInterrupt):
            try:
                client.send(f"{nickname} вийшов із чату.".encode("utf-8"))
            except socket.error:
                pass
            client.close()
            running = False
            break
        except socket.error:
            print(f"Помилка з'єднання із сервером!")
            running = False
            break


if __name__ == "__main__":
    nickname = input("Виберіть нікнейм: ")
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    # Запуск потоків для прослуховування та письма
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

    receive_thread.join()
    write_thread.join()
    client.close()
