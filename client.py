import socket
import urllib.parse
from urllib.parse import urlparse
import re
import os
import sys


socket.setdefaulttimeout = 0.50
os.environ['no_proxy'] = '127.0.0.1,localhost'
linkRegex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
CRLF = "\r\n\r\n"

def GET(url):
    print("Get method")
    url = urlparse(url)
    path = url.path
    print(path)
    print(url.netloc)
    if path == "":
        path = "/"
    HOST = url.netloc  # The remote host
    REAL_HOST = HOST.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0] #ADDED THIS
    PORT = 80         # The same port as used by the server
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.30)
   
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # set up TCP connection
    s.connect((REAL_HOST, PORT))

    # send HTTP get request
    message = "GET " + path + " HTTP/1.1\r\nHost: " + REAL_HOST + "\r\nConnection: close\r\n\r\n"
    print("msg request:\n", message)
    s.send(message.encode('utf-8'))
    print(str(s.recv(1024), 'utf-8'))
    
    dataAppend = ''

    # wait for response from server
    data = (s.recv(10000000))
    if not data: print('error, no response')
    else:
        dataAppend = dataAppend, repr(data)

    # shutdown and close tcp connection and socket
    s.shutdown(1)
    s.close()
    print('Received', dataAppend)

def HEAD(url):
    print('Head method')
    url = urlparse(url)  
    path = url.path
    print("path", path)
    print("url", url)
    if path == "":
        path = "/"
    HOST = url.netloc  # The remote host
    REAL_HOST = HOST.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0] #ADDED THIS
    PORT = 80        # The same port as used by the server
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.30)
   
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # set up TCP connection
    s.connect((REAL_HOST, PORT))

    # send HTTP get request
    message = "HEAD " + path + " HTTP/1.1\r\nHost: " + REAL_HOST + "\r\nConnection: close\r\n\r\n"
    print("msg request:\n", message)
    s.send(message.encode('utf-8'))
    print(str(s.recv(1024), 'utf-8'))

if sys.argv[2] == "GET":
    GET(sys.argv[1])  
elif sys.argv[2] == "HEAD":
    HEAD(sys.argv[1])  

