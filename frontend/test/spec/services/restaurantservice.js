'use strict';

describe('Service: restaurantService', function () {

    // load the service's module
    beforeEach(module('sichallengeApp'));

    // instantiate service
    var restaurantService;
    beforeEach(inject(function (_restaurantService_) {
        restaurantService = _restaurantService_;
    }));

    it('should not be undefined', function () {
        expect(!!restaurantService).toBe(true);
    });

    it('should have a method to retrieve all restaurants', function () {
        expect(!!restaurantService.getAll).toBe(true);
    });

});
