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
exit(0)


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