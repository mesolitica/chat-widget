import http.server
import socketserver
import argparse

parser = argparse.ArgumentParser(description='Minimal Python Web Server')
parser.add_argument('--port', type=int, default=8000, help='Port number to serve on (default: 8000)')
parser.add_argument('--hostname', type=str, default='localhost', help='Hostname to serve on (default: localhost)')
args = parser.parse_args()

PORT = args.port
HOSTNAME = args.hostname

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOSTNAME, PORT), Handler) as httpd:
    print(f"Serving at {HOSTNAME}:{PORT}")
    httpd.serve_forever()