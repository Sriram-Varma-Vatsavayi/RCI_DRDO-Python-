#!/usr/bin/env python
# coding: utf-8

import psutil
import platform
import socket
import fpdf
import wmi
from datetime import datetime

# Function to network connectivity
def get_network_type():
    network_interfaces = psutil.net_if_addrs()
    network_stats = psutil.net_if_stats()

    for interface, addrs in network_interfaces.items():
        if interface in network_stats and network_stats[interface].isup:
            for addr in addrs:
                if addr.family == psutil.AF_LINK:  # MAC address
                    interface_type = network_stats[interface]
                    if 'wireless' in interface.lower():
                        return f"Connected via WiFi: {interface}"
                    elif 'ethernet' in interface.lower():
                        return f"Connected via Ethernet: {interface}"
                    else:
                        # Heuristically determine connection type
                        if interface_type.speed >= 1000:
                            return f"Connected via Ethernet: {interface}"
                        else:
                            return f"Connected via WiFi: {interface}"

    return "No active network connection found"

if __name__ == "__main__":
    connection_type = get_network_type()
    print(connection_type)

# Function to check antivirus software
def check_antivirus():
    try:
        wmi_service = wmi.WMI(namespace="SecurityCenter2")
        antivirus_info = ""
        found_antivirus = False
        
        for product in wmi_service.AntivirusProduct():
            antivirus_info += f"Antivirus software installed:\nName: {product.displayName}, Version: {product.productState}\n"
            found_antivirus = True
        
        if not found_antivirus:
            antivirus_info = "No antivirus software found"
            
    except Exception as e:
        antivirus_info = f"An error occurred: {e}"
    
    return antivirus_info

if __name__ == "__main__":
    result = check_antivirus()
    print(result)
    
# Collect system information
print("="*40, "System Information", "="*40)
name = platform.uname()
host = socket.gethostname()

# Initialize PDF
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

# Gather system details
system_name = name.system
node_name = name.node
release_name = name.release
version_name = name.version
machine_name = name.machine
processor_name = name.processor
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host)
network_status = get_network_type()
antivirus_check = check_antivirus()

# Print system details to console
print("System Name: " + system_name)
print("Node Name: " + node_name)
print("Release Name: " + release_name)
print("Version Name: " + version_name)
print("Machine Name: " + machine_name)
print("Processor Name: " + processor_name)
print("Host Name: " + host_name)
print("IP Address: " + ip_address)
print("Network connectivity: " + network_status)
print("Antivirus Software: " + antivirus_check)

# Write system details to PDF
d1 = {
    'System Name: ': system_name,
    'Node Name: ': node_name,
    'Release Name: ': release_name,
    'Version Name: ': version_name,
    'Machine Name: ': machine_name,
    'Processor Name: ': processor_name,
    'Host Name: ': host_name,
    'IP Address: ': ip_address,
    'Network Connectivity: ': network_status,
    'Antivirus Status: ': antivirus_check
}

for key, value in d1.items():
    pdf.write(10, str(key + " " + value))
    pdf.ln()

pdf.output("drdov3.pdf")

# Keep the window open
input("Press Enter to exit...")
