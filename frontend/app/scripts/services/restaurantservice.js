'use strict';

/**
 * @ngdoc service
 * @name sichallengeApp.restaurantService
 * @description
 * # restaurantService
 * Service in the sichallengeApp.
 */
angular
    .module('sichallengeApp')
    .service('restaurantService', ['$resource', function ($resource) {
    // AngularJS will instantiate a singleton by calling "new" on this function

    var Restaurant = $resource('/restaurants');

    // Exports
    return {
        getAll: function() {
            return Restaurant.query();
        }
    };

}]);
