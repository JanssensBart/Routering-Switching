# VLAN setup.

1. create vlan & add net ip

```ini 
conf t
vlan [99]
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

4. save configuration

```ini 
enable
copy run start
```
