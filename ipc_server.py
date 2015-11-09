#!/usr/bin/env python3

import time
import socket
import signal
from threading import Thread

BUFFER_LEN = 100

class Worker(Thread):
    def __init__(self, server, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.server = server
        self.conn = None
        self.closed = False

    def run(self):
        while not self.closed:
            conn, addr = self.server.socket.accept()
            self.conn = conn
            self.closed = False
            data = conn.recv(BUFFER_LEN)
            if data:
                data = data.decode('utf8').strip()
                self.server.broadcast(data)
            if not self.closed:
                conn.close()

    def stop(self):
        if self.conn:
            self.closed = True
            self.conn.shutdown(socket.SHUT_RDWR)
            self.conn.close()

class IPCServer():
    thread_count = 4

    def __init__(self, host='', port=50007, thread_count=thread_count):
        self.host = host
        self.port = port
        self.thread_count = thread_count
        self.workers = []
        self.registry = {}

    def subscribe(self, key, fn):
        try:
            listeners = self.registry[key]
        except KeyError:
            listeners = self.registry[key] = []

        listeners.append(fn)

    def broadcast(self, key):
        if not key in self.registry:
            return

        for fn in self.registry[key]:
            fn()

    def start_workers(self):
        for i in range(self.thread_count):
            w = Worker(server=self, daemon=True)
            w.start()
            self.workers.append(w)

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(4)
        self.start_workers()

    def stop(self):
        for w in self.workers:
            w.stop()
