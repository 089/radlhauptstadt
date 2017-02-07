$(document).ready(function() {
    $.ajax({
        dataType: "json",
        url: "https://www.martinzell.de/radlhauptstadt/rest/api/v0.9/provider/mvg/vehicle"
    }).then(function(data) {
        console.log(data);
        $.each(data.vehicles, function () {
            addBicycleMarker(this.latitude, this.longitude, this.provider, generateBicyclePopup(this.number, this.type));
        });
    });
});
