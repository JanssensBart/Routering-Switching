# MAC Table

```ini 
show mac address-table
```
```ini 
clear mac address-table dynamic
```

1. ADD static MAC address to interface

```ini 
mac address-table static [0050.56BE.6C89] vlan [99] interface fastethernet [0/6]
```

2. REMOVE static MAC address to interface
```ini 
no mac address-table static [0050.56BE.6C89] vlan [99] interface fastethernet [0/6]
```