import socket

serv_sock = socket.socket(socket.AF_INET,       # задамем семейство протоколов 'Интернет' (INET)
                        socket.SOCK_STREAM,     # задаем тип передачи данных 'потоковый' (TCP)
                        proto=0)                # выбираем протокол 'по умолчанию' для TCP, т.е. IP

print(type(serv_sock))                          # <class 'socket.socket'>

class socket():
    """инициализация набора системных вызовов для работы с сокетами"""
    def __init__(self, sock_family, sock_type, proto):
        self._fd = system_socket(sock_family, sock_type, proto)
    def write(self, data):
        # обычно вместо write используется send
        system_write(self._fd, data)
    def fileno(self):
        return self._fd

# доступ к целочисленному файловому дескриптору :   
print(serv_sock.fileno())


# Вызов bind() заставляет нас указать не только IP адрес, но и порт, 
# на котором сервер будет ожидать (слушать) подключения клиентов: 
serv_sock.bind(('127.0.0.1', 53210))  # чтобы привязать сразу ко всем, можно использовать ''

# перевод сокета в состояние ожидания подключения, сообщив об этом операционной системе:

serv_sock.listen(10) 
# 10 - это размер очереди входящих подключений, т.н. backlog
# параметр backlog определяет размер очереди для установленных соединений.

# получаем соединения из этой очереди:

client_sock, client_addr = serv_sock.accept()

# вызов accept() является блокирующим, это означает, что он не возвращает управление нашему коду до тех пор, 
# пока в очереди установленных соединений не появится хотя бы одно подключение.

# Пример чтения и записи данных в клиентский сокет:
while True:
    data = client_sock.recv(1024)
    if not data:
        break
    client_sock.sendall(data)