# Schnittstellenanalyse

## MVG-Rad

## DB-Rad

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


