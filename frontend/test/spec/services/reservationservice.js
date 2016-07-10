'use strict';

describe('Service: reservationService', function () {

  // load the service's module
  beforeEach(module('sichallengeApp'));

  // instantiate service
  var reservationService;
  beforeEach(inject(function (_reservationService_) {
    reservationService = _reservationService_;
  }));

  it('should do something', function () {
    expect(!!reservationService).toBe(true);
  });

});
