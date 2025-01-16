import warnings
import sys
import os
import nmap
import signal
import time
from colorama import Fore, init


init(autoreset=True)
warnings.filterwarnings("ignore", category=DeprecationWarning)

banner = """
################################################################################
#                                                                              #
#  		  ██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗   		       #
#  		  ██║  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║   		       #
#  		  ███████║███████╗██║     ███████║██╔██╗ ██║  		       #
# 		  ██╔══██║╚════██║██║     ██╔══██║██║╚██╗██║   		       #
#  		  ██║  ██║███████║╚██████╗██║  ██║██║ ╚████║   		       #
#  		  ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝   		       #
#                                                                              #
#              HScan - Tool for efficient network port scanning.               #
#                                                                              #
################################################################################

Author : Herlan Sebastian
Github : Github.com/Hsebastianr
"""

print(Fore.CYAN + banner)

def handle(sig, frame):
    print(Fore.RED + "\n\n[!] Exiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, handle)

def mainfunction():
    host = input(Fore.YELLOW + "Enter the target >> ").strip()
    nm = nmap.PortScanner()
    ports_open = []

    print(Fore.GREEN + "[!] Performing initial scan...")
    results1 = nm.scan(hosts=host, arguments="-T5 -n -Pn -v -oN HScan.txt")
    
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        sorted(lport)
        for port in lport:
            ports_open.append(str(port))  # Añadir puertos abiertos a la lista

    for proto in nm[host].all_protocols():
        print(Fore.YELLOW + f"\nProtocol: {proto}")
        for port, data in nm[host][proto].items():
            status = data['state']
            service = data.get('name', 'Unknown')
            print(Fore.GREEN + f"Port: {port} : Status: {status} : Service: {service}")

    realizar_udp = input(Fore.YELLOW + "\nDo you want to perform the UDP scan? (y/n): ").strip().lower()

    if realizar_udp == 'y':  
        print(Fore.CYAN + "\n[!] Starting UDP scan...")
        results_udp = nm.scan(hosts=host, arguments="-sU -T5")
        
        print(Fore.CYAN + "\nUDP scan results:\n")
        for proto in nm[host].all_protocols():
            if proto == 'udp': 
                print(Fore.YELLOW + f"Protocol : {proto}")
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    services = nm[host][proto][port]['name']
                    state = nm[host][proto][port]['state']
                    print(Fore.GREEN + f"Port : {port}\tStatus : {state}\tService : {services}")
                    ports_open.append(str(port))  # Añadir puertos UDP abiertos a la lista
        print(Fore.GREEN + "\n[!] UDP scan completed.")
    else:
        print(Fore.RED + "\n[!] UDP scan skipped.")

    if '161' in ports_open or '162' in ports_open:
        print(Fore.CYAN + "\n[!] Detected SNMP ports (161/162) open.")
        snmp_scan = input(Fore.YELLOW + "Do you want to perform an SNMP check? (y/n): ").strip().lower()
        if snmp_scan == 'y':
            print(Fore.CYAN + "[!] Performing SNMP check...")
            os.system(f"snmp-check {host}")
        else:
            print(Fore.RED + "[!] SNMP check skipped.")

    if "80" in ports_open or "443" in ports_open:
        scan_directories = input(Fore.YELLOW + "¿Do you want to perform a directory scan (dirsearch)? (y/n): ").strip().lower()
        if scan_directories == "y":
            print(Fore.CYAN + "[!] Performing directory scan...")
            url = f"http://{host}" if "http" not in host else host
            os.system(f"dirsearch -u {url} -t 50 -q")
            print(Fore.GREEN + "[!] Directory scan completed.\n")
        else:
            print(Fore.RED + "[!] Directory scan will not be performed.\n")

    print(Fore.GREEN + "\n[!] Scan completed.")

if __name__ == "__main__":
    mainfunction()
