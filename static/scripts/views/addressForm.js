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
        },

        submitData: function(){
            $('.progress').removeClass('hidden');
            $('#data-results').empty();
            var processData = new App.Views.ProcessData();
            processData.queryAPIForData();
        },

        render: function(){
            this.$el.html((this.template));
            return this;
        }
    });