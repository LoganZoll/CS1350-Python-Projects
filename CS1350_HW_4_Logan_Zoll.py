#3.1
#Beginner
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for name in inventory:
    print(name)

total = 0
for count in inventory.values():
    total += count
print(total)

for name, count in inventory.items():
    print(f"{name}: {count}")


#Intermediate
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
for name, price in sorted(prices.items()):
    print(f"{name}: {price}")

for name, price in sorted(prices.items(), key=lambda item: item[1]):
   print(f"{name}: {price}")

greatest = ""
for name, price in prices.items():
    if prices.get(greatest, 0) < price:
        greatest = name
print (f"{greatest}: {prices.get(greatest)}")


#Advanced
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

average = 0
length = 0
for temp in temps.values():
    average += temp
    length += 1
average /= length
print(average)

hot = ""
cold = ""

for day, temp in temps.items():
    if(temp >= temps.get(hot, temps[day])):
       hot = day
    if(temp <= temps.get(cold, temps[day])):
       cold = day

print(f"hottest: {hot}: {temps[hot]}, coldest: {cold}: {temps[cold]}")

count = 0
for temp in temps.values():
    if temp > average:
        count += 1

print (count)



#3.2
#Beginner
products = {
"laptop": {"price": 999, "stock": 15},
"phone": {"price": 699, "stock": 50}
}


print(products["laptop"]["price"])

for name, info in products.items():
    print(f"{name}: stock {info['stock']}")

#Intermediate

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

dictionary = {}
for country, capital in zip(countries, capitals):
    dictionary[country] = capital

products["tablet"] = {"price": 449, "stock": 30}

for name, info in list(products.items()):
    if info["stock"] < 20:
        del products[name]



#Advanced
company = {
"Engineering": {"Alice": 95000, "Bob": 85000},
"Marketing": {"Carol": 75000, "Dave": 70000}
}

for dept, staff in company.items():
    for name, salary in staff.items():
        print(f"{name}: {salary}")


average = 0
length = 0

for dept, staff in company.items():
    for salary in staff.values():
        average += salary
        length += 1
average /= length

print(f"Average: {average}")


highest = {"dept": "", "name": ""}

for dept, staff in company.items():
    for name, salary in staff.items():
        if salary > company.get(highest["dept"], {}).get(highest.get("name"), 0):
            highest["dept"] = dept
            highest["name"] = name

print(f"{highest['name']}: {company[highest['dept']][highest['name']]}")



#3.3
#Beginner
cubes = {x: x**3 for x in range(1,6)}
print(cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
cels = {day: round((f - 32) * 5/9) for day, f in temps.items()}

print(cels)

#intermediate
scores = {"Alice": 88, "Bob": 64, "Carol": 92, "Dave": 71, "Eve": 58}

passing = {name: score for name, score in scores.items() if score > 70}
print(passing)
letter_grades = {name: ("A" if score > 89 else "B" if score > 79 else "C") for name, score in passing.items()}

print(letter_grades)

student_ids = {"Alice": 101, "Bob": 102}
student_ids = {id: name for name, id in student_ids.items()}
print(student_ids)


#Advanced
sales = [
        ("North", "Alice", 5000), ("South", "Bob", 4500),
        ("North", "Carol", 6000), ("South", "Alice", 3500)
        ]
by_region = {}
for region, name, amount in sales:
    by_region[region] = by_region.get(region, 0) + amount
print(by_region)
by_salesperson = {}
for region, name, amount in sales:
    by_salesperson[name] = by_salesperson.get(name, 0) + amount
print(by_salesperson)
nested = {}
for region, name, amount in sales:
    if nested.get(region, -1) == -1:
        nested[region] = {}
    nested[region][name] = nested[region].get(name, 0) + amount
print(nested)

#Sets
#1.1
#Beginner
vowels = {"a", "e", "i", "o", "u"}
print(vowels)
nums = set([1,2,2,3,3,3,4,4,4,4])
print(len(nums))

#empty = {} will create a dictionary

#Intermediate
text = "mississippi"
uniq = set(text)
print(uniq)
print(len(uniq))

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
uniq_emails = set(emails)
print(uniq_emails)

#s = {[1, 2], [3, 4]} fails because lists are not hasable

#Advanced

import time
big_set = set(range(1000000))
big_list = list(range(1000000))
start = time.time()
999999 in big_set
start = time.time() - start
print(f"Time for set: {start:.6f}")
start = time.time()
999999 in big_list
start = time.time() - start
print(f"Time for list: {start:.6f}")


frozen = frozenset([1,2])
dict = {frozen: "a"}
print(dict[frozenset([1,2])])

edges = [(1,2), (2,3), (1,3), (3,4)]

nodes = set()
for x,y in edges:
    nodes.add(x)
    nodes.add(y)
print(nodes)




#Beginner
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print (a | b)
print(a & b)
print(a - b)

#Intermediate
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}
print(morning_shift & evening_shift & weekend_shift)
print(morning_shift | evening_shift | weekend_shift)
print(morning_shift - evening_shift - weekend_shift)
print(morning_shift ^ evening_shift ^ weekend_shift)

#Advanced
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition  = {"Alice", "Carol", "Eve"}
print(prereqs_met & has_space & paid_tuition)
print(prereqs_met - paid_tuition)
all = prereqs_met | has_space | paid_tuition
print(all - (prereqs_met & paid_tuition))





#Beginner
a = {1, 2, 3}
a.add(4)
a.remove(1)
print(a)

even_nums = {x for x in range(21) if x % 2 == 0}
print(even_nums)
a.discard(99)
try:
    a.remove(99)
except Exception:
    print("remove errored")


#Intermediate
nums = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
seen = set()
unique = []
for num in nums:
    if num not in seen:
        seen.add(num)
        unique.append(num)
print(unique)

sentence = "To be or not to be that is the question"
unique = {word for word in sentence.lower().split()}
print(unique)

expected = set(range(1, 11))
actual = {1,2,4,5,7,8,10}

print(expected-actual)


#Advanced
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in lst:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
    return duplicates
print(find_duplicates([1, 2, 2, 3, 3, 4]))

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}
print(alice & bob & carol)
print(alice - bob -carol)
print((alice - bob - carol) | (bob-alice-carol) | (carol-bob-alice))

def common_characters(a, b):
    return set(a) & set(b)
print(common_characters("hello", "world"))
