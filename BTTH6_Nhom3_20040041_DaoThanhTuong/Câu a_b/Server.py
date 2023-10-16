import socket
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("localhost",1112))
server.listen()

client , adders = server.accept()
print("server is running ")
done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == '.':
        response ="Character not found ! "
        client.send(response.encode('utf-8'))
        done = True
    else:
        data = msg.split()
        total = sum(int(num) for num in data)
        response = f"tổng các số nguyên là  {total}"
        client.send(response.encode('utf-8'))

client.close()
server.close()



