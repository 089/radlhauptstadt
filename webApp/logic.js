// overlay layer erzeugen
// Beim hinzufügen eines Layers muss folgendes beachtet werden.
// - Es muss eine LayerGroup hinzugefügt werden.
// - overlayLayerControl muss um eine Zeile ergänzt werden. 
// - Bei der Erzeugung der Karte muss der neue Layer übergeben werden. 
// - In addMarker muss ein neuer Pfad hinzugefügt werden.
const MVG_BICYCLE = "MVG-Rad";
var mvgBicycleLayer = new L.LayerGroup();
const DB_BICYCLE = "DB-Rad"; 
var dbBicycleLayer = new L.LayerGroup();
const DB_BICYCLE_CORE_AREA = "DB-Rad Kerngebiet"
var dbBicycleCoreAreaLayer = new L.LayerGroup();

var overlayLayerControl = {
				MVG_BICYCLE: mvgBicycleLayer, 
				DB_BICYCLE: dbBicycleLayer,
				DB_BICYCLE_CORE_AREA: dbBicycleCoreAreaLayer
	};

// create icons
var blueIcon = L.icon({
	iconUrl: 'pics/bike.svg',

	iconSize:     [40, 80], // size of the icon
	iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
	popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});
var redIcon = L.icon({
	iconUrl: 'pics/bike-red.png',

	iconSize:     [40, 80], // size of the icon
	iconAnchor:   [20, 80], // point of the icon which will correspond to marker's location
	popupAnchor:  [0, -75] // point from which the popup should open relative to the iconAnchor
});

// erzeugt die Karte und die Layer-Auswahl
function create(){
	// baseLayer erzeugen
	var baseLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', 
	{
		attribution: '&copy; '
		+ '<a href="http://osm.org/copyright">OpenStreetMap</a> contributors '
		+ '&copy; <a href="https://thenounproject.com/">Lluisa Iborra, Noun Project</a>'
	});
	
	// Karte erzeugen
	map = L.map('map', {layers: [baseLayer, mvgBicycleLayer, 
			dbBicycleLayer, dbBicycleCoreAreaLayer]})
		.setView([48.137220, 11.575496], 12);

	// layer control hinzufügen
	L.control.layers(null, overlayLayerControl).addTo(map);
}

// Fügt einen Marker hinzu... 
// Latitude und longitude entsprichen den Koordinaten.
// Als Provider wird eine der oben definierten Konstanten MVG_BICYCLE, DB_BICYCLE... übergeben.
// der popupText ist ein beliebiger String, der später im Popup eines Markers angezeigt wird.
function addMarker(latitude, longitude, provider, popupText){
	var icon; 
	switch(provider){
		case MVG_BICYCLE:
			L.marker([latitude, longitude], {icon: blueIcon}).bindPopup(popupText).addTo(mvgBicycleLayer);
			break;
		default: //DB_BICYCLE
			L.marker([latitude, longitude], {icon: redIcon}).bindPopup(popupText).addTo(dbBicycleLayer);
	}
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
	.addTo(dbBicycleCoreAreaLayer);
}