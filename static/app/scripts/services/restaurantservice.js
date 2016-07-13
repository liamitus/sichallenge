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

    // Restaurants aren't likely to change often so let's cache it.
    var Restaurants = $resource('/restaurants', { cache: true });
    var Reservation = $resource('/restaurant/:restaurantId/reservation',
                                {restaurantId:'@id'});
    
    return { // Exports

        getAll: function () {
            return Restaurants.get().$promise;
        }

    };

}]);
