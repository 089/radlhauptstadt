# Schnittstellenanalyse

## MVG-Rad

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
Leaflet ist der Gewinner eines Vergleichs dreier Java-Script Bibliotheken zum einbinden von Kartendiensten. Basis des Vergleichs waren folgende Kriterien:
* Unabhängigkeit vom Kartenanbieter.
* Management verschiedener Layer möglich.
* Benötigter Speicher.
* Einfache Handhabung.
* Vorbedingungen zur Nutzung.

Leaflet:
+
* Erzeugen und verwalten der Karte unabhängig vom Kartenanbieter.
* Management verschiedener Layer möglich.
* Geringer Speicherbedarf. (v1.0.3 -> 0.98MB)
* Einfache Handhabung. 
* Frei Zugänglich.

GoogleMaps:
+
* Management verschiedener Layer möglich.
* Management verschiedener Layer möglich.
* Einfache Handhabung. 
-
* Setzt API-Key voraus.
* Kartenanbieter nicht frei wählbar.
* Speicherbedarf ohne API-Key nicht ermittelbar.

OpenLayers:
+
* Erzeugen und verwalten der Karte unabhängig vom Kartenanbieter.
* Management verschiedener Layer möglich.
* Einfache Handhabung. 
-
* Höchster Speicherbedarf im Vergleich. (v3.20.1 -> 2.96MB)
* Frei Zugänglich.

### jQuery
Auswahlkriterien:
* Bibliothek ist JavaScript-kompitabel.
* Schlanke Möglichkeit zum Zugriff auf REST-Schnittstellen.

## Backend

### Python + Flask

## MySQL


