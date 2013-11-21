    // view for an image
    App.Views.Result = Backbone.View.extend({

        tagName: 'div',

        className: 'result-instance col-xs-12 col-sm-6 col-md-4 col-lg-3',

        template: template('data-results-template'),

        render: function(){
            var addDisplayToggle = new App.Views.ProcessData();
            $('#display-toggle').html(addDisplayToggle.render().el);
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }

    });