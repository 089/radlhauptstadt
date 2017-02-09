$(document).ready(function() {

    // MVG-Rad
    $.ajax({
        dataType: "json",
        url: "https://www.martinzell.de/radlhauptstadt/rest/api/v0.9/provider/mvg/vehicle"
    }).then(function(data) {
        console.log(data);
        $.each(data.vehicles, function () {
            addVehicleMarker(this.latitude, this.longitude, this.provider, generateVehiclePopup(this.number, this.type));
        });
    });

    $.ajax({
        dataType: "json",
        url: "https://www.martinzell.de/radlhauptstadt/rest/api/v0.9/provider/mvg/station"
    }).then(function(data) {
        console.log(data);
        $.each(data.stations, function () {
            addStationMarker(this.latitude, this.longitude, this.provider, this.availableBikes > 0, generateStationPopup(this.name, this.availableBikes));
        });
    });

    // DB-Rad
    $.ajax({
        dataType: "json",
        url: "https://www.martinzell.de/radlhauptstadt/rest/api/v0.9/provider/dbrad/vehicle"
    }).then(function(data) {
        console.log(data);
        $.each(data.vehicles, function () {
            addVehicleMarker(this.latitude, this.longitude, this.provider, generateVehiclePopup(this.number, this.type));
        });
    });

    // car2go
    $.ajax({
        dataType: "json",
        url: "https://www.martinzell.de/radlhauptstadt/rest/api/v0.9/provider/car2go/vehicle"
    }).then(function(data) {
        console.log(data);
        $.each(data.vehicles, function () {
            addVehicleMarker(this.latitude, this.longitude, this.provider, generateVehiclePopup(this.number, this.type));
        });
    });
});
