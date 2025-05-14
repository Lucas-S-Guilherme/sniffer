# Sniffer + Login Page

## Visão Geral
Este projeto contém:
- Um **sniffer** de pacotes que captura e exibe informações de pacotes TCP/UDP (timestamp, IPs, portas e payload).
- Uma **página de login** simples (HTML+JS) que envia credenciais via POST para um servidor Flask local, gerando tráfego HTTP para teste.

O projeto está estruturado em:
- `/sniffer`: Código do sniffer (Python com Scapy).
- `/web`: Página de login e servidor Flask.
- `README.md`: Instruções completas.

## Pré-requisitos
- **Sistema**: Ubuntu 24.04
- **Permissões**: O sniffer requer privilégios de root (raw sockets).
- **Ferramentas**:
  - Python 3.12+ (`sudo apt install python3 python3-pip`)
  - Git (`sudo apt install git`)
  - Navegador web (Firefox, Chrome, etc.)
  - Opcional: Wireshark (`sudo apt install wireshark`)

## Instalação

1. Clone o repositório (se ainda não estiver em `/sniffer`):
   ```bash
   git clone https://github.com/Lucas-S-Guilherme/sniffer.git
   cd /sniffer
   ```

2. Crie e ative o ambiente virtual e Instale dependências para o sniffer:

    ```bash
    cd sniffer
    python3 -m venv venv # cria o ambiente virtual
    source venv/bin/activate # ativa ambiente virtual
    pip install -r requirements.txt # instala dependências
    deactivate   # desativa ambiente virtual
    ```

3. Crie e ative o ambiente virtual e Instale dependências do servidor web:

    ```bash
    cd web
    python3 -m venv venv # cria o ambiente virtual
    source venv/bin/activate # ativa ambiente virtual
    pip install -r requirements.txt # instala dependências
    deactivate  # desativa ambiente virtual
    ```

## Como Executar o Sniffer

```bash
    cd sniffer # Navegue até a pasta do sniffer 
    source venv/bin/activate # ative o ambiente virtual
    sudo venv/bin/python sniffer.py # execute o sniffer com privilégios de root
 ```

O sniffer capturará todos os pacotes TCP na porta 5000, exibirá no console e salvará em logs/sniffer.log. Pressione Ctrl+C para parar. Dê o comando deactivate no terminal para desativar o ambiente virtual.

## Como Iniciar a Página de Login

```bash
    cd web # navegue até a pasta web
    source venv/bin/activate # ativa o ambiente virtual
    python server.py # inicia o servidor Flask
``` 

Abra um navegador e acesse: http://localhost:5000
Preencha o formulário de login e envie. O servidor responderá com uma mensagem JSON.

Após utilizar Pressione Ctrl+C para parar. Dê o comando deactivate no terminal para desativar o ambiente virtual.

## Debugar com Wireshark

Para monitorar o tráfego gerado pela página de login:

Filtro de porta: tcp.port == 5000

Filtro de método POST: http.request.method == POST

Exemplo completo: tcp.port == 5000 and http.request.method == POST

