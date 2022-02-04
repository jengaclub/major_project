import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2566

ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(89)
while True:
            c, addr = ServerSideSocket.accept() #while the connection is true accept the client
            print('Got connection from ', addr)
            c.send(bytes("From Server", "utf-8"))
            c.send(bytes("\Hey there: ", "utf-8"))
            print(c.recv(8000)) #receive the information from the client
            c.close()# clo

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(8000)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    #print('Thread Number: ' + str(ThreadCount))

ServerSideSocket.close()





**************************Database***********************************
import sqlite3

conn = sqlite3.connect('specifics.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS CompSpecs (
             MAC_ADD PRIMARY KEY,
             memory_left text,
             RAM text
             )""")

c.execute("INSERT INTO CompSpecs(MAC_ADD,memory_left,RAM) VALUES ('04-43-F1-40-87-CC','100GB','8GB')"
          "ON CONFLICT(MAC_ADD) DO UPDATE SET memory_left = excluded.memory_left, RAM = excluded.RAM")



c.execute("INSERT INTO CompSpecs(MAC_ADD,memory_left,RAM)  VALUES ('C0-33-92-F9-D6-85','100GB','2GB')"
          "ON CONFLICT(MAC_ADD) DO UPDATE SET memory_left = excluded.memory_left, RAM = excluded.RAM")



c.execute("INSERT INTO CompSpecs(MAC_ADD,memory_left,RAM)  VALUES ('80-EE-67-10-5F-E5','150GB','8GB')"
           "ON CONFLICT(MAC_ADD) DO UPDATE SET memory_left = excluded.memory_left, RAM = excluded.RAM")



c.execute("INSERT INTO CompSpecs(MAC_ADD,memory_left,RAM)  VALUES ('0B-6D-5E-0E-63-FD','120GB','4GB')"
           "ON CONFLICT(MAC_ADD) DO UPDATE SET memory_left = excluded.memory_left, RAM = excluded.RAM")

conn.commit()

c.execute("SELECT * FROM CompSpecs WHERE MAC_ADD = '0B-6D-5E-0E-63-FD'")
print(c.fetchone())
print('the query has executed')

sql = 'SELECT * FROM CompSpecs'
c.execute(sql)
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()

***************************************************************************************************


import socket
import psutil

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2566

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
c='This is client 1 and the CPU frequency is' + ""
ClientMultiSocket.sendall(c.encode())
b = str(psutil.cpu_freq())#store the memory info of this pc
ClientMultiSocket.sendall(b.encode()) #send to server
complete_info= ' '
while True:
    msg = ClientMultiSocket.recv(1024) #we send entire message to server sometimes some part is trunkated so put it in loop
    if len(msg)<=0:
        break
    complete_info+=msg.decode("utf-8")
print(complete_info)
while True:
    Input = input('Hey there: ')
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))


ClientMultiSocket.close()



import psutil
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2566

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
c='This is client 2 and virtual memory is' + "  "
ClientMultiSocket.sendall(c.encode())
b = str(psutil.virtual_memory().percent) #store the memory info of this pc
ClientMultiSocket.sendall(b.encode()) #send to server
complete_info= ' '
while True:
    msg = ClientMultiSocket.recv(1024) #we send entire message to server sometimes some part is trunkated so put it in loop
    if len(msg)<=0:
        break
    complete_info+=msg.decode("utf-8")
print(complete_info)
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))

ClientMultiSocket.close()

*********************************Front end***********************************************

import streamlit as st
import sqlite3
import pandas as pd


def sqlExecutor():
    cnx = sqlite3.connect('specifics.db')
    df = pd.read_sql_query("SELECT * FROM CompSpecs", cnx)
    return df


def main():
    st.title("Computer statistics")
    query_results = sqlExecutor()
    st.table(query_results)


if __name__ == '__main__':
    main()



