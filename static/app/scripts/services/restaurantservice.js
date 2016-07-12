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

    var Restaurants = $resource('/restaurants');
    var Reservation = $resource('/restaurant/:restaurantId/reservation', {restaurantId:'@id'});
    
    return {
        makeReservation: function (restaurantId) {
        }
    };
}]);
