var Storage = function() {
  this.items = [];
  this.id = 0;
};

Storage.prototype.add = function(name) {
  var item = {
    name: name,
    id: this.id
  };
  this.items.push(item);
  this.id += 1;
  return item;
};

Storage.prototype.remove = function(id) {
  var item = this.items.splice(id, 1);
  return item[0];
};

Storage.prototype.put = function(id, name) {
  for (var i = 0; i < this.items.length; i++) {
    if (this.items[i].id == id) {
      this.items[i].name = name;
      return this.items[i];
    }
  }
};


module.exports = Storage;