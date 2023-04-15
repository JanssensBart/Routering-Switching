## Router-on-a-stick 


# subinterfaces aanmaken

*! lijn naar de router moet een trunklijn zijn*

```ini
enable
conf t
interface [g0/1.10]
encapsulation dot1q [10]
ip address [172.17.10.1 255.255.255.0]
exit
interface [g0/1]
no shutdown
```

# subinterfaces verifiëren

```ini
enable
show vlan
```
```ini
enable
show ip route
```