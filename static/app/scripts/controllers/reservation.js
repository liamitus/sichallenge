'use strict';

/**
 * @ngdoc function
 * @name sichallengeApp.controller:ReservationCtrl
 * @description
 * # ReservationCtrl
 * Controller of the sichallengeApp
 */
angular
    .module('sichallengeApp')
    .controller('ReservationCtrl', ['$resource', '$scope', '$uibModalInstance', 'restaurant',
                function ($resource, $scope, $uibModalInstance, restaurant) {

    var Reservation = $resource('/restaurant/:restaurantId/reservation', {restaurantId:'@id'});

    $scope.reservation = { date: new Date() };
    $scope.restaurant = restaurant;

    // These formats need adjusting but is not a priority for this POC.
    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[0];
    $scope.altInputFormats = ['M!/d!/yyyy'];

    $scope.datepicker = {
        opened: false
    };

    $scope.openDatepicker = function() {
        $scope.datepicker.opened = true;
    };

    $scope.makeReservation = function (time) {
        console.log('making reservation for ' + time);
        var reservation = $scope.reservation;
        reservation.date = reservation.date + ' ' + time;
        Reservation.save(reservation);
    };

}]);
