# VLAN setup.

1. create vlan & add net ip

```ini 
conf t
vlan [99]
name [Management]
exit
interface vlan [99]
ip address [192.168.13.1] [255.255.255.0]
no shutdown
exit
```
2. add interface to vlan

```ini 
conf t
interface [f0/6]
switchport access [vlan 99]
exit
```
3. add console connection password

*Om te verhinderen dat console boodschappen ertussen komen terwijl je commands aan het ingeven bent,gebruik je de optie logging synchronous.*

```ini 
conf t
line con 0
password [cisco]
login
logging synchronous
exit
```
*Configureer de virtual terminal (vty) lines om Telnet of ssh access via het netwerk naar de switch toe te laten. Als je geen vty paswoord configureert, zal je de switch niet via het netwerk kunnen benaderen.*

```ini 
conf t
line vty [0 15]
password [cisco]
login
end
```
4. Configure and Verify SSH Access on S1

    1. CONFIGURE SSH access on switch.
    ```ini 
    conf t
    ip domain-name [CCNA-Lab.com]
    username [admin] privilege 15 secret [sshadmin]
    line vty 0 15
    transport input ssh
    login local
    exit
    crypto key generate rsa modulus 1024
    end
    ```
    > IN PACKET TRACER:
    > crypto key generate rsa **general-keys** 1028

    2. MODIFY SSH settings
    *shows ssh settings*
    ```ini 
    show ip ssh
    ```
    *Modify the default SSH configuration*
    ```ini 
    conf t
    ip ssh time-out [75]
    ip ssh authentication-retries [2]
    ```
5. save configuration

```ini 
enable
copy run start
```
