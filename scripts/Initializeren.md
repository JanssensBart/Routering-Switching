# Initializeren en reloaden van een switch
- does vlan.dat exist ?
```shell 
enable
show flash
```
- Delete vlan.dat.
```shell 
delete vlan.dat
```
*Delete filename [vlan.dat]?* [confirm] **enter**

- delete startup-config
```shell 
erase startup-config
```
*Erasing the nvram filesystem will remove all configuration files! Continue?*
*[confirm][OK]*
*Erase of nvram: complete*


```shell 
reload
```

*System configuration has been modified. Save? [yes/no]: no*

- after reload :

*Would you like to enter the initial configuration dialog? [yes/no]: no*