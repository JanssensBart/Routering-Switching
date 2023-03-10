###  CONFIG

# 1. Commandos


- ```enable``` : global config
- ```configure terminal``` : interface config
- ```exit``` of ```ctrl z``` : Om naar een eerder configuratieniveau te gaan
- ```copy running-config startup-config``` : Configuratie bewaren RAM > NVRAM
- ```?``` : hulp vragen
- ```do``` : uitvoeren vanuit een *'verkeerd'* niveau.
- ```no``` : Een commando ingegeven waarvan je het resultaat ongedaan wil maken

*hint : TAB voor autocompletion*

```copy running-config startup-config = cop run start```

# 2. Afspraken

In de labs mogen op de fysieke toestellen enkel de wachtwoorden
```**cisco**``` en ```**class**``` *(kleine letters)* gebruikt worden

# 3.Toestellen her-initialiseren

### Stap 1

``` 
Switch> enable
Switch#
```
### Stap 2

```Switch# show flash ```

- Als de ``` vlan.dat ``` file gevonden werd in flash, delete dan deze file.
``` 
Switch# delete vlan.dat
Delete filename [vlan.dat]? [confirm] *press enter*
Switch#
```

- Gebruik het erase startup-config command om de startup configuration file van
NVRAM te wissen. U moet bevestigen dat u dat effectief wil doen.

``` 
Switch# erase startup-config
Erasing the nvram filesystem will remove all configuration files!
Continue? [confirm][OK]Erase of nvram: complete
Switch#
```

- Reload de switch. Druk Enter om verder te gaan.

``` 
Switch# reload
Proceed with reload? [confirm] *press enter*
```

- Het kan zijn dat u onderstaande vraag krijgt. Antwoord dan met no en druk **Enter**.

``` 
System configuration has been modified. Save? [yes/no]: no
```

