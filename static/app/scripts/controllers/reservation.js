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
    .controller('ReservationCtrl', ['$filter', '$resource', '$scope', '$uibModalInstance', 'restaurant',
                function ($filter, $resource, $scope, $uibModalInstance, restaurant) {

    var Reservation = $resource('/restaurant/:restaurantId/reservation', {restaurantId: restaurant.id});

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
        var reservation = $scope.reservation;
        var datetimeString = $filter('date')(reservation.date, 'yyyy-MM-dd') + 'T' + time;
        // TODO don't use the Date constructor to parse date.
        reservation.date = new Date(datetimeString);
        Reservation.save(reservation);
    };

}]);
