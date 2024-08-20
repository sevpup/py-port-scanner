# py-port-scanner

This is a simple port scanner built in Python. It allows users to scan the open TCP ports of a remote host, providing the port number and the associated service if available. The script uses socket programming to perform the scan and can be easily customized for different use cases.

**Features**
Scans TCP ports of a given remote host.
Displays open ports and the services running on them.
Simple and easy to use with Python 3.
Uses a range of ports from 1 to 65535 by default.

**Prerequisites**
Python 3.x

Socket and subprocess libraries (both are part of the Python standard library)

**How to Run**

Clone the repository to your local machine:
git clone https://github.com/sevpup/port-scanner.git

Navigate to the project directory: 
cd port-scanner

Run the Python script:
python3 port_scanner.py

Input the hostname or IP address of the remote server to scan.

**Code Overview**

The port scanner performs the following:

Clear Screen: Clears the terminal before starting the scan.

Get Remote Host: Prompts the user for a hostname or IP address and resolves it to an IP.

Scan Ports: Iterates through the specified range of ports and checks if they are open.

Service Identification: Attempts to map open ports to their associated services.
