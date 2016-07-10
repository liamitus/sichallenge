'use strict';

/**
 * @ngdoc service
 * @name sichallengeApp.reservationService
 * @description
 * # reservationService
 * Service in the sichallengeApp.
 */
angular
    .module('sichallengeApp')
    .service('reservationService', Reservation);

Reservation.$inject = ['$resource'];
function Reservation($resource) {
    // AngularJS will instantiate a singleton by calling "new" on this function
    
    
}
