# Schnittstellenanalyse
Bei beiden Datenquellen sind wir ähnlich vorgegangen. Wir haben unter anderem die Webseiten der Anbieter untersucht und nach Hinweisen zu den Daten gesucht. 

## MVG-Rad
An die Daten sind wir mit folgenden Schritten gelangt: 

1. Die MVG erwähnt in den AGB die Firma nextbike GmbH. 
1. Sucht man im Internet nach *nextbike* stößt man auf die Seite http://www.swa-rad.de/de/augsburg/. 
1. Dort werden Fahrradstandorte in Augsburg in einer Karte angezeigt.
1. Diese Karte ist in einem IFrame eingebunden, das seine Daten von einer anderen [Stelle](https://iframe.nextbike.net/reservation/?city_ids=178&amp;height=418&amp;maponly=1&amp;language=de) erhält. 
1. Im Quelltext dieser Stelle/Seite wird eine Javascript-Datei namens [helpers.min.js](https://iframe.nextbike.net/reservation/map/helpers.min.js) erwähnt, die letztlich einen Link zu einer xml-Datei enthält: /maps/nextbike-live.xml
1. Zusammengesetzt ergibt das https://iframe.nextbike.net/maps/nextbike-live.xml und die Datei existiert. Sie enthält die Standorte der oben genannten Karte. 
1. Durch Ausprobieren kamen wir auf die kreative URL: https://mvgrad.nextbike.net/maps/nextbike-live.xml
1. Wieder durch Ausprobieren haben wir entdeckt, dass die Daten auch als JSON ausgeliefert werden: https://mvgrad.nextbike.net/maps/nextbike-live.json

Von den JSON-Daten interessieren uns nur die Einträge, die im Array `['countries'][0]['cities'][0]['places']` enthalten sind. Folgende Felder lesen wir für unsere Objekte aus:
 
1. Station
    * lat: z.B. "48.165279"
    * lng: z.B. "11.493183"
    * name: z.B. "Amalienburgstraße"
    * number: z.B. "8853"
    * bikes: z.B. "5"
1. Fahrrad
    * lat: z.B. "48.17423432"
    * lng: z.B. "11.5864721"
    * bike_numbers: z.B. "97162" 
    
## DB-Rad

# Loader

# Datenbank
Das gewählte Datenbankschema hat die im [Diagramm](/doc/database-overview.png) visualisierte Struktur. Die gegebenen [Statements](/doc/create_database_radlhauptstadt.sql) erzeugen einerseits die Tabellen, andererseits definieren sie Prozeduren. Diese erlauben es Informationenen zu
* allen Stationenen,
* allen Fahrzeugen,
* einer Station und
* einem Fahrzeug

ab zu rufen. 

Die Prozeduren tragen dazu bei, die Logik der REST-Schnittstelle von der Anfragelogik der Datenbank zu trennen.

# Definition der REST-Schnittstelle

In der aktuellen Konfiguration lautet eine vollständige REST-Anfrage z.B. [https://www.martinzell.de/radlhauptstadt**/rest/api/v0.9/provider/mvg/vehicle**](https://www.martinzell.de/radlhauptstadt/rest/api/v0.9/provider/mvg/vehicle)

## Aktuelle Schnittstellen-Definition
 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|
 / | egal | Wurzel, keine Aktion | `{}` |
 /provider/{provider}/station | GET | Liefert alle Stationen, die zum Anbieter {provider} gehören (Position (lat/lng), Name, Nummer, verfügbare Räder). | siehe [Beispiel](/doc/examples/REST/station.json) |
 /provider/{provider}/station/{id} | GET | Liefert das Rad mit der Nummer {id} | siehe [Beispiel](/doc/examples/REST/station_8923.json) |
 /provider/{provider}/vehicle | GET | Liefert alle Fahrzeuge des Anbieters {provider} (Pos., Fzg.nummer, ggf. Name) | siehe [Beispiel](/doc/examples/REST/vehicle.json) |
 /provider/{provider}/vehicle/{id} | GET | Liefert ein Fahrzeug des Anbieters {provider} | siehe [Beispiel](/doc/examples/REST/vehicle_96101.json) |

## Noch nicht implementiert
 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|
 /provider | GET | Liefert alle Anbieter | { "providers": [ "MVG", "DB" ] } |
 /provider/mvg | GET | Liefert alle möglichen Objekte | { "objects": [ "Stationen", "Fahrräder", "Rückgabegebiet" ] } |
 /provider/mvg/area | GET | Liefert eine Fläche (z.B. Polygon) | { "objects": [ TODO ] } |

## History
 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|

# Technologie

## Frontend 

### Leaflet.js

### jQuery

## Backend

### Python + Flask

## MySQL


