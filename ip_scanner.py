import os
import platform

# tabulka výsledků
results = []

# ping funkce
def ping(ip):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    return os.system(f"ping {param} {ip} > nul 2>&1") == 0

network = "192.168.100."

for i in range(1, 255):
    ip = network + str(i)
    status = "ONLINE" if ping(ip) else "OFFLINE"
    results.append([ip, status])

# výpis tabulky
print("IP adresa\t\tStav")
print("-" * 30)
for row in results:
    print(f"{row[0]}\t{row[1]}")
