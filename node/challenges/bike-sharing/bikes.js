// constructors

function Bike(num, station, trips, isCheckedOut) {
  this.num = num;
  this.station = station;
  this.trips = trips || 0;
  this.isCheckedOut = isCheckedOut || false;
}

function Station(num, capacity, homePercent) {
  this.num = num;
  this.capacity = capacity;
  this.homePercent = homePercent;
  this.bikes = [];
  this.sponsors = [];
}

function Sponsor(name) {
  this.name = name;
}

function BikeProgram() {
  this.bikes = [];
  this.stations = [];
}


// methods

Bike.prototype.getInfo = function() {
  console.log(`Bike #${this.num}:`);
  console.log(`  -Has had ${this.trips} trip(s)`);
  if (this.isCheckedOut) {
    console.log(`  -Is checked out`);
  } else {
    console.log(`  -Is NOT checked out`);
    console.log(`  -Is in station ${this.station}`);
  }
};

Station.prototype.getInfo = function() {
  console.log(`\nStation #${this.num} has a capacity of ${this.capacity}.`);
  if(!this.bikes.length) {
    console.log('There are no bikes in the station!');
  } else {
    console.log(`There are ${this.bikes.length} bike(s) in the station!`);
    this.bikes.forEach((bike) => {
      bike.getInfo();
    })
  }
  if(!this.sponsors.length) {
    console.log('There are no sponsors for this station!');
  } else {
    console.log(`There are ${this.sponsors.length} sponsors for this station!`);
    this.sponsors.forEach((sponsor) => {
      sponsor.getInfo();
    })
  }
  console.log(`The odds of a bike being randomly assigned here is ${this.homePercent * 100}%.`);
};

Station.prototype.addBike = function(bike) {
  this.bikes.push(bike);
};

Station.prototype.removeBike = function(bikeNum) {
  this.bikes = this.bikes.filter((bike) => {
    return bike.num !== bikeNum;
  });
};

Station.prototype.addSponsor = function(sponsor) {
  this.sponsors.push(sponsor);
};

Sponsor.prototype.getInfo = function() {
  console.log(`Sponsor ${this.name}`);
}

BikeProgram.prototype.addBike = function(bike) {
  this.bikes.push(bike);
};

BikeProgram.prototype.addStation = function(station) {
  this.stations.push(station);
};

BikeProgram.prototype.getInfo = function() {
  if (!this.stations.length) {
    console.log('There are no stations in the program!');
  } else {
    console.log(`There are ${this.stations.length} stations in the program!`);
    this.stations.forEach((station) => {
      station.getInfo()
    })
  }
}

BikeProgram.prototype.checkOutBike = function(num) {
  for (const bike of this.bikes) {
    if (bike.num === num) {
      bike.isCheckedOut = true;
      const station = this.getStation(bike.station);
      station.removeBike(bike.num);
      bike.station = null;
      return true;
    }
  }
  return false;
}

BikeProgram.prototype.returnBike = function(bikeNum, stationNum) {
  const station = this.getStation(stationNum);
  if (station) {

  }
  if (station && station.capacity > station.bikes.length) {
    for (const bike of this.bikes) {
      if (bike.num === bikeNum) {
        bike.isCheckedOut = false;
        bike.trips += 1;
        bike.station = stationNum;
        station.addBike(bike);
        return true;
      }
    }
  }
  return false;
}

BikeProgram.prototype.getStation = function(stationNum) {
  for (const station of this.stations) {
    if (station.num === stationNum) {
      return station;
    }
  }
  return false;
}

BikeProgram.prototype.getRandomStation = function() {
  const stationList = [];
  this.stations.forEach((station) => {
    const number = station.homePercent * 10;
    for (let i = 0; i < number; i++) stationList.push(station.num);
  });
  return stationList[Math.floor(Math.random() * stationList.length)];
}


// main

const denverBikeSHare = new BikeProgram();

const station1 = new Station(1, 10, .5);
const station2 = new Station(2, 5, .2);
const station3 = new Station(3, 3, .2);
const station4 = new Station(4, 10, .1);

const sponsorA = new Sponsor('A');
const sponsorB = new Sponsor('B');
const sponsorC = new Sponsor('C');
const sponsorD = new Sponsor('D');

denverBikeSHare.addStation(station1);
denverBikeSHare.addStation(station2);
denverBikeSHare.addStation(station3);
denverBikeSHare.addStation(station4);

for (let i = 1; i < 4; i++) {
  const stationNum =  denverBikeSHare.getRandomStation();
  const bike = new Bike(i, stationNum);
  denverBikeSHare.addBike(bike);
  const station = denverBikeSHare.getStation(stationNum);
  station.addBike(bike);
}

station1.addSponsor(sponsorA);
station1.addSponsor(sponsorB);
station2.addSponsor(sponsorB);
station2.addSponsor(sponsorC);
station3.addSponsor(sponsorC);
station4.addSponsor(sponsorA);
station4.addSponsor(sponsorC);
station4.addSponsor(sponsorD);

console.log('START\n');
denverBikeSHare.getInfo();

denverBikeSHare.checkOutBike(1);
denverBikeSHare.returnBike(1, 3);
denverBikeSHare.checkOutBike(1);
denverBikeSHare.returnBike(1, 3);
denverBikeSHare.checkOutBike(1);
denverBikeSHare.returnBike(1, 3);
denverBikeSHare.checkOutBike(2);
denverBikeSHare.returnBike(2, 3);
denverBikeSHare.checkOutBike(2);
denverBikeSHare.returnBike(2, 3);
denverBikeSHare.checkOutBike(4);
denverBikeSHare.returnBike(4, 3);
denverBikeSHare.checkOutBike(3);

console.log('\nFINISH\n');
denverBikeSHare.getInfo();
