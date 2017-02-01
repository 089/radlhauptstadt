# Definition der REST-Schnittstelle

 rel. URL | Methode | Beschreibung | JSON-Antwort |
------|------|------|------|
 / | egal | Wurzel, keine Aktion | `{}` |
 /provider | GET | Liefert alle Anbieter | { "providers": [ "MVG", "DB" ] } |
 /provider/mvg | GET | Liefert alle möglichen Objekte | { "objects": [ "Stationen", "Fahrräder", "Rückgabegebiet" ] } |
 /provider/mvg/station | GET | Liefert alle Stationen (Position (lat/lng), Name, Nummer, verfügbare Räder) | { "objects": [ TODO ] } |
 /provider/mvg/vehicle | GET | Liefert alle Fahrzeuge (Pos., Fzg.nummer, ggf. Name) | { "objects": [ TODO ] } |
 /provider/mvg/area | GET | Liefert eine Fläche (z.B. Polygon) | { "objects": [ TODO ] } |

// TODO - History
