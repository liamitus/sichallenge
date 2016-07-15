'use strict';

/**
 * @ngdoc function
 * @name sichallengeApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the sichallengeApp
 */
angular
    .module('sichallengeApp')
    .controller('HeaderCtrl', ['$location', '$scope', function ($location, $scope) {

    $scope.isActive = function (viewLocation) { 
        console.log($location.path());
        return viewLocation === $location.path();
    };
}]);
