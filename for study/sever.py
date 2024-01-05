import socket
host=input("Your ip")
port=65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sever:
    sever.bind((host,port))
    sever.listen()
    conn,addr=sever.accept()
    with conn:
        print(f"Connetced by {addr}")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            print(f"recive:{data}")
            conn.sendall(data)
