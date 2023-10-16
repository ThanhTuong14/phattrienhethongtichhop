import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 1117))
server.listen()

client, adders = server.accept()
print("server is running ")
done = False
while not done:
    msg = client.recv(1024).decode()
    data = msg.splitlines()
    for line in data:
        if line == '.':
            response = "\nCharacter not found ! "
            client.send(response.encode('utf-8'))
            done = True
        else:
            number = line.split()
            total = sum(int(num) for num in number)
            response = f"\ntổng các số nguyên là  {total}"
            client.send(response.encode('utf-8'))


server.close()
