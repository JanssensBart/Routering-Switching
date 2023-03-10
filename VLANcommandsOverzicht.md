### VLAN commands overzicht

# 1. VLAN’s definiëren.

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch#vlan database                                      | Overgaan naar de vlan database                                                        |
| Switch(vlan)#vlan nummer name *naam*                      | Definieer de vlan door er een uniek nummer en unieke naam aan te geven (bvb vlan 99 name administratie )|
| Switch(config)#vlan 99                                    | De gedefinieerde vlans tonen, alsook de poorten die aan elke gedefinieerde vlan werden toegewezen|

# 2. Access poorten instellen en toewijzen.

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch(config)#interface *int-nr*                         | De interface selecteren die je gaat configureren( bvb. interface fa0/1 )              |
| Switch(config-if)#switchport mode access                  | Instellen dat de poort een access poort is en dus maar lid kan zijn van 1 vlan        |
| Switch(config-if)#switchport access vlan *nr*             | Instellen dat de poort thuishoort in 1 specifiek vlan ( bvb. switchport access vlan 99 )|
| Switch#show vlan                                          | De gedefinieerde vlans tonen, alsook de poorten die aan elke gedefinieerde vlan werden toegewezen|
| Switch#show run                                           | Configuratie verifiëren alvorens te bewaren                                           |

# 3. Trunk poorten instellen en toewijzen.

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch(config)#interface *int-nr*                         | De interface selecteren die je gaat configureren( bvb. interface fa0/1 )              |
| Switch(config-if)#switchport mode trunk                   | Instellen dat de poort een trunk poort is en verkeer van alle vlans erover toegelaten is|
| Switch(config-if)#switchport trunk native vlan *nr*       | Instellen op welke VLAN untagged verkeer dat de trunk ontvangt, moet terechtkomen     |
| Switch(config-if)#switchport trunk allowed vlan ?         | Instellen welke vlans over de trunk mogen. Het vraagteken geeft je welke opties er hier zijn|
| Switch(config-if)#switchport trunk allowed vlan except 5  | Zorgt ervoor dat vlan 5 niet toegelaten is op de trunk. Gebruik ? Om mogelijkheden op te vragen.|
| Switch#show run                                           | Configuratie verifiëren alvorens te bewaren                                           |

# 4. Werken met voice VLAN.

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch(config)#interface *int-nr*                         | De interface selecteren die je gaat configureren                                      |
| Switch(config-if)#mls qos trust cos                       | Dat er kwaliteitsgarantie gelden (qos = Quality of Service) en dat Class of Service (cos) die de telefoon aangeeft van te moeten geven aan de end-user,door de switch moet vertrouwd worden en dat deze alles moet doen om daaraan te kunnen tegemoet komen.|
| Switch(config-if)#switchport voice vlan *nr*              | Instellen op welke VLAN het voice verkeer dat ontvangen wordt, moet terechtkomen      |


# 5. VTP instellen.

| Commando                                                  | uitleg                                                                                |
| -----------                                               | -----------                                                                           |
| Switch(config)#vtp mode *server* *client*                 | De switch instellen als VTP server of als VTP client.                                 |
| Switch(config)#vtp domain *naam*                          | Alle switchen met dezelfde domein naam zullen VTP info met elkaar
                                                              uitwisselen. Een VTP client isn hetzelfde domein als de VTP server
                                                              neemt de VAN definities over van de server                                            |
| Switch#show vtp status                                    | Status opvragen van het VTP domein                                                    |
| Switch#show vtp counters                                  | VTP statistieken opvragen                                                             |

# 5. VLAN troubleshooting.

| Probleem                      | Resultaat                                             |  uitleg                                                   | 
| -----------                   | -----------                                           | -----------                                               |
| Foute native VLAN ingesteld   | Beveiligingsrisico en raar gedrag van de communicatie |   De twee trunkpoorten aan weerszijden
                                                                                            van een link hebben een ander native
                                                                                            VLAN geconfigureerd gekregen                            |
| Trunk mode fout               | Geen connectiviteit                                   |   De ene kant van de trunklijn is
                                                                                            geconfigureerd als trunk poort, maar de
                                                                                            andere kant als access poort                            |
| Toegelaten VLANs op de trunk fout ingesteld| Onverwacht verkeer of geen verkeer over de trunk lijn | De lijst van toegelaten VLANs op een 
                                                                                                        trunk lijn staat niet helemaal op punt      |