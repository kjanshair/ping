import urllib.request
import socket
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header('Content-type','text/plain')
       self.end_headers()

       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       result = sock.connect_ex(('world', 8080))

       if result == 0:
           print("Entered. !")
           f = urllib.request.urlopen("http://world:8080/api")
           self.wfile.write(b"Hello " + f.read())
       else:
           print("Exited. !")
           self.wfile.write(b"Hello 404!")   
def main():
   port = 80
   server_address = ('', port)
   httpd = HTTPServer(server_address, handler)
   print('Started at:', port)
   httpd.serve_forever()

if __name__ == '__main__':
  main()