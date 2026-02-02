# CDP Discovery Tool (Python + Tshark)

Herramienta en Python para detectar dispositivos Cisco mediante CDP
usando Tshark en Windows.

## ✨ Características

- Detección automática de interfaz Ethernet
- Captura CDP en tiempo real
- Finaliza al primer paquete válido
- Tiempo máximo configurable (default 120s)
- Muestra Hostname, IP y puerto conectaod en el switch

## 📦 Requisitos

- Windows
- Python 3.9+
- Wireshark / Tshark
- Npcap (modo WinPcap compatible)

### Dependencias internas de Tshark

- dumpcap.exe (necesario para capturar tráfico)
- Librerías DLL de Wireshark (recomendadas)

## 🚀 Uso

```bash
python src/main.py

## 📄 Example Output

See [examples/sample_output.txt](examples/sample_output.txt)

📁 Para más detalles, revisa la estructura del proyecto en
[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)