import os

base_dir = "/var/log"
app_name = "nginx"
filename = "access.log"

path = os.path.join(base_dir, app_name, filename)
print(path)
