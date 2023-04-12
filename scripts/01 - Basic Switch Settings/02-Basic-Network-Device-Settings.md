# Config Basic Network Device Settings

1. Basic switch settings.

```ini 
conf t
no ip domain-lookup
hostname [name]
service password-encryption
enable secret [class]
banner motd #
[Unauthorized access is strictly prohibited] 
#
line con 0
password [cisco]
login
logging synchronous
line vty 0 15
password [cisco]
login
exit
```

