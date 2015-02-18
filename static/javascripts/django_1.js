(function() {
    
    angular
        .module('django_1', [
            'django_1.config',
            'django_1.routes',
            'django_1.players'
        ]);
    
    angular
        .module('django_1.routes', ['ngRoute']);
    
    angular
        .module('django_1.config, []');
    
})();
