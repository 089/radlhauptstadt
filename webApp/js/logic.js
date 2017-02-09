// overlay layer erzeugen
// Beim hinzufügen eines Layers muss folgendes beachtet werden.
// - Es muss eine LayerGroup hinzugefügt werden.
// - overlayLayerControl muss um eine Zeile ergänzt werden.
// - Bei der Erzeugung der Karte muss der neue Layer übergeben werden.
// - In addMarker muss ein neuer Pfad hinzugefügt werden.
// - In layer2String muss ein neues Mapping des internen provider-Kürzels
//   zu einem lesbaren String hinzugefügt werden.
MVG_BICYCLE = "mvg";
var mvgBicycleLayer = new L.LayerGroup();
DB_BICYCLE = "dbrad";
var dbBicycleLayer = new L.LayerGroup();
DB_BICYCLE_RETURN_AREA = "DB-Rad Rückgabegebiet";
var dbBicycleReturnAreaLayer = new L.LayerGroup();
MVV_BICYCLE_RETURN_AREA = "MVG-Rad Rückgabegebiet";
var mvgBicycleReturnAreaLayer = new L.LayerGroup();
CAR_2_GO = "car2go";
var car2goLayer = new L.LayerGroup();

var layer2String = {};
layer2String[MVG_BICYCLE] = "MVG-Rad";
layer2String[DB_BICYCLE] = "call a bike";
layer2String[DB_BICYCLE_RETURN_AREA] = "call a bike Rückgabegebiet";
layer2String[MVV_BICYCLE_RETURN_AREA] = "MVG-Rad Rückgabegebiet";
layer2String[CAR_2_GO] = "car2go";

var type2String = {};
type2String['bike'] = "Fahrrad";
type2String['pedelec'] = "Radl für Faule";
type2String['car'] = "Auto";

var overlayLayerControl = {
				[layer2String[MVG_BICYCLE]]: mvgBicycleLayer,
                [layer2String[DB_BICYCLE]]: dbBicycleLayer,
                [layer2String[CAR_2_GO]]: car2goLayer,
                [layer2String[MVV_BICYCLE_RETURN_AREA]]: mvgBicycleReturnAreaLayer,
                [layer2String[DB_BICYCLE_RETURN_AREA]]: dbBicycleReturnAreaLayer
	};

// create icons
var mvvBicycleIcon = L.icon({
	iconUrl: 'pics/bike-mvg.svg',

	iconSize:     [40, 80], // size of the icon
	iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
	popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});
var mvvStationAvailableIcon = L.icon({
    iconUrl: 'pics/station-a-mvg.svg',

    iconSize:     [40, 80], // size of the icon
    iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});
var mvvStationNotAvailableIcon = L.icon({
    iconUrl: 'pics/station-na-mvg.svg',

    iconSize:     [40, 80], // size of the icon
    iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});
var dbBicycleIcon = L.icon({
	iconUrl: 'pics/bike-dbrad.svg',

	iconSize:     [40, 80], // size of the icon
	iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
	popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});
var car2goIcon = L.icon({
    iconUrl: 'pics/car-car2go.svg',

    iconSize:     [40, 80], // size of the icon
    iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});

// erzeugt die Karte und die Layer-Auswahl
function create(){
	// baseLayer erzeugen
    var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
	{
		attribution: '&copy; '
		+ '<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '
		+ '| Inspired by and derived from &copy; <a href="https://thenounproject.com/term/landmark/842708/" target="_blank">Lluisa Iborra, Noun Project</a> (<a href="https://creativecommons.org/licenses/by/3.0/us/" target="_blank">CC-BY</a>)'
	});

	// Karte erzeugen
	map = L.map('map', {layers: [baseLayer, mvgBicycleLayer,
			dbBicycleLayer, dbBicycleReturnAreaLayer,
			mvgBicycleReturnAreaLayer, car2goLayer]})
		.setView([48.137220, 11.575496], 12);

	// layer control hinzufügen
	L.control.layers(null, overlayLayerControl).addTo(map);

	map.removeLayer(mvgBicycleReturnAreaLayer)
	map.removeLayer(dbBicycleReturnAreaLayer);
}

