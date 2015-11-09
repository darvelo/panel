#!/usr/bin/env python3

import sys
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

if not len(sys.argv) > 1:
    sys.exit(1)

data = ' '.join(sys.argv[1:]).encode('utf8')
s.sendall(data)
s.close()
