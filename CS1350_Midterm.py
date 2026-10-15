#Problem 1 Library Ctalog

class Library:
    def __init__(self):
        self.books = {}
        pass

    def add_book(self, isbn, title, author, copies):
        if(self.books.get(isbn, -1) == -1):
            self.books[isbn] = {"title": title, "author": author, "copies": copies}
        else:
            self.books[isbn]["copies"] += copies
        return

    def checkout(self, isbn):
        if(self.books.get(isbn, -1) == -1 or self.books[isbn]["copies"] <= 0):
            return False
        
        self.books[isbn]["copies"] -= 1
        return True

    def by_author(self, author):
        titles = []
        
        for book in self.books.values():
            if book["author"].lower == author.lower:
                titles.append(book["title"])

        return sorted(titles)

    def inventory_value(self, prices):
        value = 0
        for book in self.books.keys():
            print(book)
            for other_book in prices.keys():
                if book == other_book:
                    value += self.books[book]["copies"] * prices[other_book]

        return value
    
    def low_stock(self, threshold):
        otherdict = {}

        for book, values in self.books.items():
            if values["copies"] < threshold:
                otherdict[book] = values["copies"]
        
        return otherdict

#Test cases
lib = Library()
lib.add_book("111", "Python Basics", "Jane Doe", 2)
lib.add_book("222", "Data Science", "John Roe", 1)
lib.add_book("333", "Advanced Python", "Jane Doe", 3)
lib.add_book("111", "Python Basics", "Jane Doe", 1)

print(lib.checkout("222"))
print(lib.checkout("222"))
print(lib.checkout("999"))
print(lib.by_author("Jane Doe"))
print(lib.inventory_value({"111": 20.0, "333": 30.0, "999": 5.0}))
print(lib.low_stock(3))



#Problem 2: Conference Sessions with Sets (Sets)


class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()
        return

    def register(self, name):
        self.attendees.add(name)
        return

    def unregister(self, name):
        self.attendees.discard(name)
        return

    def attendee_count(self):
        print(len(self.attendees))


def attended_all(sessions):
    matched = set(sessions[0].attendees)
    for i in sessions:
        for name in sessions[0].attendees:
            print(name)
            if(name not in i.attendees):
                matched.discard(name)

    return matched

def attended_exactly_one(sessions):
    matched = set()
    known = set()
    for i in sessions:
        for name in i.attendees:
            if name not in matched:
                if name not in known:
                    matched.add(name)
                    known.add(name)
            else:
                matched.remove(name)
    return matched

def no_shows(registered, sessions):
    matched = set(registered)
    for i in sessions:
        matched -= i.attendees
    return matched

def summary(sessions):
    for i in sessions:
        print(f"{i.title}, ",end="")
        i.attendee_count()
    
    known = set()
    for i in sessions:
        for name in i.attendees:
            known.add(name)
    print(f"Distinct people: {len(known)}")
    return

keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)

workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)

panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)

workshop.unregister("Eli")
workshop.unregister("Zed")

sessions = [keynote, workshop, panel]
print(attended_all(sessions))
print(attended_exactly_one(sessions))
print(no_shows({"Ana", "Ben", "Fay", "Gus",}, sessions))

summary(sessions)