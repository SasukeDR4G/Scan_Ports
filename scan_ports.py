import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"El puerto {port} está abierto en {ip}")
        sock.close()
    except socket.error:
        print("Error al conectar")

def main():
    ip = input("Ingresa la dirección IP: ")
    port = int(input("Ingresa el número de puerto: "))
    scan_port(ip, port)

if __name__ == "__main__":
    main()
