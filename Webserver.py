# References
# https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server
# https://stackoverflow.com/questions/22083359/send-text-http-over-python-socket
# https://stackoverflow.com/questions/68425239/how-to-handle-multithreading-with-sockets-in-python

# Tim Tran
# 1001638285

# Imports socket and threading libraries
import socket
import threading

# HTTP Response method, passes in the connection and address, doesn't use address but needs it because threads need iterables passed in
def response(c, addr):
    while True:
        try:
            # Receives the request from the browser
            response = c.recv(1024)
            
            # Gets the file name from the request
            file = response.split()[1:2]
            
            # Turns the file name into a string
            filename = file[0].decode()[1:]
            
            # Checks for 301 redirect, old being windex.html, new being index.html. In case of windex being used, filename is switched to index.html for opening
            if(filename == 'windex.html'):
                filename = "index.html"
                
                # Opens index.html
                f = open(filename)
                # Reads the file as a string
                output = f.read()
                # Sends the 301 response and sends index.html encoded
                c.send(b'HTTP/1.1 301 Moved Permanently\nContent-Type: text/html\n\n'+output.encode())
                # Sends the 301 response for the image
                c.send(b'HTTP/1.1 301 Moved Permanently\nContent-Type: image/jpeg\n\n')
                # Sends the image
                c.send(open("test.jpg", "rb").read())
            
            else:
                # Opens index.html in case of no 301
                f = open(filename)
                # Reads the file as a string
                output = f.read()
                # Sends the 200 response and sends index.html encoded
                c.send(b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'+output.encode())
                # Sends the 200 response for the image
                c.send(b'HTTP/1.1 200 OK\nContent-Type: image/jpeg\n\n')
                # Sends the image
                c.send(open("test.jpg", "rb").read())
            
            break
        # In case file is not found, a 404 response is generated
        except IOError:
            # Lets user know there is a 404 response
            print("404 error")
            # Sends the 404 response
            c.send(b"HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n")
            # Sends the 404 html page
            c.send(b"""
                <html>
                <body>
                <h1>404 Not Found</h1>
                </body>
                </html>
                """)
            break
    print("Done")
    # Closes the connection
    c.close()    
 
# Sets the host as the localhost
host = "127.0.0.1"
# Sets the port as 8080, but could be anything
port = 8080

# Initializes the socket and binds it to the host and the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Starts listening for traffic
s.listen(5)

# Prints message to let user know the server is open
print("Server open")

# Creates array for later threads
threads = []

try:
    while True:

        # Creates the connection and address from the socket
        c, addr = s.accept()

        # Prints message to let user know the connection information
        print('Connected to :', addr[0], ':', addr[1])
        
        # Creates the first thread, passing in the connection and the address, and starts it
        t = threading.Thread(target=response, args=(c, addr))
        t.start()
        
        # Adds the thread into the array
        threads.append(t)
# When Ctrl+C is inputted, stops the threads
except KeyboardInterrupt:
    print("Keyboard stop")
    
# Closes the socket and joins all threads
finally:
    if s:
        s.close()
    for t in threads:
        t.join()