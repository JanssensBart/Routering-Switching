# Configure and Verify Security Features on Switch

1. general security features.
    1. What IP's & physical ports are up?
    ```ini 
    enable
    show ip interface brief
    ```
    2. shutdown port with range
    ```ini 
    conf t
    interface range f0/1 – 9
    shutdown
    ```
    3. show ip http server status
    *shutdown this service*
    ```ini 
    conf t
    no ip http server
    ```

2. port security
    1. config
    ```ini 
    conf t
    interface [f0/5]
    shutdown
    switchport mode access
    switchport port-security
    switchport port-security mac-address [xxxx.xxxx.xxxx]
    switchport port-security mac-address sticky
    switchport port-security maximum [x]
    no shutdown
    end
    ```
    > xxxx.xxxx.xxxx = mac address of the incoming device to switch <br>
    > delete mac address: <br>
    > *clear port security restricted-macs ethernet 5*
    2. verify - show port security on specific port.
     ```ini 
    enable
    show port-security interface [f0/5]
    ```

