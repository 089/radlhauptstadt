# Schnittstellenanalyse

# Loader

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
