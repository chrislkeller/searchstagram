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

    $(function(){
        var renderPage = new App.Views.InitPage();
        $('#content-header').append(renderPage.render().el);
    });

})();