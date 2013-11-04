(function(){
    window.App = {
        Models: {},
        Collections: {},
        Views: {},
        Router: {}
    };

    window.template = function(id){
        return _.template( $('#' + id).html());
    };

    /* operations for content header */
    App.Views.renderPage = Backbone.View.extend({

        tagName: 'span',

        template: template('content-header-template'),

        initialize: function(){
            this.render();
        },

        events: {
            'click a.addressSearch': 'addressSearch',
            'click a.findMe': 'findMe'
        },

        addressSearch: function(){
            var addSearchForm = new App.Views.addressForm();
            $('#submission-form').html(addSearchForm.render().el);
            $('input[id="addressSearch').geocomplete({
                details: 'form'
            });
        },

        findMe: function(){
            var addLocationForm = new App.Views.locationForm();
            $('#submission-form').html(addLocationForm.render().el);

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    $("input[id='latitudeSearch']").attr('value', position.coords.latitude);
                    $("input[id='longitudeSearch']").attr('value', position.coords.longitude);
                    $('button#submit').trigger('click');
                }, null);
            } else {
                alert('Sorry, we could not find your location.');
            }
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        },

    });

    /* operations for address submission form */
    App.Views.addressForm = Backbone.View.extend({

        id: 'submission-form',

        tagName: 'form',

        template: template('address-form-template'),

        initialize: function(){
            this.render();
        },

        events: {
            'click button#submit': 'submitData',
        },

        submitData: function(){
            $('.progress').removeClass('hidden');
            $('#data-results').empty();
            var processData = new App.Views.processData();
            processData.queryAPIForData();
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        }

    });

    /* operations for geolocation form */
    App.Views.locationForm = Backbone.View.extend({

        id: 'location-form',

        tagName: 'form',

        template: template('location-form-template'),

        initialize: function(){
            this.render();
        },

        events: {
            'click button#submit': 'submitData',
        },

        submitData: function(){
            $('.progress').removeClass('hidden');
            $('#data-results').empty();
            var processData = new App.Views.processData();
            processData.queryAPIForData();
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        }

    });

    // describes an image
    App.Models.Image = Backbone.Model.extend({
        defaults: {
            user: 'wwstromberg',
            user_full_name: 'William Stromberg',
            link: 'http://instagram.com/wwstromberg',
            image_source: 'http://distilleryimage1.s3.amazonaws.com/2b8fda2e44a911e39c8b22000a9f18f4_8.jpg',
            caption: 'Thats a scramble! Onion, peppers, zucchini, and sweet sausage. I love Sunday mornings.',
            latitude: 47.601146851,
            longitude: -122.334979731,
            time_date: 'test'
        }
    });

    // a list of images
    App.Collections.Images = Backbone.Collection.extend({
        model: App.Models.Image
    });

    // view for all images
    App.Views.Images = Backbone.View.extend({

        tagName: 'div',

        id: 'image-container',

        render: function(){
            this.collection.each(function(image){
                var imageView = new App.Views.Image({model: image});
                this.$el.append(imageView.render().el);
            }, this);
            return this;
        }

    });

    // view for an image
    App.Views.Image = Backbone.View.extend({

        tagName: 'div',

        className: 'image-result col-xs-12 col-sm-6 col-md-4 col-lg-3',

        template: template('data-results-template'),

        render: function(){
            var addDisplayToggle = new App.Views.processData();
            $('#display-toggle').html(addDisplayToggle.render().el);
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }

    });

    App.Views.processData = Backbone.View.extend({

        className: 'btn-group btn-group-justified',

        tagName: 'div',

        template: template('display-toggle-template'),

        initialize: function(){
            this.render();
        },

        queryAPIForData: function(){
            var latitudeSearch = $('input[id="latitudeSearch"]').val();
            var longitudeSearch = $('input[id="longitudeSearch"]').val();
            var countSearch = $('input[id="countSearch"]').val();
            $.getJSON($SCRIPT_ROOT + '/search-query', {
                latitude: latitudeSearch,
                longitude: longitudeSearch,
                count: countSearch
            }, this.processData);
        },

        processData: function(data){
            $('#data-results').empty();
            $('.progress').addClass('hidden');
            var listView = new App.Views.Images({collection: new App.Collections.Images(data.result)});
            $('#data-results').append(listView.render().el);
        },

        events: {
            'click a#list-view': 'listView',
            'click a#map-view': 'mapView'
        },

        listView: function(data){
            //$('#data-results').removeClass('hidden');
            //$('#content-map-canvas').addClass('hidden');
        },

        mapView: function(data){
            //$('#data-results').addClass('hidden');
            //$('#content-map-canvas').removeClass('hidden');
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        }
    });
    /* this is there the magic happens */





/*
    App.Models.Marker = Backbone.Model.extend({
        defaults: {
            id: null,
            position: new google.maps.LatLng(39.828116,-98.579392),
            map: null,
            icon: new google.maps.MarkerImage('/static/images/new-instagram-logo.png'),
            title: 'Instagram Photo',
            clickable: true
        }
    });

    App.Collections.Markers = Backbone.Collection.extend({
        model:App.Models.Marker
    });
*/

/*
    App.Views.initialMapView = Backbone.View.extend({

        id: 'content-map-canvas',

        mapOptions: {
            zoom: 4,
            center: new google.maps.LatLng(39.828116,-98.579392),
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            scrollwheel: false,
            draggable: true,
            mapTypeControl: false,
            navigationControl: true,
            streetViewControl: false,
            panControl: false,
            scaleControl: true,
            navigationControlOptions: {
                style: google.maps.NavigationControlStyle.LARGE,
                position: google.maps.ControlPosition.RIGHT_TOP
            }
        },

        render: function(){
            var map = new google.maps.Map(this.el, this.mapOptions);

            google.maps.event.addDomListener(map, 'idle', function() {
              center = map.getCenter();
            });

            google.maps.event.addDomListener(window, 'resize', function() {
              map.setCenter(new google.maps.LatLng(39.828116,-98.579392));
            });

            marker = new google.maps.Marker({
                id: null,
                position: new google.maps.LatLng(39.828116,-98.579392),
                map: map,
                icon: new google.maps.MarkerImage('/static/images/new-instagram-logo.png'),
                title: 'Instagram Photo',
                clickable: true
            });

            return this;

        }

    });
*/

/*
    App.Views.initialMapMarker = Backbone.View.extend({

        render: function(){

            var marker = new google.maps.Marker({
                id: null,
                position: new google.maps.LatLng(39.828116,-98.579392),
                map: map,
                icon: new google.maps.MarkerImage('/static/images/new-instagram-logo.png'),
                title: 'Instagram Photo',
                clickable: true
            });


            return marker;

        }

    });
*/

    var renderPage = new App.Views.renderPage();
    $('#content-header').append(renderPage.render().el);
})();