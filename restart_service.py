# restart_service.py
import subprocess

def restart_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "restart", service_name], check=True)
        return f"{service_name} restarted successfully"
    except subprocess.CalledProcessError as e:
        return f"Failed to restart {service_name} - {e}"
