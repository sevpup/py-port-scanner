#!/usr/bin/env python3

import socket
import subprocess
import sys
from datetime import datetime

def clearscreen():
    subprocess.call('clear', shell=True)

def getremotehost():
    remoteserver = input("Enter a remote host to scan: ")
    try:
        remote_server_ip = socket.gethostbyname(remote_server)
        return remote_server_ip
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

def scan_ports(remote_server_ip, port_range):
    print("-" * 60)
    print(f"Please wait, scanning remote host {remote_server_ip}")
    print("-" * 60)

    t1 = datetime.now()

    try:
        for port in port_range:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                result = sock.connect_ex((remote_server_ip, port))
                if result == 0:
                    try:
                        service_name = socket.getservbyport(port, 'tcp')
                    except OSError:
                        service_name = "Unknown"
                    print(f"Port {port}: \t Open")
                    print(f"Service is =  {service_name}")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.error as err:
        print(f"Socket error: {err}")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1
    print('Scanning Completed in:', total)

if __name == "__main":
    clear_screen()
    remote_server_ip = get_remote_host()
    port_range = range(65535, 0, -1)
    scan_ports(remote_server_ip, port_range)