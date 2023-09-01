import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                s.connect((ip, port))
            open_ports.append(port)
        except (ConnectionRefusedError, TimeoutError):
            continue

    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = 1
    end_port = 65535

    open_ports = scan_ports(target_ip, start_port, end_port)

    if not open_ports:
        print(f"No open ports found on {target_ip}.")
    else:
        print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
