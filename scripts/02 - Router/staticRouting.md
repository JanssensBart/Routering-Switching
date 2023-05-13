# Static routing

# Adresseren van de routerinterfaces

### IPV4
```ini
enable
conf t
interface [int_nr]
ip address [IPV4 + MASK]
no shutdown
```
### IPV6 auto
```ini
enable
conf t
interface [int_nr]
ipv6 address [ipv6 / prefix]
ipv6 enable
no shutdown
```
### IPV6 static ingeven
```ini
enable
conf t
interface [int_nr]
ipv6 address [ipv6 / prefix] link-local
no shutdown
```
## Aanmaken van IPv4 loopback interface
```ini
enable
conf t
interface loopback [loopback nr]
ip address [ipv4 + mask]
```

## Verifiëren van routerinterface configuratie
```ini
enable
show ip interface brief
```
```ini
enable
show ipv6 interface brief
```
```ini
enable
show interfaces
```
```ini
enable
show ip interface
```
```ini
enable
show ipv6 interface [int nr]
```
```ini
enable
show ipv6 running-config interface [int nr]
```

# Routes configureren

## Configureren van een static IPv4 route
```ini
enable
conf t
 ip route [destination-address+subnet-mask] [Port ex S0/0/0]
```
## Configureren van een static IPv6 route
```ini
enable
conf t
ipv6 unicast-routing
ipv6 route [ipv6-network-address/prefix-length] [Port ex S0/0/0]
```
## Configureren van een IPv4 default gateway (Gateway of last resort)
```ini
enable
conf t
ip route 0.0.0.0 0.0.0.0 [egress-interface]
```
## Configureren van een IPv6 default gateway (Gateway of last resort)
```ini
enable
conf t
ipv6 route ::/0 [egress interface]
```
## Verifiëren van static routes

```ini
enable
show ip route static 
```
```ini
enable
show running-config | section ip route  
```
```ini
enable
show ipv6 route static 
```
```ini
enable
show running-config | section ipv6 route 
```
```ini
ping 
```
```ini
traceroute
```