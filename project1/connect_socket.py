"""
File: connect_socket.py
Author: Cody Ray
Date: 1/20/22
Description:
    For CS 372, Winter 2022, Programming Project 1 - Sockets and HTTP. Program 1.
    Sets up a socket connection to gaia.cs.umass.edu, sends an HTTP request, reads the response, and prints the
    response.
"""
import socket

TARGET_HOST = 'gaia.cs.umass.edu'
TARGET_PORT = 80  # HTTP port
REQUEST = 'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
RECV_BUF_SIZE = 4096  # Number of bytes to read from socket


def main():
    client: socket.socket = establish_connection()          # Set up socket connection
    client.send(REQUEST.encode())                           # Send the request
    print_response(client.recv(RECV_BUF_SIZE).decode())     # Read the response and print it


def establish_connection() -> socket.socket:
    # Set up socket to use IPv4 addresses and TCP
    client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to target host at the HTTP port
    client.connect((TARGET_HOST, TARGET_PORT))
    return client


def print_response(resp: str) -> None:
    # Print the original request, the response length, and the response
    print(f'Request: {REQUEST}')
    print(f'[RECV] - length: {len(resp)}')
    print(resp)


if __name__ == '__main__':
    main()
