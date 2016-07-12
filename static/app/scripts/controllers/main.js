'use strict';

/**
 * @ngdoc function
 * @name sichallengeApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the sichallengeApp
 */
angular
    .module('sichallengeApp')
    .controller('MainCtrl', ['$filter', '$scope', '$resource', '$uibModal',
                function ($filter, $scope, $resource, $uibModal) {
    
    var Restaurants = $resource('/restaurants');
    var Reservation = $resource('/restaurant/:restaurantId/reservation', {restaurantId:'@id'});

    $scope.showReservationModal = function (restaurantId) {
        var restaurantObj = $filter('filter')($scope.restaurants, {id: restaurantId})[0];

        var modalInstance = $uibModal.open({
            animation: true,
            templateUrl: 'views/restaurantModal.html',
            controller: 'ReservationCtrl',
            resolve: {
                restaurant: function () {
                    return restaurantObj;
                }
            }
        });

        modalInstance.result.then(function () {
            // TODO Send reservation
        }, function () {
            console.log('Modal dismissed at: ' + new Date());
        });
    };

    var restaurantData = Restaurants.get(function () {
        $scope.restaurants = restaurantData.restaurants;
    });
}]);
