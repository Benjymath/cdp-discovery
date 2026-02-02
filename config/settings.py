import os

# Tiempo máximo de captura (segundos)
CAPTURE_TIMEOUT = 120

# Nombre del ejecutable tshark
TSHARK_EXECUTABLE = "Wireshark/tshark.exe"

# Carpetas prohibidas (interfaces virtuales)
VIRTUAL_KEYWORDS = [
    "virtual", "vmware", "vethernet", "loopback", "npcap"
]

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
