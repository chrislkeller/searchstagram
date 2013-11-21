    // view for all images
    App.Views.Results = Backbone.View.extend({

        tagName: 'div',

        id: 'result-container',

        className: 'row',

        render: function(){
            this.collection.each(function(image){
                var imageView = new App.Views.Result({model: image});
                this.$el.append(imageView.render().el);
            }, this);
            return this;
        }

    });