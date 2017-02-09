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
Zuerst wollten wir die öffentlich dokumentierte [Schnittstelle](https://xml.dbcarsharing-buchung.de/hal2_cabserver/hal2_cabserver_2.php) per SOAP einbinden. Letztlich haben wir aber in einem ähnlichen 
Projekt namens [Pybikes](https://github.com/eskerda/pybikes) eine URL zu einer JSON Datei gefunden, die wir an unsere Bedürfnisse angepasst haben. 

# Loader

Die Loader sind dafür zuständig regelmäßig die Daten der Schnittstellen abzufragen und in die Datenbank zu schreiben.

Diese Loader sollen leicht um neue Implementierungen für verschiedene Anbieter erweiterbar sein. Daher gibt es für die
Loader eine abstrakte
Basisklasse [AbstractLoader.py](../server/loader/AbstractLoader.py).

Für jeden Anbieter wird diese abstrakte Klasse abgeleitet und ein spezifischer Loader wird implementiert.
Gemäß der Basisklasse hat jeder Loader Methoden um alle verfügbaren Fahrzeuge sowie alle Stationen zurückzugeben.

Um die Loader aufzurufen wird das [LoaderExecution.py](../server/loader/LoaderExecution.py) Skript gestartet.
In LoaderExecution wird die Datenbankverbindung aufgebaut und alle Loader werden hintereinander aufgerufen.
Die Ergebnisse werden in zwei Listen für alle Fahrzeuge und Stationen gesammelt und anschließend über 
[MysqlHandler.py](../server/loader/MysqlHandler.py) in die Datenbank geschrieben.

Um die Daten der Fahrzeuge und Stationen zu kapseln und überflüssige Informationen zu vermeiden werden die Daten von den Loadern
als Objekte der Klassen [Vehicle.py](../server/loader/Vehicle.py) bzw. [Sation.py](../server/loader/Station.py) zurückgegeben.

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

Für das Frontend brauchen wir ein Tool zur Kartendarstellung und eines für die REST-Abfragen. 

### Karten

Unsere Anforderungen lauten: 

* Unabhängigkeit vom Kartenanbieter.
* Management verschiedener Layer möglich.
* Benötigter Speicher.
* Einfache Handhabung.
* Vorbedingungen zur Nutzung.

Leaflet ist der Gewinner eines Vergleichs dreier Java-Script Bibliotheken zum einbinden von Kartendiensten. Basis des Vergleichs waren oben genannte Kriterien
  
#### Leaflet.js
* PRO
    * Erzeugen und verwalten der Karte unabhängig vom Kartenanbieter.
    * Management verschiedener Layer möglich.
    * Geringer Speicherbedarf. (v1.0.3 -> 0.98MB)
    * Einfache Handhabung. 
    * Frei Zugänglich.

#### GoogleMaps
* PRO
    * Management verschiedener Layer möglich.
    * Management verschiedener Layer möglich.
    * Einfache Handhabung. 
* CON
    * Setzt API-Key voraus.
    * Kartenanbieter nicht frei wählbar.
    * Speicherbedarf ohne API-Key nicht ermittelbar.

#### OpenLayers
* PRO
    * Erzeugen und verwalten der Karte unabhängig vom Kartenanbieter.
    * Management verschiedener Layer möglich.
    * Einfache Handhabung. 
* CON
    * Höchster Speicherbedarf im Vergleich. (v3.20.1 -> 2.96MB)
    * Frei Zugänglich.
  
### REST-Abfragen

Aus folgenden Gründne haben wir uns für jQuery entschieden:

 * Bibliothek ist JavaScript-kompitabel.
 * Schlanke Möglichkeit zum Zugriff auf REST-Schnittstellen.
 
## Backend

### Python + Flask
Die Entscheidung für Python fiel unter anderem wegen folgender Gründe:

1. Auseinandersetzung mit einer neuen Programmiersprache, mit der noch keiner von uns größere Projekte umgesetzt hat. 
1. Python war auf dem eingesetzten Server bereits vorhanden und kann einfach erweitert werden.
1. Python kann nicht nur zur objektorientierten Programmierung, sondern auch als Skriptsprache genutzt werden. 
1. Für Python gibt es gute und einfache REST-Frameworks wie das verwendete Flask. Damit lässt sich mit wenigen Zeilen Code bereits eine umfangreiche REST-Schnittstelle definieren (vgl. Beispiel unten).  


```Python
@app.route('/api/v0.9/provider/<provider>/vehicle', methods=['GET'])
def all_vehicles(provider):
    if provider == '':
        abort(400)

    cursor = g.mysql_db.cursor()

    cursor.callproc('all_vehicles', args=(provider, ))

    return mysqlToVehicle(cursor)
```

## MySQL
Aufgrund der - bei diesem [Angebot](https://uberspace.de/prices) gut hinnehmbaren - Einschränkungen auf dem Server fiel die Entscheidung schnell auf MySQL. Die Lösung ist derzeit auf MySQL ausgerichtet, könnte aber mit wenig Aufwand auf andere Datenbanken portiert werden. Aufgrund der zur Verfügung stehenden Zeit, haben wir hier bisher noch keine weitere Abstraktion vorgenommen. 