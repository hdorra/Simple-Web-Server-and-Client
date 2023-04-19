# Simple Web Server and Client
Implementation of a simple web server and client using HTTP/1.1 protocol. </br>
(Part of MS Computer Science graduate coursework.) </br>

## Description ## 

This repository contains code for a basic socket-based web server and web client. The server listens on a specified port and serves static web pages from the specified directory. The client connects to the server and retrieves static web pages.

## Installation and Usage ## 

1. Clone this repository to your local machine. </br>
2. Navigate to the root directory of the repository. </br>
3. To start the server, run python web_server.py PORT DIRECTORY, where PORT is the port number on which you want to run the server and DIRECTORY is the directory containing the static web pages you want to serve. </br>
4. To start the client, run python web_client.py host:port/path [METHOD], where host:port/path is the URL of the static web page you want to retrieve, and [METHOD] is optional and can be GET or HEAD. The default method is GET. </br>

## Features ## 

### Server ###
*  The server supports GET and HEAD methods.
*  The server returns appropriate HTTP error codes, such as 404 Not Found if the requested file does not exist.
*  The server returns the following HTTP response headers: Date, Server (with the server's name), Content-Length (where appropriate), and Content-Type (for supported file types).
*  The server serves the default file (index.html) when the root of the server is requested.
*  The server can serve large files.

### Client ###

*  The client supports GET and HEAD methods.
*  The client handles HTTP status codes appropriately.
*  The client outputs the HTTP status, headers, and body of the retrieved static web page.
