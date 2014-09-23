
from bicycle_model import Bicycle, Wheel, Frame, Manufacturer, BikeShop, Customer

"""create 6 bicycle models"""
b1 = Bicycle('slick', 9, 14, 40, 30, 1, 'Champion', 'Eagle', 0.1)
b2 = Bicycle('medium', 6, 16, 30, 75, 2, 'Tour', 'Eagle', 0.1)
b3 = Bicycle('medium', 6, 16, 15, 300, 3, 'Speedy', 'Eagle', 0.1)

b4 = Bicycle('slick', 9, 14, 40, 30, 1, 'RoadRage', 'Seagull', 0.2)
b5 = Bicycle('slick', 9, 14, 15, 300, 3, 'MonsterHill', 'Seagull', 0.2)
b6 = Bicycle('hard', 3, 125, 15, 300, 3, 'Giro', 'Seagull', 0.2)

"""create 2 manufacturers"""
manufacturer_one = Manufacturer('Eagle', 0.1, [b1, b2, b3])
manufacturer_two = Manufacturer('Seagull', 0.2, [b4, b5, b6])

"""create 1 bike shop"""
bikeshop_one = BikeShop('East Village Shop', 0.2, [b1, b2, b2, b3, b3, b4, b4, b5, b5, b6])

"""create 3 customers"""
customer_one = Customer('Sarah', 200)
customer_two = Customer('Ella', 500)
customer_three = Customer('Hannah', 1000)

customers = [customer_one, customer_two, customer_three]

"""print out name and total weight of each bicycle model carried by the bike shop"""
bikeshop_one.bikeweight() 

"""print out a list of bikes that the customers can afford given their budget, customer purchases one and prints out their fund balance"""
for c in customers:
	print bikeshop_one.affordable_bikes(c)

"""print out bikeshop's initial inventory"""
print "{}'s initial inventory is: {}\n".format(bikeshop_one.bikeshop_name, bikeshop_one.inventory)

"""prints out bikeshop's remaining inventory"""
bikeshop_one.remaining_inventory()

"""bikes shop calculates profit made on sold bikes"""
print "{}'s profit from the sale of the three bikes is ${}\n".format(bikeshop_one.bikeshop_name, bikeshop_one.profit())


















