var previous = null;
var current = null;
var lat = document.getElementById('lat');
var long = document.getElementById('long');
var bat = document.getElementById('bat');

setInterval(function() {
    $.getJSON("data.json", function(json) {
        current = JSON.stringify(json);
        if (previous !== current) {
            lat.value = json.latitude;
            long.value = json.longitude;
            bat.value = json.charge + '%';
        }
        previous = current;
    });
}, 500);
