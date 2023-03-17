from netmiko import ConnectHandler

my_device = {
    'device_type': 'cisco_ios',
    'host':   '192.168.69.1',
    'username': 'beheerder',
    'password': 'class',
    'port': 22,          # optional, defaults to 22
    'secret': 'class',     # optional, defaults to ''
}

# Factory function selects the proper class and creates object based on device_type.
# ConnectHandler(*args: Any, **kwargs: Any) ‑> BaseConnection //
connect = ConnectHandler(**my_device)

output = connect.send_command('show ip int brief')
print(output)
