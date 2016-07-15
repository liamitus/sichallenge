# SI Challenge - reservation system

>The first task is to identify three things:
>  - The actors and their core properties
>  - Use cases
>  - Features

## Actors
* Customer
  - name
  - party
* Party
  - size
  - reservation
* Reservation
  - table
  - date
* Table
  - number
  - size
  - movable
  - restaurant
* Restaurant
  - name
* Employee
  - name
  - restaurant

---

## Use cases
###### Normal flow
1. Customer make a reservation.
2. Restaurant receives reservation and assigns table(s) based on party size.
3. Staff can check reservation and see table number when party arrives.
4. Staff marks table as occupied.
5. Party leaves and stadd marks table as free.

###### Party size adjustment
1. First two steps of normal flow.
2. Customer modifies the party size of the reservation.
3. New table is selected and old table is marked as available.

###### Cancellation
1. First two steps of normal flow.
2. Customer cancels reservation.
3. Table is marked as available.

---

## Features
* Restaurant can add tables of given size.
* Restaurant can remove tables of given size.
* Customer can make a reservation.
* Customer can modify the party size of a reservation.
* Customer can modify the time of the reservation.
* System will mark tables as reserved or available based on customer input.
* Staff can see upcoming reservations.
* Staff are notified at the time and date of each reservation.

---

> It's also useful to list any assumptions as we go.

## Assumptions
* Party will only be seated when whole party is present.
* Some tables can be joined, e.g., two four-person tables can be combined to seat six people.

---

> Our business goals should guide our choice of metrics.  
> As a restaurant owner, we'd care about breaking down where our profits are coming from and if people enjoy our restaurants.

> Ideally our payment system will be connected, so we can map profit earned to our system's actors.

> If we flag items as deleted instead of actually deleting them from the database, we can use the history for our metrics.

## Desired metrics
* Profit per restaurant/reservation/party/customer.
* Profit per day from reservations, to compare with total profit of the day.
* Profit per table.
* Who are the regular customers.
* Frequency of large parties by day of week/hour of day.

---

> At this point I considered the best languages and frameworks:

> Python, Go, and Node were up for consideration because of how rapidly new web services can be created.  
> Other candidates include Ruby on Rails (too little experience), Java (slow development time, even with Spring's Roo for scaffolding), and PHP ("object enabled" but not object oriented).

> Python won in the end because it is the most mature and gave me a good excuse to learn and practice Django.  
> Plus Django offers a nice database aggregation API, which can be used to produce our desired metrics.

> Django comes with sqlite out of the box, which was kept for development.
> Postgres was the natural choice for the production database because of maturity, features, and it's supported out-of-the-box by both Django and AWS.

> Angular1.x was chosen for the front end because it the current industry standard. Also considered were Aurelia (smaller community and ecosystem), React (no experience), vanilla/jquery (more boilerplate to write).

> AWS was chosen for the infrastructure because it is the industry leader and because of familiarity.

## Stack
* Python3.4/Django1.9
* Angularjs1.4
* PostgreSQL9.5
* AWS - Elastic Beanstalk & Route53
* Yeoman for frontend scaffolding

---

## API
This is the current API:

| URL  | Method | Action |
| ------------- | ------------- | ------------- |
| /restaurants  | GET  | Retrieve all of our restaurants  |
| /restaurant/\<restaurant_id\>/reservation  | POST  | Make a reservation at the given restaurant  |

The proposed API can be found here: https://docs.google.com/spreadsheets/d/1BxGyZILXILwwORCvFmUcaDpXPjuaoK6swiA7SBmrDu4/edit?usp=sharing

## Deployment
- AWS Elastic Beanstalk makes setting up and tearing down the entire infrastructure quick and painless (I found this guide to be the most helpful: https://realpython.com/blog/python/deploying-a-django-app-to-aws-elastic-beanstalk/).
- The domain name was registered through Route53 and pointed to the Elastic Beanstalk endpoint.

---

## Things I would add but didn't because of time and/or priority:
 - Full test coverage.
 - Sockets for live updates of upcoming reservations.
 - Nicer URLs.
 - Authentication.
 - Modifying existing reservations as a customer.
 - Marking reservations as complete or cancelled as an employee.
 - Add open/close times to Restaurant and generate reservation time buttons (currently hardcoded).
 - Hide or disable reservation time buttons that aren't available.
 - Frontend unit tests
 - E2E tests
