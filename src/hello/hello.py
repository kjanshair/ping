import urllib.request
import requests
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

WORLD_ADDR = os.environ['WORLD_ADDR']
WORLD_PORT = os.environ['WORLD_PORT']

class handler(BaseHTTPRequestHandler):
   def do_GET(self):
       try:
         r = requests.get("http://" + WORLD_ADDR + ":" + WORLD_PORT.__str__() + "/api", timeout=2)
         result = True
       except:
         result = False

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