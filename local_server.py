import http.server
import socketserver
import os

PORT = 8000
BASE_PATH = "/DNlite-Report-Generator-for-GluCare"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle the rewritten path for resources
        if self.path.startswith(BASE_PATH):
            original_path = self.path
            # Strip the base path
            self.path = self.path[len(BASE_PATH):]
            if not self.path.startswith('/'):
                self.path = '/' + self.path
            print(f"Rewriting {original_path} to {self.path}")
            
        return super().do_GET()

print(f"Starting server at http://localhost:{PORT}")
print(f"Simulating base path: {BASE_PATH}")

# Ensure we can reuse the address to avoid 'Address already in use' errors on restart
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
