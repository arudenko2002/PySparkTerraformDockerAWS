import socket
import time
#run this one, then streaming.py
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9999  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        for ind in range(100000):
            data = b'ddddddddddd eeeeeeeee fffffffff ggggggggg hhhhhhhh\n'
            print(ind, data)
            conn.sendall(data)
            if ind>0 and ind % 10000 == 0:
                time.sleep(30)
                #n = input()
        print("close connection")
        conn.close()
