#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP, Raw
from datetime import datetime
import os
import logging

# Configurar logging
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sniffer.log")

# Criar diretório de logs, se não existir
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

# Configurar formato do log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Salvar no arquivo
        logging.StreamHandler()         # Exibir no console
    ]
)

def packet_callback(packet):
    if IP in packet and TCP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        port_src = packet[TCP].sport
        port_dst = packet[TCP].dport
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        # Filtrar apenas pacotes na porta 5000
        if port_src != 5000 and port_dst != 5000:
            return

        log_message = f"[{timestamp}] TCP {ip_src}:{port_src} -> {ip_dst}:{port_dst}"
        logging.info(log_message)

        # Processar payload
        if Raw in packet:
            payload = packet[Raw].load
            try:
                # Tentar decodificar como texto
                payload_text = payload.decode('utf-8', errors='ignore')
                logging.info(f"Payload: {payload_text}")
            except:
                # Se não for texto, exibir em hexadecimal
                logging.info(f"Payload (hex): {payload.hex()}")
        else:
            logging.info("No payload")
        logging.info("-" * 50)

def main():
    print("Starting packet sniffer (TCP on port 5000, interface lo)... Press Ctrl+C to stop.")
    print(f"Logs will be saved to {LOG_FILE}")
    try:
        # Capturar na interface 'lo' para tráfego localhost
        sniff(iface="lo", filter="tcp port 5000", prn=packet_callback, store=0)
    except PermissionError:
        print("Error: Run this script as root (e.g., with sudo).")
    except KeyboardInterrupt:
        print("\nStopped sniffer.")

if __name__ == "__main__":
    main()