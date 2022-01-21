"""
File: http_server.py
Author: Cody Ray
Date: 1/20/22
Description:
    For CS 372, Winter 2022, Programming Project 1 - Sockets and HTTP. Program 3.
    Creates a socket server on LOCALHOST and listens for connections. When a new connection is made, the request is
    printed and a response message is sent back to the client. The connection is then closed.
"""
import socket

HOST = '127.0.0.1'
PORT = 8082
RECV_BUF_SIZE = 4096
DATA = "HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"


def main():
    handle_connections(setup_socket())


def setup_socket() -> socket.socket:
    # Set up socket to use IPv4 addresses and TCP
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to localhost:8082
    sock.bind((HOST, PORT))

    # Listen on the socket for new connections
    sock.listen()
    print(f'Listening for connections on {HOST}:{PORT}')
    return sock


def handle_connections(sock: socket.socket) -> None:
    while True:                                                         # Continuously handle connections
        conn, _ = sock.accept()                                         # Accept a new connection
        print(f'\nReceived:  {conn.recv(RECV_BUF_SIZE).decode()}')      # Read the request and print it
        print(f'Sending>>>>>>>>>>>\n{DATA}>>>>>>>>>>>')                 # Print the response
        conn.send(DATA.encode())                                        # Send the response to the client


if __name__ == '__main__':
    print('Starting HTTP server...')
    main()
