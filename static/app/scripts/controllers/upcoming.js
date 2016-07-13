'use strict';

/**
 * @ngdoc function
 * @name sichallengeApp.controller:UpcomingCtrl
 * @description
 * # UpcomingCtrl
 * Controller of the sichallengeApp
 */
angular
    .module('sichallengeApp')
    .controller('UpcomingCtrl', ['$scope', 'restaurantService',
            function ($scope, restaurantService) {

    restaurantService.getAll().then(function (data) {
        $scope.restaurants = data.restaurants;
    });

}]);
