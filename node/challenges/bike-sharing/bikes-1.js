class BikeShareProgram {

  constructor(num, capacity) {
    this.bikes = [];
    this.stations = [
      {
        num: 1,
        current: 0,
        capacity: 10,
        sponsors: [],
      },
      {
        num: 2,
        current: 0,
        capacity: 5,
        sponsors: [],
      },
      {
        num: 3,
        current: 0,
        capacity: 3,
        sponsors: [],
      },
      {
        num: 4,
        current: 0,
        capacity: 10,
        sponsors: [],
      },
    ]

  }

  getInfo() {
    console.log(this.bikes);
    console.log(this.stations);
  }

  createBike(num, station) {
    this.bikes.push({
      num: num,
      station: station,
      checkedOut: false,
      trips: 0
    })
    const stationInfo = this.getStation(station);
    stationInfo.current += 1;
  }

  checkOutBike(num) {
    (this.bikes).forEach((bike) => {
      if (bike.num === num) {
        bike.checkedOut = true;
        const stationInfo = this.getStation(bike.station);
        stationInfo.current -= 1;
      }
    })
  }

  returnBike(num, station) {
    const stationInfo = this.getStation(station);
    if (stationInfo && stationInfo.current < stationInfo.capacity) {
        stationInfo.current += 1;
        (this.bikes).forEach((bike) => {
          if (bike.num === num && bike.checkedOut) {
            bike.checkedOut = false;
            bike.trips += 1;
            bike.station = station;
          }
        })
    }
  }

  getStation(num) {
    return (this.stations).filter((station) => {
      return station.num === num
    })[0]
  }

  addSponsor(station, name) {
    const stationInfo = this.getStation(station);
    (stationInfo.sponsors).push(name);
  }

}

const newProgram = new BikeShareProgram();
console.log(newProgram);
newProgram.createBike(1, 1);
newProgram.createBike(2, 1);
newProgram.createBike(3, 1);
console.log(newProgram);
newProgram.checkOutBike(1);
newProgram.returnBike(1, 2);
newProgram.checkOutBike(1);
newProgram.returnBike(1, 2);
newProgram.checkOutBike(1);
newProgram.returnBike(1, 3);
newProgram.checkOutBike(2);
newProgram.returnBike(2, 2);
newProgram.checkOutBike(2);
newProgram.returnBike(2, 1);
newProgram.checkOutBike(3);
console.log(newProgram);
newProgram.addSponsor(1, 'A');
newProgram.addSponsor(1, 'B');
newProgram.addSponsor(2, 'B');
newProgram.addSponsor(2, 'C');
newProgram.addSponsor(3, 'C');
newProgram.addSponsor(4, 'A');
newProgram.addSponsor(4, 'C');
newProgram.addSponsor(4, 'D');
console.log(newProgram);

// * Allow any number of sponsors to be assigned to stations. For example:

// Station 1: Sponsor A and Sponsor B
// Station 2: Sponsor B and Sponsor C
// Station 3: Sponsor C
// Station 4: Sponsor A, Sponsor C, and Sponsor D

//  * Allow new bikes to be randomly assigned to a “home” station. For example:

// Station 1: 50% chance of a bike being assigned to this home station
// Station 2: 20% chance of a bike being assigned to this home station
// Station 3: 20% chance of a bike being assigned to this home station
// Station 4: 10% chance of a bike being assigned to this home station

// Note that bikes can only have one home station and the odds must add up to 100% across all stations

// * When a bike is assigned to a full station, try to assign it to another station. If all stations are full, display an error to the user.

// * Write code to test your design.
