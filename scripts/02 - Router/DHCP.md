# DHCPv4 op het netwerk

## Routerinterface instellen

### interface
```ini
enable
conf t
int [interface]
ip address [ipv4 + mask]
no shutdown
```
### enable dhcp
```ini
enable
conf t
,nq 3wqhnnip address dhcp
no shutdown
```
## dhcp in ander netwerk
```ini
enable
conf t
int [interface van vragende partij]
ip helper-address [ip van DHCP] 
```