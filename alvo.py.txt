################################################################
# alvo.py                                                      #
# Script para emular o painel interno vulneravel HTTP no host, #
# injetando os cabecalhos CORS e Private Network Access (PNA)  #
#                                                              #
# Escrito por Carlos Alexandre Menezes                         #
# Last update on 29052026                                      #
# Version 1.4                                                  #
# Megabytez CyberSec Labs                                      #
#                                                              #
################################################################
from http.server import HTTPServer, BaseHTTPRequestHandler

class VulnerableHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        self.end_headers()
        self.wfile.write(b"CHAVE_SECRETA_DO_LAB_REPLICADA_COM_SUCESSO")

# IMPORTANTE: Utilizar '0.0.0.0' para responder em qualquer interface local
server = HTTPServer(('0.0.0.0', 8080), VulnerableHandler)
print("Painel Local ativo em http://127.0.0.1:8080...")
server.serve_forever()