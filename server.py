import socket
import threading
from pickle import dumps,loads
def from_client():
    global con,connect
    while(connect):
        data=con.recv(1024)
        print("Received from client",loads(data))
        data=input()
        x.sendall(dumps(data))
x=socket.socket()
port,host=49673,'127.0.0.1'
x.bind((host,port))
x.listen(5)
con,address=x.accept()
connect=True
t=threading.Thread(target=from_client)
t.start()
print("Receiving started....")