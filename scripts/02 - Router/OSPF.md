# OSPF commands

## commands
```ini
enable
conf t
router ospf [proces-id] #int
router-id [ipv4 address bv 1.1.1.1]
network [ip_addr] [wildcard_mask] area [nummer] # moet op alle routers die binnen eenzelfde area werken, hetzelfde zijn
passive-interface [interface-id] 
```

*alernative*

```ini
enable
conf t
interface [int-id] 
ip ospf [proces-id] area [nummer] 
```

## config verifiëren

```ini
enable
show ip protocols
show ip ospf neighbor 
show ip ospf interface 
show ip route ospf 
```