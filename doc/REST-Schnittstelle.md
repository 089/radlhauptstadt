# Definition der REST-Schnittstelle

In der aktuellen Konfiguration lautet eine vollständige REST-Anfrage z.B. https://www.martinzell.de/radlhauptstadt**/rest/api/v0.9/provider/mvg/vehicle **

## Aktuelle Schnittstellen-Definition
 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|
 / | egal | Wurzel, keine Aktion | `{}` |
 /provider/{provider}/station | GET | Liefert alle Stationen, die zum Anbieter {provider} gehören (Position (lat/lng), Name, Nummer, verfügbare Räder). |  |
 /provider/{provider}/station/{id} | GET | Liefert das Rad mit der Nummer {id} | { "objects": [ TODO ] } |
 /provider/{provider}/vehicle | GET | Liefert alle Fahrzeuge des Anbieters {provider} (Pos., Fzg.nummer, ggf. Name) |  |
 /provider/{provider}/vehicle/{id} | GET | Liefert ein Fahrzeug des Anbieters {provider} |  |

## Noch nicht implementiert
 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|
 /provider | GET | Liefert alle Anbieter | { "providers": [ "MVG", "DB" ] } |
 /provider/mvg | GET | Liefert alle möglichen Objekte | { "objects": [ "Stationen", "Fahrräder", "Rückgabegebiet" ] } |
 /provider/mvg/area | GET | Liefert eine Fläche (z.B. Polygon) | { "objects": [ TODO ] } |

## History
 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|

