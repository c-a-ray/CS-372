"""
File: lab2.py
Author: Cody Ray
Date: 1/20/22
Description:
    For CS 372, Winter 2022, Programming Project 1 - Sockets and HTTP. Program 2.
    Sets up a socket connection to gaia.cs.umass.edu, sends an HTTP request, reads the response, and prints the
    response. The only difference between this file and connect_socket.py is that lab2.py can handle a response of
    arbitrary length.
"""
import socket

TARGET_HOST = 'gaia.cs.umass.edu'
TARGET_PORT = 80
REQUEST = 'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
RECV_BUF_SIZE = 4096


def main():
    client: socket.socket = establish_connection()  # Set up a socket connection
    client.send(REQUEST.encode())                   # Send the request
    print_response(recv_file(client))               # Read the response and print it


def establish_connection() -> socket.socket:
    # Set up socket to use IPv4 addresses and TCP
    client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to target host at the HTTP port
    client.connect((TARGET_HOST, TARGET_PORT))
    return client


def recv_file(client: socket.socket) -> str:
    full_resp: str = ''                                 # To keep track of the entire response so far
    resp: str = client.recv(RECV_BUF_SIZE).decode()     # Read a chunk of the response
    full_resp = str_append(full_resp, resp)             # Record it
    while len(resp) > 0:                                # While there is still data in the pipe
        resp = client.recv(RECV_BUF_SIZE).decode()      # Read another chunk
        full_resp = str_append(full_resp, resp)         # Record it
    return full_resp                                    # When no more data is left, return the full response string


def str_append(s1: str, s2: str) -> str:
    # Append s2 to s1
    return f'{s1}{s2}'


def print_response(resp: str) -> None:
    # Print the original request, the response length, and the response
    print(f'Request: {REQUEST}')
    print(f'[RECV] - length: {len(resp)}')
    print(resp)


if __name__ == '__main__':
    main()
