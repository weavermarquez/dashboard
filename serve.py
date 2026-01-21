#!/usr/bin/env python3
"""Simple static file server for the dashboard."""

import http.server
import socketserver
import os

PORT = 8088
DIRECTORY = "/var/home/core/www"

os.chdir(DIRECTORY)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY} on http://127.0.0.1:{PORT}")
    httpd.serve_forever()
