import subprocess
import sys
from config.settings import TSHARK_EXECUTABLE, VIRTUAL_KEYWORDS

def list_interfaces(tshark_path):
    """
    Devuelve un diccionario {numero: nombre_interfaz}
    """
    try:
        output = subprocess.check_output(
            [tshark_path, "-D"],
            text=True,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print("❌ Error ejecutando tshark -D")
        print(e)
        sys.exit(1)

    interfaces = {}
    for line in output.splitlines():
        if "." in line:
            num, name = line.split(".", 1)
            interfaces[num.strip()] = name.strip()

    return interfaces


def auto_detect_ethernet(interfaces):
    """
    Detecta automáticamente una interfaz Ethernet física
    """
    for num, name in interfaces.items():
        lname = name.lower()
        if "ethernet" in lname and not any(v in lname for v in VIRTUAL_KEYWORDS):
            return num, name
    return None, None
