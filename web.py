from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        # Verificamos si la ruta es "/" para servir el contenido de home.html
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            # Leemos el contenido de home.html
            try:
                with open("home.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                # Enviamos el contenido del archivo como respuesta
                self.wfile.write(html_content.encode("utf-8"))
            except FileNotFoundError:
                # Si el archivo no existe, regresamos un error 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 - File not found")

                        # Nueva ruta para servir 1.html
        elif self.path == "/proyecto/1":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            # Leemos el contenido de 1.html
            try:
                with open("1.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                # Enviamos el contenido del archivo como respuesta
                self.wfile.write(html_content.encode("utf-8"))
            except FileNotFoundError:
                # Si el archivo no existe, regresamos un error 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 - File not found")
        elif self.path == "/proyecto/web-uno?autor=Jaime":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            
        elif self.path == "/proyecto/2":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            # Leemos el contenido de 1.html
            try:
                with open("2.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                # Enviamos el contenido del archivo como respuesta
                self.wfile.write(html_content.encode("utf-8"))
            except FileNotFoundError:
                # Si el archivo no existe, regresamos un error 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 - File not found")
        elif self.path == "/proyecto/web-uno?autor=Jaime":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            # Leemos el contenido de 1.html
            try:
                self.wfile.write(b"Proyecto: web-uno Autor: Jaime")
            except FileNotFoundError:
                # Si el archivo no existe, regresamos un error 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 - File not found")
        else:
            # Para cualquier otra ruta, regresamos un mensaje de ruta no encontrada
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - Ruta no encontrada</h1>")

            
if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
