'use strict';

describe('Controller: UpcomingCtrl', function () {

  // load the controller's module
  beforeEach(module('sichallengeApp'));

  var UpcomingCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    UpcomingCtrl = $controller('UpcomingCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(UpcomingCtrl.awesomeThings.length).toBe(3);
  });
});
