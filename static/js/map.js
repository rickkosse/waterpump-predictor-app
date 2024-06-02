document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([-6.369028, 34.888822], 6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
    }).addTo(map);

    function onMapClick(e) {
        var lat = e.latlng.lat;
        var lon = e.latlng.lng;

        $.ajax({
            url: '/predict',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ lat: lat, lon: lon }),
            success: function(response) {
                var probability = response.probability;
                L.popup()
                    .setLatLng(e.latlng)
                    .setContent("Probability that the pump will be functional: " + (probability * 100).toFixed(2) + "%")
                    .openOn(map);
            }
        });
    }

    map.on('click', onMapClick);
});
