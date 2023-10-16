import socket
from typing import List

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 1117))

done = False
file_path = "data.txt"
my_array = []
while not done:
    for i in range(0, 4):
        msg = (input("input your line : "))
        my_array.append(msg)
        print(f"{i} line is : {msg}")
        if i == 4:
            break
    break

for item in my_array:
    print(item)

with open(file_path, 'w') as file:
    for item in my_array:
        file.write(str(item) + '\n')

with open(file_path, 'r') as file:
    content = file.read()

while not done:
    client.send(content.encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    print(f"from server : {msg}")

client.close()
