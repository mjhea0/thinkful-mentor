# Design a Bike Sharing Service

A new bike sharing service, called Denver Bike Share, allows individuals to check bikes out of stations and return them at other stations throughout Denver, CO.

Denver Bike Share is a service that consists of many Bikes.

* New Bikes should be able to be created and added to Denver Bike Share.
* Bikes should be able to be checked out of a station and returned to any other station.
* On a per-Bike basis, a trip counter should exist, which shows how many times a bike was checked out and returned. A checkout followed by a return counts as one trip. So a bike that was checked out, returned, and then checked out (but not yet returned), would show a trip counter of 1. When it’s returned, the trip counter would increment to 2.

To test your design, create Bike 1, Bike 2, and Bike 3. Then check out and return Bike 1 three times, Bike 2 two times. Check out but do not return Bike 3.

## Stations and Sponsors

Now that Denver Bike Share is a success, we want to expand.

We’ll be opening up multiple new bike share stations, which are places where bikes can be rented from. We also have a number of corporate sponsors who want to put their logos on stations.

* Improve Denver Bike Share to support Stations. Stations can hold up to either 3, 5, or 10 bikes.

    For your test case, use:
    * Station 1: 10
    * Station 2: 5
    * Station 3: 3
    * Station 4: 10

* Bikes should be able to be checked out of a station and returned to any other station with available capacity.

* Allow any number of sponsors to be assigned to stations.

    For example:
    * Station 1: Sponsor A and Sponsor B
    * Station 2: Sponsor B and Sponsor C
    * Station 3: Sponsor C
    * Station 4: Sponsor A, Sponsor C, and Sponsor D

* Allow new bikes to be randomly assigned to a “home” station.

    For example:
    * Station 1: 50% chance of a bike being assigned to this home station
    * Station 2: 20% chance of a bike being assigned to this home station
    * Station 3: 20% chance of a bike being assigned to this home station
    * Station 4: 10% chance of a bike being assigned to this home station

    Note that bikes can only have one home station and the odds must add up to 100% across all stations

* TODO: When a bike is assigned to a full station, try to assign it to another station. If all stations are full, display an error to the user.

* Write code to test your design.
