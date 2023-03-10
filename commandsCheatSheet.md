### Basic Switch Settings

# 1. Switch Virtual Interface (= SVI)

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch>enable                                             | Overgaan naar privileged mode                                                         |
| Switch#configure terminal                                 | Overgaan naar configuration mode                                                      |
| Switch(config)#vlan 99                                    | Een vlan met ID-nr 99 aanmaken                                                        |
| Switch(config-vlan)#exit                                  | Teruggaan naar configuration mode                                                     |
| Switch(config)#interface vlan 99                          | Overgaan naar interface configuratie mode van vlan 99 om de SVI te configureren       |
| Switch(config-if)#ip address 192.168.1.2 255.255.255.0    | Een IP adres en masker toekennen aan de SVI van vlan 99.                              |
| Switch(config-if)#no shutdown                             | De SVI actief zetten                                                                  |
| Switch(config-if)#exit                                    | Overgaan naar configuration mode                                                      |
| Switch(config)#interface range f0/1 – 24 , g0/1 - 2       | De 24 fast-ethernet poorten + de 2 gigabit ethernet poorten van de switch selecteren  |
| Switch(config-if-range)#switchport access vlan 99         | Al deze poorten lid maken van vlan 99                                                 |
| Switch(config-if-range)#exit                              | Teruggaan naar configuration mode                                                     |
| Switch(config)#ip default-gateway 192.168.1.254           | Default gateway instellen                                                             |
| Switch(config)#exit                                       | Teruggaan naar privileged mode                                                        |
| Switch#show vlan brief                                    | Een kort overzicht geven van welke poorten deel uitmaken van vlan 99.                 |
| Switch#copy run star                                      | De configuratie bewaren                                                               |

# 2. Console toegang beveiligen

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch>enable                                             | Overgaan naar privileged mode                                                         |
| Switch#configure terminal                                 | Overgaan naar configuration mode                                                      |
| Switch(config)#line console 0                             | De toegang via consolekabel regelen                                                   |
| Switch(config-line)#password cisco                        | Als out-band wachtwoord ‘cisco’ instellen                                             |
| Switch(config-line)#login                                 | Enablen van password checking bij benaderen via console                               |
| Switch(config-line)#end                                   | Terugkeren naar privileged mode                                                       |

# 3. In-band toegang verkrijgen via netwerk (telnet,SSH)

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch>enable                                             | Overgaan naar privileged mode                                                         |
| Switch#configure terminal                                 | Overgaan naar configuration mode                                                      |
| Switch(config)#line vty 0 15                              | De toegang via telnet kanalen 0 tot en met 15 regelen                                 |
| Switch(config-line)#password cisco                        | Als toegangswachtwoord ‘cisco’ instellen                                              |
| Switch(config-line)#login                                 | Controleren of er nog telnet lijnen onbeveiligd zijn (i.e. of er nog telnet lijnen zonder wachtwoord zijn)|
| Switch(config-line)#end                                   | Terugkeren naar privileged mode                                                       |