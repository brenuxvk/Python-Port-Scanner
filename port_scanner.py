# -*- coding: utf-8 -*-
import socket
import sys
from datetime import datetime

# Função principal do scanner
def scan_ports(target):
    """Escaneia as portas 1-1024 de um alvo."""
    
    # Imprime um banner inicial com informações
    print("-" * 50)
    print(f"Escaneando o alvo: {target}")
    print(f"Início em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 50)
    
    open_ports = []

    try:
        # Itera sobre as portas mais comuns (1 a 1024)
        for port in range(1, 1025):
            # Cria o objeto socket para conexão TCP/IP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Define um timeout de 1 segundo para a tentativa de conexão
            socket.setdefaulttimeout(1)
            
            # Tenta conectar ao alvo na porta atual. Retorna 0 se for bem-sucedido.
            result = sock.connect_ex((target, port))
            
            if result == 0:
                print(f"Porta {port}: \t Aberta")
                open_ports.append(port)
            
            # Fecha a conexão do socket
            sock.close()

    except socket.gaierror:
        print("[ERRO] O nome do host não pôde ser resolvido.")
        sys.exit()
    except socket.error:
        print("[ERRO] Não foi possível conectar ao servidor.")
        sys.exit()
    except KeyboardInterrupt:
        print("\n[INFO] Saindo do programa.")
        sys.exit()

    print("-" * 50)
    if open_ports:
        print(f"Escaneamento concluído. Portas abertas encontradas: {open_ports}")
    else:
        print("Escaneamento concluído. Nenhuma porta aberta encontrada no range 1-1024.")
    print("-" * 50)


# Verifica se o script foi chamado com o argumento correto
if len(sys.argv) == 2:
    # Pega o alvo a partir do argumento da linha de comando
    target_ip = socket.gethostbyname(sys.argv[1])
    scan_ports(target_ip)
else:
    print("Uso inválido!")
    print("Sintaxe: python3 port_scanner.py <alvo>")
    print("Exemplo: python3 port_scanner.py google.com")