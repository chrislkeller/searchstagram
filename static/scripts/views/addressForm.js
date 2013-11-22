    /* operations for address submission form */
    App.Views.AddressForm = Backbone.View.extend({

        id: 'submission-form',

        tagName: 'form',

        className: 'form-inline',

        template: template('address-form-template'),

        initialize: function(){
            this.render();
        },

        events: {
            'click button#submit': 'submitData',
            'keyup :input': 'enterToSubmitForm'
        },

        submitData: function(){
            $('.progress').removeClass('hidden');
            $('#data-results').empty();
            var processData = new App.Views.ProcessData();
            processData.queryAPIForData();
        },

        enterToSubmitForm: function(e){
            var latitudeSearch = $('input[id="latitudeSearch"]').val();
            var longitudeSearch = $('input[id="longitudeSearch"]').val();

    		if(e.keyCode != 13) {
    		    return false;
    		} else if (e.keyCode === 13 && latitudeSearch === '' && longitudeSearch === '') {
    		    return false;
    		} else {
                this.submitData();
    		}
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        }
    });