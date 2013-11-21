    // describes an image
    App.Models.Result = Backbone.Model.extend({
        defaults: {
            id: null,
            result_type: 'result_type',
            user: 'user',
            user_full_name: 'user_full_name',
            link: 'link',
            image_source: 'image_source',
            caption: 'caption',
            latitude: 47.601146851,
            longitude: -122.334979731,
            time_date: 'time_date'
        }
    });
