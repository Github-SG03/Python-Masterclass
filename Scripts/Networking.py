############################################################
# NETWORKING IN PYTHON (BASIC → ADVANCED)
# Learn sockets, client-server, HTTP, APIs step by step
############################################################

############################################################
# 1. WHAT IS NETWORKING?
# Networking = communication between computers
# Example: Browser → Server → Response
############################################################


############################################################
# 2. SOCKET BASICS
# socket = endpoint for communication
############################################################

import socket

# Create a socket object
# AF_INET = IPv4
# SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n--- Socket Created ---")


############################################################
# 3. GET LOCAL HOST NAME & IP
############################################################

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("\nHostname:", hostname)
print("IP Address:", ip_address)


############################################################
# 4. SIMPLE CLIENT (CONNECT TO SERVER)
############################################################

# NOTE: This connects to Google server (example)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("google.com", 80))  # port 80 = HTTP
    print("\nConnected to Google server")
    client.close()
except Exception as e:
    print("Connection error:", e)


############################################################
# 5. SIMPLE SERVER
############################################################

# WARNING: Run this separately (it blocks execution)

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))  # local host + port
    server.listen(1)

    print("\nServer listening on port 9999...")

    conn, addr = server.accept()
    print("Connected by:", addr)

    conn.send(b"Hello Client!")  # send bytes
    conn.close()


# Uncomment to run server
# run_server()


############################################################
# 6. SIMPLE CLIENT FOR ABOVE SERVER
############################################################

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    data = client.recv(1024)
    print("\nReceived from server:", data.decode())

    client.close()


# Uncomment to test
# run_client()


############################################################
# 7. HTTP REQUEST USING requests LIBRARY
############################################################

# Install first: pip install requests

import requests

try:
    response = requests.get("https://api.github.com")

    print("\n--- HTTP Response ---")
    print("Status Code:", response.status_code)
    print("Data:", response.json())
except Exception as e:
    print("Request error:", e)


############################################################
# 8. DOWNLOADING DATA FROM INTERNET
############################################################

url = "https://jsonplaceholder.typicode.com/posts"

try:
    res = requests.get(url)
    data = res.json()

    print("\n--- Sample API Data ---")
    print(data[:2])  # first 2 records
except:
    print("API failed")


############################################################
# 9. SOCKET TIMEOUT
############################################################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)  # 5 seconds timeout

try:
    sock.connect(("google.com", 80))
    print("\nConnected with timeout")
except socket.timeout:
    print("Connection timed out")


############################################################
# 10. MULTI-CLIENT SERVER (BASIC)
############################################################

import threading

def handle_client(conn):
    msg = conn.recv(1024)
    print("Client says:", msg.decode())
    conn.send(b"Message received")
    conn.close()


def multi_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8888))
    server.listen(5)

    print("\nMulti-client server running...")

    while True:
        conn, addr = server.accept()
        print("Connected:", addr)

        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()


# Uncomment to run multi-client server
# multi_server()


############################################################
# 11. PORT SCANNER (BASIC)
############################################################

def port_scan(host):
    print("\nScanning ports...")

    for port in range(75, 85):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()


# Example:
# port_scan("127.0.0.1")


############################################################
# 12. IMPORTANT CONCEPTS
############################################################

# TCP = reliable connection (used in web)
# UDP = fast but no guarantee

# IP Address = unique identifier
# Port = application endpoint

# Example:
# 127.0.0.1:8080
# IP       Port


############################################################
# END NOTE
############################################################

# Networking is used in:
# - Web applications
# - APIs
# - Data Engineering pipelines
# - Distributed systems

print("\n🎉 Networking Learning Completed!")