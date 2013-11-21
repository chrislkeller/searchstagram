    App.Views.MapView = Backbone.View.extend({
        id: '#content-map-canvas',

        render: function(data) {

            var map = this.map = L.map('content-map-canvas', {
                scrollWheelZoom: false,
                zoomControl: true
            });

            var center = new L.LatLng(data.geolatitude, data.geolongitude);

            map.setView(center, data.zoom);

            L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png', {
                attribution: 'Tiles, data, imagery and map information provided by <a href="http://www.mapquest.com" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png">, <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and OpenStreetMap contributors.',
                subdomains: ['otile1','otile2','otile3','otile4']
            }).addTo(map);

            // render each of the markers
            this.markerViews = this.model.get('markers').map(function(marker) {
                return new App.Views.MarkerView({model:marker, map:map}).render();
            });
        },
    });