import socket

target_host = "127.0.0.1"
Target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AAABBBCCC", (target_host,Target_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()


