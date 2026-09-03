# 1.1
print("1.1")
# Beginner
print("Beginner")
my_info = {"name": "Logan", "age": 19, "major": "CyberSecurity"}

# Intermediate
print("Intermediate")

menu = {"Pizza": 5.50, "Garlic Bread": 3.30, "Breadsticks": 3.50, "Wings": 4.50}

course_credits = {"CS1350": 3, "CS 1500": 3, "CS 2500": 3, "CS 3800": 3}

# Advanced
print("Advanced")

weekly_temps = dict(Monday=70, Tuesday=70, Wednesday=70, Thursday=70, Friday=70, Saturday=70, Sunday=80)

# 1.2
print("1.2")

# Beginner
print("Beginner")


pet = {"name": "Buddy", "type": "dog", "age": 3}

print(f"Pets name is {pet.get('name', 'unknown')}, pets age {pet.get('age', 'unknown')}")

# Intermediate
print("Intermediate")

pet.get('color', 'unknown')

grades = dict(Bob = 90, Dylan = 50, John = 60)

def is_passed(student_name):
    student_grade = grades.get(student_name)
    if(student_grade != None):
        if(student_grade >= 70):
            print(f"{student_name} passed")
        else:
            print(f"{student_name} did not pass")
        return
    print("Student was not found")

is_passed("John")
is_passed("Bob")
is_passed("Dylan")
is_passed("Logan")

# Advanced
print("Advanced")

products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

def find_price(product_name):
    found_product = products.get(product_name)
    if(found_product == None):
        print("Product not available")
        return
    print(found_product)

find_price("laptop")
find_price("mouse")
find_price("keyboard")
find_price("watch")
find_price("desktop")

#1.3
print(1.3)

#Beginner
print("Beginner")

inventory = dict()
inventory["Apples"] = 10
inventory["Oranges"] = 20
inventory["Bananas"] = 30
inventory["Peaches"] = 40

#Intermediate
print("Intermediate")

scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41
print(scores.pop("Team A"))

#Advanced
print("Advanced")

empty_cart = {}

empty_cart["Pencils"] = 3.50
empty_cart["Pens"] = 3.52
empty_cart["Notebooks"] = 5.41

empty_cart["Notebooks"] = 5.99

print(empty_cart.pop("Pens"))
print(f"Pens were removed from the empty cart")

remaining_cart_items = ""
for remaining_cart_item in empty_cart.keys():
    remaining_cart_items += f"\n\t {remaining_cart_item}: {empty_cart.get(remaining_cart_item)}"

sum_of = 0
for empty_cart_value in empty_cart.values():
    sum_of += empty_cart_value

print(f"Final Cart storage:{remaining_cart_items} \n final price is {sum_of}")

#2.1

#Beginner
#Which of these are valid dictionary keys? Write "valid" or "invalid" and explain why:
#a) "student_name" # valid (reason: string and immutable)
#b) [1, 2, 3] # invalid (reason: list and mutable)
#c) 100 # valid (reason: int and mimmutable)
#d) ("x", "y") # valid (reason: tuple and immutable)
#e) {"a": 1} # invalid (reason: dictionary and mutable)
#f) frozenset({1,2}) # valid (reason: frozenset and immutable

#Intermediate
#locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}
#is trying to use a list as a key

#Will probably print 3, 4 then 2 because a dictionary can't have two identical keys leading to different values so it just changes the one that exists instead of a new one

data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))

print(f"hash('Logan') = {hash("logan")}")
print(f"hash(100) = {hash(100)}")

#Advanced

high_scores = {("Bob", "Tetris"): 3000, ("John", "Space Invaders"): 2000, ("Connor", "Tetris"): 10000}

print(high_scores.get(("Connor", "Tetris")))

import time

my_list = list(range(1000000))
my_dict = {i: i for i in range(1000000)}

start = time.time()
result = 999999 in my_list
list_time = time.time() - start

start = time.time()
result = 999999 in my_dict
dict_time = time.time() - start

print(f"List search: {list_time:.6f} seconds")
print(f"Dict search: {dict_time:.6f} seconds")
print(f"Dict is {list_time/dict_time:.0f}x faster!")

#2.2

#Beginner

temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(len(temps))

#Intermediate
print("Highest:", max(temps.values()))
print("Lowest:", min(temps.values()))

if "Friday" in temps:
    print("Friday is there")
else:
    print("Friday isnt there")

temps.setdefault("Thursday", 70)

days = temps.keys()
temps["Friday"] = 10
print(days)

#Advanced

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

total = sum(prices.values())
average = total / len(prices)
print(f"Total: {total}")
print(f"Average: {average}")

most = max(prices, key=prices.get)
least = min(prices, key=prices.get)
print(f"Most: most, {prices[most]}")
print(f"Least: least, {prices[least]}")

import sys
print("Keys:", sys.getsizeof(prices.keys()))
print("List Of Keys:", sys.getsizeof(list(prices.keys())))

prices.update({"headphones": 100, "desktop": 999, "external monitor": 229})
print(prices)

#2.3

#Beginner
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for a,b in colors.items():
    print(f"{a}, {b}")
#[[apple, red][banana, yellow][grape, purple]]

#Intermediate
prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

for a,b in prices.items():
    print(f"{a}: ${b} + tax = ${b*1.07:.2f}")

count = 0
for a in prices.values():
    if a > 4: count += 1
print (count)

x,y = 10,20
x,y=y,x
a,*b,c = [1,2,3,4,5]
print(a)
print(*b)
print(c)

#Advanced

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
name, highest_score = max(scores.items(), key=lambda x: x[1])

passed, failed = {},{}
for a,b in scores.items():
    if b >=70:
        passed[a]=b
    else:
        failed[a]=b
average = sum(scores.values()) / len(scores)
deviation = {}
for a,b in scores.items():
    deviation[a] = b - average

big_dict = {i: i for i in range(50000)}
start = time.time()
for k, v in big_dict.items():
    _ = k + v
items_time = time.time() - start

start = time.time()
for k in big_dict.keys():
    v = big_dict[k]
    _ = k + v
keys_time = time.time() - start
