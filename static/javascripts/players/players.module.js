(function () {
  'use strict';

  angular
    .module('django_1.players', [
      'django_1.players.controllers',
      'django_1.players.services'
    ]);

  angular
    .module('django_1.players.controllers', []);

  angular
    .module('django_1.players.services', ['ngCookies']);
})();