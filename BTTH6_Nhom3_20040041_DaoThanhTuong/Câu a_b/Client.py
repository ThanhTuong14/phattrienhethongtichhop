import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("localhost",1112))

done = False

while not done:
    client.send(input("input your list number : ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    print(f"from to server : {msg}")

client.close()
