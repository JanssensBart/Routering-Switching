###  Makkelijk configuraties overzetten

# 1. Out-of-Band management: het betere copy/paste werk

We spreken van *out-of-band* management als het gaat om een toestel dat
**geen IP adres** heeft.

``` show running-config ```

![Running Config](./images/runningConfig.png)

Je kan vervolgens deze configuratie info plakken in een eenvoudig tekst
bestandje (bvb in Notepad/Kladblok). Je kan er dan wijzigingen in
aanbrengen (bvb een andere hostname instellen) en deze gewijzigde versie
onder een andere naam bewaren.


# 2. In-Band management: Via FTP / TFTP

We spreken van **in-band management** als het gaat om een toestel dat **wel een
IP adres** heeft. Een IP adres hebben, wil zeggen dat een device bereikbaar is via
het netwerk via specifieke ondersteunde protocollen zoals *SSH*, *HTTP* of *FTP*.

>Dit houdt in dat de netwerk-configuratie van de router of switch in orde moet zijn
>+ dat de configuratie van eventueel tussenliggende apparaten in orde moet zijn
>+ dat de netwerkconfiguratie van de FTP server in orde moet zijn!

## 2.1 Bestand copiëren van toestel naar FTP server:

``` copy filenameDevice ftp://username:password@location[/directory/filenameFTP] ```

**Verplichte parameters:**

- **username**: naam van de gebruiker die op de FTP server werd aangemaakt en lees en schrijfrechten heeft op de directory waarin weggeschreven wordt
- **password**: wachtwoord dat hoort bij de usernaam waarmee je de FTP operatie uitvoert
- **location**: IP adres van de FTP server
- **filenameDevice**: naam van het bestand zoals het op de switch if router heet. 

Enkele voorbeelden van zaken die je hier kan invullen zijn:
- *system:running-config*
- *nvram:startup-config*

**Optionele parameters die je kan meegeven zijn:**

- **Directory**: map op de FTP server waarin je het gecopieerde bestand wil zetten.
- **filenameFTP**: naam dat het bestand op de FTP server moet krijgen. Als je niets opgeeft, dan behoudt het bestand dezelfde naam als datgene wathet was op de switch of router.

## 2.2 Bestand copiëren van FTP server naar toestel:

De werkwijze is gelijkaardig. Je moet verbinding hebben tussen de FTP server
en het toestel, en de gebruiker uit onderstaand commando moet voldoende
rechten hebben op de map waaruit de file wordt opgehaald. Het commando dat
je op de router of switch ingeeft om bestanden van een FTP server af te halen,
is

``` copy ftp://username:password@location[/directory/filename] filenameDevice ```