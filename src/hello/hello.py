import socket
import urllib.request
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

WORLD_ADDR = os.environ['WORLD_ADDR']
WORLD_PORT = os.environ['WORLD_PORT']

class handler(BaseHTTPRequestHandler):
   def is_connected(self):
     try:
       host = socket.gethostbyname(WORLD_ADDR)
       s = socket.create_connection((host, WORLD_PORT), 1)
       return True
     except:
       pass
     return False
    
   def do_GET(self):
       self.send_response(200)
       self.send_header('Content-type','text/plain')
       self.end_headers()

       result = self.is_connected()

       if result:
           f = urllib.request.urlopen("http://" + WORLD_ADDR + ":" + WORLD_PORT.__str__() + "/api")
           self.wfile.write(b"Hello " + f.read())
       else:
           self.wfile.write(b"Hello 404!")

def main():
   port = 80
   server_address = ('', port)
   httpd = HTTPServer(server_address, handler)
   print('Started at:', port)
   httpd.serve_forever()

if __name__ == '__main__':
  main()