import os
import sys
from config.settings import BASE_DIR, TSHARK_EXECUTABLE
from src.interface_utils import list_interfaces, auto_detect_ethernet
from src.cdp_scanner import scan_cdp

def find_tshark():
    local = os.path.join(BASE_DIR, "Wireshark", TSHARK_EXECUTABLE)
    return local if os.path.exists(local) else TSHARK_EXECUTABLE

def main():
    tshark = find_tshark()

    interfaces = list_interfaces(tshark)

    print("\nInterfaces disponibles:\n")
    for num, name in interfaces.items():
        print(f"{num}. {name}")

    choice = input("\nNúmero de interfaz (ENTER = auto Ethernet): ").strip()

    if choice and choice in interfaces:
        iface_num = choice
        iface_name = interfaces[choice]
    else:
        iface_num, iface_name = auto_detect_ethernet(interfaces)

    if not iface_num:
        print("❌ No se encontró interfaz Ethernet física")
        sys.exit(1)

    print(f"\n📡 Usando interfaz: {iface_name}")
    print("⏳ Escaneando CDP...\n")

    result = scan_cdp(tshark, iface_num, iface_name)
    

    if result:
        print("✅ CDP detectado")
        print(f" Hostname : {result['hostname']}")
        print(f" IP       : {result['ip'].split(",")[0].strip()}")
        print(f" Puerto   : {result['port']}")
        print(f" Interfaz : {result['interface']}")
        print(f" Tiempo   : {result['elapsed']} s")
    else:
        print("❌ No se detectó CDP")

if __name__ == "__main__":
    main()