// Fügt einen Fahrzeug-Marker hinzu...
// Latitude und longitude entsprichen den Koordinaten.
// Als Provider wird eine der oben definierten Konstanten MVG_BICYCLE, DB_BICYCLE... übergeben.
// Als Typ wird das interne Typen-Kürzel übergeben.
// Als Provider das interne provider-Kürzel.
// Als number wird die Fahrzeugnummer (provider-Abhängig -> mehrdeutig) übergeben.
function addVehicleMarker(latitude, longitude, type, provider, number){
    var popupText = generateVehiclePopup(type, provider, number);
	switch(provider){
		case MVG_BICYCLE:
			L.marker([latitude, longitude], {icon: mvvBicycleIcon}).bindPopup(popupText).addTo(mvgBicycleLayer);
			break;
		case CAR_2_GO:
            L.marker([latitude, longitude], {icon: car2goIcon}).bindPopup(popupText).addTo(car2goLayer);
            break;
		default: //DB_BICYCLE
			L.marker([latitude, longitude], {icon: dbBicycleIcon}).bindPopup(popupText).addTo(dbBicycleLayer);
	}
}

function generateVehiclePopup(type, provider, number){
    var typeText = type2String[type];

    return'<b>Anbieter:</b> ' + layer2String[provider] + '<br>'
        + '<b>Fahrzeugnummer:</b> ' + number + '<br>'
        + '<b>Typ:</b> ' + typeText;
}

// Fügt einen Stations-Marker hinzu...
// Latitude und longitude entsprichen den Koordinaten.
// Als Provider wird eine der oben definierten Konstanten MVG_BICYCLE, DB_BICYCLE... übergeben.
// der popupText ist ein beliebiger String, der später im Popup eines Markers angezeigt wird.
function addStationMarker(latitude, longitude, provider, name, availableBikes){
    var popupText = generateStationPopup(provider, name, availableBikes);
    switch(provider){
        case MVG_BICYCLE:
            if(availableBikes > 0)
                L.marker([latitude, longitude], {icon: mvvStationAvailableIcon}).bindPopup(popupText).addTo(mvgBicycleLayer);
            else
                L.marker([latitude, longitude], {icon: mvvStationNotAvailableIcon}).bindPopup(popupText).addTo(mvgBicycleLayer);
            break;
        default: //DB_BICYCLE, CAR_2_GO
            // no stations existing
    }
}

function generateStationPopup(provider, name, availableBikes){

    return '<b>Anbieter:</b> ' + layer2String[provider] + '<br>'
        + '<b>Stationsname:</b> ' + name + '<br>'
        + '<b>verfügbare Räder:</b> ' + availableBikes;
}

// Fügt Polygone zum visualisieren von Kern-/Geschäfts- & Rückgabegebieten hinzu.
function addArea(){
	// Kerngebiet DB_BICYCLE
	L.polygon([
    [48.176255, 11.540561],
    [48.175969, 11.565495],
    [48.178008, 11.573080],
	[48.177550, 11.586513],
	[48.171883, 11.599860],
	[48.164184, 11.595955],
	[48.151759, 11.615481],
	[48.129294, 11.615314],
	[48.123564, 11.620737],
	[48.111522, 11.614576],
	[48.104675, 11.582381],
	[48.112110, 11.574116],
	[48.113255, 11.565532],
	[48.110050, 11.521742],
	[48.111388, 11.517717],
	[48.120556, 11.518207],
	[48.127364, 11.523267],
	[48.133652, 11.533583]
	]).setStyle({fillColor: '#cc0605', color: '#990403'})
	.addTo(dbBicycleReturnAreaLayer);

	// Rückgabegebiet MVV_BICYCLE
	L.polygon([
    [48.094229, 11.587050],
    [48.083493, 11.553522],

	[48.067462, 11.544960],
    [48.078085, 11.540424],

	[48.088590, 11.545711],
    [48.101867, 11.500480],
    [48.194102, 11.505714],
    [48.186326, 11.541337],
    [48.183452, 11.630360],
    [48.175471, 11.624990],
    [48.167811, 11.661335],
    [48.125468, 11.652927],
    [48.087062, 11.617409]
	]).setStyle({fillColor: '#4562a2', color: '#4562a2'})
	.addTo(mvgBicycleReturnAreaLayer);
}

