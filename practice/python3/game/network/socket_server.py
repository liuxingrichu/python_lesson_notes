import socketserver

class MyTCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024)
            except ConnectionResetError as e:
                print('client %s is disconnected!' % self.client_address[0])
                break
            if not self.data:
                print('client %s is closed!' % self.client_address[0])
                continue
            print(self.data, type(self.data))
            self.request.send(self.data)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), MyTCPServer)
    print('waiting for client ... ')
    server.serve_forever()
    server.server_close()