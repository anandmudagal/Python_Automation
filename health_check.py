# health_check.py
import requests
import socket
import subprocess

def check_url_health(url):
    try:
        response = requests.get(url, timeout=5)
        return f"{url} - Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"{url} - Error: {e}"

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return f"{host}:{port} is reachable"
    except Exception as e:
        return f"{host}:{port} is NOT reachable - {e}"

def check_service_status(service_name):
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
        return f"{service_name}: {result.stdout.decode().strip()}"
    except Exception as e:
        return f"{service_name} check failed - {e}"
