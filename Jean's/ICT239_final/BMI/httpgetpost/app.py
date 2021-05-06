#This module defines classes for implementing HTTP servers (Web servers).
import http.server

#The SocketServer module is a framework for creating network servers.
# It defines classes for handling synchronous network requests (the server request handler blocks until the request is completed) over TCP
import socketserver

#Python has a built-in module logging which allows writing status messages to a file or any other output streams.
import logging

#Using buffer modules(StringIO, BytesIO, cStringIO) we can impersonate string or 
# bytes data like a file.These buffer modules help us to mimic our data like a normal file 
# which we can further use for processing.
from io import BytesIO

#The URL parsing functions focus on splitting a URL string into its components, or on combining URL components into a URL string.
from urllib.parse import urlparse

#parse_qs() and parse_qsl() are provided in this module to parse query strings into Python data structures
from urllib.parse import parse_qs

#The parser module The primary purpose for this interface is to allow Python code to edit the parse tree of a Python expression and create executable code from this
from urllib import parse

# To use mathematical functions under this module
import math

#the process of encoding data into JSON format (like converting a Python list to JSON)
import json

#The OS module in Python provides functions for interacting with the operating system. 
# OS comes under Python's standard utility modules. 
import os

####
#To create one temporary file in Python, you need to import the tempfile module.
import tempfile

#Python has a module called webbrowser, which allows to open the web browser from a python script By simply calling the open() function of the module. T
import webbrowser
#import jinja2

###
error_msg = "<html><head></head><body><h1>There is an error</h1></body></html>"


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    #https://developer.mozilla.org/en-US/docs/Web/HTTP/Session
    #https://docs.python.org/3/library/http.server.html


    #Adds a response header to the headers buffer and logs the accepted request.
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    #The request is mapped to a local file by interpreting the request as a path relative to the current working directory.
    def do_GET(self):

        #Python method getcwd() returns current working directory of a process.
        pwd=os.getcwd()

        # Concerning Step 3 
        if self.path == '/':
            try:
                
                with open(pwd + "/httpgetpost/BMI.html") as file:
                    data = file.read()

                self._set_response()
                self.wfile.write(bytes(data, "utf8"))

            except:
                self.wfile.write(bytes(error_msg, "utf8"))

            return

    #This method serves the 'POST' request type
    def do_POST(self):
        bmi = 0

        # Concerning Step 3 
        #BMI.html ajax url after click on calculate button
        if '/bmi-ajax' in self.path:  
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
        
            self._set_headers()     
            post_data_str = post_data.decode("utf-8")

            #Parse a query string given as a string argument
            #Data are returned as a dictionary. The dictionary keys are the unique query variable names and the values are lists of values for each name.
            params = parse_qs(post_data_str)

            #input codes here for BMI calculation and pass back to front-end
            weight = float(params['weight'][0])
            height = float(params['height'][0])

            if params['unit'][0] == 'm':
                bmi = weight / math.pow(height, 2)
            else:
                bmi = weight / math.pow(height/100, 2)

            self.wfile.write(json.dumps({'bmi' : bmi}).encode('utf-8'))

            print(f'{bmi.:f})

        return



# Create an object of the above class to handle HTTP request
handler_object = MyHttpRequestHandler

PORT = 8001

#socketserver.TCPServer creates and listens at the HTTP socket, dispatching the requests to a handler.
my_server = socketserver.TCPServer(("", PORT), handler_object)


def main():
    my_server.serve_forever()

# Star the server
if __name__ == "__main__":
    print('started '+ str(PORT))
    my_server.serve_forever()
    