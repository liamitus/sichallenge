'use strict';

/**
 * @ngdoc service
 * @name sichallengeApp.reservationService
 * @description
 * # reservationService
 * Service in the sichallengeApp that handles server requests for reservations.
 */
angular
    .module('sichallengeApp')
    .service('reservationService', ['$resource', function Reservation($resource) {
    // AngularJS will instantiate a singleton by calling "new" on this function

    var resourceUrl = '/restaurant/:restaurantId/reservation';
    var Reservation = $resource(resourceUrl, {restaurantId:'@restaurantId'});
    
    return { // Exports
        create: function (reservation) {
            return Reservation.save(reservation).$promise;
        }
    }
    
}]);
