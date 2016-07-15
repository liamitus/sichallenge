'use strict';

/**
 * @ngdoc function
 * @name sichallengeApp.controller:ReservationCtrl
 * @description
 * # ReservationCtrl
 * Controller of the sichallengeApp for the reservation form.
 *
 */
angular
    .module('sichallengeApp')
    .controller('ReservationCtrl', ['$filter', '$scope', '$uibModalInstance',
                'Notification', 'reservationService', 'restaurant',
                function ($filter, $scope, $uibModalInstance,
                          Notification, reservationService, restaurant) {

    $scope.reservation = { date: new Date() };
    $scope.restaurant = restaurant;

    // Date picker settings
    // These formats need adjusting but is not a priority for this POC.
    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy'];
    $scope.format = $scope.formats[0];
    $scope.altInputFormats = ['M!/d!/yyyy'];
    $scope.datepicker = {
        opened: false
    };

    $scope.openDatepicker = function() {
        $scope.datepicker.opened = true;
    };

    $scope.makeReservation = function (time) {
        // TODO Form validation
        var reservation = $scope.reservation;
        var datetimeString = combineDateAndTime(reservation.date, time);
        // TODO don't use the Date constructor to parse date.
        reservation.date = new Date(datetimeString);
        reservation.restaurantId = $scope.restaurant.id;

        reservationService.create(reservation).then(function () {
            $uibModalInstance.close();
            Notification.success('Reservation made for ' + reservation.size + 
                                 ' at ' + $scope.restaurant.name);
        }, function (reason) {
            Notification.error('Could not make reservation because ' + reason.data.error);
        });

    };

    // Helper(s)

    function combineDateAndTime(date, time) {
        return $filter('date')(date, 'yyyy-MM-dd') + 'T' + time;
    }

}]);
