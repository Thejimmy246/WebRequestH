from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
         path = self.url().path
         query_data = self.query_data()

        # Componemos la respuesta basada en el path y el query string
         if(path == "/proyecto/web-uno"):
            autor = query_data.get("autor", "Yo")
            return f"""
                <h1> Proyecto: web-uno Autor: {autor} </h1>
            """
         else:
            return f"""
                <h1>Ruta no encontrada</h1>
                <p> Path Original: {self.path} </p>
                <p> Query: {self.query_data()} </p>
            """

if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
