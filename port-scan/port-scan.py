import socket

def port_scanner(target, ports):
    clcoding = socket.gethostbyname(target)
    print(f"Scanning {target} ({clcoding})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((clcoding, port))

        if result == 0:
            print(f"Port {port} : Open")
        else:
            print(f"Port {port} : Closed")

        sock.close()

# Sample
targetHost = "x.com"
targetPorts = [22, 80, 443, 8000, 8080]

port_scanner(targetHost, targetPorts)