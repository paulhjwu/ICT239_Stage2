import http.server
import socketserver
import logging
from io import BytesIO
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib import parse
import math
import json

import os

####

import tempfile
import webbrowser
#import jinja2

###

error_msg = "<html><head></head><body><h1>There is an error</h1></body></html>"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_GET(self):

        pwd=os.getcwd()

        # Concerning Step 3 
        if self.path == '/':
            try:
                with open(pwd + "/2.1_Server/index5.html") as file:
                    data = file.read()

                self._set_response()
                self.wfile.write(bytes(data, "utf8"))

            except:
                self.wfile.write(bytes(error_msg, "utf8"))

            return

        # Concerning Step 1 
        if '/bmi' in self.path:
            
            self._set_response()   

            print(f"The self.path is {self.path}")

            query_components = parse_qs(urlparse(self.path).query)

            if 'height' in query_components:
                height = float(query_components["height"][0])
            
            if 'weight' in query_components:
                weight = float(query_components["weight"][0])
        
            bmi = weight / pow(height, 2)

            html = f"<html><head></head><body><h1>The BMI is {bmi}!</h1></body></html>"
            self.wfile.write(bytes(html, "utf8"))
        return
        
    def do_POST(self):

        bmi = 0
        
        # Concerning Step 3 
        if '/bmi-ajax' in self.path:
            
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
        
            self._set_headers()     
            post_data_str = post_data.decode("utf-8")
            params = parse_qs(post_data_str)

            weight = float(params['weight'][0])
            height = float(params['height'][0])

            if params['unit'][0] == 'm':
                bmi = weight / math.pow(height, 2)
            else:
                bmi = weight / math.pow(height/100, 2)

            self.wfile.write(json.dumps({'bmi': bmi}).encode('utf-8'))

            return

        # Concerning Step 1 
        if '/bmi' in self.path:
            
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself

            logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
        
            self._set_response()     

            self.wfile.write(f'<html><body>POST request for {self.path} and params {post_data}</body></html>'.encode('utf-8'))

        return


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

def main():
    my_server.serve_forever()

# Star the server
if __name__ == "__main__":   
    my_server.serve_forever()