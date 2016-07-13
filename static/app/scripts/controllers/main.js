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
    .controller('MainCtrl', ['$filter', '$scope', '$uibModal', 'restaurantService',
                function ($filter, $scope, $uibModal, restaurantService) {
    
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

    restaurantService.getAll().then(function (data) {
        $scope.restaurants = data.restaurants;
    });

}]);
