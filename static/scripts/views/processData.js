    App.Views.ProcessData = Backbone.View.extend({

        className: 'btn-group btn-group-justified',

        tagName: 'div',

        template: template('display-toggle-template'),

        initialize: function(){
            this.render();
        },

        queryAPIForData: function(){
            var radiusSearch = $('input[id="radiusSearch"]').val();
            var latitudeSearch = $('input[id="latitudeSearch"]').val();
            var longitudeSearch = $('input[id="longitudeSearch"]').val();
            var startDate = $('input[id="startDate"]').val();
            var startTime = $('input[id="startTime"]').val();
            var endDate = $('input[id="endDate"]').val();
            var endTime = $('input[id="endTime"]').val();
            var countSearch = $('input[id="countSearch"]').val();

            $.getJSON($SCRIPT_ROOT + '/search-query', {
                radius: radiusSearch,
                latitude: latitudeSearch,
                longitude: longitudeSearch,
                startdate: startDate,
                starttime: startTime,
                enddate: endDate,
                endtime: endTime,
                count: countSearch
            }, this.processData);
        },

        processData: function(data){
            $('#data-results').empty();

            $('.progress').addClass('hidden');

            // initialize new collection
            var resultsCollection = new App.Collections.Results();

            // add array of instagram images
            resultsCollection.add(data.result);

            // add array of tweets
            resultsCollection.add(data.tweets);

            // set the collection to a view
            var resultsView = new App.Views.Results({collection: resultsCollection});

            // add the view to the page
            $('#data-results').append(resultsView.render().el);

            // perform some gymnastics so the map is updated with results of second search
            if ($('#content-map-canvas').hasClass('initial')) {

                // create an instance of the model with a collection
                var map = new App.Models.Map({
                    markers: resultsCollection
                });

                // create an instance of the view
                var addMapView = new App.Views.MapView({model:map});

                // render the map
                addMapView.render(data);

                // remove designator so we can re-render the map
                $('#content-map-canvas').removeClass('initial');

            } else {

                $('#content-map-canvas').remove();

                $('<div/>', {
                    id: 'content-map-canvas',
                }).appendTo('#results-container');

                // create an instance of the model with a collection
                var map = new App.Models.Map({
                    markers: resultsCollection
                });

                // create an instance of the view
                var addMapView = new App.Views.MapView({model:map});

                // render the map
                addMapView.render(data);

            }
        },

        events: {
            'click a#list-view': 'listView',
            'click a#map-view': 'mapView',
            'click a#export-view': 'exportView'
        },

        listView: function(data){
            $('#data-results').removeClass('hidden');
            $('#content-map-canvas').addClass('hidden');
        },

        mapView: function(data){
            $('#data-results').addClass('hidden');
            $('#content-map-canvas').removeClass('hidden');
        },

        exportView: function(data){
            var countSearch = $('input[id="countSearch"]').val();

            $.getJSON($SCRIPT_ROOT + '/download-csv', {
                download: 'yes'
            }, this.promptDownload);

        },

        promptDownload: function(data){
            console.log('boom');
        },

        render: function(){
            $('#data-results-filter').removeClass('hidden');
            this.$el.html((this.template));
            return this;
        }
    });