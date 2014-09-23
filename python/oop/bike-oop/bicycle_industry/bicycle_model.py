
class Wheel(object):	
	
	def __init__(self, wheel_name, wheel_weight, wheel_cost):
		self.wheel_name = wheel_name
		self.wheel_weight = wheel_weight
		self.wheel_cost = wheel_cost

	def __repr__ (self):
		return "wheel model name is {}, wheel weight is {}lbs per wheel, wheel manufacturing cost is ${}.00 per wheel".format(self.wheel_name, self.wheel_weight, self.wheel_cost)
	
	
class Frame(object):
	ALUMINIUM_TYPE = 1
	STEEL_TYPE = 2
	CARBON_TYPE = 3 

	def __init__(self, frame_weight, frame_cost, frame_code):
		self.frame_weight = frame_weight
		self.frame_cost = frame_cost
		if frame_code == Frame.ALUMINIUM_TYPE:
			self.material = "aluminium"
		elif frame_code == Frame.STEEL_TYPE:
			self.material = "steel"
		else:
			self.material = "carbon"		

	def __repr__(self):
		return "frame is made of {}, weight of the frame is {}lbs and manufacturing cost of the frame is ${}.00".format(self.material, self.frame_weight, self.frame_cost)

class Bicycle(object):
	
	def __init__(self, wheel_name, wheel_weight, wheel_cost, frame_weight, frame_cost, frame_code, bicycle_name, manufacturer, manufacturer_margin):
		self.wheel = Wheel(wheel_name, wheel_weight, wheel_cost)
		self.frame = Frame(frame_weight, frame_cost, frame_code)
		self.bicycle_name = bicycle_name
		self.manufacturer = manufacturer
		self.manufacturer_margin = manufacturer_margin

	def __repr__(self):
		return "{}, the manufacturer of this bicycle model is {}, {}, {}\n".format(self.bicycle_name, self.manufacturer, self.wheel, self.frame)

	def total_weight(self):		
		total_weight = (self.wheel.wheel_weight * 2) + self.frame.frame_weight
		return total_weight

	def total_cost(self):
		parts_cost = (self.wheel.wheel_cost * 2) + self.frame.frame_cost
		total_cost = parts_cost + (parts_cost * self.manufacturer_margin)
		return total_cost


class Manufacturer(object):

	models = []

	def __init__(self, manufacturer_name, manufacturer_margin, models):
		self.manufacturer_name = manufacturer_name		
		self.models = models
	
	def __repr__(self):
		return 'name of the manufacturer is {}, manufacturer margin is {}, the models it manufacturers are {}'.format(self.manufacturer_name, self.manufacturer_margin, self.models)
	
class BikeShop(object):

	inventory = []
	sold = []

	def __init__(self, bikeshop_name, retail_margin, inventory):
		self.bikeshop_name = bikeshop_name
		self.retail_margin = retail_margin
		self.inventory = inventory

	def __repr__(self):
		return 'name of the bike shop is {}, bike shop margin is {}, bike shop\'s inventory is {}'.format(self.bikeshop_name, self.retail_margin, self.inventory)
	
	def inventory_value(self):
		"""total cost of wholesale bike shop's inventory"""
		cost = 0
		for bike in self.inventory:
			cost = cost + bike.total_cost()
		return cost
	
	def sell_bike(self, i):
		"""add bike at inventory index i to sold list"""
		if i < len(self.inventory):
			self.sold.append(self.inventory[i])
		else:
			print "That bike is not in stock"
		
	def profit(self):
		"""profit from sold bikes"""
		retail_value = 0
		wholesale_value = 0
		for bike in self.sold:
			retail_value += bike.total_cost() + (self.retail_margin * bike.total_cost())
			wholesale_value += bike.total_cost() 
		return retail_value - wholesale_value

	def bikeweight(self):
		"""name, weight of each bike in the bikeshop inventory"""
		for bike in self.inventory:
			print "bicycle model name is {} and total weight is {}lbs\n".format(bike.bicycle_name, bike.total_weight())	
	
	def affordable_bikes(self, customer):		
		"""lists bikes the customer can afford within their budget, customer purchases most expensive within budget"""
		affordable_bikes = []				
		for bike in self.inventory:
			price = bike.total_cost() + (self.retail_margin * bike.total_cost())
			if customer.fund >= price:
				paid = price
				customer_fund_balance = customer.fund - paid				
				affordable_bikes.append(bike)
				purchase = affordable_bikes[-1]		
				print "{} can afford {} for ${}".format(customer.customer_name, bike.bicycle_name, paid)				
		self.sold.append(purchase)		
		return "{} buys {} for ${} and her fund balance is ${}\n".format(customer.customer_name, purchase, paid, customer_fund_balance)

	def remaining_inventory(self):
		"""remove sold bikes from bikeshop inventory"""
		for bike in self.sold:
			if bike in self.inventory:
				self.inventory.remove(bike)
		print "{}'s remaining inventory is: {}".format(self.bikeshop_name, self.inventory)

class Customer(object):
	
	def __init__(self, customer_name, fund):
		self.customer_name = customer_name
		self.fund = fund

	def __repr__(self):
		return "name of the customer is {}, customer\'s bike fund is ${}".format(self.customer_name, self.fund)










