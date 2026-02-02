import subprocess
import time
import sys
from config.settings import CAPTURE_TIMEOUT

def scan_cdp(tshark_path, iface_num, iface_name):
    """
    Escanea CDP y retorna dict con hostname, ip y port
    """
    cmd = [
        tshark_path,
        "-i", iface_num,
        "-Y", "cdp",
        "-a", f"duration:{CAPTURE_TIMEOUT}",
        "-T", "fields",
        "-e", "cdp.deviceid",
        "-e", "cdp.nrgyz.ip_address",
        "-e", "cdp.portid",
        "-l"
    ]

    start = time.time()

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
    except Exception as e:
        print("❌ Error iniciando captura")
        print(e)
        sys.exit(1)

    for line in proc.stdout:
        line = line.strip()
        if not line:
            continue

        fields = line.split("\t")
        result = {
            "hostname": fields[0] if len(fields) > 0 and fields[0] else "N/A",
            "ip": fields[1] if len(fields) > 1 and fields[1] else "N/A",
            "port": fields[2] if len(fields) > 2 and fields[2] else "N/A",
            "interface": iface_name,
            "elapsed": round(time.time() - start, 2)
        }

        proc.terminate()
        return result

    proc.wait()
    return None
