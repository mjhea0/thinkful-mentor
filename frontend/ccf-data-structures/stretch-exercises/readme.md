# Ready for a a real challenge?

 - For each store, create two objects:
    * The first one will use the candy names as the keys and the value will be another object containing the sale price and the quantities sold.
    * The second object will use the dates as the main key and each value will be an object with key-value pairs of each candy name and the money made selling that candy.


 - Using the ideal data structure that you laid out before as a pattern, create functions to create new store data arrays from the existing data. This is called 'normalizing' the data - you are making it all consistent to ease future tasks.


 - Build onto the previous functions by combining the data from the four separate stores so that you have a single set of data. Make sure that you don't lose any details from the initial data.


 - After creating a function to combine the data, create two additional functions, `getInventoryCountSold()` and `getGrossProfit()` which respectively get the total numbers of items sold and the total dollars from sales. Each item can optionally take a type of candy to return the numbers about that candy. If there's no argument passed, it should return the total numbers for all candy types. For example, `getInventoryCountSold('Banana Bunches')` should return 12.