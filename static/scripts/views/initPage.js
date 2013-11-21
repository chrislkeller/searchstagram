    /* operations for content header */
    App.Views.InitPage = Backbone.View.extend({

        tagName: 'span',

        template: template('content-header-template'),

        initialize: function(){
            this.render();
        },

        events: {
            'click a.addressSearch': 'addressSearch',
            'click a.findMe': 'findMe',
            'click a.clickMap': 'clickMap'
        },

        addressSearch: function(){
            var addSearchForm = new App.Views.AddressForm();
            $('#form').html(addSearchForm.render().el);
            $('#submission-form').attr('role', 'form');
            this.completeDateValues();
            $('input[id="addressSearch').geocomplete({
                details: 'form'
            });
        },

        findMe: function(){
            var addLocationForm = new App.Views.LocationForm();
            $('#form').html(addLocationForm.render().el);
            this.completeDateValues();
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

        /*
        clickMap: function(){

            console.log('works');

            // create an instance of the model with a collection
            var map = new App.Models.Map({});

            // create an instance of the map
            var clickMapView = new App.Views.MapView({model:map});

            // this should be moved to the map model defaults?
            var initialMapData = {
                zoom: 4,
                geolatitude: 39.828116,
                geolongitude: -98.579392
            };

            // render the map
            clickMapView.render(initialMapData);

            // remove designator so we can re-render the map
            $('#content-map-canvas').removeClass('initial');
        },
        */

        completeDateValues: function(){
            var todayDate = new Date();
            var year = todayDate.getFullYear();
            var month = todayDate.getMonth()+1;
            var today = todayDate.getDate();
            var yesterday = todayDate.getDate()-1;
            var startDateValue = year + '-' + month + '-' + yesterday;
            var endDateValue = year + '-' + month + '-' + today;
            $("input[id='startDate']").attr('value', startDateValue);
            $("input[id='endDate']").attr('value', endDateValue);
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        },

    });