from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
}

# Show command that we execute
connexion = ConnectHandler(**cisco1)
command = "show ip int brief"
commands = "show ip route"
output = connexion.send_command(command)
outputs = connexion.send_command(commands)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print(outputs)
print()
