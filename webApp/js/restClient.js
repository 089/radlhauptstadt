/**
 * Created by rudi on 04.02.2017.
 */

$(document).ready(function() {
    $.ajax({
        dataType: "json",
        url: "https://www.martinzell.de/radlhauptstadt/api/v0.9/provider/mvg/vehicle"
    }).then(function(data) {
        console.log(data);
        $.each(data.vehicles, function () {
            addBicycleMarker(this.latitude, this.longitude, this.provider, generateBicyclePopup(this.number, this.type));
        });
    });
});
