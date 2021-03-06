# a lambda function (anonimous functions)
def call_lambda(some_lambda):
    some_lambda(value=10)
call_lambda(lambda value: print(value))
exit(0)

# to call a function inside another functions
def f1(): print("inside f1()")
def f2(pointer_to_some_function):
    print(callable(pointer_to_some_function)) # True\
    if callable(pointer_to_some_function):
        pointer_to_some_function()

f2(f1)


# to loop for a range of numbers
for number in range(0, 10):
    print(number, end=", ")
print("", end="\n")


# filter(): to find elements that suit you
class car: 
    def __init__(self, name, price): self.name = name; self.price = price
    def __str__(self): return self.name

cars = [ car("audi", 100), car("nissan", 200), car("honda", 300)]
my_money = 100

def costs_no_more_than(car): 
    global my_money; return True if car.price <= my_money else False

found_cars = list(filter(costs_no_more_than, cars))
for car in found_cars: print(f"the car you can allow yourself is {car.name}")


# map(): perform the action on each element of the array
goods_list = []
goods_list.append("bread")
def sale(good, percent): return f"today {good} {percent} % cheaper"
goods_with_sale = list(map(sale, goods_list, "10" * 10))
print(goods_with_sale)

# a global valiable and how we can change it
global_variable = 1
def change_global_variable():
    global global_variable
    global_variable = 2

change_global_variable()
print(global_variable) // 2

# class fields, static method 
class car:
    """
    this is a description of the class car
    you can show it with help(car)
    """
    min_speed = None # a static field (common for all instances of the car class)
    def __init__(self, max_speed): # the constructor
        min_speed = 0 # the local variable in the constructor
        car.min_speed = min_speed # the static variable
        self.max_speed = max_speed # the usual field of the instance of the class

    @staticmethod
    def compare(one, two):
        # one-line if
        return "yes" if one.max_speed > two.max_speed else "no"

    def fit(self):
        """
        it will check of we can fin someone into your vehicale
        """
        pass

my_car = car(100)
his_car = car(200)

print(my_car.max_speed) # 100
print(his_car.max_speed) # 200
print(car.min_speed) # 0
print(f"my car is faster: {car.compare(my_car, his_car)}")

# inheritance
class bus(car): # add more parent classes to multiple inheritance
    def __init__(self, max_speed, seats):
        #car.__init__(self, max_speed) # way1: call the parent constuctor
        super().__init__(max_speed) # way2: call the parent constuctor
        self.seats = seats

    def fit(self, passengers):
        return "yes" if self.seats >= passengers else "no"

passenges = 30
some_bus = bus(80, 20) # call the car constructor
print(f"can I fit {passenges} passengers? = {some_bus.fit(passenges)}")
print(some_bus.max_speed)

# was it derived from?
print(isinstance(some_bus, car))


# unpack a list (an array)
message = []
message.append("operation code")
message.append("size")
message.append("data")

opcode, size, data = message
print(size)


# a dictionary is a key-value pairs
price_list = {
    "car": 80000,
    "laptop": 3000
}
car_price = price_list.get("car")
house_price = price_list.get("house", "not found")
print(f"car costs {car_price}")
print(f"house costs {house_price}")
# unpack keys and values
for good, price in price_list.items():
    print(f"{good} costs {price}")


# a loop for-item-in-items
for element in "elements":
    print(element)


# does a character exist in a string?
email = "name@host.xx"
it_exists = '@' in email
print(f"@ is {it_exists}") # True

# list type is a poiner until two variables points on one array
a = [1,2,3]
b = a
b[0] = 1000
print(a)

# if statement
is_valid = True
is_online = True
if is_valid and is_online:
    print("do something")
elif False:
    pass # do nothing
else:
    exit(0) # it ends the app

# one-line if
# valiable = <smth> if <condition> else <smth>
is_connected = None
is_online = True if is_connected != None else False
print(is_online)

# logical operators
print(f"not true is {not True}")
print(True and True)
print(True or False)
print(1 == 1)
print(1 != 2)
print(10 >= 5)
print(10 <= 20)