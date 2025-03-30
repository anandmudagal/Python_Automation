# main.py
from health_check import check_url_health, check_port, check_service_status
from resource_monitor import check_disk_usage, check_memory
from restart_service import restart_service

print(check_url_health("https://yourapp.com/health"))
print(check_port("yourhost.com", 443))
print(check_service_status("nginx"))
print(check_disk_usage("/"))
print(check_memory())
print(restart_service("your-app-service"))
