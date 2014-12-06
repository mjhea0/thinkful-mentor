from models import Wheel, Frame, Bicycle, Manufacturer, BikeShop, Customer

# Raw materials
w1 = Wheel(weight=1050, cost=50, name="Vuelta 37mm")
w2 = Wheel(weight=900, cost=100, name="Vuelta Corsa Lite")
w3 = Wheel(weight=850, cost=150, name="Reynolds Eighty One")

f1 = Frame(material="steel", weight=8000, cost=100)
f2 = Frame(material="aluminum", weight=6000, cost=200)
f3 = Frame(material="carbon", weight=5000, cost=300)

# Manufacturers
m1 = Manufacturer(20, "Trek")
m2 = Manufacturer(15, "Navarro")

m1.add_inventory(w1, f1, "transportation")
m1.add_inventory(w2, f1, "transportation+")
m1.add_inventory(w3, f1, "transportation super")

m2.add_inventory(w1, f2, "comp")
m2.add_inventory(w2, f2, "comp extra")
m2.add_inventory(w3, f3, "elite max")

# Shop
s1 = BikeShop(name="Sam's Bikes", margin=20)
s1.restock(m1.ship(3))
s1.restock(m2.ship(3))

s1.print_stock()

#Customer
c1 = Customer(name="Dave", budget=200)
c2 = Customer(name="Sally", budget=500)
c3 = Customer(name="Daisy", budget=1000)

s1.print_filtered_stock(c1)
s1.print_filtered_stock(c2)
s1.print_filtered_stock(c3)

s1.sell(0)

print "{} total sales are {}".format(s1.name, s1.total_sales())