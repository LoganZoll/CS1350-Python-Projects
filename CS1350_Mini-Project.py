# Contact records: name -> dictionary of details
contact_book = {
"Mom": {"phone": "555-1234", "category": "Family", "city": "FortWayne"},
"Dad": {"phone": "555-4321", "category": "Family", "city": "FortWayne"},
"Sister": {"phone": "555-7777", "category": "Family", "city":"Chicago"},
"Best Friend": {"phone": "555-8888", "category": "Friend", "city":"Indianapolis"},
"Roommate": {"phone": "555-3141", "category": "Friend", "city": "FortWayne"},
"Boss": {"phone": "555-0000", "category": "Work", "city":"Chicago"},
"Professor": {"phone": "555-2718", "category": "Work", "city": "FortWayne"},
"Dentist": {"phone": "555-2222", "category": "Business", "city":"Indianapolis"},
}
# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
"Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
"Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
"Sister": {"Jan": 80, "Mar": 70},
"Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
"Roommate": {"Feb": 15, "Mar": 25},
"Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
"Professor": {"Feb": 20, "Mar": 35},
"Dentist": {"Jan": 10},
}

print("Phase 1")

quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"

print(quick_contacts)

print(quick_contacts["Mom"])
quick_contacts["Dad"] = "555-4321"
quick_contacts["Dentist"] = "555-2222"

print(quick_contacts.get("Grandma", "Contact not found"))
print(quick_contacts)
del(quick_contacts["Pizza Place"])
old_work = quick_contacts.pop("Work")
print(old_work)
print(f"{len(quick_contacts)}, {list(quick_contacts.keys())}, {list(quick_contacts.values())}")




print("Phase 2")

total_minutes = {}
for name, months in call_log.items():

    total = 0
    busiest = ""
    for month, minutes in months.items():
        total += minutes
        if(minutes > int(months.get(busiest, 0))):
            busiest = month

    total_minutes[name] = total

    print(name)
    print(f"Number of months called {len(months)} \ntotal minutes {total} \naverage minutes{total/12:.2f} \nBusiest month {busiest}: {months[busiest]}")



print("Phase 3")

month_stats = {}

for name, months in call_log.items():
    for month, minutes in months.items():
        month_stats[month] = month_stats.get(month, {"minutes": [], "total": 0, "avg": 0, "contacts": []})
        month_stats[month]["minutes"].append(minutes)
        month_stats[month]["total"] += minutes
        month_stats[month]["contacts"].append(name)

for month, stats in month_stats.items():
    month_stats[month]["avg"] = stats["total"] / len(stats["minutes"])

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for name, months in call_log.items():
    minutes_by_category[contact_book[name]["category"]] = minutes_by_category.get(contact_book[name]["category"], 0) + sum(months.values())
    minutes_by_city[contact_book[name]["city"]] = minutes_by_city.get(contact_book[name]["city"], 0) + sum(months.values())
    contacts_per_city[contact_book[name]["city"]] = contacts_per_city.get(contact_book[name]["city"], 0) + 1





print("Phase 4")

phone_book = {name: info["phone"] for (name, info) in contact_book.items()}

print(phone_book)

local_contacts = {name: info["phone"] for (name, info) in contact_book.items() if info["city"] == "FortWayne"}

print(local_contacts)

activity_level = {name: "Frequent" if minutes >= 200 else "Occasional" for (name, minutes) in total_minutes.items()}

print(activity_level)





print("phase 5")

def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    if minutes >= 200:
        return "Gold"
    if minutes >= 100:
        return "Silver"
    if minutes >= 50:
        return "Bronze"
    return "Inactive"

for name, total in total_minutes.items():
    print(f"{name}: {get_tier(total)}")

count = {"Platinum": 0, "Gold": 0, "Silver": 0, "Bronze": 0, "Inactive": 0}

for name, total in total_minutes.items():
    returned = get_tier(total)
    if(total >= 400):
        count["Platinum"] += 1
    elif(total >= 200):
        count["Gold"] += 1
    elif(total >= 100):
        count["Silver"] += 1
    elif(total >= 50):
        count["Bronze"] += 1
    else:
        count["Inactive"] +=  1
    
for tier, val in count.items():
    print(f"{tier}: {val}")


most = ""
least = ""
grand_total = 0

for name, total in total_minutes.items():
    if total > total_minutes.get(most, 0):
        most = name
    if total < total_minutes.get(least, float('inf')):
        least = name
    grand_total += total

average = grand_total / len(total_minutes)

print(f"Most: {most} {total_minutes[most]}")
print(f"Least: {least} {total_minutes[least]}")
print(f"total: {grand_total}")
print(f"Average: {average:.2f}")

for name, total in total_minutes.items():
    if total > average:
        print(f"{name}: {total} min")




print("Phase 6")

sorted_contacts = sorted(total_minutes.items(), key=lambda item: item[1], reverse=True)
print(f"{'Name':<15}{'Category':<15}{'City':<15}{'Minutes':<15}{'Tier':<15}")
print()
for name, total in sorted_contacts:
    print(f"{name:<15}{contact_book[name]['category']:<15}{contact_book[name]['city']:<15}{total:<15}{get_tier(total):<15}")

print(f"{len(sorted_contacts)} contacts | {grand_total} total minutes | {average:.2f} average minutes")