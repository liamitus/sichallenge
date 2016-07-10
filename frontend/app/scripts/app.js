'use strict';

/**
 * @ngdoc overview
 * @name sichallengeApp
 * @description
 * # sichallengeApp
 *
 * Main module of the application.
 */
angular
  .module('sichallengeApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/start', {
        templateUrl: 'views/start.html',
        controller: 'StartCtrl',
        controllerAs: 'start'
      })
      .when('/upcoming', {
        templateUrl: 'views/upcoming.html',
        controller: 'UpcomingCtrl',
        controllerAs: 'upcoming'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
