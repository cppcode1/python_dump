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

    def name(self):
        """
        it will return a name of a car
        """
        pass

my_car = car(100)
his_car = car(200)

print(my_car.max_speed) # 100
print(his_car.max_speed) # 200
print(car.min_speed) # 0
print(f"my car is faster: {car.compare(my_car, his_car)}")

exit(0)

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