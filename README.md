# Simple-Web-Server-and-Client
Implementation of a simple web server and client using HTTP/1.1 protocol. 

## Description ## 

1. Two programs are provided - a web server and a web client.</br>
2. Considerations:</br>
    a. Cookies or other forms of state are not supported in these simple implementations.</br>
    b. HTTP/1.1 protocol (not HTTP/1.0) is implemented.</br>
    c. A Host header field is required.</br>
3. Overview:</br>
    a. client.py:</br>
       - Implements a basic socket-based web client by connecting and sending HTTP protocol
messages to a web server (no detailed GUI or user interface is included here).</br>
       - The basic call for the program: </br>
        ` python web_client.py host:port/path [METHOD]`

    b. server.py:</br>
       - Implements a basic socket-based web server by listening on a specified port.</br>
       - The basic call for the web server will be: </br>
        ` python web_server.py PORT DIRECTORY`

