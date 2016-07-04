# SI Challenge - restaurant reservation system
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

## Features
* Restaurant can add tables of given size.
* Restaurant can remove tables of given size.
* Customer can make a reservation.
* Customer can modify the party size of a reservation.
* Customer can modify the time of the reservation.
* System will mark tables as reserved or available based on customer input.
* Staff can see upcoming reservations.
* Staff are notified at the time and date of each reservation.

## Assumptions
* Party will only be seated when whole party is present.
* Some tables can be joined, e.g., two four-person tables can be combined to seat six people.

## Desired metrics
* Profit per reservation/party/customer/table by different time periods.
* Who are the regular customers.
* Frequency of large parties by different time periods.

