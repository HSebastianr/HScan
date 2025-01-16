# HScan - Network Port Scanning Tool

**Author**: Herlan Sebastian  
**GitHub**: [Github.com/Hsebastianr](https://github.com/Hsebastianr)

---

**HScan** is a Python-based network scanning tool designed to perform efficient port scanning and vulnerability checks on a target network. Built with Nmap and additional utilities, it helps identify open ports, services running on those ports, and allows for advanced scans like UDP, SNMP, and directory enumeration.

### Features

- **TCP Port Scanning**  
  Identifies open TCP ports and the associated services on the target using Nmap with optimized arguments for faster scanning.
  
- **UDP Scan**  
  Optionally scan for open UDP ports to gain a broader view of the target’s network activity.

- **SNMP Detection**  
  If SNMP ports (161/162) are open, the tool can initiate an SNMP check using the `snmp-check` tool to detect SNMP-related vulnerabilities.

- **Directory Scanning**  
  If HTTP/HTTPS ports (80/443) are open, it offers the option to run a directory scan using `dirsearch` to find hidden web directories or files.

- **Interactive CLI**  
  Provides an easy-to-use command-line interface for users to interact with and customize scan options.

- **Colorful Output**  
  The output is color-coded using `colorama` to make it easier to read and distinguish between different types of results (open ports, services, etc.).

---

### Installation

To install and use HScan, follow these steps:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/Hsebastianr/HScan.git

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt

3. Run the script:
   ```bash
   python HScan.py

